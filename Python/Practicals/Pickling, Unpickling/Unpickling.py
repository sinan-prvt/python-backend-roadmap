##========================================= Unpickling



# -------------- Basic Example 


import pickle

with open("data.pkl", "rb") as file:
    result = pickle.load(file)

print(result)




