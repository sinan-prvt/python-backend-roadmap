# =============================== Two Sum


# def twosum(nums, target):
#     seen = {}

#     for i, num in enumerate(nums):
#         complement = target - num

#         if complement in seen:
#             return [seen[complement], i]
#             return [complement, num]           # If we want to return the numbers instead of their indices

#         seen[num] = i

# nums = [2, 7, 11, 15]
# target = 9

# print(twosum(nums, target))





# =============================== unique pairs in Two Sum

# def unique_pairs(nums, target):
#     seen = set()
#     pairs = set()

#     for num in nums:
#         complement = target - num

#         if complement in seen:

#             pair = tuple(sorted((num, complement)))

#             pairs.add(pair)
#         seen.add(num)
    
#     return list(pairs)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 10

# print(unique_pairs(nums, target))







# =============================== Square Even Numbers Only

# nums = [1, 2, 3, 4, 5, 6]

# result = []

# for num in nums:
#     if num % 2 == 0:
#         result.append(num ** 2)
#     else:
#         result.append(num)
    
# print(result)






# =============================== reverse even numbers and odd numbers in a list


# nums = [1, 2, 3, 4, 5, 6]

# evens = []

# for n in nums:
#     if n % 2 == 0:
#         evens.append(n)

# evens.reverse()

# result = []
# index = 0

# for n in nums:
#     if n % 2 == 0:
#         result.append(evens[index])
#     else:
#         result.append(n)

# print(result)





# =============================== Move Even Numbers Front

# nums = [1, 2, 3, 4, 5, 6]

# even = []
# odd = []

# for n in nums:
#     if n % 2 == 0:
#         even.append(n)
#     else:
#         odd.append(n)

# print(even + odd)






# ============================== Reverse a String

# word = "Hello, World!"

# print(word[::-1])


# ## or

# n = "Hello, World!"
# rev = ""

# for ch in n:
#     rev = ch + rev

# print(rev)





# ============================== Vowel Count

# n = "Sinan"

# vowels = "aeiouAEIOU"
# count = 0

# for ch in n:
#     if ch in vowels:
#         count += 1
    
# print(count)


## or

# n = "Sinan"

# vowels = "aeiouAEIOU"
# li = []

# for ch in n:
#     if ch in vowels:
#         li.append("*")
#     else:
#         li.append(ch)
    
# print(" ".join(li))



## or


# def decorator(func):
#     def wrapper(text):
#         vowels = "aeiouAEIOU"
#         count = 0

#         for ch in text:
#             if ch in vowels:
#                 count += 1
        
#         print(f"Number of vowels: {count}")
    
#     return wrapper

# @decorator
# def show(word):
#     return word

# show("Sinan")






# ============================== Find Sum without sum()

# nums = [1, 2, 3, 4, 5]

# total = 0

# for ch in nums:
#     total += ch

# print(total)





# ============================== Find letters in a string

# n = "Hello, World!"
# letters = {}

# for ch in n:
#     if ch in letters:
#         letters[ch] += 1
#     else:
#         letters[ch] = 1
    
# print(letters)