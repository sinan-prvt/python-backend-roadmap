##========================================= Pickling



# -------------- Basic Example


import pickle

data = {
    "name" : "Sinan",
    "age" : 19
}

with open("data.pkl", "wb") as file:
    pickle.dump(data, file)



