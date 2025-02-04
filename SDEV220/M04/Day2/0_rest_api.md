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


### DELETE

### POST


### PUT


### Idempotency
Pregnant cows are idempotent!


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

The backend is refers to the services in the background, doing alot of the heavy lifting to collect, calculate 
and deliver data. One's database system is often placed within the realm of the backend, but it can include
anything else doing work behind the scenes.

### Full stack is just, both of these, both front nad backend of a server. A 'fullstack developer' is simply saying they can work on both.

Now, the line between what is considered frontend and backend can sometimes 
be a bit fuzzy depending on the service you are creating, 



# Flask (REST API Package in python)




