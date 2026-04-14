# Register your models here.
from django.contrib import admin
from .models import Student, Category, Product

admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Product)
