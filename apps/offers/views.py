from django.views.generic import ListView, DetailView

from .models import Offer


class OffersListView(ListView):
    model = Offer
    paginate_by = 6


class OfferDetailView(DetailView):
    model = Offer
