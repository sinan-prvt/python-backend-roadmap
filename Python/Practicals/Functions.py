##========================================= Fuctions



# -------------- Function with parameter

# def add(name):
#     print("Hello " + name)

# add("Sinan")



# -------------- Function with return value

# def add(a, b):
#     return a + b

# # print(add(5, 6))

# result = add(5, 6)
# print(result)




# -------------- Multiple parameters

# def greet(name, age):
#     print(name, age)

# greet("Sinan", 19)




# -------------- Default value 

# def greet(name="Guest"):
#     print("Hello " + name)

# greet()
# greet("Sinan")



# -------------- Default boolean parameter

# def login(is_admin=False):
#     print(is_admin)

# login()
# login(True)




# -------------- Positional arguments

# def add(a, b):
#     print(a + b)

# add(5, 3)




# -------------- Keyword arguments

# def add(a, b):
#     print(a + b)

# add(b=3, a=2)



# -------------- Mixed 

# def add(a, b):
#     print(a + b)

# add(3, b=4)



# -------------- Variable number of arguments

# def total(*args):
#     print(sum(args))

# total(1, 2, 3)



# -------------- Keyword variable arguments

# def user(**kwargs):
#     print(kwargs)

# user(name="Sinan", age=19, city="Malapuram")



# -------------- Multiple return values

# def calc(a, b):
#     return a + b, a - b

# result = calc(5, 3)
# print(result)



# -------------- Function inside function

# def outer():
#     print("Outer function")

#     def inner():
#         print("Inner function")
    
#     inner()

# outer()



# -------------- Closure base

# def outer(x):
#     def inner(y):
#         return x + y
    
#     return inner

# add = outer(5)
# print(add(3))



# -------------- Simple lambda

# add = lambda a, b : a + b
# print(add(4, 6))



# -------------- Sort example

# user = [
#     {"age": 25},
#     {"age": 20},
#     {"age": 30}
# ]

# user.sort(key=lambda x: x["age"])
# print(user)



# -------------- Factorial using recursion

# def factorial(n):
#     if n == 1:
#         return 1
    
#     return n * factorial(n - 1)

# print(factorial(5))



# ------------- Without Argument, Without Return Value

# def greet():
#     print("Hello, World!")

# greet()



# ------------- With Argument, Without Return Value

# def greet(name):
#     print("Hello, " + name + "!")

# greet("Sinan")



# ------------- With Argument, With Return Value

# def get_pi():
#     return 3.14159

# print(get_pi())



# ------------- With Argument, With Return Value

# def add(a, b):
#     return a + b

# print(add(5, 3))

