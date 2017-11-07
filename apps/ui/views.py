from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from apps.resort.models import Resort
from apps.offers.models import Offer
from .forms import ContactForm


class IndexView(TemplateView):
    template_name = 'ui/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resort_top_left'] = Resort.objects.featured(0)
        context['resort_top_right'] = Resort.objects.featured(1)
        context['resort_bottom_left'] = Resort.objects.featured(2)
        context['resort_bottom_center'] = Resort.objects.featured(3)

        context['offer_top_left'] = Offer.objects.featured(0)
        context['offer_top_right'] = Offer.objects.featured(1)
        context['offer_bottom_left'] = Offer.objects.featured(2)
        context['offer_bottom_center'] = Offer.objects.featured(3)

        return context


def contact(request):
    if request.method == 'POST':
        context = {}
        feedback_form = ContactForm(request.POST)
        context["form"] = feedback_form
        if feedback_form.is_valid():
            feedback_form.save()
            response = redirect('ui:index')
            response['Location'] += '?message_sent=success'
            return response
        else:
            return render(request, 'ui/contact.html', context)
    else:
        return render(request, 'ui/contact.html')
