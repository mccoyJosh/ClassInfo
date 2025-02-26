# Components

There are two ways one could implement components in their django application.
One has much more work, and the other one less so.

# Create the component

In both ways we are going to be inserting the component into the html, we are going
to need a standalone file representing the component. 

In this example, we are trying to just have a component for the posts list (as it is used
in multiple pages).

So, we are creating a file called  `list_posts.html` to demonstrate it.

list_posts.html
```html
<div>
    {% for post in posts %}
    <div id="outer_post">
        <div id="post">
            <div id="post_header">
                <a class="epic">{{ post.epic_value }} </a>
                <a href="" class="button" >EPIC</a>
                <a href="topics/{{post.topic.id}}"> {{ post.topic }} </a> / <a> {{ post.author }}  </a>
            </div>
            <p> {{ post.text }} </p>
        </div>
    </div>
    {% endfor %}
</div>
```

This is going to contain the bit of html just for the post list.

-----

# Using component (easy)

The easiest way to use the component is the {% include <HTML FILE NAME> %}.

This requires no other set up other than just having the other HTML file.

So, if we were trying to use this component we just made, we can reference it using:
```html
{% include 'list_posts.html' %}
```

This would just take the place of the piece of html we took out from the original. What this
allows us to do is now use it both in our main page and the topics page, and anytime we need to update just
the list, we can not do that!

# Using component (less easy)

The second way of using the components is template tags.

This requires us to:

- make a directory in our app called `templatetags`
- create a function and register it with our programs
```python
from django import template
register = template.Library()

@register.inclusion_tag('list_posts.html')
def list_posts(posts):
    return {'posts': posts}
```

- call the template tag in our code using:
```html
    {% load list_posts %}
    {% list_posts posts %}
```

This still uses the same html file we made before, and is alot more work,
so why might we even want to use this?

Well, we make a function that executes when the component is used. This
allows us to run and get information on the creation of the component, so that it
could potentially save us time of re-writing the same code when regardless of where the component is going
to be, we need a small script to run any ways.

So, if your component would benefit from the execution of some code, then this is the path for you.

Otherwise, it is easier just to include!