##========================================= Generators



# -------------- Basic generator

# def gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# g = gen()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))



# -------------- Looping with generators

# def gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5


# for num in gen():
#     print(num)




# -------------- Range-like generator

# def my_range(n):
#     i = 0

#     while i < n:
#         yield i
#         i += 1

# for x in my_range(5):
#     print(x)



# -------------- Generator Expression

# nums = (x*x for x in range(5))

# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))



# -------------- Multiple Yield States

# def flow():
#     print("State 1")
#     yield 1

#     print("State 2")
#     yield 2

#     print("State 3")
#     yield 3

# g = flow()

# print(next(g))
# print(next(g))
# print(next(g))




