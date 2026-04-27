##========================================= Comprehension


## ========= List Comprehension


# -------------- Create list from 1 to 5

# num = [x for x in range(1, 6)]
# print(num)



# -------------- Square numbers

# num = [x * x for x in range(1, 6)]
# print(num)



# -------------- Cube numbers

# num = [x * 3 for x in range(1, 6)]
# print(num)



# -------------- Convert names to uppercase

# names = ["sinan", "mohamed"]

# result = [name.upper() for name in names]
# print(result)



# -------------- String length list

# words = ["python", "djangoo"]

# lenghts = [len(word) for word in words]
# print(lenghts)



# -------------- Even numbers

# evens = [x for x in range(1, 11) if x % 2 == 0]

# print(evens)



# -------------- Odd numbers

# odd = [x for x in range(1, 11) if x % 2 != 0]

# print(odd)



# -------------- Numbers greater than 10

# num = [5, 12, 7, 18, 3]

# result = [x for x in num if x > 10]
# print(result)



# ------------- Filter active users

# users = [
#     {"name": "Alice", "active": True},
#     {"name": "Bob", "active": False},
#     {"name": "Charlie", "active": True}
# ]

# active = [u for u in users if u["active"]]
# print(active)



# ------------- Label pass/fail

# scores = [85, 42, 78, 90, 55]

# result = [
#     "Pass" if score >= 60 else "Fail" 
#     for score in scores
# ]
# print(result)



# ------------- Flatten nested list

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# flat = [x for row in matrix for x in row]
# print(flat)



## ========= Dictionary Comprehension

# -------------- Square dictionary

# squares = {
#     x: x * x
#     for x in range(1, 6)
# }

# print(squares)



# -------------- Convert names to uppercase

# names = ["sinan", "mohamed"]

# result = {
#     name: name.upper()
#     for name in names
# }

# print(result)



# -------------- Create default config

# keys = ["host", "port", "debug"]

# config = {key: None for key in keys}
# print(config)



## ========= Set Comprehension

# -------------- Unique squares

# x = {x * x for x in [1, 2, 3, 2, 4]}
# print(x)



# -------------- Unique first letters

# names = ["Alice", "Bob", "Charlie", "David"]

# letters = {
#     name[0]
#     for name in names
# }

# print(letters)



## ========= Generator Expression

# -------------- Generator version

# gen = (
#     x * x
#     for x in range(5)
# )

# print(gen)



# -------------- Sum using generator

# total = sum(
#     x * x
#     for x in range(5)
# )

# print(total)