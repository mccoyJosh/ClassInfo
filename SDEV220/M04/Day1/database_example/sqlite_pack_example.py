# Connecting to database
import sqlite3

conn = sqlite3.connect('company.db')  # does not need to exist
curs = conn.cursor()


# Creating a table
curs.execute('''
CREATE TABLE company(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL
);

''')


# Executing inserts and what nots
curs.execute("""
INSERT INTO company VALUES (1,'Big Ads Company', '123 Advertisement Way, LA, CA');
""")

curs.execute("""
INSERT INTO company(name,address)  VALUES ('Big Products LLC', '096 Make Money Avenue, LA, CA');
""")


# MAKE SURE YOU COMMIT, OTHERWISE YOUR ADDITIONS ARE NOT MADE
conn.commit()


# Accessing data
curs.execute('SELECT * FROM company;')
rows = curs.fetchall()
print(rows)


conn.close()