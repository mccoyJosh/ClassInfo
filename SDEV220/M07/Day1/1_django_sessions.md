# Keepin Data with SESSIONS

By default, django will store and retrieve arbitrary data on a per-site-visitor basis and stores this data
on the server side and abstracts out the sending and receiving of cookies.

Here that is that same information from the [horse's mouth](https://docs.djangoproject.com/en/5.1/topics/http/sessions/)

This gives us the ability to EASILY store data about specific users visiting our website.

The way the website does this is by giving every browser that visits the website a cookie with an id.
This is used to identify the computer in the future.

This is going to be the basis for storing information that needs to be consistent between pages, like whether a 
user is logged in or not.

# Simple Example

Getting access to the session is actually super simple.

Whenever we make a function to take in requests from the front end of our website
we have access to the 'request' as a parameter.
One of the many things within it is session, so all we need to do
to access it is do ```request.session```

We can see the values printed out by appending this line to the main page's view function:
```python
print(dict(request.session))
```

If not logged in, this should be an empty directory.

If we opened up a new tab and logged in as the admin, and then RERAN the main page, we
can see the user information that is saved for us to keep us logged in.

Notice they hash the user info so your information doesn't instantly become exposed if you look at your cookies.

# Getting values from the session

Getting values from the session is also super easy.
It is 'kinda' a dictionary, so getting information from it consist of simply
asking for a specific key from it just like a dictionary.
```python
def page(request):
    my_value = request.session['my_key']
```

# Setting values to the session

Setting these values is also easy.
All you have to do is add a value to it just like a dictionary:

```python
def page(request):
    request.session['my_key'] = 'my_value'
```


# Example:

See the `session_example.py` file along with urls.py for an example of using the session to add and get color!



# Final Notes For Sessions

- These are NOT permanent storage systems
- If someone deletes their cookies, they are going to be logged out and anything you saved to the session will be lost
- Make sure you save permanent info in a database of some sort
- SHOW OFF DELETING COOKIES
