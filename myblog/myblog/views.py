#(MVT) model view template
from django.http import HttpResponse
from django.shortcuts import render
from .form import ContactForm

def home(request):
    return render(request, "home.html",{"title": "Home","list":['Html','CSS','Python','Java']})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render(request, "form.html",context)

def about(request):
    return render(request, "about.html",{"title": "About"})