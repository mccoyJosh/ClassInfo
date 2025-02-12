# Django ORM

Make sure everything up to date:

```
python manage.py makemigrations
```

```
python manage.py migrate
```



Create admin account:
```
python manage.py createsuperuser
```

-----

The orm has its own very special way of accessing information
from the database, whether that be inserting or looking up info,
so, let's learn how to do that.

Let's do something simple to start with: getting the information from the 
database. 

Also, for this example to work, make sure you have created at least 1 user (like the admin)

See orm_examples.py for how to do these things!!
