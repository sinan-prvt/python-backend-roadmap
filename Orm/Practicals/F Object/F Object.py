# =================================== F Object



# --------------- Basic Methods

## == models.py

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     sold_count = models.IntegerField()


# --------------- Increment field

# products = Product.objects.update(
#     stock = F("stock") + 1
# )


# --------------- Decrement field

# products = Product.objects.update(
#     stock = F("stock") - 1
# )



# --------------- Increment product price by 1000

# products = Product.objects.update(
#     price = F("price") + 1000
# )



# --------------- Decrement product price by 1000

# products = Product.objects.update(
#     price = F("price") - 1000 
# )



# --------------- Calculate total revenue for each product

# products = Product.objects.annotate(
#     total_revenue = F("price") * F("sold_count")
# )



# --------------- Compare Two Fields

# products = Product.objects.filter(
#     stock__gt=F("sold_count")
# )




