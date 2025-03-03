# Example Mostly Stolen from https://pythonspot.com/login-authentication-with-flask/

from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import db

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return f'Hello {session['username']}!  <a href="/logout">Logout</a>'


@app.route('/login', methods=['POST'])
def do_admin_login():
    username_input = request.form['username']
    password_input = request.form['password']

    result, found_user = db.query_for_user_and_password(username_input, password_input)

    if result:
        session['logged_in'] = True
        session['username'] = found_user
    else:
        flash('wrong password!')
        print(f"FAILED LOGIN: '{username_input}'\t'{password_input}'")
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['username'] = 'NULL NOT A VALUE AHH'
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
