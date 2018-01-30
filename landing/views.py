from django.shortcuts import render
from .models import *


def landing(request):
    image = Section2.objects.all()
    return render(request, 'landing/landing.html', locals())