from django.shortcuts import render,get_object_or_404
from .models import Musical,Exhibition,Concert,Classic


def home(request):
    musicals=Musical.objects
    return render(request, 'show/home.html',{'musicals':musicals})

def musical_home(request):
    musicals=Musical.objects
    return render(request, 'show/musical_home.html',{'musicals':musicals})

def musical_detail(request,musical_id):
    musical_detail=get_object_or_404(Musical,pk= musical_id)
    return render(request, 'show/musical_detail.html',{'musical':musical_detail})

def exhibition_home(request):
    exhibitions=Exhibition.objects
    return render(request, 'show/exhibition_home.html',{'exhibitions':exhibitions})

def exhibition_detail(request,exhibition_id):
    exhibition_detail=get_object_or_404(Exhibition,pk= exhibition_id)
    return render(request, 'show/exhibition_detail.html',{'exhibition':exhibition_detail})

def concert_home(request):
    concerts=Concert.objects
    return render(request, 'show/concert_home.html',{'concerts':concerts})

def concert_detail(request,concert_id):
    concert_detail=get_object_or_404(Concert,pk= concert_id)
    return render(request, 'show/concert_detail.html',{'concert':concert_detail})

def classic_home(request):
    classics=Classic.objects
    return render(request, 'show/classic_home.html',{'classics':classics})

def classic_detail(request,classic_id):
    classic_detail=get_object_or_404(Classic,pk= classic_id)
    return render(request, 'show/classic_detail.html',{'classic':classic_detail})