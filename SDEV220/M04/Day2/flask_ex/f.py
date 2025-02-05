# Imports flask
from flask import Flask, jsonify, request

app = Flask(__name__)


# Simple example: just returns a string at this index
@app.route('/')
def home_route():
    return 'Welcome to the root of our api'


# We can return whatever we want, including html
@app.route('/html')
def html_index():
    # Setting this up to read the file every time also makes the page update as we change it!
    file = open("t1.html", 'r')
    html_content = file.read()
    file.close()
    return html_content


# BUT HOW DO WE MAKE A RESTFUL API
import sqlite3


def create_database_connect():
    conn = sqlite3.connect('app.db')
    curs = conn.cursor()
    return conn, curs


# Returns to the user the information of all employees (in json)
@app.route('/employees')
def get_employees():
    conn, curs = create_database_connect()
    query = 'SELECT * FROM employee'
    curs.execute(query)
    results = curs.fetchall()
    conn.close()
    return results


# Returns to the user the information of all companies (in json)
@app.route('/companies')
def get_companies():
    conn, curs = create_database_connect()
    query = 'SELECT * FROM company'
    curs.execute(query)
    results = curs.fetchall()
    conn.close()
    return results


# But what if we want to ask for specific data, like for an employee based on their ID?

# Create some way to obtain data
def db_get_employee_by_id(e_id):
    conn, curs = create_database_connect()
    query = f'SELECT * FROM employee WHERE id = {e_id}'
    curs.execute(query)
    results = curs.fetchone()
    conn.close()
    return results


@app.route('/employees/<e_id>')
def get_employee(e_id):
    result = db_get_employee_by_id(e_id)
    print(result)
    return jsonify(result)


# What if we want to insert data though!

# Create object (makes transferring around data in backend alot easier)
class Employee:
    def __init__(self, f_name, l_name, dob, cmp_id):
        self.first_name = f_name
        self.last_name = l_name
        self.dob = dob
        self.cmp_id = cmp_id


# Have some sort of way to insert into database
def insert_employee(new_employee: Employee):
    conn, curs = create_database_connect()
    query = f'''INSERT INTO employee (cmp_id, first_name, last_name, dob) VALUES 
        ({new_employee.cmp_id}, '{new_employee.first_name}', '{new_employee.last_name}', '{new_employee.dob}');
    '''
    curs.execute(query)
    conn.commit()
    conn.close()

# Have app route to handle post requests
@app.route('/employees', methods=['POST'])
def add_employee():
    # We need to grab the data we need from the json request we received
    f_name = request.json["first_name"]
    l_name = request.json["last_name"]
    dob = request.json["dob"]
    cmp_id = request.json["company_id"]  # Making this one different to show that it can be programmed dumb-ly

    # Create employee object
    new_employee = Employee(f_name, l_name, dob, cmp_id)

    # Insert it into database
    insert_employee(new_employee)

    #Return success
    return jsonify({})

###############################
###############################
# You can run the flask program instead of using 'flask run'
# if __name__ == '__main__':
#     app.run()
