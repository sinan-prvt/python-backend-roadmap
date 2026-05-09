# =================================== Creating Django Admin



# --------------- Step 1: Create Models

# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()

#     def __str__(self):
#         return self.name




# --------------- Step 2: Register Models in Admin

# -- In admin.py

# from django.contrib import admin
# from .models import Product

# admin.site.register(Product)




# --------------- Step 3: Run Migrations

# python manage.py makemigrations

# python manage.py migrate




# --------------- Step 4: Create Superuser

# python manage.py createsuperuser




# --------------- Step 5: Run Server

# python manage.py runserver






## ================================ Admin Customization

# from django.contrib import admin
# from .models import Product

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):

#     list_display = ['name', 'price']       # Displaying fields in the admin list view

#     search_fields = ['name']               # Adding search functionality for the 'name' field

#     list_filter = ['price']                # Adding filter options for the 'price' field

#     ordering = ['id']                      # Ordering the products by their ID in the admin list view



