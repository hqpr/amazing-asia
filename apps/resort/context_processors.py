from .models import Destination


def get_destinations(request):
    return {'all_destinations': Destination.objects.all()}
