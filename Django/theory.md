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


