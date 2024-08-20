# import sqlite3

# conn = sqlite3.connect("movies.db")


# cur = conn.cursor()

# # sql_command = """
# # CREATE TABLE IF NOT EXISTS movie (
# #     title TEXT,
# #     year INTEGER,
# #     score REAL    
# # );
# # """
# # cur.execute(sql_command)

# # sql_command = """
# # INSERT INTO movie VALUES
# # ('MR A', 1996, 9.2),
# # ('MR B', 1997, 9.3),
# # ('MR C', 1998, 9.4);
# # """
# # cur.execute(sql_command)

# sql_command = """
#     UPDATE movie
#     SET year = 2000
#     WHERE title = 'Mr A';
# """
# cur.execute(sql_command)

# # lst = cur.fetchall()
# # print(lst)

# # for line in cur:
# #     print(line)

# # lst = cur.fetchone()
# # print(lst)

# conn.commit()


# conn.close()

import sqlite3

conn  = sqlite3.connect("books.db")

cur = conn.cursor()

# sql_command = """
#     CREATE TABLE book (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         author TEXT NOT NULL
#     )
# """


#cách tạo giá trị của TABLE 1
sql_command = """
    INSERT INTO book (name, author) VALUES
        ('Python Programming','John'),
        ('Clean Code','Jen')
"""

#Cách tạo ra giá trị của TABLE 2
sql_command2 ="""
    INSERT INTO book (name, author) VALUES (?, ?)
"""

lst = [
    ('CODE LEARNING', 'Jack'),
    ('TEST CODE', 'Jenny')
]

# cur.execute(sql_command)
cur.executemany(sql_command2,lst)

sql_command = """
    UPDATE book
    SET name = 'Marchine Learning'
    WHERE id=  1;
"""

cur.execute(sql_command)
conn.commit()

conn.close()