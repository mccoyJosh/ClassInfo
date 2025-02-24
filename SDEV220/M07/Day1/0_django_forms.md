# Django Forms

Having a way for users to actually import information is pretty important.

For instance, our example website currently has the ability to VIEW posts,
but no way to actually make a post, which is probably not great!
There is no way to even make a topic either!

So, lets make a way to do this!

-----

There are many, many ways one could go about this. The easiest thing we can do right now
is to just use django's built in tools for display insert fields.

To start using these forms we do have a bit of set up:

## Create `forms.py` in our application

Within the directory with our models, views and other files, we need to create a new file called forms.py.

Within this file, we need to define exactly what can be entered into our form.

What you need to make is a class extending forms.ModelForm
It will look something like this:

```python
from django import forms
from .models import MODEL


class FORM_NAME(forms.ModelForm):
    class Meta:
        model = MODEL
        fields = ('field1', 'field2', ) #Put however many fields you want in here!
```

With this created, we now need to get it to a webpage.

## Getting it to html

So, you would go through the usual process of creating a webpage, as in, 
making a new html file, creating a function for it in the views.py and ascribing an
url for said function within the urls.py's urlpatterns.

Now, within **view.py**, we just need to make sure we do a few thing:

Import:
```
import .forms import FORM_NAME
```

and pass a form object to our html:
```
def page(request):
    form = FORM_NAME()
    return render(request, 'page.html', {'form': form})
```

Now with this going to the html, you can simply use it within your html.

Inside your html document, place this where you want your form to be:
```html
    <form method="POST" class="post-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-secondary">Save</button>
    </form>
```

Now you should have your form DISPLAYING, but not really functioning.

-----

For my example project, these steps look like this:

forms.py
```python
from django import forms
from .models import Topic, Post


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('name', )
```

urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    ...,
    path('make/topic', views.make_topic),
    ...
]
```

views.py
```python
from django.shortcuts import render
from .models import Topic
from .forms import TopicForm


def make_topic(request):
    form = TopicForm()
    return render(request, 'make_topic.html', {'form': form})
```

make_topic.html
```html
{% extends 'main.html' %}

{% block content %}
<h1 id="creation_header">
    MAKE TOPIC
</h1>
<div>
    <div id="outer_post">
        <form method="POST" class="post-form" id="post">{% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="save btn btn-secondary">Save</button>
        </form>
    </div>
</div>
{% endblock %}
```

Notice that the elements being place on the html can also be stylized just like we did before!

HEY, but, this doesn't actually insert the data! How can we make that happen!

## Getting your form to actually insert data

Now actually information to save actually involves only changing the views.py file.

Now, technically, this is ALL you have to do, but there are a lot of parts
so lets take a look at each addition made here to the make_topic() function.
```python
from django.shortcuts import render, redirect
from .models import Topic
from django.contrib.auth.models import User
from .forms import TopicForm
from django.utils import timezone

def make_topic(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            admin_user = User.objects.get(username='admin')  # TEMP
            topic.author = admin_user
            topic.created_date = timezone.now()
            topic.save()

            this_topic = Topic.objects.get(name=topic.name)
            link = f"/topics/{this_topic.id}"
            return redirect(link, pk=topic.pk)
    else:
        form = TopicForm()
    return render(request, 'make_topic.html', {'form': form})
```

First there is the initial if statement `if request.method == "POST":`.
This would be TRUE after we save the form we have made in html, as it returns a POST request
to save the data, hence it then attempts to work out the details here.
If this is FALSE, the page views just as it did before.

Within the if statement, we need to first make sure everything is filled out correctly inside the form.
So, we grab the form from the POST request, and check if it is valid. If it is, we can start making our
database entry.


------

This next section is responsible for simply making our topic object.
First, we pull the data that was given to the form (with form.save()).

And then we add the EXTRA info that we don't expect the user to type in,
in our case, the author of the topic, and the time it is created.

Currently, we have no way to login, so we are going to use the admin as the author of
every post.
```python
topic = form.save(commit=False)
admin_user = User.objects.get(username='admin')  # TEMP
topic.author = admin_user
topic.created_date = timezone.now()
topic.save()
```

At this point in the code, the topic has been added.
Whenever they do this, we DO NOT want them to still be on the screen. They probably
don't want to be stuck in a perpetual state of creating topics!

So, we are going to want to redirect them somewhere else. Now, we can use
either a html document in our templates, or an url link that is within our url_patterns.
Here, we are doing the latter and redirecting them to the now newly created topic page.
```python
this_topic = Topic.objects.get(name=topic.name)
link = f"/topics/{this_topic.id}"
return redirect(link, pk=topic.pk)
```
-----

HEY, let's quickly do this to posts too! (see methods relating to posts)

Do notice
- since post relies on an existing Topic, when using the Topic field, it instead gives you a dropdown of all your options instead of allowing you to type.



