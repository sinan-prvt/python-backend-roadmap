##========================================= Variable Scope 



# -------------- Local Variable Example

# def greet():
#     name = "Sinan"
#     print(name)

# greet()



# -------------- Global Variable Example

# name = "Sinan"

# def greet():
#     print(name)

# greet()



# -------------- Correct way to modify global

# x = 10

# def show():
#     global x
#     x = 14

# show()
# print(x)



# -------------- Counter Example

# count = 0

# def increment():
#     global count
#     count += 1

# increment()
# print(count)



# -------------- Nested Function

# def outer():
#     x = "Hello"

#     def inner():
#         print(x)
    
#     inner()

# outer()



# -------------- Modify outer variable

# def outer():
#     x = 10

#     def inner():
#         nonlocal x
#         x = 19
#         print(x)
    
#     inner()

# outer()


