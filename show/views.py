from django.shortcuts import render
from .models import Musical


def home(request):
    musicals=Musical.objects
    return render(request, 'show/home.html',{'musicals':musicals})

def musical_home(request):
    musicals=Musical.objects
    return render(request, 'show/musical_home.html',{'musicals':musicals})