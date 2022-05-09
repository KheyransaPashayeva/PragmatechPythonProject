from django.shortcuts import render,redirect
from .models import Blog,Comment
# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog-list.html', context)

def blog_detail(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    if request.method == 'POST':
        Comment.objects.create(
        name=request.POST.get('name'),
        email=request.POST.get('email'),
        subject=request.POST.get('subject'),
        text=request.POST.get('text'),
        blog=blog
      )
        return redirect ('/')
    comments = blog.comments.all()
    context = {'blog': blog,
               'comments': comments,
            #    'post': blog.comments.all()
    }
    return render(request, 'blog-detail.html', context)



