# =================================== Q Objects and Conditions



# --------------- Basic Conditions

## == models.py

# class Product(models.Model):
#     name = models.CharField(max_length=100)   
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     category = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)



# --------------- OR Condition

# from .models import Product
# from django.db.models import Q

# products = Product.objects.filter(
#     Q(category="Electronics") | Q(price__lte=500)
# )




# --------------- AND Condition

# products = Product.objects.filter(
#     Q(category="Electronics") & Q(price__lte=500) 
# )




# --------------- NOT Condition

# products = Product.objects.filter(
#     ~Q(category="Electronics")
# ) 




# --------------- Multiple OR Conditions

# products = Product.objects.filter(
#     Q(category="Electronics") | Q(category="Clothing") | Q(price__lte=500)
# )




# -------------- Complex Conditions

# products = Product.objects.filter(
#     (Q(category="Electronics") & Q(price__lte=500)) | Q(stock__gt=0)
# )




