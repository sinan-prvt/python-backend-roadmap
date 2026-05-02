##========================================= Dictionary



# -------------- Access value using key


# x = {
#     "name": "Sinan",
#     "age": 19
# }

# print(x["name"])



# -------------- Using get() method

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# print(x.get("age"))



# -------------- Check keys 

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# print(x.keys())



# -------------- Check values

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# print(x.values())



# -------------- Check items

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# print(x.items())



# -------------- Add new key value pair

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# x["city"] = "Malapuram"
# print(x)



# -------------- Update value

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# x["age"] = 20
# print(x)



# -------------- Using update() method

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# x.update({"age": 21})
# print(x)



# -------------- Multiple updates 

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# x.update({"age": 22, "city": "Malapuram"})
# print(x)



# -------------- Remove using pop()

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# x.pop("age")
# print(x)



# -------------- Remove last item

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# x.popitem()
# print(x)



# -------------- Delete using del 

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# del x["name"]
# print(x)



# -------------- Clear dictionary

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# x.clear()
# print(x)



# -------------- Access nested value

# x = {
#     "name": "Sinan",
#     "age": 19,
#     "address": {
#         "city": "Malapuram",
#         "state": "Kerala"
#     }
# }

# print(x["address"]["city"])



# -------------- Using setdefault() method

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# x.setdefault("city", "Malapuram")
# print(x)



# -------------- Using fromkeys() method

# keys = ["name", "age", "city"]

# data = dict.fromkeys(keys, "Unknown")
# print(data)



# -------------- copy() method

# x = {
#     "name": "Sinan",
#     "age": 19
# }

# y = x.copy()
# print(y)