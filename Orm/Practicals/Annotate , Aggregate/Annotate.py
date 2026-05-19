# =================================== Annotate 



# --------------- Basic Methods


## == models.py

# class Category(models.Model):
#     name = models.CharField(max_length=100)


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

# class Order(models.Model):
#     customer_name = models.CharField(max_length=100)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()




# --------------- Count Products Per Category

# from .models import Category
# from django.db.models import Count

# categories = Category.objects.annotate(
#     product_count=Count("product")
# )



# --------------- Count Orders Per Customer

# from .models import Order
# from django.db.models import Count

# categories = Category.objects.annotate(
#     total_order=Count("order")
# )




# --------------- Sum Total Order Amount Per Customer

# from .models import Order
# from django.db.models import Sum

# categories = Category.objects.annotate(
#     total_spend=Sum(order__total_amount)
# )




# --------------- Average Product Price Per Category

# from .models import Category
# from django.db.models import Avg

# categories = Category.objects.annotate(
#     avg_price=Avg("product__price")
# )




# --------------- Highest Product Price Per Category

# from .models import Category
# from django.db.models import Max

# categories = Category.objects.annotate(
#     max_price=Max("product__price")
# )




# --------------- Lowest Product Price Per Category

# from .models import Category
# from django.db.models import Min

# categories = Category.objects.annotate(
#     min_price=Min("product__price")
# )





# --------------- Multiple Annotation

# categories = Category.objects.annotate(
#     product_count=Count("product"),
#     avg_price=Avg("product__price"),
#     max_price=Max("product__price"),
#     min_price=Min("product__price")
# )





# --------------- Filtered Annotation

# categories = Category.objects.annotate(
#     expensive_product_count=Count(
#         "product",
#         filter=Q(product__price__gt=1000)
#     )
# )





