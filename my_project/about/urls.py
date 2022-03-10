from django.urls import path
from about.views import about,aboutme

app_name='about'
urlpatterns = [
    path('', about, name='about'),
    path('aboutme/', aboutme, name='aboutme')
]
