# Django Theory Notes


## What is Django

It is High-level, Open-source web framework in python that enables developers to build secure, scalable, and maintainable web application quickly.
It Follows the MVT Architecture pattern.


- Features :-   
    - MVT Architecture
    - Ripid Development
    - Batteries Included
    - Build-in Admin Interface
    - Powerful ORM
    - Security
    - Scalability
    - Cross-Platform


## Work Flow of Django

User Request (Browser) → WSGI/ASGI (wsgi.py/asgi.py) → Middleware (Security, Session, Auth, CSRF, etc.) → URL Dispatcher (urls.py) → View (views.py) → Models (models.py / ORM / Database) → Templates (HTML rendering) → Response (HttpResponse / JsonResponse) → Middleware (response phase) → Client (Browser)




## What is MVT

It represent Model, View, Template.
It similar like MVC but slightly diffrent.

- Model :-      
    It handle database layers (structure, queries, relationship).
    It uses Object Relational Mapper(ORM) it means no need to write SQL queries manually.

- View :-    
    It handle the business logic (what data to fetch, what rule to apply, etc).
    It connect the django models with templates.

- Templates :-          
    It is a HTML file with Django Template Language(DTL) to display data.
    It handles UI(HTML + CSS + JS).
    It combines static HTML with dynamic data from the view


## What is Virtual Environment

It is a isolated python environment for the project that keeps dependencies separate from other projects.


## What is Django Admin

It is auto-generated web-based interface that allows developers and site administrators to manage database content without writing any code.
It enables CRUD operations.



## What is URL Routing

It means mapping the URL to a specific view function.
It is the system that tell Django to which view to call when a user click a particular url.
Django user URL Dispatcher to map URL --> views



 
## What is View Engine

It is the part of the framework that handles user requests and returns responses.

- Types of Views :- 
    - Function Based View :-   
        It define as a function. 
        Accept a request object and return a responce object.

    - Class Based View :-   
        It define as a Class.
        Django provides Generic Class-Based Views.










