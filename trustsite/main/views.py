from django.shortcuts import render
from datetime import datetime
from .models import Contact


def index(request):
    if request.method == "POST":
        # print("ddd")
        # name = request.POST.get('name')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        cont = Contact(name=name, email=email, phone=phone, message=message)
        cont.save()
    return render(request, "index.html")


def contact_view(request):
    return render(request, "contact_view.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    print("ddd")
    return render(request, 'index.html')
