from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about/aboutcompany.html')

def aboutme(request):
    return render(request, 'about/aboutme.html')
     