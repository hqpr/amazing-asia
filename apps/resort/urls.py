from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ResortListView.as_view(), name='list'),
    url(r'^destinations/$', views.DestinationListView.as_view(), name='destinations'),
    url(r'^destinations/(?P<destination_id>\d*)/$', views.DestinationDetailView.as_view(),
        name='destination-detail'),
    url(r'^(?P<pk>\d*)/$', views.ResortDetailView.as_view(), name='resort-detail'),
]
