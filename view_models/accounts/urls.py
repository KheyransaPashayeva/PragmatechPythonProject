from django.urls import path
from accounts.views import user,register

urlpatterns = [
    path('user/', user),
    path('register/',register)
]
