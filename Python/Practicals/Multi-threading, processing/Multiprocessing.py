##========================================= Multi-processing



# -------------- Basic Example

# from multiprocessing import Process

# def task():
#     print("Task running")

# p = Process(target=task)

# p.start()
# p.join()




# -------------- Multiple Processes

# from multiprocessing import Process

# def task():
#     print("Task running")

# p1 = Process(target=task)
# p2 = Process(target=task)

# p1.start()
# p2.start()

# p1.join()
# p2.join()




# -------------- Process with Arguments

# from multiprocessing import Process

# def greet(name):
#     print(f"Hello, {name}!")

# p = Process(target=greet, args=("Sinan",))

# p.start()
# p.join()




# -------------- CPU-bound Task

# from multiprocessing import Process

# def task():
#     total = 0

#     for i in range(10**7):
#         total += i

# p1 = Process(target=task)
# p2 = Process(target=task)

# p1.start()
# p2.start()

# p1.join()
# p2.join()




# -------------- Queue for Inter-process Communication

# from multiprocessing import Process, Queue

# def task(q):
#     q.put("Hello")

# q = Queue()

# p = Process(target=task, args=(q,))

# p.start()
# p.join()

# print(q.get())




# -------------- Process Pool

# from multiprocessing import Pool

# def square(x):
#     return x * x

# with Pool(4) as p:
#     result = p.map(square, [1, 2, 3, 4, 5])

# print(result)


