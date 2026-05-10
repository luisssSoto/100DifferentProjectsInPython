import sqlite3
import os

# Create the database in the current directory (Day 63)
db_path = os.path.join(os.path.dirname(__file__), 'example.db')
db = sqlite3.connect(db_path)
cursor = db.cursor()

# cursor.execute("CREATE TABLE books (" \
#                 "id INTEGER PRIMARY KEY," \
#                 "title varchar(250) NOT NULL UNIQUE," \
#                 "author varchar(250) NOT NULL," \
#                 "rating FLOAT NOT NULL )")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', 9.3)")
# db.commit()
cursor.execute("INSERT INTO books VALUES(2, 'The Lord of the Rings', 'J.R.R Tolkien', 10.0)")
db.commit()
