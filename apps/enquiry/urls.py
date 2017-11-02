from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AddEnquiryView.as_view(), name='add'),
]
