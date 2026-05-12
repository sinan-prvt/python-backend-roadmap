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




## What is Models

It defines the structure of our database.
model is a Python class. Django convert it into a database table.

- Common Fields :- 
    - CharField :- Short text (requires max_length)
    - TextField :- Large text
    - IntegerField :- Whole numbers
    - PositiveIntegerField :- Only positive integers
    - BigIntegerField :- Large integers
    - FloatField :- Floating point numbers (approximate)
    - DecimalField :- Fixed-precision decimal (exact)
    - BooleanField :- True/False
    - DateField :- Date only
    - TimeField :- Time only
    - DateTimeField :- Date + Time
    - DurationField :- Time duration
    - EmailField :- Stores & validates email
    - URLField :- Stores URLs
    - SlugField :- SEO-friendly identifier
    - UUIDField :- Universally unique identifier
    - FileField :- Stores file uploads
    - ImageField :- Stores image uploads
    - BinaryField :- Stores binary data
    - AutoField :- Auto-increment integer (primary key)
    - BigAutoField :- Auto-increment big integer
    - ForeignKey :- Many-to-One relation
    - OneToOneField :- One-to-One relation
    - ManyToManyField :- Many-to-Many relation


- Types of Models :- 
    - Normal Model :-       
        Each class creates it's own table in the database.

    - Abstract Model :-     
        It is Used for code reuse.
        Don't create their own database.
        Provide common fields that child model inherits.

    - Proxy Model :- 
        It Don't create new table.
        It used for change behaviour of an existing model without duplicating the table.

    - Multi-Table Inheritance Model :-      
        It means each models gets its own table, but Djangolinks them together with OneToOneField.





## What is Template

Templates define how data is presented (UI).
Django Templates use Django Template Language (DTL) with {% %} and {{ }}.
A template is an HTML file that contains static parts (normal HTML) and dynamic placeholders where Django will insert data. 
Django uses a special system called Django Template Language (DTL).


- Key Concept :- 
    - Dynamic Variable :-   
        Syntax : {{ variable_name }}

    - Template Tags	:-    
        Logic Operations, Loops, Conditions, template inheritance

    - Filters :-    
        Modify Data Output

        - Common Filters :-     
            - upper :- Uppercase
            - lower	:- Lowercase
            - length :- Count
            - date :- Format date
            - truncatechars	:- Shorten text



## What is Template Inheritance

It allows you to reuse a common structure (base.html) across multiple pages using {% extends %}.



## What is Block Content

It means {% block content %} ... {% endblock %} defines a placeholder section in the base template where child templates can inject their content.




## What is Include Tag

It means reuse smaller parts like navbars or footers.




## What is Static Files

Static files (CSS, JS, images) are used for front-end styling.
Static files are files that don’t change dynamically


