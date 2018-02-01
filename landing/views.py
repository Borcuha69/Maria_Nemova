from django.shortcuts import render
from .models import *
from .forms import *


def landing(request):
    image = Section2.objects.all()
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())