# =================================== GET Method



# --------------- Basic GET Method


## == Views.py

from django.http import HttpResponse

# def home(request):
#     if request.method == "GET":
#         return HttpResponse("This is a GET request")




# --------------- GET Method with Query Parameters


## == Views.py

# from django.http import HttpResponse

# def home(request):
#     search = request.GET.get("search")

#     return HttpResponse(search)




# --------------- GET Method with Multiple Query Parameters


## == Views.py

# from django.http import HttpResponse

# def home(request):
#     search = request.GET.get("search")
#     category = request.GET.get("category")

#     return HttpResponse(f"Search: {search}, Category: {category}")



