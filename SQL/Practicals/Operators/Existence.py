# =================================== Existence Operators



# --------------- EXISTS Operator

# SELECT name FROM Employees e
# WHERE EXISTS (SELECT 1 FROM Departments d WHERE d.id = e.department_id);    

# -- Retrieve employee names where the department exists in the Departments table





# --------------- NOT EXISTS Operator

# SELECT name FROM Employees e
# WHERE NOT EXISTS (SELECT 1 FROM Departments d WHERE d.id = e.department_id);    

# -- Retrieve employee names where the department does not exist in the Departments table



