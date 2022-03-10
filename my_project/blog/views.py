from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog/newsblog.html')

def myblog(request):
    return render(request, 'blog/myblogs.html')