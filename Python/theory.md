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

It is Mutable, Ordered and Indexed collection of key-value pairs defined with {}.
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



## What is Set

It is Mutable, Unordered Collection of Unique Items defined with Curly Braces {}.
It not allows duplicate values

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



## What is Module

It means a file contains Python code that can be imported and reused in other Python Programs

- Build-in Modules :- 
    - math :- Math operations (sqrt,pi,degree,redians,sin,cos,tan,etc)
    
    - random :- Generate Random Numbers
    
    - datetime :- It works with date and time
    
    - os :- Interact with Operating System
    
    - sys :- System-specific parameters & functions
    
    - json :- Work with JSON data


## What is Exception Handling

It is a Mechanism in Python to handle runtime errors so that the program doesn't crash and can continue execution

- Build-in Exception :- 
    - ValueError :- Invalid Value Type
    
    - TypeError :- Wrong Data Type Operation
    
    - IndexError :- Invalid Sequence Index
    
    - KeyError :- Missing Dictionary Key
    
    - FileNotFoundError :- File doesn't exist 
    
    - ZeroDivisionError :- Division by Zero (1/0)
    
    - ImportError :- Module not Found



## What is NameSpace

It is a place where python stores variable names, function names, class names and object names

- Types of NameSpace
    - Local Namespace :- Inside a function
    
    - Enclosing Namespace :- Nested Function
    
    - Global Namespace :- Outer function
    
    - Built-in Namespace :- Python Built-in functions


## What is Closure

It is the function defined inside another function that remembers the variables of outer function even after the outer function finished execution



## What is Decorator

It is a function that takes another function as input, and add extra behaviour and return a new function, without changing the original function code

- Types of Decorators :-
    - Function Decorator :-  
        It takes a function as input and return a new function
    
    - Method Decorator :-  
        It is used to decorate methods with a class
    
    - Class Decorator :-  
        It is used to modify and enhance the behaviour of class


- Built-in Decorators :-
    - @staticmethod :-   
        It is a method that does not access the instance (self) or Class (cls)
    
    - @classmethod :-  
        It is a method that receives the class(cls) as its first argument instead of an instance
    
    - @property :-  
        It covert a method into read only attribute



## What is Class

It is a blueprint or template used for creating objects that have attributes and methods.
It is defined with class keyword


- Types of Classes :-
    - Normal/Regular Class :-   
        It is Standard Class with Attribute (data) and Methods (function) for creating objects
    
    - Abstract Class :-   
        A class that is used only as a blueprint. It is not meant for direct object creation.
    
    - Concrete Class :-   
        Normal class with complete implementation.
    
    - Nested / Inner Class :-   
        Class defined inside another class
    
    - Derived / Child Class :-   
        Class that inherits from another class
    
    - Singleton Class :-    
        Class that allows only one object (instance) to be created throughout the program


- Methods in Class :- 
    - Instance Method :-  
        It works with an instance variable, Its first Argument is self. It accessed by Object 	
    
    - Class Method (@classmethod) :-  
        It works with class variables, Its first argument is cls. It accessed by class/Object
    
    - Static Method (@staticmethod) :-  
        It is a normal function inside class, It has no self or cls. It accessed by class/Object
    
    - Property Method :-  
        It is a special method that converts methods into read only attributes. It allows getter, setter, deleter for attributes


- Types of Variables :-
    - Instance Variable :-  
        Belong to each object. Declared using self inside __init__ or other instance methods. Each object gets its own copy.
    
    - Class Variable :-  
        Declared inside class but outside methods. Shared by all objects of that class. Accessed using Class.var or self.var.
    
    - Global Variable :-  
        Declared outside all classes/functions. Accessible everywhere unless shadowed by a local variable. Can be modified inside a function with global keyword



## What is object

It is the instance of a class that represents a real-world entity.
It is a collection of data and behaviour defined by its class

