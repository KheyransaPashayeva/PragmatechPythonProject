from django.shortcuts import render,redirect
from .models import Products
import math
# Create your views here.
def product(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page =1
    per_count =2
    all_products = Products.objects.all().count()
    products = Products.objects.all()[per_count*(page-1):(page*per_count)]
    total_page_count = math.ceil(all_products / per_count)
    previous_page = page - 1 if not page == 1 else page
    next_page = page + 1 if not total_page_count == page else page
    current_page = page
    page_range = range(1,total_page_count +1)
    context = {
        'products': products,
        'previous_page':previous_page,
        'next_page':next_page,
        'current_page':current_page,
        'page_range':page_range
        }
    post_id = request.POST.get('post_id')
    response = render(request, 'product-list.html', context)
    liked_posts = request.COOKIES.get('liked_posts','')
    if request.method == 'POST' and post_id not in liked_posts:
        response.set_cookie('liked_posts',f'{liked_posts}{post_id}')
    return response

def product_detail(request,slug):
    product = Products.objects.filter(slug=slug).first()
    context = {'product': product
    }
    return render(request, 'product-detail.html', context)

