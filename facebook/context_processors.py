from django.conf import settings
""" This context processor is depreciated.
    It only works it if you only have one Facebook App. 
    Use the facebook_tags instead.
"""
def application_settings(request):
    firstapp = getattr(settings, 'FACEBOOK_APPS').values()[0]
    return { 'FACEBOOK_API_KEY' : firstapp['API-KEY'],
             'FACEBOOK_APP_ID' : firstapp['ID'],
             'FACEBOOK_CANVAS_PAGE' : firstapp['CANVAS-PAGE'],
             'FACEBOOK_CANVAS_URL' : firstapp['CANVAS-URL']}
    
def facebook_config(request):
    return {'facebook' : request.session['facebook']}

def session_without_cookies(request):
    """ simple helper to use sessions without cookies """
    cookie_name = settings.SESSION_COOKIE_NAME
    session_key = request.session._get_session_key()
    
    return {'session_GET' : '%s=%s' %(cookie_name, session_key),
            'session_id'  : session_key,
            'session_hidden_field' : '<div style="display:none"><input type="hidden" name="%s" value="%s" /></div>' %(cookie_name, session_key)}
