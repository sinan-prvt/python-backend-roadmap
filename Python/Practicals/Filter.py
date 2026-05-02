##========================================= filter() Function



# -------------- Filter even numbers

# nums = [1, 2, 3, 4, 5, 6]

# result = filter(lambda x: x % 2 == 0, nums)

# print(list(result))




# -------------- Filter odd numbers

# nums = [1, 2, 3, 4, 5, 6]

# result = filter(lambda x: x % 2 != 0, nums)

# print(list(result))



# -------------- Using normal function (not lambda)

# nums = [1, 2, 3, 4, 5, 6]

# def is_even(n):
#     return n % 2 == 0

# result = list(filter(is_even, nums))

# print(result)




# -------------- Filter names starting with 'A'

# names = ["sinan", "ahmet", "ayse", "mehmet"]

# result = filter(lambda name: name.startswith("a"), names)

# print(list(result))




# -------------- List Comprehension

# nums = [1, 2, 3, 4, 5, 6]

# result = [x for x in nums if x % 2 == 0]

# print(result)




