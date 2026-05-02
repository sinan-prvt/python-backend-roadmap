##========================================= Class



# -------------- Regular Class 

# class Student:
#     def __init__(self, name):
#         self.name = name
    
# s1 = Student("Sinan")
# s2 = Student("Mohamed")

# print(s1.name)
# print(s2.name)




# -------------- Parent Class

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# Animal().sound()




# -------------- Child Class

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# Dog().sound()




# -------------- Abstract Class

# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self):
#         pass




# -------------- Inner Class

# class Company:
#     class Employee:
#         def show(self):
#             print("Employee of the company")

# c = Company()
# c.Employee().show()




# -------------- Utility Class

# class JWTUtils:
#     @staticmethod
#     def generate_token():
#         pass