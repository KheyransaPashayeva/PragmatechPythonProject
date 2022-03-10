from django.urls import path
from contact.views import contact,phone

app_name='contact'
urlpatterns = [
    path('', contact,name='contact'),
    path('phone/',phone,name='phone')
]
