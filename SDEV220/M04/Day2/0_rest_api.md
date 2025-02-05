# Rest API


API (Application Programming Interface)

API's in general are used as the communication between two programs.
We literally saw this last lecture where we had a CRUD API to communicate with SQLite databases.

The relationship between programs is typically described as a 'client' and a 'server'.
The client requests information from a server, and the server delivers the info.

For databases, we have a database server we are connecting to, and we are the client
asking for information (which, may seem a bit odd since we used SQLite, which is serverless, but still).

Another example is using the internet. Your browser is a client asking website servers for 
information. APIs are how the communication happens.

To make this magic happen, what you use is called endpoints. These are essentially paths
to get different types of information. They are typically structured like file paths on
a computer... or, HTTP urls.

For instance, if google had path to get information on cats, it may look like this

```
www.google.com/cats
```


# Why is it REST tho?

REST stands for **RE**presentational **S**tate **T**ransfer.

It is NOT a protocol or standard, but really an architectural style.

Typically, these API's use JSON to transfer and take in information. It
is not necessary, as some use XML or other data formats, but it is
most common to see JSON.

Similarly to CRUD, there are terms describing how to get data to and fro the API.
Technically this is more of HTTPs methods, but still need to be understood.
These are those:

### GET

This function of the API retrieves data. Typically, this will be in JSON. It should
be said that both the information received and the information sent to get these requests are typically
going to be JSON.

### DELETE

This function of the API is to delete a piece of data aka a resource from an endpoint.

### POST

POST is TYPICALLY utilized to create new resources.

### PUT

PUT is TYPICALLY USED to update (aka replace) an existing resource, but also can be used to update an existing resource.

Using PUT is usually done with the use of an existing ID of a resource.

### Idempotency

Pregnant cows are idempotent!

Now, when talking about data creation, idempotency becomes an important issue to cover.

For a function to be considered **_idempotent_**, it just means that by calling it more than once, you still get the same result.

For instance, the **GET** function is idempotent because it should just return to you the same resource no matter
the number of times you run it.

Now, for put and post, this may be confusing.

**PUT** is considered (if implemented correctly) idempotent, because if you run the same update command 100 times,
the data should remain the same, since it is endlessly being changed to the same value. Nothing new state-wise
is occurring.

This can NOT be said about **POST**. **POST** commands will add a new entry when it is called. So, if you run the 
same POST command 100 times for a specific resource, you would have inserted 100 NEW DIFFERENT resources into
your service, all of which should return some type of different result. Every call will enact some sort of change. 
Thus, **POST** is NOT idempotent

Now finally, delete. It depends on who you ask if **DELETE** is considered idempotent, but it REALLY it comes
down to whose state you care about.

If you are looking purely at the server retrieving the requests, if a piece of data is **DELETED**, and then another
request to **DELETE** the data comes through, there's nothing to delete, so nothing has changed, and nothing will
change after even 100 requests to delete the already deleted resource, so the function IS IDEMPOTENT

The **DELETE** command would be considered NOT idempotent if we look
from the perspective of making the request. Calling it the first time would be
successful as it removes the resource, but calling it the second time would result in some sort of error
with the resource not existing (since it was ALREADY **DELETED**). The result changed after the first request, and thus
wouldn't be idempotent.


# Frontend and Backend

When talking about various services and servers and databases, a few terms arise:

- Frontend
- Backend
- Fullstack

These are terms mostly used by developers to describe themselves and what they work on, but it is also 
a way to describe the system itself in a general sense.

These terms are pretty self-explanatory, but they shall be explained:

### Frontend

The frontend is the services that actually provide some output to the user.
If you are making a website, this would be the portion of your code base delivering the web pages to
a browser.

If it was some service delivering information via endpoints, the service hosting the endpoints would be your frontend.

### Backend

The backend refers to the services in the background, doing alot of the heavy lifting to collect, calculate 
and deliver data. One's database system is often placed within the realm of the backend, but it can include
anything else doing work behind the scenes.

### Full stack is just, both of these, both front nad backend of a server. A 'fullstack developer' is simply saying they can work on both.

Now, the line between what is considered frontend and backend can sometimes 
be a bit fuzzy depending on the service you are creating, 



# Flask (REST API Package in python)

Flask is a great, simple tool to begin making a server.
Flask itself is a 'lightweight WSGI web application framework'
[Their website is here!](https://flask.palletsprojects.com/en/stable/)

Making a path in an url is a simple set of a few lines of code.

But first, we need to install it:

```
pip install flask
```

Just like any other package, it is also available on anaconda.

See flask_ex/f.py for a good example in using flask!


