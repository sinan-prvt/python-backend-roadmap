# =================================== select_related()



# --------------- Basic Methods

## == models.py

# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)

# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     order_date = models.DateTimeField(auto_now_add=True)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)





# --------------- Basic select_related() usage

# from .models import Order

# orders = Order.objects.select_related('customer')




# --------------- Accessing related data efficiently

# orders = Order.objects.select_related('customer')

# for order in orders:
#     print(order.customer.name)  




# --------------- Multiple select_related() fields

# orders = Order.objects.select_related('customer')



# --------------- Multiple relations

# orders = Order.objects.select_related(
#     'customer',
#     'customer__profile',
#     'customer__profile__address'
# )




# --------------- select_related with filter

# orders = Order.objects.select_related(
#     'customer'
# ).filter(
#     total_amount__gte=100
# )





# --------------- select_related with order_by

# orders = Order.objects.select_related(
#     'customer'
# ).order_by('-id')




# --------------- select_related with values

# orders = Order.objects.select_related(
#     'customer'
# ).values(
#     'id',
#     'total_amount',
#     'customer__name',
#     'customer__email'
# )




# --------------- select_related with only()

# orders = Order.objects.select_related(
#     'customer'
# ).only(
#     'id',
#     'total_amount',
#     'customer__name'
# )




