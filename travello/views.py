from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination, Contact
# Create your views here.


def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        website = request.POST['website']
        message = request.POST['message']

        print(name)
        contact = Contact(name=name, email=email, number=number,
                          website=website, message=message)
        contact.save()
        print('done')
        return redirect('/')

    else:
        return render(request, 'contact.html')
