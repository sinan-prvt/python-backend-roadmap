##========================================= Closure



# -------------- Simple closure


# def outer():
#     msg = "Hello"

#     def inner():
#         print(msg)

#     return inner

# greet = outer()
# greet()



# -------------- Addition closure


# def outer(x):
#     def inner(y):
#         return x + y
    
#     return inner

# add = outer(5)
# print(add(3))



# -------------- Multiplication closure

# def outer(x):
#     def inner(y):
#         return x * y
    
#     return inner

# mul = outer(4)
# print(mul(2))



# -------------- Counter Example

# def counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     return increment

# c = counter()

# print(c())
# print(c())
# print(c())




# -------------- Lambda Closure

# def power(n):
#     return lambda x: x ** n

# square = power(2)
# print(square(4))  


