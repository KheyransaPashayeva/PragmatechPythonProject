from django.shortcuts import render

# Create your views here.
def user(request):
    return render(request, 'account/user.html')

def register(request):
    return render(request, 'account/register.html')