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





## What is Settings (settings.py)

It is the configuration file in Django Project.
It controls everthings like Database connections, middlewares, authentication, Installed apps, Security, templates, static files, etc...
Without Settings the Django wont know how to run the project.

- Default Files :- 
    - INSTALLED_APPS :-     
        List of all Django apps and third-party apps used in the project
        
        - Built-in apps :- 
            - admin :- Admin panel
            - auth :- Authentication
            - session :- Session management
            - messages :- Flash messages
            - staticfiles :- Static file handling

    - DATABASES :- 
        Controls Database connection

        - Common Database Engines :- 
            - SQLite
            - PostgreSQL 
            - MySQL
    
    - MIDDLEWARE :- 
        Act as middle man between user request and server response

    - Templates :- 
        Controls Django template system

    - STATIC_URL :- 
        Controls static file URL prefix

    - SECRET_KEY :- 
        Cryptographic key for sessions, passwords, CSRF protection, and tokens
 
    - DEBUG :- 
        Shows detailed error messages in development. False:Production mode(don’t expose internal errors)

    - ALLOWED_HOSTS :- 
        Defines which domains your Django site can serve.
        Prevents Host Header attacks.

    - LANGUAGE_CODE :- 
        Controls default language.

    - TIME_ZONE :- 
        It Controls timezone

    - USE_TZ :- 
        Timezone-aware datetime support
    
    - ROOT_URLCONF :- 
        Defines main URL router

    - WSGI_APPLICATION :- 
        Used for deployment

    - ASGI_APPLICATION :- 
        Modern async support

    - AUTH_USER_MODEL :- 
        Used for custom user model



## What is Routing 

It means mapping a url to a specific view function in app.


## What is Dynamic Routing

It means urls that accept variables/parameters instead of being fixed.

- Path Converts :- 
    - <int:pk> :- Interger Value
    - <str:username> :- String Value
    - <slug:slug> :- Slug for SEO friendly urls
    - <uuid:uuid> :- UUID Value
    - <path:path> :- Matches any path including /



## What is HTTP Methods

It is a standardized action type sent with an HTTP request.
 

- GET :-    
    Retrieve data from the server.
    Read Only.

- POST :-   
    Send data to the server.
    Used for creating new resourses or submitting forms.

- PUT :-    
    Updates the existing resources completely.
    Typically used in REST APIs

- PATCH :-      
    Updates parts of resource
    Often used in APIs for partial updates

- DELETE :-         
    Deletes an existing resource.
    Common in REST APIs



## What is Session

It is the way for store data for a specific users across multiple requests.
It unlike cokkies, Session data stored in the server side and the user keep only the session-id.
It alows to remember things like loggin-users, shopping carts, or temperary messages, etc...




## What is Cookies

It is small piece of data stored in user browers.
It is used to remember user information between the request.
It Unlike Session, It stired data in the client side and the server reads them on each request.




## What is forms

In Django forms is a Python class that represent an HTML form.
It handles :- Rendering HTML form elements and Receiving user input and validating input and saving data to the database.

- Types of forms :- 
    - Forms :-      
        It manual forms not directly linked to models
    
    - ModelForms :-     
        It Automatically linked to Django models, easy CRUD operations.

    


## What is Middleware

It act as a middle man between the user requets and response.
It’s a lightweight, low-level plugin that processes requests before they reach the view and responses before they are sent to the client.

It’s a Python class or function that processes:
	Request before reaching the view
	Response before sending back to the client




## What is WSGI

It stands for Web Server Gateway Interface
It is a interface that define how a web server communicates with python web applications or frameworks.
Synchronous: Handles one request at a time per worker.
It used by Django by default in traditional deployment (Gunicorn, uWSGI)




## What is ASGI

It stands for Asynchronous Server Gateway Interface.
It is modern interface for asynchronous communication.
It supports Websocket, long-polling, HTTP2, async views.
Used for real-time apps (chat apps, notifications).





## What is Relationships

It means in Django uses ORM relationships to links models together.

- Types of Relationships :- 
    - OneToOneField :-      
        One record in model A is related to exactly one record in Model B.
        Eg :- Each patients has one medical record.

    - OneToManyField :-     
        One record in Model A is related to many records in Model B.
        Eg :- One Doctor has many patients

    - ManyToManyField :-        
        Multiple records in Model A related to multiple records in Model B.
        A patient can have many diseases, and a disease can affect many patients.




## What is Manager

In Django it is the gateway between the models and the database.
By default manager is object.



## What is Signal

It is a messaging system that allows to different parts of an applications communicates with each others when a certain event/action occurs.

- Built-in Signals :- 
    - pre_save :- Before save
    - post_save	:- After save
    - pre_delete :- Before delete
    - post_delete :- After delete
    - m2m_changed :- ManyToMany changes
    - request_started :- Request starts
    - request_finished :- Request ends



## What is Makemigrations

It is a Django command that creates migration files based on changes in our models .
These migration files are Python instructions that describe how to modify the database schema


## What is migrate

It is the Django command that applies migration files to the actual database.
It looks at migration files (created by makemigrations) and runs the SQL commands needed to create or update tables.



