##========================================= NameSpace



# -------------- Access global variable

# x = 10

# def func():
#     print(x)

# func()



# -------------- View globals

# x = 10

# print(globals())



# -------------- Local namespace

# def func():
#     x = 5
#     print(x)

# func()



# -------------- View locals 

# def func():
#     x = 5
#     print(locals())

# func()



# -------------- Built-in namespace

# print(len("Hello"))

# print(type(5))



# -------------- Enclosing namespace

# def outer():
#     x = 50

#     def inner():
#         print(x)

#     inner()

# outer()



# -------------- Modify enclosing variable with nonlocal

# def outer():
#     x = 50

#     def inner():
#         nonlocal x
#         x = 26
    
#     inner()
#     print(x)

# outer()



# -------------- local wins in LEGB Rule

# x = 100

# def func():
#     x = 10
#     print(x)

# func()



# -------------- Enclosing wins in LEGB Rule

# x = 100

# def outer():
#     x = 50

#     def inner():
#         print(x)
    
#     inner()

# outer()




# -------------- Global wins in LEGB Rule

# x = 100

# def func():
#     print(x)

# func()



