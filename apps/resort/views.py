from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Destination, Resort


class ResortListView(ListView):
    model = Resort


class DestinationListView(ListView):
    model = Destination


class DestinationDetailView(DetailView):
    model = Destination
    template_name = 'resort/destination_detail.html'

    def get_object(self, *args, **kwargs):
        object = Destination.objects.get(id=self.kwargs['destination_id'])
        return object

    def get_context_data(self, **kwargs):
        context = super(DestinationDetailView, self).get_context_data(**kwargs)
        return context
