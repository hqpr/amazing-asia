from django.urls import reverse
from django.views.generic import CreateView

from .models import Enquiry
from .forms import EnquiryForm


class AddEnquiryView(CreateView):
    model = Enquiry
    form_class = EnquiryForm

    def get_success_url(self):
        return reverse('ui:index')
