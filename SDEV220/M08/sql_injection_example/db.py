import sqlite3


def get_users():
    conn = sqlite3.connect('users.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM user;')
    rows = curs.fetchall()
    conn.close()
    return rows


def query_for_user_and_password(username, password):
    conn = sqlite3.connect('users.db')
    curs = conn.cursor()

    query = f'SELECT * FROM user WHERE user.username = "{username}" AND user.password = "{password}";'
    print(query)

    curs.execute(query)
    rows = curs.fetchall()
    conn.close()

    if len(rows) > 0:
        user = rows[0]
        u_t = user[1]
        return True, u_t
    return False, None


def query_for_user_and_password_escaped(username : str, password : str):
    try:
        conn = sqlite3.connect('users.db')
        curs = conn.cursor()
        username = username.replace('"', '""')
        username = username.replace("'", "''")

        password = password.replace('"', '""')
        password = password.replace("'", "''")

        query = f'SELECT * FROM user WHERE user.username = "{username}" AND user.password = "{password}";'
        print(query)

        curs.execute(query)
        rows = curs.fetchall()
        conn.close()

        if len(rows) > 0:
            user = rows[0]
            u_t = user[1]
            return True, u_t
    except Exception:
        print('bad sql')
    return False, None


def query_for_user_and_password_prepared(username : str, password : str):
    try:
        conn = sqlite3.connect('users.db')
        curs = conn.cursor()

        curs.execute('SELECT * FROM user WHERE user.username = ? AND user.password = ?;', (username, password))
        rows = curs.fetchall()
        conn.close()

        if len(rows) > 0:
            user = rows[0]
            u_t = user[1]
            return True, u_t
    except Exception:
        print('bad sql')
    return False, None
