from .models import Tale


def get_tales(request):
    return {'all_tales': Tale.objects.filter(published=True)}
