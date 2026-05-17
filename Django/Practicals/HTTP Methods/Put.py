# =================================== PUT Method



# --------------- Basic PUT Method


## == views.py

# from django.http import HttpResponse

# def home(request):
#     if request.method == "PUT":
#         return HttpResponse("This is a PUT request")




# --------------- PUT Method with JSON Data

## == views.py

# from django.http import JsonResponse
# import json

# def update_product(request):
#     if request.method == "PUT":
#         body = json.loads(request.body)

#         print(body)

#         return JsonResponse({"message": "Product updated successfully!"})
    




# --------------- PUT Method with URL Parameters


## == views.py

# from django.http import HttpResponse

# def update_product(request, product_id):
#     if request.method == "PUT":
#         return HttpResponse(f"Product with ID {product_id} updated successfully!")
    




