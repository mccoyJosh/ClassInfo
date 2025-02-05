# MAKE SURE YOU HAVE FLASK INSTALLED: pip install flask

# Make sure these commands are run from your command line before running command!
# Otherwise, these required environment variables will break your system.
export FLASK_APP=f.py
export FLASK_ENV=development

python db.py # Creates database for us

flask run



# You can do this if you use app.run() within your program
#python f.py