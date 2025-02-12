Initial set up runs:

- `mkdir example_django_proj`
- `cd example_django_proj`
- `django-admin startproject website_central .`
- `python manage.py startapp day_social`
- Register app in settings file of central folder (in INSTALLED_APPS list)
- Create admin account: `python manage.py createsuperuser`
- Run site: `python manage.py runserver`

-----

# Create Simple Url with Http Response

All we need to do is two things.

- Create method with Http request (see website_central/simple_url.py)
- Import method into url path list AND create path using method as parameter (don't call, simply pass as value)

# What about our app thought -> Creating link to urls in app

So creating URLs straight from our 'main site' is just fine, but,
the beauty of using something DJANGO is the ability to separate discrete 
parts of your website (or service) into their own applications. So,
we have already made an application, but how to do we create urls in our app and get access
to them from the main site?

First, we need a place for our MAIN site to look, so within your application's directory:
- CREATE A urls.py file

Now, within your MAIN site's directory, add to your urlpatterns in urls.py
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app_name.urls')), # THIS LINE
]
```

*Make sure you import include from django.urls!!!*

Now, when accessing the root url, you are redirected to the urls in the application.
From there, you can create urls in your application.

# URLS in application

Creating an url is easy! And we already did it!
Make an urlpatterns list in your urls.py file within your application, and make a 
path for it to follow.

See day_social/urls.py for how to do this specifically.
In there, you will see another very simple url being returned using an anonymous function, but
we want to make better, COOLER things to return (like an actual page).

So, lets talk about DJANGO views!
