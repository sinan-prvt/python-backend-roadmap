# =================================== SQL Clauses 



# --------------- SELECT Clause

# SELECT * FROM table_name;



# --------------- FROM Clause

# SELECT column1, column2 FROM table_name;



# --------------- WHERE Clause

# SELECT * FROM Employees
# WHERE age >= 18;




# --------------- ORDER BY Clause

# SELECT * FROM Employees
# ORDER BY name ASC;              -- Sort by name in ascending order
# ORDER BY age DESC;              -- Sort by age in descending order




# --------------- GROUP BY Clause

# SELECT department, COUNT(*) AS employee_count
# FROM Employees
# GROUP BY department;



# --------------- HAVING Clause

# SELECT department, COUNT(*) AS employee_count
# FROM Employees
# GROUP BY department
# HAVING COUNT(*) > 5;              -- Filter groups with more than 5 employees




# --------------- DISTINCT Clause

# SELECT DISTINCT department FROM Employees;    -- Get unique department names from Employees table



# -------------- LIMIT Clause

# SELECT * FROM Employees
# LIMIT 10;              -- Retrieve only the first 10 rows from the Employees table




# --------------- IN Clause

# SELECT * FROM Employees
# WHERE department IN ('HR', 'IT');    -- Retrieve employees from HR and IT departments




# --------------- BETWEEN Clause

# SELECT * FROM Employees
# WHERE age BETWEEN 25 AND 35;    -- Retrieve employees aged between 25 and




# --------------- LIKE Clause

# SELECT * FROM Employees
# WHERE name LIKE 'A%';    -- Retrieve employees whose names start with 'A'
# WHERE name LIKE '%son';   -- Retrieve employees whose names end with 'son'
# WHERE name LIKE '%an%';   -- Retrieve employees whose names contain 'an'
# WHERE name LIKE '_a%';    -- Retrieve employees whose names have 'a' as the second character




# -------------- IS NULL Clause

# SELECT * FROM Employees
# WHERE email IS NULL;    -- Retrieve employees who do not have an email address




# -------------- IS NOT NULL Clause

# SELECT * FROM Employees
# WHERE email IS NOT NULL;    -- Retrieve employees who have an email address




# -------------- EXISTS Clause

# SELECT * FROM Employees e
# WHERE EXISTS (
#     SELECT 1 FROM Departments d
#     WHERE d.id = e.department_id
# );    -- Retrieve employees who belong to a department that exists in the Departments table




# -------------- ALL Clause

# SELECT * FROM Employees
# WHERE age > ALL (
#     SELECT age FROM Employees
#     WHERE department = 'HR'
# );    -- Retrieve employees whose age is greater than all employees in the HR department




# -------------- ANY Clause

# SELECT * FROM Employees
# WHERE age > ANY (
#     SELECT age FROM Employees
#     WHERE department = 'HR'
# );    -- Retrieve employees whose age is greater than any employee in the HR department








