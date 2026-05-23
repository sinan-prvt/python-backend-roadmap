# SQL Theory Notes


## What is SQL

It Stands for Structured Query Language.

It is a programming language used to communicate with the database.

With SQL we can store, retreive , update and manage data inside a database.




## What is Database 

It is an organized collectiion of data in a structured way so that it can be easilt accessed, managed and updated.

It can store huge amounts of data efficiently, supports multi-users access at the same time, prevent data redundancy and ensure data security

- Types of data stored in Database :-
    - Textual Data :- Names, Address, Notes, etc..
    - Numerical Data :- Age, Salary, Price, etc..
    - Date/Time :- Order date, login Time, etc..
    - Multimedia :- Images, Videos, etc..




## What is DBMS

It Stands for DataBase Management System.

It is a Software tool that allows as to create, store, organize and manage data in database.


- Types of DBMS
    - RDBMS :-      
        It Stand for Relational Database Management System
        It stores data in the tables with raws and coloumns.
        It is used SQL

    - NoSQL DBMS :-     
        It stored data as JSON, key-value or documents.
        It for unstructured and large scale data.
        Eg :- MongoDB, Cassandra

    - Hierarchical DBMS :-      
        It stored data as tree structured.
        Eg :- IBM IMS
    
    - Network DBMS :-       
        It stored data as nodes and connections.
        Eg :- Integrated Data Store (IDS)




## What is PostgreSQL

It is a Open-source, Powerful Object Relational Database Management System (ORDBMS).

It stored data as tables and also support JSON and many powerful tools like MVIC, rich indexing, etc..

It Support SQL and NoSQL. It used cross platforms, and It is free and Open-source.


- Basic Postgres Workflow :-    
    - Create a Database :-      
        [ CREATE DATABASE name; ]
    
    - Connect to Database :-        
        [ \c name; ]
    
    - Create a Table :-         
        [ 
            CREATE TABLE name (
                id SERIAL PRIMARY KEY,
                name VARCHAR(25),
                age INT,
                department VARCHAR(50)
            );
        ]

    - Insert Data :-        
        [
            INSERT INTO name(name, age, department)
            VALUE ('Sinan', 19, 'IT'),
                  ('Mohamed', 34, 'HR');
        ]

    - Query Data :-     
        [ SELECT * FROM name; ]




## What is Table

It is a collection of data that organized into rows and columns inside a database.

It is the physical structure we can see in the database.

Each row represent a record and each column represent a field.

    - Columns = fields/attributes (like name, age, salary).
    - Rows = records/tuples (actual data entries).





## What is Relation

In relational database theory, a relation is a mathematical concept a set of rows that share same set of columns.




## What is Key

It is a attribute or set of attribute that used to uniquely identify a row in a table.

- Types of Keys :-  
    - Primary Key :-    
        It Uniquely idetify each row in a table.
        It cannot be NULL and Cannot Repeat

    - Candidate Key :-      
        A column or set of column that qulaify as primary key.
        Only one choose as Primary Key

    - Alternate Key :-      
        Candidate key not chosen as Primary key.

    - Unique Key :-         
        Ensure all values in a column are unique but allow one NULL.

    - Foreign Key :-    
        A column in one table refers to the primary key of another table.

    - Composite Key :-      
        A primary key made up with multiple columns.

    - Super Key :-      
        Any set of a column that can uniquely idenify a row.

    


## What is Constraints

It is rules applies on columns and tables to ensure valid and consistent data.

Key are type of constraint.


- Types of Constraints :-   
    - NOT NULL :-       
        It ensure a column cannot have NULL value

    - UNIQUE :-     
        It ensure all values in column are differnt
        
    - PRIMARY KEY :-        
        It Uniquely identify each row in table.

    - FOREIGN KEY :-        
        A column in one table that refers to the primary key of another table.

    - CHECK :-      
        It ensure the values meet a condition

    - DEFAULT :-        
        It assigns a default value if none is provided.

    - INDEX :-      
        It like indexing in the book.
        It helps to quickly find information without scanning the entire table.

    


## What is SQL Clauses

It is a keyword or set of keywords that performs a specific task in the query.

- Common Clauses :- 
    - SELECT :-     
        It Specifies which columns we want to retrieve from the table.
        It is mandatory in almost all queries.
    
    - FROM :-       
        It specifies the tables from which data retrieve in a SQL query.

    - WHERE :-      
        It used to filter rows and returned by query based on condition.
    
    - ORDER BY :-       
        It used to sort the rows and returned by query based on one or more columns.
    
    - GROUP BY :-       
        It used to group the rows that have same values in the specified columns into summary rows.
    
    - HAVING :-     
        It used to filter groups of rows after aggregation.
        It used when GROUP BY is used.
    
    - DISTINCT :-       
        It is used to remove duplicates rows.
    
    - LIMIT / TOP :-        
        It is used to restrict the number of rows returned by the query.
        - LIMIT :- Used in PostgreSQL, MySQL, SQLite.
        - TOP :- Used in SQL Server, MS Access.
    
    - JOIN :-       
        It is used to combines rows from two or more tables based on related columns.
    
    - IN :-         
        It is used to check if the value exist in the list.
    
    - BETWEEN :-        
        It is used to check if the value is within in range.

    - LIKE :-       
        It is used to pattern matching with % and _ 





## What is Operators

It are symbols or keywords used to perform operations on values, columns, or expressions.


- Types of Operators :-     
    - Arithmetic Operators :-       
        It used for math calculation on numeric data
    
    - Comparison Operators :-   
        It compare values and return TRUE/FALSE

    - Logical Operators :-      
        It combines multiple conditions
    
    - Bitwise Operators :-      
        It work on binary representation of numbers

    - Range Operators (Between) :-      
        It used to filter values within a range (inclusive)

    - Set Operators (IN / NOT IN) :-        
        Check if a value exists in a list or subquery 
    
    - Pattern Matching Operators (LIKE , ILIKE, Wildcards) :-       
        It used to search string patterns

    - NULL Operators (IS NULL / IS NOT NULL) :-         
        It used for checking missing values
    
    - Existence Operators( EXISTS / NOT EXISTS) :-      
        Checks if a subquery returns results

    - Concatenation Operators :-    
        It is used to join strings together




