##========================================= Iterators



# -------------- Basic iterator

# nums = [1, 2, 3, 4, 5]

# it = iter(nums)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))




# -------------- Looping with iterators

# for num in [1, 2, 3, 4, 5]:
#     print(num)



# -------------- for Loop Works Internally

# it = iter([1, 2, 3, 4, 5])

# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         break



# -------------- Custom iterator

# class Count:
#     def __init__(self, max):
#         self.max = max
#         self.current = 0
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current < self.max:
#             self.current += 1
#             return self.current
#         else:
#             raise StopIteration
    
# c = Count(6)

# for num in c:
#     print(num)



# -------------- Check Iterator

# num = [1, 2, 3]

# it = iter(num)

# print(hasattr(num, "__next__"))
# print(hasattr(it, "__next__"))

