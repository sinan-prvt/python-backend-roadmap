# =================================== Primary Key



# --------------- Create Table with Primary Key

# CREATE TABLE Employees (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(25)
# );




# --------------- Insert Data into Table

# INSERT INTO Employees (name)
# VALUES ('Alice'), ('Bob'), ('Charlie');




# --------------- Fetch Data Using Primary Key

# SELECT * FROM Employees
# WHERE id = 1;




# --------------- Add Primary Key Later

## ----- Create Table Without PK

# CREATE TABLE employees (
#     id INT,
#     name VARCHAR(25)
# );



## ----- Add Primary Key

# ALTER TABLE employees
# ADD PRIMARY KEY (id);




# --------------- Drop Primary Key

# ALTER TABLE employees
# DROP CONSTRAINT employees_pkey;




# --------------- UUID as Primary Key

# CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

# CREATE TABLE products (
#     id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
#     name VARCHAR(50)
# );




