from django.shortcuts import render

from .models import Page


def single_page(request, slug):
    page = Page.objects.get(slug=slug)
    pages = Page.objects.filter(published=True)
    data = {'page': page, 'pages': pages}
    return render(request, 'custom_page/single_page.html', data)
