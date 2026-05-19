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
    

