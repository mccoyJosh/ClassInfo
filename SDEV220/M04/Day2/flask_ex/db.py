import sqlite3
from pathlib import Path

database_file = Path('app.db')
if database_file.is_file():
    print("DATABASE EXISTS")
    exit()

conn = sqlite3.connect('app.db')
curs = conn.cursor()

print("CREATING COMPANY TABLE")
curs.execute('''

CREATE TABLE company (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL
);
''')

print("CREATING EMPLOYEE TABLE")
curs.execute('''
CREATE TABLE employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cmp_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob DATE NOT NULL,
    FOREIGN KEY (cmp_id) REFERENCES company(id)
);
''')

print("INSERTING COMPANIES")
curs.execute('''
INSERT INTO company (name, address) VALUES 
('Big Ads Company', '123 Advertisement Way, LA, CA'),
('Big Products LLC', '096 Make Money Avenue, LA, CA');
''')

print("INSERTING EMPLOYEES")
curs.execute('''
INSERT INTO employee (cmp_id, first_name, last_name, dob)
VALUES (1, 'John', 'Smith', '1/1/1999'),
       (1, 'John', 'Smith', '1/1/1999'),
       (2, 'Bingus', 'Smingus', '1/1/1999'),
       (2, 'Walter', 'Halter', '1/1/1999'),
       (1, 'Cherish', 'Clinton', '1/1/1999');
''')

conn.commit()

conn.close()
