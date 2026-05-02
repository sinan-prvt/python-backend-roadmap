##========================================= map() function



# -------------- Double numbers

# nums = [1, 2, 3, 4, 5]

# result = map(lambda x: x * 2, nums)

# print(list(result))



# -------------- Square numbers

# nums = [1, 2, 3, 4, 5]

# result = map(lambda x: x*x, nums)

# print(list(result))





# -------------- Using normal function (not lambda)

# nums = [1, 2, 3, 4, 5]

# def square(n):
#     return n * n

# result = map(square, nums)

# print(list(result))




# -------------- Multiple iterables add two lists

# a = [1, 2, 3]
# b = [4, 5, 6]

# result = map(lambda x, y: x + y, a, b)

# print(list(result))




# -------------- Convert to uppercase

# name = ["sinan", "ahmet", "ayse", "mehmet"]

# result = map(lambda x: x.upper(), name)

# print(list(result))



# -------------- List Comprehension

# nums = [1, 2, 3, 4, 5]

# result = [x*2 for x in nums]

# print(result)



# -------------- Combine map + filter

# nums = [1, 2, 3, 4, 5]

# result = map(lambda x: x*x,
#              filter(lambda x: x % 2 == 0, nums))

# print(list(result))



