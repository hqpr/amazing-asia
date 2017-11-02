from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.OffersListView.as_view(), name='list'),
    url(r'^(?P<pk>\d*)/$', views.OfferDetailView.as_view(), name='detail'),
]
