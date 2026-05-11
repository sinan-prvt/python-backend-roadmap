# =================================== Views



# --------------- Basic View Example

# == views.py


# from django.http import HttpResponse

# def Home(request):
#     return HttpResponse("Home Page")




# --------------- HTML Response Example

# == views.py


# from django.http import HttpResponse

# def about(request):

#     html = """
#     <h1>About Us</h1>
#     <p>We are a company dedicated to providing excellent services.</p>
#     """

#     return HttpResponse(html)





# --------------- render() Example

# == views.py


# from django.shortcuts import render

# def home(request):
    
#     return render(request, 'home.html')



# == templates/home.html


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Home Page</title>
# </head>
# <body>
#     <h1>Welcome to the Home Page!</h1>
#     <p>This page is rendered using the render() function.</p>
# </body>
# </html>





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





# --------------- Class Based View Example

# == views.py


# from django.views import View
# from django.http import HttpResponse

# class HomeView(View):

#     def get(self, request):
#         return HttpResponse("Welcome to the Home Page using Class Based View!")
    


# == urls.py

# from django.urls import path
# from .views import HomeView

# urlpatterns = [
#     path('', HomeView.as_view()),
# ]




