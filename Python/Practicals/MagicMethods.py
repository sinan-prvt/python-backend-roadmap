##========================================= Magic Methods (Special Methods / Dunder Methods)



# -------------- __init__ (Constructor)

# class User:
#     def __init__(self, name):
#         self.name = name

# u = User("Sinan")
# print(u.name)




# -------------- __str__ (Readable Output)


# class User:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"User: {self.name}"
    
# u = User("Sinan")
# print(u)




# -------------- __repr__ (Developer Output)

# class User:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"User(name='{self.name}')"
    
# u = User("Sinan")
# print(u)




# -------------- __len__ (Length of object)

# class Cart:
#     def __init__(self, items):
#         self.items = items

#     def __len__(self):
#         return len(self.items)
    
# c = Cart([1,2,3])
# print(len(c))




# -------------- __add__ (Addition)

# class Number:
#     def __init__(self, value):
#         self.value = value
    
#     def __add__(self, other):
#         return self.value + other.value

# n1 = Number(5)
# n2 = Number(10)

# print(n1 + n2)




# --------------- __sub__ (- operator)

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __sub__(self, other):
#         return self.value - other.value
    
# n1 = 8
# n2 = 3

# print(n1 - n2)




# -------------- __mul__ (* operator)

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __mul__(self, other):
#         return self.value * other.value

# n1 = 2
# n2 = 6

# print(n1 * n2)




# -------------- __eq__ (==)

# class User:
#     def __init__(self, id):
#         self.id = id

#     def __eq__(self, other):
#         return self.id == other.id

# u1 = User(1)
# u2 = User(1)

# print(u1 == u2)



# -------------- __lt__ (<)

# class Number:
#     def __init__(self, value):
#         self.value = value
    
#     def __lt__(self, other):
#         return self.value < other.value
    
# n1 = Number(5)
# n2 = Number(10)

# print(n1 < n2)



# -------------- __gt__ (>)

# class Number:
#     def __init__(self, value):
#         self.value = value
    
#     def __gt__(self, other):
#         return self.value > other.value
    
# n1 = Number(5)
# n2 = Number(10)

# print(n1 > n2)



# -------------- __getitem__

# class Data:
#     def __init__(self, items):
#         self.items = items

#     def __getitem__(self, index):
#         return self.items[index]

# d = Data([10, 20, 30])
# print(d[1])



# -------------- __setitem__

# class Data:
#     def __init__(self, items):
#         self.items = items

#     def __setitem__(self, index, value):
#         self.items[index] = value
    
# d = Data([10, 20, 30])
# d[1] = 25
# print(d.items)



# -------------- __delitem__

# class Data:
#     def __init__(self, items):
#         self.items = items

#     def __delitem__(self, index):
#         del self.items[index]

# d = Data([10, 20, 30])
# del d[1]
# print(d.items)




# -------------- __iter__

# class Numbers:
#     def __init__(self):
#         self.data = [1, 2, 3]

#     def __iter__(self):
#         return iter(self.data)

# for n in Numbers():
#     print(n)




# -------------- __call__

# class Greeter:
#     def __call__(self):
#         print("Hello")
    
# g = Greeter()
# g()




# ------------- __getattr__

# class User:
#     def __getattr__(self, name):
#         return "Not Found"

# u = User()
# print(u.age)




# ------------- __setattr__

# class User:
#     def __setattr__(self, key, value):
#         print("Settings", key)
#         super().__setattr__(key, value)
    
# u = User()
# u.name = "Sinan"
# print(u.name)




