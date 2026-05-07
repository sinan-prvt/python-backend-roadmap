##========================================= Data Abstraction



# -------------- Simple Abstraction

# class Car:

#     def start(self):
#         print("Car Started")

# c = Car()
# c.start()




# -------------- Basic ABC Example

# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self):
#         pass


# class CardPayment(Payment):

#     def pay(self):
#         print("Card Payment")

    
# c = CardPayment()

# c.pay()




# -------------- Multiple Implementations

# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self):
#         pass

# class CardPayment(Payment):

#     def pay(self):
#         print("Card Payment")
    
# class UPIPayment(Payment):

#     def pay(self):
#         print("UPI Payment")


# payments = [CardPayment(), UPIPayment()]

# for p in payments:
#     p.pay()




