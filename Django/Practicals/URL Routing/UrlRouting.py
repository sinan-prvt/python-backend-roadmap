# =================================== URL Routing in Django



# --------------- Basic URL Routing Example


# == urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home),
# ]



# == views.py

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Home Page!")




# --------------- Static URL Example

# == urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('about/', views.about),
# ]



# == views.py

# from django.http import HttpResponse

# def about(request):
#     return HttpResponse("This is the About Page!")





# --------------- Dynamic URL Example


# == urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('product/<int:id>/', views.product_details),
# ]



# == views.py

# from django.http import HttpResponse

# def product_details(request, id):
#     return HttpResponse(f"Details of Product with ID: {id}")




# --------------- String Parameter Example

# == urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('user/<str:name>/', views.user_profile),
# ]



# == views.py

# from django.http import HttpResponse

# def user_profile(request, name):
#     return HttpResponse(f"User Profile for: {name}")




# --------------- Query Parameter Example

# == urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('search/', views.search),
# ]



# == views.py

# from django.http import HttpResponse

# def search(request):
#     category = request.GET.get('category', 'All')

#     return HttpResponse(category)





# --------------- URL Namespacing Example

# == urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('blog/', views.blog_home, name='blog-home'),
# ]



# == views.py

# from django.http import HttpResponse

# def blog_home(request):
#     return HttpResponse("Welcome to the Blog Home Page!")




# --------------- include() Example

# == project urls.py

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('blog/', include('blog.urls')),
# ]



# == blog urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.blog_home, name='blog-home'),
# ]




