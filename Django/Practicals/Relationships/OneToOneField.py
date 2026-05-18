# =================================== OneToOneField



# --------------- Basic Example

## == models.py

# class Profile(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#     )
#     bio = models.TextField()




# ------------------- Accessing Related Objects

## == models.py

# class Profile(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#     )
#     bio = models.TextField()



## == views.py

# Accessing the related User from a Profile instance

# profile = Profile.objects.get(id=1)





# ------------------------- Reverse Access

## == models.py

# class Profile(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#     )
#     bio = models.TextField()



## == views.py

# Accessing the related Profile from a User instance

# user = User.objects.get(id=1)
