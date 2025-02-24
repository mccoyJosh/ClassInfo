# SECURITY

# Using user information
Now with users being able to REALLY exist, we can fix our code to 
ascribe the current user to the post/topic being created


# Ensuring only signed-in users can see certain information

Currently, there are a few things we probably should do to secure our website:

Make sures users who are logged in can actually see the things they are suppose to, including:
- account page
- 'login' if they are logged out
- the creation of topics/posts

Now you may have noticed most of this is implemented in the example project already!
Well, we can still harden it a bit.

## Add if/else to create pages of topics/posts

By using the django html language, you can easily add if statements to only show info
to those who are logged in. Implementing it is easy as this:

```html
{% if user.is_authenticated %}
<!--SOMEONE WHO IS LOGGED IN WOULD SEE THIS SECTION-->
{% else %}
<!--SOMEONE WHO IS LOGGED OUT WOULD SEE THIS SECTION-->
{% endif %}
```

The  `user.is_authenticated` is a parameter that is always passed and `is_authenticated` is just one of
many things contained within it. For instance, it also has the username of a user too: ```user.username```

## Add `@login_required` to the functions for their creation

By utilizing the login_required tag within your views, it automatically redirects people who
are not logged in to the login page instead of their initially desired page, even if
they type in the url by hand.

views.py
```python
from django.contrib.auth.decorators import login_required

@login_required
def page(request):
    pass
```


