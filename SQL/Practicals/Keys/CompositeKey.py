# =================================== Composite Key



# --------------- Create Table with Composite Key

# CREATE TABLE Orders (
#     order_id INT,
#     product_id INT,
#     quantity INT,
#     PRIMARY KEY (order_id, product_id)
# );

### == here, the combination of 'order_id' and 'product_id' forms a composite key, which uniquely identifies each record in the Orders table.





# --------------- Insert Data into Table

# INSERT INTO Orders (order_id, product_id, quantity)
# VALUES (1, 101, 2), (1, 102, 1), (2, 101, 3);





# --------------- Fetch Data Using Composite Key

# SELECT * FROM Orders
# WHERE order_id = 1 AND product_id = 101;





# --------------- Update Data Using Composite Key

# UPDATE Orders
# SET quantity = 5
# WHERE order_id = 1 AND product_id = 101;





# --------------- Delete Data Using Composite Key

# DELETE FROM Orders
# WHERE order_id = 1 AND product_id = 102;




