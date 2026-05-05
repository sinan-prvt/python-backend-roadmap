##========================================= Pass By Reference



# -------------- Mutable Example (Looks like Pass by Reference)


def add_items(lst):
    lst.append(10)

num = [1, 2, 3]

add_items(num)

print(num)



