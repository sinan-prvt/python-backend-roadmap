##========================================= Polymorphism



# -------------- Basic Example

# class Cat:
#     def sound(self):
#         return "Meow"

# class Dog:
#     def sound(self):
#         return "Bark"
    
# c = Cat()
# d = Dog()

# c.sound()
# d.sound()




# -------------- Polymorphism with Inheritance

# class Animal:
#     def sound(self):
#         return "Animal makes a sound"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"
    
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
    
# animals = [Cat(), Dog()]

# for animal in animals:
#     print(animal.sound())




# -------------- Polymorphism with Functions

# class Cat:
#     def sound(self):
#         return "Meow"
    
# class Dog:
#     def sound(self):
#         return "Bark"
    
# def animal_sound(animal):
#     print(animal.sound())

# c = Cat()
# d = Dog()

# animal_sound(c)
# animal_sound(d)




# -------------- Method Overloading (Not Supported in Python)

# class Animal:
#     def sound(self, sound_type=None):
#         if sound_type == "loud":
#             return "LOUD SOUND"
#         elif sound_type == "soft":
#             return "soft sound"
#         else:
#             return "Animal makes a sound"
    
# a = Animal()
# print(a.sound())
# print(a.sound("loud"))
# print(a.sound("soft"))



# -------------- Operator Overloading

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1 + p2
# print(f"p1: ({p1.x}, {p1.y})")
# print(f"p2: ({p2.x}, {p2.y})")
# print(f"p3: ({p3.x}, {p3.y})")




# -------------- Duck Typing

# class Cat:
#     def sound(self):
#         print("Meow")
    
# class Human:
#     def sound(self):
#         print("Hello")
    
# def talk(obj):
#     obj.sound()
    
# talk(Cat())
# talk(Human())




