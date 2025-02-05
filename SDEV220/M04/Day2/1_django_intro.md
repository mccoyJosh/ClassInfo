# [DJANGO](https://www.djangoproject.com/)

[Tutorial](https://tutorial.djangogirls.org/en/) for learning (from modules)

Django is a web framework built on and for python that is widely 
used, have tons of built-in features, FREE, and [open source](https://github.com/django/django).

Flask is considered a 'micro web framework', as it does many of the things that a web server would need
to do like delivering data from endpoints, among other things. But, it is not built to go much further, 
as it is designed as a minimalistic.

Django, along with the creation of urls, has many, MANY more features built in (so you don't need
to literally implement EVERYTHING).
This includes:

- built-in ORM (you won't be dependent on using another package like SQLAlchemy)
- Customizable Admin Panel for dev and product owners to manage website from
- TEMPLATE ENGINE (extra stuff for helping render dynamic HTML and being able to easily reuse content/components)
- Extra Security for web based vulnerabilities, like SQL Injection and others
- Their website claims they are "Ridiculously fast", but that is more advertising than anything else.
- more :P

A lot of these are built into web frameworks for many, many other programming languages, so learning 
how to navigate through Django is good practice for other languages too!

# Installation

Obviously, make sure you have python installed, duh, but then you just need to install Django
there are [many](https://pypi.org/project/Django/), [many](https://anaconda.org/anaconda/django), 
[many](https://docs.djangoproject.com/en/5.1/topics/install/#installing-official-release) ways
to install python.

Easiest way is to use pip, but also, you can use their website!
```
pip install django
```

# Initializing Project

To create a project in django, it is not like
flask where we make a python file and simply import the package.

Instead, we need to generate a whole django project.
With django installed, we should be able to simply run this command:

```
django-admin startproject <your_website_name> <location to generate project>
```

If I wanted to make a website called 'mysite' and make it in the directory I am currently in, 
I would run the following command:

```
django-admin startproject mysite .
```

This will create a project looking like this:

```
dir_ur_in
├── manage.py
└── mysite
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Now, what are each of these files for?

### manage.py

This file gives us access to command line features for our project. These
commands will allow to manage (hence the name) our website.

Some commands built in are:

- Run server: `python manage.py runserver` 
  - You can append a port if you want to use something other than default 8000 port
- Syncs database with new migrations: `python manage.py migrate`
- Creates a new migration based on changes made to models: `python manage.py makemigration`
- Runs a commandline interface to our preferred database `python manage.py dbshell`

Also, the use of the manage.py file allows you to make your own custom commands 
for your project specifically: https://docs.djangoproject.com/en/5.1/howto/custom-management-commands/

### mysite/__init__.py

Init is only here because it is required in some python 
versions to know this directory is a package


### mysite/settings.py

This file will have all the configurations for our project. This includes stuff like API keys, debug values,
database configs, among many, many other things.

### mysite/urls.py

This defines all of our definitive urls for our project. This file is similar to what
we were doing in our flask program with `@app.route('/employees', methods=['POST'])` followed by a function.

We will be using this file very, very soon.

### mysite/wsgi.py

WSGI stands for Web Server Gateway Interface. It is a python webserver that Django
uses under the hood and defines how web servers should interact with web applications.
We do not need to worry about this until deployment, which might not even matter
for the sake of this class.

### mysite/asgi.py

ASGI stands for Asynchronous Server Gateway Interface. Does a lot of what WSGI and is kinda replacing it.
Again, do not really about working with this file; just leave it as it is.


------

------

# Apps

To keep things organized within our project, separate functionalities are going to be seperated
into their own individual apps.

To make an app, use the following manage.py command:

```
python manage.py startapp <app_name>
```

I'm going to make a WHOLE social media website, so, I'm using this command

```
python manage.py startapp socialapp
```

Within the app, there are even more files provided to use to understand:

### __init__.py

This again is simply a file to make sure some versions of python know this is a package

### admin.py

This file deals with making sure our project features are registered and working with
the admin side of django. For instance, you will 'register' models so they are accessible to
that side of your application.

### apps.py

This file is for configuring your app in a number of ways. Think of this
as the settings file for just your app.

### models.py

This file contains the models which you are going to use throughout this application.
These are typically going to be classes, and django will automatically make 
database tables for these for you.

### tests.py

This file is obviously for tests. If you are familiar with unit testing, this is
the file where those will go.

### views.py

The views file will be where you define the pages a user of your web app sees.
Think of it as where html is delivered to the user's browser, but, more complicated than that.

# ADD APPLICATION

With your application created, make sure you register it within your projects setting file.
Your settings file should look similar to this:

```python
# ... more code

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'socialapp'  # <---- This is the important part!!! Make sure you do this
]

# ... more code
```



# Setting Up A Database and Models

The first thing we want to do is ensure our project is using the database
we want. To ensure this, take a look into the settings.py file.

There should be a section looking like this:

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```

Here we can see it is currently set up to use sqlite, which is what we want. SO, we should be good.
If we want to use something else, we could look that up.

----

With the creation of an application (something actually with a
designated purpose), we can being adding models to help create our app.

So, I'm going to be making a user model for my social media app. It will go 
inside the `models.py` file in the app's directory. The class will look something like this:

```python
from django.db import models
from django.utils import timezone


class User(models.Model):
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=100)
  epic_value = models.IntegerField()

  created_date = models.DateTimeField(default=timezone.now)

  def create(self):
    self.save()

  def __str__(self):
    return self.username
```

Just like SQLAlchemy, for the sake of utilizing the ORM that is a part of
django, you are forced to use their own data types like models.CharField instead
of things like strings.

With a model created properly in the django way, making the tables for them is easy.

We simply need to make a migration, and then apply it.

We use two commands to do this:

MAKE MIGRATION
```
python manage.py makemigrations socialapp
```

APPLY MIGRATION
```
python manage.py migrate socialapp
```

This will make for us the table for users!

With this created, we can add ways to add users and what not, but right now
lets it from the admin screen. To do so, we need to register it with the admin part 
of the app.

Here is the 'admin.py' file in our apps folder
```python
from django.contrib import admin
from .models import User

admin.site.register(User)
```

# Working with Admin Screen

The admin part of out project will allow us to deal with the backend of our project
more effectively. Before we can use it though, we need to create a login for it (to
make sure not everyone can access it).

To create an admin user (aka, superuser, run this):
```
python manage.py createsuperuser
```
This will create an admin user on the database you had chosen. This isn't like the
user table I had made for the social app, but instead a database specifically
for the sake of django. 

With all this set up we can access the admin page from http://localhost:8000/admin

Right now, there is not a lot we can do from the admin screen, but we can access the database from the browser instead
of a silly thing like an 'ide' guh. We can also add items in the admin screen as well.
