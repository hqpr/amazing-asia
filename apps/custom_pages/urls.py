from django.conf.urls import url

from .views import single_page

urlpatterns = [
    url(r'^(?P<slug>.+)/$', single_page, name='single_page'),
]
