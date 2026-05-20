# =================================== Aggregate



# --------------- Basic Methods


## == models.py

# class Category(models.Model):
#     name = models.CharField(max_length=100)

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)



# --------------- Count Total Products

# products = Product.objects.aggregate(
#     total_products=Count("id")
# )




# --------------- Total Revenue

# total_revenue = Product.objects.aggregate(
#     revenue=Sum("total_amount")
# )



# --------------- Average Product Price

# products = Product.objects.aggregate(
#     average=Avg("price")
# )




# --------------- Highest Product Price

# products = Product.objects.aggregate(
#     max_price=Max("price")
# )




# -------------- Lowest Product Price

# products = Product.objects.aggregate(
#     min_price=Min("price")
# )




# --------------- Multiple Aggregations

# products = Product.objects.aggregate(
#     total_products=Count("id"),
#     total_revenue=Sum("total_amount"),
#     average_price=Avg("price"),
#     max_price=Max("price"),
#     min_price=Min("price")
# )




