from django.shortcuts import render

# Create your views here.
def user(request):
    return render(request, 'user.html')

def register(request):
    return render(request, 'register.html')