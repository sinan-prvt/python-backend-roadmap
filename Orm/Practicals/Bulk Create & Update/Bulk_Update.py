# =================================== bulk_update Method



# --------------- Basic bulk_update

## == models.py

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     category = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)





# --------------- Bulk Update Example

# products = Product.objects.all()

# for product in products:
#     product.stock = 100

# Product.objects.bulk_update(products, ['stock'])




# --------------- Bulk Update with Multiple Fields

# products = Product.objects.all()

# for product in products:
#     product.stock = 100
#     product.price = product.price * 0.9  # Apply a 10% discount

# Product.objects.bulk_update(products, ['stock', 'price'])




# --------------- Bulk Update with Filter

# products = Product.objects.filter(category="Electronics")

# for product in products:
#     product.stock = 100

# Product.objects.bulk_update(products, ['stock'])






