from django.urls import path
from blog.views import blog,myblog


app_name='blog'
urlpatterns = [
    path('', blog, name='blog'),
    path('myblog', myblog, name='myblog')
]
