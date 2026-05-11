# =================================== Template Inheritance 



# --------------- Base Template (base.html)


## == base.html


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>My Website</title>
# </head>

# <body>
#     <header>
#         <h1>Welcome to My Website</h1>
#     </header>   

#     <nav>
#         <ul>
#             <li><a href="/">Home</a></li>
#             <li><a href="/about/">About</a></li>
#             <li><a href="/contact/">Contact</a></li>    
#         </ul>
#     </nav>

#     <main>
#         {% block content %} 
#         {% endblock %}
#     </main>

#     <footer>
#         <p>&copy; 2024 My Website</p>
#     </footer>
# </body>
# </html>




## == home.html

# {% extends 'base.html' %}

# {% block content %}

#     <h2>Home</h2>
#     <p>Welcome to the home page!</p>

# {% endblock %}



## == about.html

# {% extends 'base.html' %}

# {% block content %}

#     <h2>About</h2>
#     <p>This is the about page.</p>

# {% endblock %}




# -------------- block.super Example

## == base.html

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>My Website</title>
# </head>

# <body>
#     <header>
#         <h1>Welcome to My Website</h1>
#     </header>

#     <nav>
#         <ul>
#             <li><a href="/">Home</a></li>
#             <li><a href="/about/">About</a></li>
#             <li><a href="/contact/">Contact</a></li>
#         </ul>
#     </nav

#     <main>
#         {% block content %}
#         {% endblock %}
#     </main>

#     <footer>
#         <p>&copy; 2024 My Website</p>
#     </footer>

#     {% block extra_scripts %}
#     {% endblock %}    

# </body>
# </html>



## == home.html

# {% extends 'base.html' %}

# {% block content %}
#     <h2>Home</h2>
#     <p>Welcome to the home page!</p>

# {% endblock %}



## == about.html

# {% extends 'base.html' %}

# {% block content %}
# {% block.super %}

#     <h2>About</h2>
#     <p>This is the about page.</p>

# {% endblock %}





