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





# ============================== Count words in sentence

# n = "Hello, World! Hello everyone."

# words = n.split()
# freq = {}

# for ch in words:
#     freq[ch] = freq.get(ch, 0) + 1

# print(freq)





# ============================== convert list into dict with even and odd

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# res = {"even": [], "odd": []}

# for ch in nums:
#     if ch % 2 == 0:
#         res["even"].append(ch)
#     else:
#         res["odd"].append(ch)
    
# print(res)





# ============================== Palindrome Check

# n = "madam"

# if n == n[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")





# ============================== Factorial 

# num = 5
# fac = 1

# for i in range(1, num+1):
#     fac *= i

# print(fac)





# ============================== Fibonacci Sequence

# a, b = 0, 1

# for i in range(10):
#     print(a)

#     a, b = b, a + b




# ============================== Count Digits in a Number

# num = 12345

# count = 0

# while num > 0:
#     count += 1
#     num //= 10

# print(count)





# ============================== Reverse Word in a Sentence

# s = "Hello, World!"

# word = s.split()

# rev = " ".join(word[::-1])

# print(rev)





# ============================== Anagram Check

# s1 = "listen"
# s2 = "silent"

# if sorted(s1) == sorted(s2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")






# ============================== Multiplication Table

# num = 5

# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")





# ============================== Armstrong Number Check

# num = 153

# digit = [int(d) for d in str(num)]

# total = sum(d ** 3 for d in digit)

# if total == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")






