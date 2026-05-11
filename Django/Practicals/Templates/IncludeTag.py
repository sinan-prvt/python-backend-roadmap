# =================================== Include Tag 



# --------------- Basic Example


## == navbar.html

# <nav>
#     <a href="/">Home</a>

#     <a href="/about/">About</a>

# </nav>



## == home.html

# {% include 'navbar.html' %}

# <h1>Welcome to the Home Page</h1>
# <p>This is the home page of our website.</p>    




# --------------- Navbar + Footer Example


## == navbar.html

# <nav>
#     <a href="/">Home</a>
#     <a href="/about/">About</a>
#     <a href="/contact/">Contact</a>
# </nav>



## == footer.html

# <footer>
#     <p>&copy; 2024 My Website</p>
# </footer>


## == home.html

# {% include 'navbar.html' %}

# <h1>Welcome to the Home Page</h1>
# <p>This is the home page of our website.</p>

# {% include 'footer.html' %}






