# =================================== OneToManyField



# --------------- Basic Example

## == models.py

# class Author(models.Model):
#     name = models.CharField(max_length=100)
    

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(
#         Author,
#         on_delete=models.CASCADE,
#         related_name='books'
#     )



# ------------------- Accessing Related Objects

## == models.py

# class Author(models.Model):
#     name = models.CharField(max_length=100)


# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(
#         Author,
#         on_delete=models.CASCADE,
#         related_name='books'  
#     )


## == views.py

# Accessing the related Author from a Book instance

# book = Book.objects.get(id=1)

# author = book.author
# print(author.name)





