from django.shortcuts import render


def index(request):
    template = 'section_statistics.html'
    return render(request, template, {})
