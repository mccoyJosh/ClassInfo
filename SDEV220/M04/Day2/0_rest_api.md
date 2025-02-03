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



# Flask (REST API Package in python)




