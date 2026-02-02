from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
    return render(request, 'contact.html', {'form': form})
