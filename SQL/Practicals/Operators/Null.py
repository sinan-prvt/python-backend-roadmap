# =================================== Null Operators



# --------------- IS NULL Operator

# SELECT * FROM Employees
# WHERE department IS NULL;    -- Retrieve employees whose department is NULL





# --------------- IS NOT NULL Operator

# SELECT * FROM Employees
# WHERE department IS NOT NULL;    -- Retrieve employees whose department is not NULL




# -------------- COALESCE Function

# SELECT name, COALESCE(department, 'Unknown') AS department
# FROM Employees;    -- Retrieve employee names and their departments, replacing NULL with 'Unknown'




# -------------- NULLIF Function

# SELECT name, NULLIF(department, 'HR') AS department
# FROM Employees;    -- Retrieve employee names and their departments, returning NULL if the department is 'HR'





