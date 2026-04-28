# Python Theory Notes


## What is Python

Python is a High Level, Interpreted, Object Oriented Programming Language with easy syntax, dynamic typing and a large library used for web development, data science, AI, automation, and more.


## What is Variables

They are Fundamental Building blocks in Python. It is a Container using for store data in memory


## What is Type Casting 

It is the process converting one data type to another data type


## What is Mutable

It means the value can be changed/modified after creation (list, set , dict, bytearray)


## What is Immutable

It means the value cannot be changed after creation 
(int, float, str, tuple, frozenset)


## What is Variable Scope

It defines where the variable can be accessed or modified


## What is Data Types

It is the Classification or Categorization of data items

- Numeric Data Type
    Int :- Whole Numbers (+ve, -ve)
    Float :- Decimal Numbers (3.23, -2.33)
    Complex :- Number with Real & Imaginary Part

- Sequence Data Type
    Str :- Text 
    List :- Ordered , Mutable Collection
    Tuple :- Ordered , Immutable Collection
    Range :- Immutable, Efficient for Looping

- Mapping Data Type
    Dict :- Mutable, unordered

- Set Data Type
    Set :- Unordered, Mutable Unique Value
    Frozenset :- Immutable version of set  

- Boolean Data Type
    Bool :- Logical Values (True/False)

- Binary Data Type
    bytes() :- Immutable sequence of bytes
    bytearray() :- Mutable sequence of bytes
    memoryview() :- access memory without copying

- None Data Type
    It represents absence of value


## What is Operators 

It is the Symbol or Keyword that Perform Operations on Variable and Value

