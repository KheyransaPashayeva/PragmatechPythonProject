from django.shortcuts import render,redirect
from .models import Blog,Comment
import math
# Create your views here.
def blog(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page =1
    per_count =2
    all_blogs = Blog.objects.all().count()
    blogs = Blog.objects.all()[per_count*(page-1):(page*per_count)]
    total_page_count = math.ceil(all_blogs / per_count)
    previous_page = page - 1 if not page == 1 else page
    next_page = page + 1 if not total_page_count == page else page
    current_page = page
    page_range = range(1,total_page_count +1)
    context = {
        'blogs': blogs,
        'previous_page':previous_page,
        'next_page':next_page,
        'current_page':current_page,
        'page_range':page_range
        }
    post_id = request.POST.get('post_id')
    response = render(request, 'blog-list.html', context)
    liked_posts = request.COOKIES.get('liked_posts','')
    if request.method == 'POST' and post_id not in liked_posts:
        response.set_cookie('liked_posts',f'{liked_posts}{post_id}')
    return response

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
    count = blog.comments.count()
    context = {'blog': blog,
               'comments': comments,
               'count': count
    }
    return render(request, 'blog-detail.html', context)



