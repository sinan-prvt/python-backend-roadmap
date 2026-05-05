##========================================= Multi-threading



# -------------- Basic Example

# import threading

# def task():
#     print("Task executed")

# t = threading.Thread(target=task)

# t.start()
# t.join()




# -------------- Multiple Threads

# import threading

# def task():
#     print("Task executed")

# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)

# t1.start()
# t1.join()

# t2.start()
# t2.join()




# -------------- Thread with Arguments

# import threading

# def greet(name):
#     print(f"Hello, {name}!")

# t = threading.Thread(target=greet, args=("Sinan",))
# t.start()
# t.join()




# -------------- Multiple API calls

import threading
import time

def fetch():
    time.sleep(2)
    print("Data fetched")

threads = []

for _ in range(5):
    t = threading.Thread(target=fetch)
    threads.append(t)
    t.start()

for t in threads:
    t.join()



