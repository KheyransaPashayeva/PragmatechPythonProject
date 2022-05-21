from django.urls import path
from products.views import product,product_detail


app_name='products'
urlpatterns = [
    path('', product, name='products'),
    path('<slug:slug>', product_detail, name='product_detail')

]