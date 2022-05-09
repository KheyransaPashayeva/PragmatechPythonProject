from django.urls import path
from index.views import home,about,contact


app_name='index'
urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about')
]