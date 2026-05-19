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



