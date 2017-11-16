from django.views.generic import ListView, DetailView

from .models import Destination, Resort


class ResortListView(ListView):
    model = Resort


class DestinationListView(ListView):
    model = Destination
    paginate_by = 9

    def get_paginate_by(self, queryset):
        return self.request.GET.get('show', self.paginate_by)

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('destination_id')
        queryset = Resort.objects.filter(is_active=True, destination=pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Destination.objects.get(id=self.kwargs['destination_id'])
        return context


class ResortDetailView(DetailView):
    model = Resort
