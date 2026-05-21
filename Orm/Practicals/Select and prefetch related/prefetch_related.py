# =================================== prefetch_related()



# --------------- Basic Methods

## == models.py

# class Customer(models.Model):
#     name = models.CharField(max_length=100)

# class Order(models.Model):
#     customer = models.ForeignKey(
#         Customer,
#         on_delete=models.CASCADE
#     )




# --------------- Basic prefetch_related() usage

# from .models import Author

# authors = Author.objects.prefetch_related('book_set')




# --------------- Accessing related data efficiently

# authors = Author.objects.prefetch_related('book_set')

# for author in authors:
#     print(author.book_set.all())




# --------------- reverse foreign key

# authors = Author.objects.prefetch_related('book_set')




# --------------- Multiple prefetch_related() fields

# authors = Author.objects.prefetch_related(
#     'book_set',
#     'book_set__publisher'
# )



# --------------- prefetch_related with filter

# authors = Author.objects.prefetch_related(
#     Prefetch(
#         'book_set',
#         queryset=Book.objects.filter(publication_year__gte=2000)
#     )
# )




