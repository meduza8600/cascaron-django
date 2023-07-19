import os

def site_key(request):
    return {
        'site_key': os.getenv("RECAPTCHA_SITE_KEY"),
    }
