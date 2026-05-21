# =================================== bulk_create() Method



# --------------- Basic bulk_create

## == models.py

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     category = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)


# --------------- Bulk Create Example

# products = [
#     Product(name="Laptop", price=999.99, stock=10, category="Electronics"),
#     Product(name="Smartphone", price=499.99, stock=20, category="Electronics"),
#     Product(name="Headphones", price=199.99, stock=15, category="Electronics"),
# ]

# Product.objects.bulk_create(products)



