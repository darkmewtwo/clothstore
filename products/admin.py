from django.contrib import admin

from products.models import Category, Product, ProductAttribute

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductAttribute)
