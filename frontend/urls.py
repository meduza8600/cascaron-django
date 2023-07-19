from django.urls import path

from . import views
from django.views.generic import TemplateView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('', views.index, name='index'),

]
