from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import single_page

urlpatterns = [
    url(r'^(?P<slug>.+)/$', single_page, name='single_page'),
]
