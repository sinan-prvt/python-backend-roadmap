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





