from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TalesListView.as_view(), name='list'),
    url(r'^(?P<pk>.+)/$', views.single_tale, name='single_tale'),
]
