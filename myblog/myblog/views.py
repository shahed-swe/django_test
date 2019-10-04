#(MVT) model view template
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html",{"title": "Home","list":['Html','CSS','Python','Java']})

def contact(request):
    return render(request, "contact.html",{"title":"Contact"})

def about(request):
    return render(request, "about.html",{"title": "About"})