from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'olymp_site/index.html')
