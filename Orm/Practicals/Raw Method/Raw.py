# =================================== raw() Methods



# --------------- Basic Methods

## == models.py

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     category = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)



# --------------- Basic raw() usage

# from .models import Product

# products = Product.objects.raw(
#     'SELECT * FROM app_product'
# )

# for product in products:
#     print(product.name)





# --------------- Filter Query

# products = Product.objects.raw(
#     'SELECT * FROM app_product WHERE price > 1000'
# )




# --------------- Parameterized Query

# products = Product.objects.raw(
#     'SELECT * FROM app_product WHERE price > %s',
#     [1000]
# )




# --------------- Multiple Conditions

# products = Product.objects.raw(
#     'SELECT * FROM app_product WHERE price > %s AND stock > %s',
#     [1000, 10]
# )




# --------------- Order By Clause

# products = Product.objects.raw(
#     'SELECT * FROM app_product ORDER BY created_at DESC'
# )





# --------------- Limit Query

# products = Product.objects.raw(
#     'SELECT * FROM app_product LIMIT 5'
# )




# --------------- Join Query

# products = Product.objects.raw(
#     '''
#     SELECT p.*, c.name as category_name
#     FROM app_product p
#     JOIN app_category c ON p.category_id = c.id
#     WHERE p.price > %s
#     ''',
#     [1000]
# )





# --------------- Aggregation Query

# products = Product.objects.raw(
#     '''
#     SELECT category, COUNT(*) as product_count
#     FROM app_product
#     GROUP BY category
#     '''
# )





