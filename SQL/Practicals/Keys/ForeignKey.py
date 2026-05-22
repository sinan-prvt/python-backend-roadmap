# =================================== Foreign Key



# --------------- Create Table with Foreign Key

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




# --------------- Insert Data into Table

# INSERT INTO Departments (name)
# VALUES ('HR'), ('Engineering'), ('Marketing');

# INSERT INTO Employees (name, department_id)
# VALUES ('Alice', 1), ('Bob', 2), ('Charlie', 3);




# --------------- Fetch Data Using Foreign Key

# SELECT e.name AS employee_name, 
# d.name AS department_name
# FROM Employees e
# JOIN Departments d 
# ON e.department_id = d.id;




# --------------- Update Foreign Key

# UPDATE Employees
# SET department_id = 2 
# WHERE name = 'Alice';



# --------------- Delete with Foreign Key

# DELETE FROM Departments
# WHERE id = 1;




