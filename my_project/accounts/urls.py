from django.urls import path
from accounts.views import user,register


app_name='accounts'
urlpatterns = [
    path('user/', user, name='user'),
    path('register/', register,name='register')
]
