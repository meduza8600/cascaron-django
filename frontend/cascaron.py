from django.conf import settings
def docs_base_url(request):
    return {'root_files': settings.DOCS_BASE_URL,
            'CANONICAL_PATH': request.build_absolute_uri(request.path),
            'css_js_version':'?v=3.0.40'
            }
