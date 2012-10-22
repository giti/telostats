from django.views.generic import DetailView, TemplateView
from django.conf import settings
from djpjax import PJAXResponseMixin

from .models import Station


class StationMap(TemplateView):
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super(StationMap, self).get_context_data(**kwargs)
        context['tileserver_url'] = settings.TILESERVER_URL
        return context


class StationDetail(PJAXResponseMixin, DetailView):
    model = Station
    context_object_name = 'station'

    def get_context_data(self, **kwargs):
        context = super(StationDetail, self).get_context_data(**kwargs)
        context['tileserver_url'] = settings.TILESERVER_URL
        return context

class About(StationMap):
    template_name = 'about.html'

class AboutApi(StationMap):
    template_name = 'about_api.html'
