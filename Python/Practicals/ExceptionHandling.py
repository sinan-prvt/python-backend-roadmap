##========================================= Exception Handling



# -------------- Division Error

# try:
#     print(10/0)

# except ZeroDivisionError:
#     print("Cannot divide by zero.")



# -------------- Invalid int conversion

# try:
#     num  = int("abx")

# except ValueError:
#     print("Invalid input. Please enter a number.")



# -------------- List index error

# nums = [1, 2, 3]

# try:
#     print(nums[5])

# except IndexError:
#     print("Index out of range.")



# -------------- Dictionary key error

# user = {"name": "Sinan"}

# try:
#     print(user["age"])

# except KeyError:
#     print("Key not found in dictionary.")



# -------------- File not found

# try:
#     file = open("text.txt")

# except FileNotFoundError:
#     print("File not found.")



# -------------- Multiple exceptions

# try:
#     num = int("abc")
#     print(10 / num)

# except ValueError:
#     print("Invalid input. Please enter a number.")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")



# -------------- Multiple exceptions together

# try:
#     print(int("abc"))

# except (ValueError, ZeroDivisionError):
#     print("An error occurred.")




# -------------- else block

# try:
#     num = int("10")

# except ValueError:
#     print("Invalid input. Please enter a number.")

# else:
#     print(num, "is a valid number.")




# -------------- finally block

# try:
#     print(10/0)

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# finally:
#     print("This will always execute.")



# ------------- Manual raise

# age = -1

# if age < 0:
#     raise ValueError("Age cannot be negative.")



# ------------- Custom validation

# amout = 0

# if amout <= 0:
#     raise Exception("Amount must be greater than zero.")


