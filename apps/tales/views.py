from django.shortcuts import render
from django.views.generic import ListView

from .models import Tale


def single_tale(request, pk):
    tale = Tale.objects.get(id=pk)
    data = {'tale': tale}
    return render(request, 'tales/single_tale.html', data)


class TalesListView(ListView):
    model = Tale
    paginate_by = 6
