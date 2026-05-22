# =================================== Alternative Key



# --------------- Create Table with Alternative Key

# CREATE TABLE Employees (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(25) UNIQUE,
#     email VARCHAR(50) UNIQUE,
#     phone VARCHAR(15) UNIQUE
# );

###== here, 'name', 'email', and 'phone' are alternative keys because they are unique and can be used to identify records, but they are not the primary key.




# --------------- Insert Data into Table

# INSERT INTO Employees (name, email, phone)
# VALUES ('Alice', 'alice@example.com', '123-456-7890');



# --------------- Fetch Data Using Alternative Key

# SELECT * FROM Employees
# WHERE email = 'alice@example.com';




