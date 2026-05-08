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

