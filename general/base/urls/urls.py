from django.urls import path
from base.views.blog_view import blog
from base.views.account_view import account

urlpatterns =[
    path('', blog),
     path('user/',account)
]
