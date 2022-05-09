from django.urls import path
from blogs.views import blog,blog_detail


app_name='blogs'
urlpatterns = [
    path('', blog, name='blog'),
    path('<slug:slug>', blog_detail, name='blog_detail')

]