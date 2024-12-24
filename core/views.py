from django.http import HttpResponse
from django.shortcuts import render


def home(request): 
    return render(request=request, template_name="home.html")
