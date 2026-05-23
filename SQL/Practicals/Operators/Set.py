# =================================== Set Operators



# --------------- IN Operator

# SELECT * FROM Employees
# WHERE department IN ('HR', 'IT');    -- Retrieve employees who work in HR or




# --------------- NOT IN Operator

# SELECT * FROM Employees
# WHERE department NOT IN ('HR', 'IT');    -- Retrieve employees who do not work




# -------------- UNION Operator

# SELECT name FROM Employees
# UNION
# SELECT name FROM Managers;    -- Retrieve unique names from both Employees and Managers tables




# -------------- UNION ALL Operator

# SELECT name FROM Employees
# UNION ALL
# SELECT name FROM Managers;    -- Retrieve all names from both Employees and Managers tables, including duplicates