- Self Parameter :-   
    It is a reference to the current instance of the class. It allows us to access the attributes and methods of the object



## What is Special/ Magic/ Dunder Method

It is a special Method in Python with Double UnderScore(__) in start and end of a name.

- Methods :- 
    - __ init __ :-  
        Constructor method, automatically called when an object created
    
    - __ str __ :-   
        It is the Human-readable string representation of an Object ( for print() ) - for user
    
    - __ repr __ :-   
        It is the official string representation of an object. It make string unambiguous(it debugging)- for developers
     
    - __ add __ :-   
        It define the behavior of the + operator for objects of a class 
    
    - __ sub __ :-  
        It is used to overload the subtraction operator ( - ) 
    
    - __ mul __ :-   
        It is used to overload the multiplication operator ( * ) 
    
    - __ truediv __ :-  
        It is used to overload the division operator ( / ) 
    
    - __ del __ :-   
        It is Destructor method, automatically called when an object is deleted (or goes out of scope)
    
    - __ len __ :-   
        It define the behaviour of built-in function len() for custom object
    
    - __ call __ :-  
        It means make object behaviour like a function
    
    - __ eq __ :-   
        It define the behaviour of equality operator (==) for objects of a class
    
    - __ lt __ :-   
        It define the behaviour of less than operator (<)
    
    - __ gt __ :-   
        It define the behaviour of less than operator (<)
    
    - __ getitem __ :-  
        It define assign value using Indexing operator [ ]
    
    - __ setitem __ :-   
        It define the behaviour of less than operator (<)
    
    - __ delitem __ :-   
        It define the behaviour when use the del keyword with indexing
    
    - __ enter __ :-   
        It defines what happens when you enter a with block
    
    - __ exit __ :-   
        It defines what happens when you exit a with block



## What is Iterator

It is a object that allows to traverse through a collection of element one at a time.

- __ iter __() :-   
    It returns the iterator object itself

- __ next __() :-  
    It returns the next element from the collection. Raises StopIteration when no items are left



## What is Generator

It is a Function that produce values one at a time using with function and yield keyword instead of returning everthing at once 



## What is File Handling

It allows us to create, read, write, and modify files stored on the system. 
We use the built-in open() function to work with files.

- Modes :- 
    - r :- Read (default). A file must exist.
    
    - w :- Write. Creates a new file or overwrites if it exists.
    
    - a :- Append, Add data at end of file
    
    - x :- Create, Creates file but gives error if file already exists
    
    - t :- Text mode (default)
    
    - b :- binary mode (image, video, etc)
    
    - r+ :- Read + Write
    
    - w+ :- Write + Read (overwrite)
    
    - a+ :- Append + Read



## What is filter()

It is a function that select a collection of element based on a condition.

- Syntax :-  
    filter(function, iterable)  



## What is map()

It is a function that apply a function to every items in a collection.
map() returns an iterator, not a list.

- Syntax :-   
    map(function, iterable1, iterable2, ....)



## What is reduce()

It is a function that applies cumulatively to items in an iterable to produce a single value.
In simple take many values and compine and get one result.

- Syntax :-   
    from functools import reduce 
    reduce(function, iterable)



## What is zip()

It is a function that combaines multiple iterables in element-wise.
In simple take multiple list and pait their elements

- Syntax :-   
    zip(iterable1, iterable2, ....)



## What is enumerate()

It is a function that adds index to an iterable.
It means it get both index and value while looping

- Syntax :-    
    enumerate(iterable, start=0)



## What is Pass-by-Value

It is a copy of the actual value passed to the function.
It changes made to the inside the function do not affect the original variable of outside the function.



## What is Pass-by-reference

It means the function receives a reference to the original object, not a copy.
Changes made inside the function affect the original variable.



## What is Monkey Patching

It is dynamically modifying or extending a class, module, or object at runtime without changing its original source code.



## What is Global Interpreter Lock (GIL)

