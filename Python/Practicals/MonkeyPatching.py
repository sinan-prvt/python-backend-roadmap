##========================================= Monkey Patching



# -------------- Basic Example

# def greet():
#     print("Hello")

# def new_greet():
#     print("Hi")

# greet = new_greet
# greet()




# -------------- Modify Class Method

# class User:
#     def greet(self):
#         print("Hello")

# def new_greet(self):
#     print("Hi")

# User.greet = new_greet

# u = User()
# u.greet()




# -------------- Add New Method to Class

# class User:
#     pass

# def greet(self):
#     print("Hello")

# User.greet = greet

# u = User()
# u.greet()




# -------------- Modify Object Only


# class User:
#     def greet(self):
#         print("Hello")
    
# u = User()

# def new_greet():
#     print("Hi")

# u.greet = new_greet

# u.greet()



