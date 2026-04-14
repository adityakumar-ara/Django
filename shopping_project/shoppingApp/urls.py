from django.contrib import admin
from django.urls import path,include
from .views import show_products, product_detail  ## Importing all views from the current app's views.py file

urlpatterns = [
    path('', show_products, name='products'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('category/<int:cat_id>/', show_products, name='category_filter'),
]