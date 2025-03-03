import sqlite3

conn = sqlite3.connect('users.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    admin_level INTEGER NOT NULL
);
''')

curs.execute("""
INSERT INTO user(username, password, admin_level)  VALUES 
('big_guy', 'p1', 0),
('admin', 'password', 9),
('dev_tom', 'password', 5),
('dev_jim', 'password', 2),
('small_fella', 'p2', 0),
('lumbo', 'p3', 0),
('silly', 'p4', 0),
('billy', 'p5',0)
;
""")

conn.commit()
conn.close()
