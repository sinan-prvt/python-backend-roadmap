# =================================== Aggregate Functions



# --------------- COUNT

# SELECT COUNT(*) AS total_employees FROM Employees;    -- Count total number of employees




# --------------- SUM

# SELECT SUM(salary) AS total_salary FROM Employees;    -- Calculate the total salary of all employees




# --------------- AVG

# SELECT AVG(salary) AS average_salary FROM Employees;    -- Calculate the average salary of employees




# --------------- MIN

# SELECT MIN(salary) AS minimum_salary FROM Employees;    -- Find the minimum salary among employees




# --------------- MAX

# SELECT MAX(salary) AS maximum_salary FROM Employees;    -- Find the maximum salary among employees




# -------------- GROUP_CONCAT

# SELECT department, GROUP_CONCAT(name) AS employee_names
# FROM Employees
# GROUP BY department;    -- Concatenate employee names by department




# ------------- STRING_AGG

# SELECT department, STRING_AGG(name, ', ') AS employee_names
# FROM Employees
# GROUP BY department;    -- Concatenate employee names by department with a comma separator



