# =================================== Cursor Methods



# --------------- Basic SELECT Query

# from django.db import connection

# with connection.cursor() as cursor:
#     cursor.execute("""
#         SELECT * FROM app_product
#     """)

#     rows = cursor.fetchall()

# print(rows)




# --------------- Fetch one row

# from django.db import connection

# with connection.cursor() as cursor:
#     cursor.execute("""
#         SELECT * FROM app_product
#     """)

#     rows = cursor.fetchone()

# print(rows)




# --------------- Fetch all

# rows = cursor.fetchall()




# --------------- Fetch many

# rows = cursor.fetchmany(5)





# --------------- Insert Query

# from django.db import connection


# with connection.cursor() as cursor:
#     cursor.execute("""
#         INSERT INTO app_product
#         (name, price, stock)

#         VALUES(%s, %s, %s)
    
#     """, ['New Product', 99.99, 50])





# --------------- Update Query

# with connection.cursor() as cursor:
#     cursor.execute("""
#         UPDATE app_product
#         SET price = %s
#         WHERE id = %s
#     """, [79.99, 1])      
                   



# --------------- DELETE Query

# with connection.cursor() as cursor:
#     cursor.execute("""
#         DELETE FROM app_product
#         WHERE id = %s
#     """, [1])




# --------------- Count Query

# with connection.cursor() as cursor:
#     cursor.execute("""
#         SELECT COUNT(*) FROM app_product
#     """)

#     count = cursor.fetchone()[0]
# print(count)





# --------------- SUM Query

# with connection.cursor() as cursor:
#     cursor.execute("""
#         SELECT SUM(price) FROM app_product
#     """)

#     total_price = cursor.fetchone()[0]




# --------------- Group By Query

# with connection.cursor() as cursor:
#     cursor.execute("""
#         SELECT category, COUNT(*) FROM app_product
#         GROUP BY category
#     """)

#     results = cursor.fetchall()




# --------------- Join Query

# with connection.cursor() as cursor:
#     cursor.execute("""
#         SELECT p.name, c.name FROM app_product p
#         JOIN app_category c ON p.category_id = c.id
#     """)

#     results = cursor.fetchall()




# --------------- Parameterized Query

# with connection.cursor() as cursor:
#     cursor.execute("""
#         SELECT * FROM app_product
#         WHERE price > %s
#     """, [1000])





