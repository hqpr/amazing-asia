from django.views.generic import CreateView

from .models import Enquiry
from .forms import EnquiryForm


class AddEnquiryView(CreateView):
    model = Enquiry
    form_class = EnquiryForm
