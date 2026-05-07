##========================================= Inheritance



# -------------- Basic Inheritance

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
    
# class Cat(Animal):
#     pass

# c = Cat()
# c.sound()



# -------------- Child Extending Parent

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def bark(self):
#         print("Bark!")

# d = Dog()
# d.sound()
# d.bark()




# -------------- Method Overriding


# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# d = Dog()
# d.sound()




# -------------- super() Function

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("Dog barks")

# d = Dog()
# d.sound()




# -------------- Constructor Inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     pass

# d = Dog("Buddy")
# print(d.name)




# -------------- Parent Constructor with super()

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

# d = Dog("Buddy", "Golden Retriever")
# print(d.name)
# print(d.breed)






## ================================ Types of Inheritance


## ------------------ Single Inheritance


# -------------- Basic Example

# class Parent:
#     def greet(self):
#         print("Hello from Parent")

# class Child(Parent):
#     def greets(self):
#         print("Hello from Child")
    
# c = Child()
# c.greet()
# c.greets()





## ------------------ Multiple Inheritance


# -------------- Basic Example


# class Father:
#     def skills(self):
#         print("Programming")

# class Mother:
#     def skills(self):
#         print("Cooking")
    
# class Child(Father, Mother):
#     def skills(self):
#         Father.skills(self)
#         Mother.skills(self)
#         print("Sports")
    
# c = Child()
# c.skills()






## ------------------ Multilevel Inheritance


# -------------- Basic Example


# class Grandparent:
#     def legacy(self):
#         print("Legacy from Grandparent")

# class Parent(Grandparent):
#     def heritage(self):
#         print("Heritage from Parent")

# class Child(Parent):
#     def traits(self):
#         print("Traits from Child")
    
# c = Child()

# c.legacy()
# c.heritage()
# c.traits()





## ------------------ Hierarchical Inheritance


# -------------- Basic Example


# class Parent:
#     def greets(self):
#         print("Hello from Parent")

# class Son(Parent):
#     def greet(self):
#         print("Hello from Son")
    
# class Daughter(Parent):
#     def greet(self):
#         print("Hello from Daughter")

# s = Son()
# d = Daughter()

# s.greet()
# s.greets()

# d.greet()
# d.greets()




## ------------------ Hybrid Inheritance


# -------------- Basic Example


# class A:
#     def method_a(self):
#         print("Method A")

# class B(A):
#     def method_b(self):
#         print("Method B")

# class C(A):
#     def method_c(self):
#         print("Method C")

# class D(B, C):
#     def method_d(self):
#         print("Method D")
    
# d = D()

# d.method_a()
# d.method_b()
# d.method_c()
# d.method_d()




# -------------- Method Resolution Order (MRO)


# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     pass

# d = D()
# d.show()




