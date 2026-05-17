# =================================== PATCH Method



# --------------- Basic PATCH Method


## == views.py

# from django.http import HttpResponse

# def home(request):
#     if request.method == "PATCH":
#         return HttpResponse("This is a PATCH request")
    




# --------------- PATCH Method with JSON Data

## == views.py

# from django.http import JsonResponse
# import json

# def update_product(request):
#     if request.method == "PATCH":
#         body = json.loads(request.body)

#         print(body)

#         return JsonResponse({"message": "Product updated successfully!"})





# -------------- PATCH Method with URL Parameters

## == views.py

# from django.http import HttpResponse

# def update_product(request, product_id):
#     if request.method == "PATCH":
#         return HttpResponse(f"Product with ID {product_id} updated successfully!")




