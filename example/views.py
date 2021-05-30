from django.shortcuts import render
from django.http import HttpResponse
from.tasks import gotosleeo

# Create your views here.

def index(request):
    gotosleeo(1, 1)

    return HttpResponse("done")
