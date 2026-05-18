# =================================== Forms



# --------------- Basic HTML Form Example

## == Template

# <form method="POST">
#     {% csrf_token %}
    
#     <input type="text" name="username">

#     <button type="submit">
#         Submit
#     </button>
# </form>







# --------------- Handle Form Data Example

## == Views

# from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         return HttpResponse(f"Hello, {username}!")
#     return render(request, "home.html")






# --------------- Django Forms Example

## == Forms

# from django import forms

# class UserForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     age = forms.IntegerField()




## == Views

# from django.shortcuts import render
# from .forms import UserForm

# def home(request):
#     form = UserForm()

#     return render(request, "home.html", {"form": form})




## == Template

# <form method="POST">
#     {% csrf_token %}
    
#     {{ form }}

#     <button type="submit">
#         Submit
#     </button>
# </form>






# --------------- Form validation Example


## == Views

# from django.shortcuts import render
# from .forms import UserForm

# def home(request):

#     form = UserForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             print(form.cleaned_data)
        
#     return render(request, "home.html", {"form": form})





