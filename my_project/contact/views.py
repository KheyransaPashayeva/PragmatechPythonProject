from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'contact/mailmassage.html')

def phone(request):
    return render(request, 'contact/phonecall.html')