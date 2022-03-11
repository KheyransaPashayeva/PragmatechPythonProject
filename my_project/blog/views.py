from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog(request):
    blogs = Post.objects.filter(status='active')
    context={
        'blogs': blogs
        }
    return render(request, 'blog/newsblog.html', context=context)

def myblog(request):
    return render(request, 'blog/myblogs.html')


def blog_detail(request, blog):
    blogs = [
            {
                'blog1': {
                    'author': 'Eli',
                    'title': 'Django',
                    'publish_date': '15.05.2020'
                },

                'blog2': {
                    'author': 'Vahid',
                    'title': 'Python',
                    'publish_date': '15.01.2022'
                },

            }
        ]
    blog = blogs[0][blog]

    return render(request, 'blog-detail.html', {'blog': blog})