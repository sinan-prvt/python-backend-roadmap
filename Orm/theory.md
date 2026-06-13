# ORM Theory Notes


## What is ORM

It stands for Object Relational Mapping.

It is built-in feature in django that allows to developers to intract with database with python classes and methods instead of written raw sql queries.

In Django, models(Python classes) are mapped to database tables, and ORM automatically generates SQL queries behind the scenes.



## What is QuerySets

It is the collection of data retreived from the database.

It easier to get data only we need by letting you filtering, sorting and organize your data early on before actually fetching it from the database 


- QuerySets Methods :- 
    - all() :-      
        It is used to return all rows.

    - get() :-  
        It is used to retrieve a single object from the database that matches the given condition.
        If no object founded it raises DoesNotExist exception. If multiple object founded it raises MultipleObjectReturned exception.

    - filter() :-       
        It is used to retreive a querysets that matches the given conditions.
        In SQL terms filter translates the WHERE clause

    - exclude() :-    
        It is opposite of the filter method.
        It is used to return all objects that does not matches the given conditions.
        In SQL terms exclude translate WHERE NOT clause.

    - order_by() :-         
        It is used for sorting.
        "-" is used for reverse.
    
    - reverse() :-      
        It is used to reverse ordering.
    
    - first() :-    
        It is used to returned first object.

    - last() :-         
        It is used to returned last object.

    - count() :-    
        It is used to count rows.

    - exists() :-   
        It is used to check if record is exists.

    - create() :-       
        It is used to create new row.

    - update() :-       
        It is used to update row directly.

    - delete() :-   
        It is used to delete row.

    - values() :-       
        It is used to returns dictionaries.
    
    - values_list() :-      
        It is used to returns tuples.
        flat=True is lists the values.

    - distint() :-  
        It is used to remove duplicates.

    - latest() :-       
        It is used to gets latest row based on field.

    - earliest() :-         
        It is used to gets oldest row.
    



## What is Query Lookups

It is the special keyword that we use with filter, exclude, get methods to apply conditions on fields.

- Categories and Essential lookups :- 
    - exact :- Exact Match
    - iexact :- Case Insensitive exact
    - gt :- Grether than
    - gte :- Grether than or equal to
    - lt :- Less than
    - lte :- Less than or equal to
    - contains :- Case-sensitive text search
    - icontains :- Case Insensitive text search
    - startswith :- Check statswith
    - istartwith :- Check case insensitive startwith
    - endswith :- Check endswith
    - iendswith :- Check case insensitive endswith
    - in :- SQL in
    - range :- between
    - isnull :- Check is Null
    - year :- Year lookup
    - month :- Month lookup
    - day :- Day lookup
    - date :- date loopup
    - joined_year :- date lookup (year/month/day)
    - regax :- regex (DB-dependent)
    - iregax :- Case insensitive regax




## What is Q Object

It is used to built complex queries with OR, AND and NOT Conditions.

Normally, filter and exclude only combine with AND, if we need OR logic , nested complex condition we use Q Object.


- Conditions :- 
    - OR Condition :- With "|"
    - AND Condition :- With "&"
    - NOT Condition :- With "~"




## What is Annotate

It is used to add calculated value to each objects in Queryset.

It performs counting, averaging, summing, calculations, grouping, aggregations per row/object.




## What is Aggregate

It is a queryset method that is used to perform calculation on a set of rows in our database and return a single summary value.

It does not return multiple rows like filter() or all(). Instead it returns a dictionary with key and values being the computed result

- Common Functions :-   
    - Sum :- Total sum of a field
    - Avg :- 	Average
    - Max :- Maximum Value
    - Min :- Minimum Value
    - Count :- Number of Records



## What is F Object

It is a object that represent a model field value directly in the database.

It allows to reference a field’s value directly in queries, so we can perform database-side operations instead of fetching the object into Python




## What is Manager

In Django it is the gateway between the models and the database.
By default manager is object.




## What is Model Inheritance

It allows to create a new model based on one or more existing models, resuing field and functionality.

It helps to reuse common fields and create hierarchies in our database models

- Types of Model Inheritance :- 
    - Abstarct Base Classes :-      
        Parent Model won’t create a database table; only child models will.
        Its purpose is to share common fields and methods across models.
    
    - Multi-Table Inheritance :-      
        Each model gets its own database table.
        Django automatically creates a OneToOneField linking child to parent

    - Proxy Models :-       
        The child doesn't create a new table but allows to change behavior or add methods.
        Its purpose is to modify Python behaviour without changing DB structure.




## What is Meta Class

