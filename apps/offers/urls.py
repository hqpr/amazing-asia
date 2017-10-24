from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.OffersListView.as_view(), name='list'),
]
