##========================================= Decorators



# -------------- Basic Example

# def decorator(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")

#     return wrapper

# def greet():
#     print("hello")

# result = decorator(greet)
# result()



# -------------- Using @ syntax

# def decorator(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")
    
#     return wrapper

# @decorator
# def greet():
#     print("hello")

# greet()



# -------------- Decorator with arguments

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before")

#         result = func(*args, **kwargs)

#         print("After")

#         return result

#     return wrapper

# @decorator
# def add(a, b):
#     return a + b

# print(add(4, 5))



# ------------- Decorator Returning Value

# def decor(func):
#     def wrapper():
#         result = func()

#         return result.upper()
    
#     return wrapper

# @decor
# def greet():
#     return "hello"

# print(greet())



# ------------- Decorator with Parameters

# def repeat(time):
#     def decorator(func):
#         def wrapper():
#             for _ in range(time):
#                 func()
        
#         return wrapper
    
#     return decorator

# @repeat(4)
# def greet():
#     print("Hello")

# greet()



# ------------- Built-in Decorator Example --> staticmethod

# class User:
#     @staticmethod
#     def greet():
#         print("Hello")

# User.greet()




# ------------- Built-in Decorator Example --> classmethod

# class User:
#     name = "Alice"

#     @classmethod
#     def greet(cls):
#         print(f"Hello, I am {cls.name}")
    
# User.greet()



# ------------- Built-in Decorator Example --> property

# class User:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
# user = User("Alice")
# print(user.name)



# ------------- Count Vowels using Decorator

# def decorator(func):
#     def wrapper(text):
#         vowels = "aeiouAEIOU"
#         count = 0

#         for char in text:
#             if char in vowels:
#                 count += 1
        
#         print(f"Number of vowels: {count}")

#         func(text)
    
#     return wrapper

# @decorator
# def display(text):
#     print(f"Input text: {text}")

# display("Hello World")
# display("Python is great")




# ------------- Reverse String using Decorator

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result[::-1]
    
#     return wrapper

# @decorator
# def greet(name):
#     return name

# print(greet("Sinan"))



# ------------- Palindrome Check using Decorator

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)

#         if result == result[::-1]:
#             print(f"{result} is a palindrome")
#         else:
#             print(f"{result} is not a palindrome")

#         return result
    
#     return wrapper

# @decorator
# def check(word):
#     return word

# print(check("madam"))
# print(check("hello"))



