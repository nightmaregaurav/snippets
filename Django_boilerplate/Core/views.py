from django.shortcuts import render


def custom_error_500(request):
    return custom_error(request, err_code='500')


def custom_error_400(request, exception):
    return custom_error(request, exception=exception, err_code='400')


def custom_error_403(request, exception):
    return custom_error(request, exception=exception, err_code='403')


def custom_error_404(request, exception):
    return custom_error(request, exception=exception, err_code='404')


def custom_error(request, exception=None, err_code=None):
    if exception:
        if type(exception.args[0]) == str:
            msg = exception
        else:
            msg = "That's all i know..."
    else:
        msg = "That's all i know..."

    context = {
        'err_code_1': err_code[0],
        'err_code_2': err_code[1],
        'err_code_3': err_code[2],
        'err_code_msg': msg
    }

    return render(request, 'Core/error-pages.html', context)
