from django.contrib import messages
from django.shortcuts import render, redirect

from contact.forms import ContactForm


# Create your views here.

def get_in_touch(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Xabaringiz qabul qilindi!')
            return redirect('/contact/')
    context = {'form': form}
    return render(request, 'contact.html', context)
