##========================================= Pass By Value



# -------------- Immutable Example (Looks like Pass by Value)

def change(x):
    x = x + 10

num = 5
change(num)

print(num)


