# =================================== POST Method



# --------------- Basic POST Method

## == Views.py

# from django.http import HttpResponse

# def home(request):
#     if request.method == "POST":
#         return HttpResponse("This is a POST request")
    



# --------------- POST Method with Form Data


## == Views.py

# from django.http import HttpResponse

# def home(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         return HttpResponse(f"Hello, {name}!")


## == login.html

# <form method="POST">
#     {% csrf_token %}
#     
#     <input type="text" name="name" placeholder="Enter your name">
# 
#     <button type="submit">Submit</button>
# </form>





# --------------- POST Method with JSON Data

## == Views.py


# from django.http import JsonResponse
# import json

# def home(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         name = data.get("name")
#         return JsonResponse({"message": f"Hello, {name}!"})
    



