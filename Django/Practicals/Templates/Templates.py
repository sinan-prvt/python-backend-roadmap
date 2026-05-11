# =================================== Templates



# --------------- Sending Data to Template


# == views.py

# from django.shortcuts import render

# def home(request):

#     data = {
#         "name" : "Sinan",
#         "age" : 19
#     }

#     return render(request, 'home.html', data)



# == templates/home.html

# <p>Name: {{ name }}</p>
# <p>Age: {{ age }}</p>





# --------------- Loop Example


# == views.py

# from django.shortcuts import render

# def home(request):

#     data = {
#         "products" : [
#             {"name": "Laptop", "price": 1000},
#             {"name": "Phone", "price": 500},
#             {"name": "Tablet", "price": 300},
#         ]
#     }

#     return render(request, 'home.html', data)



# == templates/home.html

# <ul>
#     {% for product in products %}
#         <li>{{ product.name }} - ${{ product.price }} </li>
#     {% endfor %}
# </ul>




# --------------- Database Loop Example


# == views.py

# from django.shortcuts import render
# from .models import Product

# def home(request):

#     products = Product.objects.all()
    
#     return render(request, 'home.html', {"products": products})



# == templates/home.html

# {% for product in products %}

#     <h1>{{ product.name }}</h1>
#     <p>Price: ${{ product.price }}</p>

# {% endfor %}





# --------------- if Condition Example

# {% if age >= 18 %}

#     <p>You are an adult.</p>

# {% else %}

#     <p>You are a minor.</p>

# {% endif %}




# --------------- Filter Example

# == views.py

# from django.shortcuts import render

# def home(request):
#     data = {
#         "name" : "Sinan",
#         "age" : 19
#     }

#     return render(request, 'home.html', data)


# == templates/home.html

# <p>Name: {{ name|upper }}</p>
# <p>Age: {{ age }}</p>

# <p>Name: {{ name|lower }}</p>

# <p>Name: {{ name|length }}</p>

# <p>Name: {{ name|default:"No Name Provided" }}</p>

# <p>Name: {{ name|truncatechars:3 }}</p>

# <p>Name: {{ name|title }}</p>

# <p>Date: {{ "2024-01-01"|date:"F j, Y" }}</p>

# <p>Safe String: {{ "<script>alert('Hello');</script>"|safe }}</p>