It is an inner class inside our model that is used to configure model metadata.

It tells Django how our model should behave in the database and the admin interface


- Model Meta Option :- 
    - abstract :-       
        It makes a model abstract base class(no db table),used to share fields/behaviours. 

    - app_label :-      
        If a model is denied outside a applications in INSTALLED_APPS, it must declare which app it belongs to 

    - verbose_name & verbose_name_plural :-         
        It human readable names shown in admin,messages

    - ordering :-       
        It is Default ordering for the queryset.

    - proxy :-      
        If we add proxy = True a model which subclasses another model will be treated as a proxy model

    - permissions :-        
        Declare custom model permissions that are created during migrations and visible in admin.

    - db_table :-       
        Force the DB table name for the model

    - get_latest_by :-      
        Field name used by Model.objects.latest() / earliest() when we call  them without arguments

    - indexes :-        
        Add database indexes for faster queries.

    - unique_together :-    
        Enforcing multiple fields together must be unique.

    - default_related_name :-       
        Custom reverse relation name.

    - constraints :-        
        Custom reverse relation name.

    - managed :-        
        Controls whether Django manages the database table.





## What is select_related()

It is a queryset method used to reduce database queries when fetching related object using ForeinKey and OneToOneField.

select_related() uses SQL JOIN to fetch related objects in a single query.




## What is prefetch_related()

It is a queryset method used t optimize the database queries for multi-values relationships like ManyToManyField and Reverse ForeignKey.

prefetch_related() fetches all related objects in a separate query and joins them in Python, reducing database hits.




## What is raw() Method

It is a raw sql query that allows to run directly in django and get model instance back.

It acts like bridge between raw SQL and ORM models

It’s part of Django’s QuerySet API.




## What is Cursor

It is a database object used to retreive, traverse and manipulate row returned by a query one at a time.

It like a pointer that moves throught rows returned by SQL query.


- Types of Cursor :- 
    - Implicit Cursors :-    
        Creates automatically by the database when executing DML statements(INSERT, UPDATE, SELECT, DELETE).

    - Explicit Cursors :-     
        We declare and control in explicitly. 
        Useful when you want fine-grained control over row-by-row processing.

    - Scrollaable Cursors :-     
        Allow moving forward and backward in the result set.
        Example: FETCH PRIOR, FETCH FIRST, FETCH LAST, FETCH ABSOLUTE n.

    - Static and Dynamic Cursors :-    
        Static → Snapshot of data; changes in table after cursor open are not reflected.
        
        Dynamic → Reflects changes in the underlying table (insert/update/delete).



- Cursor Methods :-     
    - cursor.execute(sql, params) :- 
        Executes SQL queries
    
    - cursor.executemany(sql, param_list) :- 
        Runs the same SQL with multiple parameter sets
    
    - cursor.fetchone() :- 
        Get one row
    
    - cursor.fetchall() :- 
        Get all row
    
    - cursor.fetchmany(n) :- 
        Get n row





## What is redirect()

It is a shortcut fuction in django to send the user to another URL.

It is often used after a form submission, login, logout, or any action that changes data.




## What is reverse_lazy()

It is a lazy version of reverse.

It resolves a URL pattern name into an actual URL, but only when it’s needed.

Useful in class-based views (CBVs), settings, or anywhere the URL needs to be evaluated later, not at import time.





## What is bulk_create()

It is a queryset method that is used to instert multiple model instance into the databse in a single query.

Instead of creating objects one by one, bulk_create() sends all objects at once




## What is bulk_update()

It is a queryset method that allows to update multiple model objects in the database in a single query, instead of saving them one by one 





## What is AbstractUser

It is a built-in Django class that provides a fully functional User model, but allows to extend or customize it.

It inherit from AbstractBaseUser and adds common user fields like ( username, first_name, last_name, email, is_staff, is_active, is_superuser, last_login, date_joined, password, plus related methods [ get_full_name(), get_short_name()]
, etc)




## What is AbstractBaseUser

It is the lowest-level base class for creating a fully custom User model in Django.


Unlike AbstractUser, it does not include fields like username, email, first_name, last_name, is_staff, etc… it only provides password, last_login, required methods like set_password(), check_password()








ffd
fdsfds
fd
sd
fsd
dsfds
fds
fd
sf
sdf
dsfds
fsdds
fsd
fsd
fs
sd
s
f
fsd
fd
sfd
fsd
fsd
sddsfd
sd
fds
sd
fds
fds
fds
fds
fds
fsd
d
fds
fsd
fsd
sd
sd
fsd
fsd
fsd

sd