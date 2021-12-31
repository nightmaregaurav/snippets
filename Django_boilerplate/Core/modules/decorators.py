import json
from urllib.parse import quote

from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse, redirect


def require_ajax(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest("This request is not allowed here.")
        else:
            return f(request, *args, **kwargs)
    return wrap


def require_post(f):
    def wrap(request, *args, **kwargs):
        if not request.POST:
            if request.is_ajax():
                return HttpResponse(json.dumps({
                    'ERROR': True,
                    'title': "ERROR",
                    'message': '''This request is not allowed here.''',
                }), content_type='application/json')
            else:
                return HttpResponseBadRequest("This request is not allowed here.")
        else:
            return f(request, *args, **kwargs)
    return wrap


def require_login(redirect_to):
    def inner(f):
        def wrap(request, *args, **kwargs):
            if not request.user.is_authenticated:
                if request.is_ajax():
                    messages.error(request, "You must login first.")

                    post_src_url = request.POST.get('src_url', None)
                    get_src_url = request.GET.get('src_url', None)

                    if post_src_url:
                        src_url = post_src_url
                    elif get_src_url:
                        src_url = get_src_url
                    else:
                        src_url = "/"

                    return HttpResponse(json.dumps({
                        'redirect': True,
                        'redirect_path': reverse(redirect_to) + "?next=" + quote(src_url, safe='')
                    }), content_type='application/json')
                else:
                    messages.error(request, "You must login first.")
                    return HttpResponseRedirect(reverse(redirect_to) + "?next=" + quote(request.get_full_path(), safe=''))
            else:
                return f(request, *args, **kwargs)
        return wrap
    return inner


def restrict_staff_entry(redirect_to):
    def inner(f):
        def wrap(request, *args, **kwargs):
            if request.user.is_staff:
                if request.is_ajax():
                    messages.error(request, "You are not allowed to visit those pages with staff account.")
                    return HttpResponse(json.dumps({
                        'redirect': True,
                        'redirect_path': reverse(redirect_to)
                    }), content_type='application/json')
                else:
                    messages.error(request, "You are not allowed to visit those pages with staff account.")
                    return redirect(redirect_to)
            else:
                return f(request, *args, **kwargs)
        return wrap
    return inner


def require_atomic_transaction(f):
    def wrap(request, *args, **kwargs):
        if request.is_ajax():
            res = HttpResponse(json.dumps({
                    'ERROR': True,
                    'title': "ERROR",
                    'message': '''Something went wrong...''',
                }), content_type='application/json')
            error = True
            # noinspection PyBroadException
            try:
                with transaction.atomic():
                    res = f(request, *args, **kwargs)
                    error = False
                    if json.loads(res.content.decode()).get('ERROR', False):
                        raise Exception("")
            except Exception:
                if error:
                    raise
                else:
                    return res

            return res
        else:
            with transaction.atomic():
                return f(request, *args, **kwargs)
    return wrap
