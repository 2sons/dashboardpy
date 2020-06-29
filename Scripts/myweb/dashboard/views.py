from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.
def index(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})
