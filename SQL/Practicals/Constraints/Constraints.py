# =================================== Constraints



# --------------- Create NOT NULL Column

# CREATE TABLE Employees (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(25) NOT NULL,
#     email VARCHAR(50) NOT NULL
# );



# --------------- Create UNIQUE Constraint

# CREATE TABLE Employees (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(25) UNIQUE,
#     email VARCHAR(50) UNIQUE
# );




# --------------- Create CHECK Constraint

# CREATE TABLE Employees (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(25),
#     age INT CHECK (age >= 18)
# );





# --------------- Create DEFAULT Constraint

# CREATE TABLE Employees (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(25),
#     department VARCHAR(50) DEFAULT 'General'
# );




# --------------- Create PRIMARY KEY Constraint

# CREATE TABLE Employees (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(25),
#     email VARCHAR(50)
# );




# --------------- Create FOREIGN KEY Constraint

# CREATE TABLE Departments (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(25) UNIQUE
# );

# CREATE TABLE Employees (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(25),
#     department_id INT,
#     FOREIGN KEY (department_id) REFERENCES Departments(id)
# );




