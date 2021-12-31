from django.conf import settings

from ..models import SiteSetting


site_settings_abstract = {
    'site_logo': r'',
    'site_title': r'',
    'header_main': r'',
    'footer_main': r'',
}


def urls(request):
    app = ''
    # noinspection PyBroadException
    try:
        app = request.resolver_match.app_name
        if app:
            app += '/'
    except Exception:
        app += '/'

    app = app.strip()

    return {
        'APP_URL': app,
        'STATIC_URL': settings.STATIC_URL,
        'MEDIA_URL': settings.MEDIA_URL,
        'BASE_URL': 'base.html',
    }


# noinspection PyUnusedLocal
def site_setting(request):
    site_settings = SiteSetting.objects.all()
    for setting in site_settings:
        site_settings_abstract[setting.key] = setting.value
    return {
        'site_setting': site_settings_abstract,
    }
