from django.shortcuts import render,redirect
from .models import Contact
from django.views.generic.base import TemplateView
# Create your views here.
class HomeView(TemplateView):
  template_name = 'index.html'


class AboutView(TemplateView):
  template_name = 'about-us.html'


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