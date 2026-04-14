from django.shortcuts import render
from .models import Product, Category # NAYI LINE: Category ko bhi import karna zaroori hai

# Is function ko SMART bana diya
def show_products(request, cat_id=None):
    
    # 1. Pehle database se SAARI categories nikal lo (Taaki button bana sakein)
    all_categories = Category.objects.all()

    # 2. Check karo ki user ne kisi category par click kiya hai kya?
    if cat_id:
        # Agar HAA, toh sirf us category ke products nikalo
        all_items = Product.objects.filter(category_id=cat_id)
    else:
        # Agar NAHI, toh pehle ki tarah saare products dikha do
        all_items = Product.objects.all()
    
    # 3. Dono cheezein dibbe me pack karke HTML ko bhej do
    data = {
        'products': all_items,
        'categories': all_categories # Naya data
    }
    return render(request, 'products_list.html', data)

# Niche wala product_detail function waisa ka waisa hi chhod dein...
def product_detail(request, id):
    single_product = Product.objects.get(id=id)
    data = {'item': single_product}
    return render(request, 'product_detail.html', data)