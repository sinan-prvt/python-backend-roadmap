# =================================== Models



# --------------- Basic Model Example

# from django.db import models

# class Product(models.Model):
    
#     name = models.CharField(max_length=100)
#     price = models.IntegerField() 



# --------------- Create Objects Example

# == Shell

# from products.models import Product

# Product.object.create(
#     name = "Laptop",
#     price = 1000
# )




# --------------- Fetch All Data Example



# products = Product.objects.all()

# print(products)



# --------------- Fetch Single Object Example

# product = Product.objects.get(id=1)

# print(product.name)



# -------------- Filter Data Example

# products = Product.objects.filter(price__gt=500)

# print(products)



# --------------- Update Object Example

# product = Product.objects.get(id=1)

# product.price = 1200

# product.save()



# --------------- Delete Object Example

# product = Product.objects.get(id=1)

# product.delete()



# --------------- EmailField Example

# class User(models.Model):

#     email = models.EmailField(unique=True)




# --------------- BooleanField Example

# class Product(models.Model):

#     is_available = models.BooleanField(default=True)




# --------------- DateTimeField Example

# class Product(models.Model):

#     created_at = models.DateTimeField(auto_now_add=True)




# --------------- Update Time Example

# class Product(models.Model):

#     updated_at = models.DateTimeField(auto_now=True)




# --------------- ImageField Example

# class Product(models.Model):

#     image = models.ImageField(upload_to='products/')




# --------------- TextField Example

# class Product(models.Model):

#     description = models.TextField()



# --------------- DecimalField Example

# class Product(models.Model):

#     price = models.DecimalField(
#         max_digit=10,
#         decimal_place=2
#     )



# --------------- ChoiceField Example

# class Product(models.Model):

#     STATUS = (
#         ('pending', 'Pending'),
#         ('completed', 'Completed'),
#     )

#     status = models.CharField(
#         max_length=20,
#         choices=STATUS,
#         default='pending'
#     )




# --------------- ForeignKey Example

# from django.db import models
# from django.contrib.auth.models import User

# class Order(models.Model):

#     user = models.ForeignKey(
#         User, 
#         on_delete=models.CASCADE
#     )

#     total = models.IntegerField()





# --------------- OneToOneField Example

# class UserProfile(models.Model):

#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE
#     )

#     bio = models.TextField()





# --------------- ManyToManyField Example


# class Tag(models.Model):
#     name = models.CharField(max_length=50)

# class Product(models.Model):
#     name = models.CharField(max_length=100)

#     tags = models.ManyToManyField(Tag)






## ================== Types of Models


# --------------- NORMAL MODEL 

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()



# --------------- ABSTRACT MODEL

# class BaseModel(models.Model):

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


# class Product(BaseModel):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()


# class Order(BaseModel):
#     total = models.IntegerField()




# --------------- PROXY MODEL

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()


# class ProductProxy(Product):

#     class Meta:
#         proxy = True
#         ordering = ["-id"]




# --------------- MULTI-TABLE INHERITANCE MODEL

# class Person(models.Model):
#     name = models.CharField(max_length=100)

# class Student(Person):
#     course = models.CharField(max_length=100)