- Arithmetic Operators :- ( +, -, *, /, //, %, ** )

- Comparison Operators :- ( ==, !=, >, <, <=, >= )

- Assignment Operators :- ( =, +=, -=, *=, /=, //=, %=, **= )

- Logical Operators :- ( and, or, not )

- Identity Operators :- 2 obj same memory ( is, is not )

- Membership Operators :- Value exists ( in, not in)

- Bitwise Operators :- ( &, |, ^, ~, <<, >> )


## What is Conditional Statement

It Control Program Flow using Boolean Logic 

- If Statement :-  
    It Execute a Block of Code if the Given Condition is True

- If-else Statement :-   
    it Execute a Block of Code based on Condition

- elif Statement :-   
    It Stands for else if when Multiple Condition is Occured

- Ternary Statement :-   
    It is Short-Hand for if-else Statement

- Match-Case Statement :-   
    It Pattern Matching like Switch Case and it to Handle Multiple Conditions



## What is Loop

It is used to Repeat a Block of Code Multiple times until a Condition is met

- For Loop :- It Iterates over a Sequence ( list, tuple, string, range, etc..)

- While Loop :- It Repeats until a Condition become False

- Nested Loop :- It Loop inside another Loop

- Control Statement in Loops :- 
    - break :- It Stop the Loop Immediately 
    - continue :- It Skip the Current Iteration and go to next
    - pass :- It is a Placeholder. It does nothing



## What is List

It is a collection data type that allows to store multiple items in a single variable.
It is Mutable and Ordered Collection of items defined with [].
It allows mixed data types

- Methods :- 
    - append() :- Add to Last
    - insert() :- Add with Index Number
    - extend() :- Add Multiple Items
    - remove() :- Remove with Item Name
    - pop() :- Remove last Item
    - clear() :- Remove All Items
    - sort() :- Sorting Items
    - sorted() :- Return New Sorted List without Modify Org List
    - reverse() :- Reversing Items
    - len() :- Find Length of Item 
    - index() :- Find the Position of item
    - count() :- Find Count Occurrence
    - copy() :- Shallow Copy
    - min() :- Smallest Number
    - max() :- Largest Number
    - sum() :- Sum of Number


## What is Tuple

It is Immutable Ordered Collection of data defined with ().
It allows Mixed Data Types.

- Methods
    - index :- It Return First Index

    - count :- It Return the No of Values Appears in Tuple

- Tuple Packing :- It putting multiple values together into one tuple object

- Tuple Unpacking :- It extracts tuple values into separate variables.



## What is Dictionary

It is Mutable, Unordered and Indexed collection of key-value pairs defined with {}.
It not allowed duplicate values.

- Methods :-
    - keys() :- Get all keys
    
    - values() :- It Access Dictionary Values
    
    - clear() :- It Remove all Items 
    
    - copy() :- Shallow Copy
    
    - items() :- It retrieves all (key, value) tuples
    
    - popitem() :- It remove & return (key,value) pairs in LIFO order
    
    - update() :- It add/update key-value pairs from another dict
    
    - setdefault() :- It get value for key if exist, else default & return



## What is set

It is Mutable, Unordered Collection of Unique Items defined with Curly Braces {}.
It not aloows duplicate values

- Methods :- 
    - add() :- Add a Single Item
    
    - update() :- Add Multiple Items
    
    - remove() :- It for Removing but there is no value it occurs error
    
    - discard() :- for Removing but there is no value it not occur error
    
    - pop() :- Removing Random Element
    
    - clear() :- Removing All Element
    
    - len() :- Find Number of Items
    
    - min() :- Find Smallest Item
    
    - max() :- Find Largest Item
    
    - sum() :- Find Sum of Number
    
    - sorted() :- Sorting Item

- Mathematical Set Operations :- 
    - Union ( | ) :- It Combining Sets , Removing Duplicates
    
    - Intersection ( & ) :- It Find Common Element
    
    - Difference ( - ) :- It Check element in “a” but not in “b”
    
    - Symmetric ( ^ ) :- It Check elements in either set but not both
    
    - Subset ( <= ) :- All elements of “a” are in “b”
    
    - Superset ( >= ) :- All elements of “b” are in “a” 
    
    - Proper Subset :- All elements in “a” in “b” and (a ≠ b) “a” must be smaller than “b”



## What is Comprehension 

It is a short and elegant way to create new sequences from existing sequences in a single line.

- Types of Comprehension :-
    - List Comprehension :- Create a list in a Single Line
    
    - Set Comprehension :- Like list , but Create a set (remove duplicates)
    
    - Dictionary Comprehension :- Create dict in One line
    
    - Generator Comprehension :- 	Like list, but use () instead of []
    
    - Nested Comprehensions


## What is String

It is a sequence of characters enclosed in single (''), double("") or triple quotes (""" or '''). 
It is Immutable squence of characters

- Methods :- 
    - upper() :- It convert into Upper Case
    
    - lower() :- It convert into Lower Case
    
    - capitalize() :- It Capitalize the first letter
    
    - title() :- It Capitalize the first letter of every word
    
    - strip() :- It remove leading & trailing Whitespaces
    
    - replace() :- It replace Old substring with new
    
    - split() :- It spits string into a list using separators
    
    - join() :- It Join elements of iterable into string
    
    - startswith(prefix) :- Check string start with given substring
    
    - endswith(suffix) :- Check string end with given substring
    
    - center(width, char) :- centered string with given width 
    
    - count() :- Count how many times a substring appears
    
    - find(substring) :- Find index
    
    - isalnum() :- return true if string contain only letter & numbers
    
    - isalpha() :- return true if string contains only letters
    
    - isdigit() :- return true if string contains only digit
    
    - islower() :- Check all characters in lower case
    
    - isupper() :- Check all characters in upper case
    
    - isspace() :- Check string contain only whitespaces
    
    - swapcase() :- Converts uppercase to lowercase & vice versa



## What is Function

It is a Reusable Building Block of code that perform specific task.
Instead of repeating the same code again and again, we define it once and call it whenever needed

- Types of Fuctions :-

    - Built-in Function :-   
        It is the Standard Function in Python that already available to use ( print(), len(), type() )
    
    - User defined Function :-   
        We can create our own functions based on our requirements. Use def to create
    
    - Lambda Function :-   
        It is a smallest anonymous function, written in one line using with lambda keyword

    - Recursion Function :-   
        It is the technique where a function call itself in order to solve a smaller part of the same problem

- Types of Function Arguments :- 
    - Default Argument :-  
        It is a function parameter that takes default value if the caller does not provide one

    - Keyword Argument :-  
        It is the way to passing argument to a function explicitly naming the parameter along with its value

    - Positional Argument :-   
        It is an argument is passed to a function in the correct order as defined in the functions parameter list

    - Variable Length Argument :-  
        - Arbitrary Positional Argument (*args) :-  
            It collects extra positional arguments into a tuple inside the function

        - Arbitrary Keyword Argument (**kwargs) :-  
            It collects extra keyword arguments into dictionary inside the function


- Types of Function based on Argument & Return value
    - Without Argument , Without Return Value :-  
        It does not take any input and does not return any value
    
    - With Argument, Without Return Value :-  
        It takes input but does not return a value
    
    - Without Argument , With Return Value :-  
        It does not take input but return a value
    
    - With Argument , With Return Value :-  
        It takes input and return a value
