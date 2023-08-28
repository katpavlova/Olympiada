from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    return render(request, 'olymp_site/index.html')


def register(request):
    if request.method == 'POST':
        form = AddBlankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddBlankForm()
    return render(request, 'olymp_site/register.html', {'form': form})
