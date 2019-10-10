#(MVT) model view template
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html",{"title": "Home","list":['Html','CSS','Python','Java']})

def about(request):
    return render(request, "about.html",{"title": "About"})