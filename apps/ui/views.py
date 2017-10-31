from django.views.generic import TemplateView

from apps.resort.models import Resort


class IndexView(TemplateView):
    template_name = 'ui/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resort_top_left'] = Resort.objects.featured(0)
        context['resort_top_right'] = Resort.objects.featured(1)
        context['resort_bottom_left'] = Resort.objects.featured(2)
        context['resort_bottom_center'] = Resort.objects.featured(3)
        return context

