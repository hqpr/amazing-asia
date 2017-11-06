from .models import Page


def bottom_menu(request):
    return {'pages': Page.objects.filter(published=True)}