It is a mutex in CPython that ensures only one thread executes Python bytecode at a time within a single process.



## What is Multithreading

It is a technique in which running multiple tasks (threads) inside a single process, sharing the same memory space. 



## What is Multiprocessing

It is a technique in which multiple processes run concurrently, each with its own memory space, allowing true parallel execution on multiple CPU cores




## What is Pickling

It is the process of converting a python object into a byte stream so that it can be saved to a file or transferred over a network.



## What is Unpickiling

It is the process of converting a byte stream into a python object.
It is the reverse process of pickling.



## What is OOPS

It is Object Oriented Programming.
It organizes code into objects and classes which combine data and functions.

- Pillars of OOPS
    - Inheritance :-   
        It means a child class can reuse attributes and methods from the parent class 

        - Types of Inheritance :-   
            - Single Inheritance :-    
                A child class inherits from a single parent class.

            - Multiple Inheritance :-   
                A child class inherits from two or more parent class.

            - Multilevel Inheritance :-    
                A child class inherits from a parent class, and another class inherits from that child class

            - Hierarchical Inheritance :-    
                Multiple child class inherits form a parent class

            - Hybrid Inheritance :-    
                A combination of two or more types of inheritance.


    - Polymorphism
        It means it allows to have same name but behave differntly based on the object context

        - Types of Polymorphism :-
            - Compile-Time Polymorphism :-   
                It occurs when methods/operators has multiple forms, and the form to be used is determined at compile-time not run-time

                - Method Overloading :-   
                    It has multiple functions/methods with the same name but differnt parameter.
                    It supported in C, C++, Java, etc... not in python because python is dynamic typed.

            - Run-Time Polymorphism
                It occurs when the methods that is executed is determined at runtime

                - Method Overriding :-   
                    It occurs when a child class defined a method with the same name as a method in Parent class

                - Built-in / Duck typing
                    It means python dont care about the type of object, it only care about if the object has the method/behavior python want


    - Encapsulation
        It is bundling of data and methods together while restricting direct access to some data security and control.

        - Types of Encapsulation :- 
            - Public Encapsulation :-    
                Variables and Methods of a class are accessible from anywhere.
                Data Fully visible for everyone. No restricting on reading, accessing, and modifying  (obj.data)

            - Private Encapsulation :-    
                Variables and Methods are restricted to the class itself only (obj.data)

            - Protected Encapsulation :-    
                Variables and Methods of a class intended to be accessed only within the class and its subclasses. (obj.__data)

        - Name Mangled :-    
            It is the process in python that automatically changes the name of private variables (those starting with __ )


    - Data Abstraction
        It is the proccess of hiding implementation details and showing only the essetial features of an object to the users

        - Components of Abstraction :- 
            - Abstract class :-   
                It is a Class that cannot be instantiated directly and is meant to be inherited by other classes. It is implemented using the abc module.

            - Abstract method :-   
                Methods declared in an abstract class, but without implementation. Subclasses must implement them.

            - Concrete class :-    
                Classes that implement abstract methods. Can be instantiated normally.

            - Data Hiding :-   
                Helps abstraction by restricting access using private/protected variables.





- SOLID Principles
- Dependency Injection
- Design Patterns
- Repository Pattern
- Service Layer Pattern
- Factory Pattern
- Singleton
- Strategy Pattern
- Adapter Pattern
- identity vs equality
- __slots__
- descriptors
- callable objects
- enums
- namedtuple
- collections module
- heapq
- deque
- defaultdict
- OrderedDict
- Counter
- blocking vs non-blocking
- asyncio
- event loop
- coroutines
- aiohttp
- exception chaining
- logging module
- structured logging
- retry strategies
- graceful failure
- circuit breaker concepts
- unittest
- pytest
- mocking
- patching
- fixtures
- integration testing
- API testing
- test isolation
- coverage
- dependency mocking
- JWT internals
- idempotency




