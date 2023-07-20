from django.shortcuts import render
from django.utils.translation import gettext as _

import json
from django.views import generic

class EventosView(generic.ListView):
    def get_event_catg1_es_data():
        with open('frontend/static/datos/eventos.json', encoding='utf-8') as f:
            data = json.load(f)
        eventsCatg1List = data["eventos_category1"]
        # Get the blog from id and add it to the context
        context = eventsCatg1List
        return eventsCatg1List

    def get_event_catg2_es_data():
        with open('frontend/static/datos/eventos.json', encoding='utf-8') as f:
            data = json.load(f)
        eventsCatg2List = data["eventos_category2"]

        # Get the blog from id and add it to the context
        context = eventsCatg2List
        return eventsCatg2List

    def get_event_catg3_es_data():
        with open('frontend/static/datos/eventos.json', encoding='utf-8') as f:
            data = json.load(f)
        eventsCatg3List = data["eventos_category3"]
        # Get the blog from id and add it to the context
        context = eventsCatg3List
        return eventsCatg3List

# @cache_page(60 * 15)
def index(request):
    eventos_catg1 = EventosView.get_event_catg1_es_data()
    eventos_catg2 = EventosView.get_event_catg2_es_data()
    eventos_catg3 = EventosView.get_event_catg3_es_data()
    # evento_rel = eventos[0]
    context = {
        'title': "Index",
        'page': 'index',
        'eventos_catg1': eventos_catg1,
        'eventos_catg2': eventos_catg2,
        'eventos_catg3': eventos_catg3,
        'eventos': eventos_catg1 + eventos_catg2 + eventos_catg3,
    }
    return render(request, '{0}/index.html'.format(request.LANGUAGE_CODE), context)
