# =================================== Candidate Key



# --------------- Create Table with Candidate Key

# CREATE TABLE Employees (
#     id SERIAL,
#     name VARCHAR(25),
#     email VARCHAR(50) UNIQUE
# );  

###== here, 'email' is a candidate key because it is unique and can be used to identify records, but it is not the primary key.



# --------------- Insert Data into Table

# INSERT INTO Employees (name, email)
# VALUES ('Alice', 'alice@example.com');




# --------------- Fetch Data Using Candidate Key

# SELECT * FROM Employees
# WHERE email = 'alice@example.com';




