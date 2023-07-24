from django.shortcuts import render
from django.utils.translation import gettext as _

from django.views.decorators.gzip import gzip_page

import json
from django.views import generic
from django.contrib.staticfiles.storage import staticfiles_storage


class EventsView(generic.ListView):
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


    def get_event_rel_es_data():
        with open('frontend/static/datos/eventos.json', encoding='utf-8') as f:
            data = json.load(f)
        eventsRelList = data["events_rel"]
        # Get the blog from id and add it to the context
        context = eventsRelList
        return eventsRelList


class ReportesView(generic.ListView):
    def get_reportes_trim_es_data():
        with open('frontend/static/datos/reportes.json', encoding='utf-8') as f:
            data = json.load(f)
        rptTrimESList = data["trimestrales"]
        # Get the blog from id and add it to the context
        context = rptTrimESList
        return rptTrimESList

    def get_reportes_anu_es_data():
        with open('frontend/static/datos/reportes.json', encoding='utf-8') as f:
            data = json.load(f)
        rptAnuESList = data["anuales"]
        # Get the blog from id and add it to the context
        context = rptAnuESList
        return rptAnuESList

    def get_directivos_es_data():
        with open('frontend/static/datos/directivos.json', encoding='utf-8') as f:
            data = json.load(f)
        directivosESList = data["directivos"]
        # Get the blog from id and add it to the context
        context = directivosESList
        return directivosESList


# @cache_page(60 * 15)
def index(request):
    events_catg1 = EventsView.get_event_catg1_es_data()
    events_catg2 = EventsView.get_event_catg2_es_data()
    events_catg3 = EventsView.get_event_catg3_es_data()
    # evento_rel = eventos[0]
    context = {
        'title': "Index",
        'page': 'index',
        'eventos_catg1': events_catg1,
        'eventos_catg2': events_catg2,
        'eventos_catg3': events_catg3,
        'eventos': events_catg1 + events_catg2 + events_catg3,
    }
    return render(request, '{0}/index.html'.format(request.LANGUAGE_CODE), context)


######################
# Noticias
######################


@gzip_page
def noticias(request):
    events_rel = EventsView.get_event_rel_es_data()
    events = EventsView.get_event_catg2_es_data()
    context = {
        'title': _("Noticias"),
        'page': 'noticias',
        'events_rel': events_rel,
        'events': events,
        'imagen': staticfiles_storage.url('img/parallax/1.jpg'),
    }
    return render(request, '{0}/noticias.html'.format(request.LANGUAGE_CODE), context)
