from django.urls import path
from index.views import HomeView,AboutView,contact


app_name='index'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('about/', AboutView.as_view(), name='about')
]