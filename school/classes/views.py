from django.shortcuts import render, get_object_or_404

from .models import Discipline


def discipline_list(request):
    d = Discipline.objects.all()
    return render(request, 'classes/list.html', {'disciplines': d})


def discipline_detail(request, pk: int):
    d = get_object_or_404(Discipline, pk=pk)
    return render(request, 'classes/detail.html', {'discipline': d, 'student_list': d.student_set.all()})
