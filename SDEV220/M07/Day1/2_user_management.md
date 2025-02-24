# USER MANAGEMENT

This little portion is going to go over how to let users log in, log out, and sign up!

So, with all of this information at our fingertips, how can we actually utilize the session
to have a user log in and stay signed in (and let that affect the website).

Well, as you might expect, we are actually just gonna use a django way of doing it and not worry too much about
the specific details.


# Main Site Set Up:

Within main website directory, you need to add these lines to your settings.py
page:
```python
LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'
```
You can change these if you would like, but it tells the website to redirect a user once they have 
logged out or logged in. In our case here, they simply are put back on the home page.

Also, include a new additional link in your main site's url patterns:
```path("accounts/", include("django.contrib.auth.urls")),```

Here it is where it is supposed to be:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('day_social.urls')),
]
```

# Logging In

Alright, with that set up, we now have... more set up.
So, to let someone log in, all we really need is a login page set up and an url ready for it

What we are require to do though is make a directory called 'registration' in our templates folder.

Inside of this registration folder, we are going to be making a file called `login.html`

This is what is inside my login.html file
```html
{% extends 'main.html' %}

{% block content %}
{% if form.errors %}
<p>Your username and password didn't match. Please try again.</p>
{% endif %}

<form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <table>
        <tr>
            <td>{{ form.username.label_tag }}</td>
            <td>{{ form.username }}</td>
        </tr>
        <tr>
            <td>{{ form.password.label_tag }}</td>
            <td>{{ form.password }}</td>
        </tr>
    </table>

    <input type="submit" value="login" />
    <input type="hidden" name="next" value="{{ next }}" />
</form>
<div>
    Don't have an account, create one:
    <a href="/signup">HERE</a>
</div>
{% endblock %}
```

The main portion here is the FORM section, as it has all the fields to login.
This 'template' is given to us from Django, but you can obviously play around with it more than I have here.

But, once you type in your info here, the backend will verify it is correct and then award you with cookies proving you are logged in!


# Logging Out 

Logging out is even easier. All you need to do is have a button which called the logout url. This:

```html
<form action="{% url 'logout' %}" method="post">
    {% csrf_token %}
    <button type="submit">Log Out</button>
</form>
```

I have this button placed on a page with account info:

account.html
```html
{% extends 'main.html' %}

{% block content %}
{% if user.is_authenticated %}
Hi {{ user.username }}!
<form action="{% url 'logout' %}" method="post">
    {% csrf_token %}
    <button type="submit">Log Out</button>
</form>
{% else %}
<p>You are not logged in</p>
<a href="{% url 'login' %}">Log In</a>
{% endif %}
{% endblock %}
```

Note: if you are getting an error instead of being logged out, you probably forgot to add the extra url to the
main website's urls.py page.

# Signing Up

To allow users to sign up for your website, it is similar to login in, but also, completely different.

The first step is to create a signup page, like this one here:

MAKE SURE IT IS IN THE REGISTRATION DIRECTORY, JUST LIKE THE LOGIN PAGE:

/templates/registration/signup.html
```html
{% extends 'main.html' %}

{% block title %}Sign Up{% endblock %}

{% block content %}
<h2>Sign up</h2>
<form method="post">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Sign Up</button>
</form>
{% endblock %}
```

Then you are going to create an object in the views.py file to essentially configure our signup page.

This is going to look like:
```python

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

```

After that, you just make a signup url path for that object:

```python
    path("signup/", views.SignUpView.as_view(), name="signup"),
```


# YAY

Now you should be able to create accounts, and then log in and out of them all from within the website!
