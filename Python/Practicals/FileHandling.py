##========================================= File Handling



# -------------- Opening a File

# file = open("file.txt", "r")



# -------------- Reading a File

# file = open("file.txt", "r")

# data = file.read()
# print(data)

# file.close()



# -------------- Reading a File with

# with open("text.txt", "r") as file:
#     data = file.read()
#     print(data)



# -------------- Read method Read all

# file = open("text.txt", "r")
# data = file.read()

# print(data)
# file.close()



# -------------- Read method Read Line

# file = open("text.txt", "r")
# line1 = file.readline()
# line2 = file.readline()

# print(line1)
# print(line2)
# file.close()



# -------------- Read method Read all Lines

# file = open("text.txt", "r")
# lines = file.readlines()

# print(lines)
# file.close()



# -------------- Loop through file

# with open("text.text", "r") as file:
#     for line in file:
#         print(line)




# -------------- Writing to a File

# file = open("output.txt", "w")

# file.write("Hello World!")

# file.close()




# -------------- Appending to a File

# file = open("output.txt", "a")

# file.write("\nWelcome to Python!")

# file.close()



# -------------- Write multiple lines

# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

# with open("output.txt", "w") as file:
#     file.writelines(lines)



# -------------- Tell position 

# with open("text.txt", "r") as file:
#     print(file.tell())
    
#     print(file.read(5))
#     print(file.tell())



# -------------- Move pointer

# with open("text.txt", "r") as file:
#     file.seek(5)
#     print(file.read())




# -------------- Binary Mode writing

# with open("a.jpg", "rb") as file:
#     data = file.read()



# -------------- Binary Mode copying

# with open("a.jpg", "rb") as f1:
#     with open("b.jpg", "wb") as f2:
#         f2.write(f1.read()) 




# -------------- File Exist Checking

# import os

# if os.path.exists("text.txt"):
#     print("File exists")




# -------------- Exception Handling

# try:
#     with open("nonexistent.txt", "r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("File not found")



