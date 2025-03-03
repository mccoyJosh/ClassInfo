import db
rows = db.get_users()
print(type(rows))
for user in rows:
    print('\n\n_______________________________')
    print("USER:")
    print("\tid:", user[0])
    print("\tusername:", user[1])
    print("\tpassword:", user[2])
    print("\tadmin level:", user[0])

