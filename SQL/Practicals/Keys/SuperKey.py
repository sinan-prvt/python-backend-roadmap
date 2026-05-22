# =================================== Super Key



# --------------- Create Table with Super Key

# CREATE TABLE Employees (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(25),
#     email VARCHAR(50) UNIQUE,
#     phone VARCHAR(15) UNIQUE
# );


### == here, 'id', 'email', and 'phone' are super keys because they can uniquely identify records in the table, but they are not necessarily the primary key.




# --------------- Insert Data into Table

# INSERT INTO Employees (name, email, phone)
# VALUES ('Alice', 'alice@example.com', '123-456-7890');



# --------------- Fetch Data Using Super Key

# SELECT * FROM Employees
# WHERE email = 'alice@example.com';



