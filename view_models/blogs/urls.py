from django.urls import path
from blogs.views import blog

urlpatterns = [
    path('', blog)
    
]
