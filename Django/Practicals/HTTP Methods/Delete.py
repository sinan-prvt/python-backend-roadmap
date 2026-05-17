# =================================== DELETE Method



# --------------- Basic DELETE Method

## == views.py

# from django.http import HttpResponse

# def home(request):
#     if request.method == "DELETE":
#         return HttpResponse("This is a DELETE request")





# --------------- DELETE Method with URL Parameters

## == views.py

# from django.http import HttpResponse

# def delete_product(request, product_id):
#     if request.method == "DELETE":
#         return HttpResponse(f"Product with ID {product_id} deleted successfully!")





# --------------- DELETE Method with JSON Data


## == views.py

# from django.http import JsonResponse
# import json

# def delete_product(request):
#     if request.method == "DELETE":
#         body = json.loads(request.body)

#         print(body)

#         return JsonResponse({"message": "Product deleted successfully!"})



