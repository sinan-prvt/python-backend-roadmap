# =================================== Query Lookups



# --------------- Basic Methods


## == models.py

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     category = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)




# --------------- exact Lookup

# products = Product.objects.filter(name__exact="Laptop")



# --------------- iexact Lookup

# products = Product.objects.filter(name__iexact="laptop")



# --------------- contains Lookup

# products = Product.objects.filter(name__contains="top")



# --------------- icontains Lookup

# products = Product.objects.filter(name__icontains="TOP")



# --------------- gt (greater than) Lookup

# products = Product.objects.filter(price__gt=1000)



# --------------- gte (greater than or equal) Lookup

# products = Product.objects.filter(price__gte=1000)



# --------------- lt (less than) Lookup

# products = Product.objects.filter(price__lt=500)



# --------------- lte (less than or equal) Lookup

# products = Product.objects.filter(price__lte=500)



# --------------- in Lookup

# products = Product.objects.filter(category__in=["Electronics", "Books"])



# --------------- startswith Lookup

# products = Product.objects.filter(name__startswith="Lap")



# --------------- istartswith Lookup

# products = Product.objects.filter(name__istartswith="lap")



# --------------- endswith Lookup

# products = Product.objects.filter(name__endswith="top")




# --------------- iendswith Lookup

# products = Product.objects.filter(name__iendswith="TOP")



# -------------- range Lookup

# products = Product.objects.filter(price__range=(100, 500))




# --------------- date Lookup

# products = Product.objects.filter(created_at__date="2024-01-01")



# --------------- year Lookup

# products = Product.objects.filter(created_at__year=2024)



# --------------- month Lookup

# products = Product.objects.filter(created_at__month=1)



# --------------- day Lookup

# products = Product.objects.filter(created_at__day=1)



# --------------- isnull Lookup

# products = Product.objects.filter(stock__isnull=True)



# --------------- regex Lookup

# products = Product.objects.filter(name__regex=r"^Lap.*top$")



# --------------- iregex Lookup

# products = Product.objects.filter(name__iregex=r"^lap.*top$")



