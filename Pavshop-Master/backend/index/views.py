from django.shortcuts import render,redirect
from .models import Contact
# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about-us.html')


def contact(request):
      if request.method == 'POST':
        Contact.objects.create(
        fullname=request.POST.get('fullname'),
        email=request.POST.get('email'),
        subject=request.POST.get('subject'),
        message=request.POST.get('message'),
        phone=request.POST.get('phone')
     )
        return redirect ('/')
      return render(request, 'contact.html')