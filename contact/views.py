from django.shortcuts import render
from .form import ContactForm
from .models import Contact
# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        obj = Contact.objects.create(**form.cleaned_data)
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render(request, "form.html",context)