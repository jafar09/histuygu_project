from django.shortcuts import render, redirect, HttpResponseRedirect
from  emotions.forms import ContactForm  # Formani import qilish
import pdb
from django.contrib import messages


# index views
def index(request):
    return render(request, 'index.html')

# about views
def about(request):
    return render(request, 'about.html')

# contact views


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent. Thank you!")
            return redirect("contact")  # Redirect back to the contact page
        else:
            messages.error(request, "There was an error in your form.")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

# gallery_single views
def gallery_single(request):
    return render(request, 'gallery-single.html')

# gallery views
def gallery(request):
    return render(request, 'gallery.html')

# services views
def services(request):
    return render(request, 'services.html')

# starter_page views
def starter_page(request):
    return render(request, 'starter-page.html')