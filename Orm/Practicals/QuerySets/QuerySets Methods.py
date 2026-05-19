# =================================== QuerySet Methods



# --------------- Basic Methods

## == models.py

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     category = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)



# --------------- Get all products

# from .models import Product

# products = Product.objects.all()




# --------------- Get a single product by ID

# product = Prodct.object.get(id=1)



# --------------- Filter products by category

# products = Product.objects.filter(category="Electronics")



# --------------- Multiple Filters

# products = Product.objects.filter(
#     category="Electronics",
#     price__lte=500
# )



# --------------- Exclude products out of stock

# products = Product.objects.exclude(stock=0)



# --------------- First Object

# product = Product.objects.first()



# --------------- Last Object

# product = Product.objects.last()




# --------------- Order products by price by ascending

# products = Product.objects.order_by("price")



# --------------- Order products by price by descending

# products = Product.objects.order_by("-price")




# --------------- Limit records

# products = Product.objects.all()[:5]




# --------------- Existence Check

# product = Product.objects.filter(name="Iphone").exists()




# --------------- Count Records

# products = Product.objects.filter(category="Electronics").count()




# --------------- Values

# products = Product.objects.values("name", "price")



# --------------- Values List

# products = Product.objects.values_list("name", flat=True)




# -------------- Distinct

# products = Product.objects.values("category").distinct()



# --------------- Update Records

# products = Product.objects.filter(
#     stock = 0
# ).update(stock = 10)



# --------------- Delete Records

# products = Product.objects.filter(stock=0).delete()



