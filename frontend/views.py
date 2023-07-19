from django.shortcuts import render
from django.utils.translation import gettext as _


# @cache_page(60 * 15)
def index(request):
    evento_rel = {
            "title": _("title"),
            "date": "09/03/2023",
            "url": "http"
        }
    invitacion = {
            "title": _("title"),
            "date": "09/03/2023",
            "url": "http"
        }
    noticias = [
        {
            "title": _("title"),
            "date": "09/03/2023",
            "url": "http"
        }
    ]
    eventos = [
        {
            "title": _("title"),
            "date": "09/03/2023",
            "url": "http"
        }
    ]
    eventos_en = [
        {
            "title": _("title"),
            "date": "09/03/2023",
            "url": "http"
        }
    ]
    # evento_rel = eventos[0]
    context = {
        'title': "Index",
        'page': 'index',
        'noticias': noticias,
        'eventos': eventos,
        'eventos_en': eventos_en,
        'last_evento': eventos[0],
        'last_evento_en': eventos_en[0],
        'last_noticia_en': noticias[0],
        'evento_relevante': evento_rel,
        'invitacion': invitacion
    }
    return render(request, '{0}/index.html'.format(request.LANGUAGE_CODE), context)
