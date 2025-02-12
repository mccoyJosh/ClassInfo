
# Django Views

Views is how django refers to the pages you can actually see.

This will be the actual pages on your website!

# How to make em:

Making a views in Django is quite simple. Add a definition in 'view.py' and have it connect to 
your urls.py file.

This works similar to the previously made URL connections, BUT, you want to return a call
to the 'render' function call (as is seen in day_social/urls.py file). This will render
a given html file... which gets to the topic of, hey, how do we make HTML files.

SO, disregarding that for one moment, the full steps are:

- CONNECT main site to app url file
- Create HTML to display
- Create method to return render of HTML in views.py
```
def simple_html_page(request):
    return render(request, 'simple.html', {})
```
This will look inside the templates directory for a file called simple.html
- Connect that method to url in urls.py
```
urlpatterns = [
    path('simple', views.simple_html_page, name='Simple'),
]
```

Anyway, how do we use html?

# Kinda Using HTML

HTML is a 'language' that is organized using tags.

Tags are used to described objects, the structure of the page itself, different types of text, 
and many, many other things.

Here is the most basic HTML you will see:

```html
<!DOCTYPE html> <!--This tells the surrounding system that this is a html file-->
<html lang="en"> <!-- The html holds the actual HTML content; here we also see the use of an attribute!-->
    <body> <!--The BODY is typically used to describe where the body, the actual WORK of the file is going to go -->
       
    </body>
</html>

```
Notice the start of each tag is simple the name surrounded by <> while the end contains a backslash before the name </>.
This is how HTML renderers determine the beginning and end of each tag.

Another basic tag is p, which is short for PARAGRAPH and is used to hold a piece of text, like a paragraph.
As can be seen below, the contents of the paragraph (and whatever other tag you are using)
goes between the opening and closing tags.

```html
<p>Here is some text within the "paragraph"</p>
```

With these simple tools, we can actually render some HTML to the screen.

In our templates directory, we can make a file ending in html (in the given example, see 'simple.html'), and
then call that from our views file.

We can then go see it from the /simple url path (or however you named it)
