# Day 1 Fun Thing: SQL INJECTION

Fun little thing we are going to talk about is SQL INJECTION.

Now when you make field for a user to type in that ends up connecting to
a database, you COULD be susceptible to an SQL INJECTION. This is exactly what it sounds like,
someone injecting sql into your pre-made query.

This can have many, many bad consequences, like:
- people access a list of items never intended
- being able to logged in without a password

# See example server

For the sake of showing this off, there is
an example server which is vulnerable.

Run:
```
python createdb.py
```

AND

```
python server.py
```

This takes input from a simple flask project, and logins you in (and that is it).

# How to SQL Inject

So, to inject sql, we simply need to understand how our current query looks:

The query in question:
```
SELECT * FROM user WHERE user.username = "{username}" AND user.password = "{password}";
```

Since the thing we are typing in is just inserted into the query, what
we type inside the username field will be put there.

So, we login as the admin by a query like this:
```
admin";--
```

If you notice, we are doing a few things here:
- ending the string
- ending the sql query
- adding a comment to cancel out the rest of the query

This makes it so that it just only checks for the username and lets us in!


We can also login without even knowing a username:

```
not_a_user" OR 1=1;--
```

We can expand on this and walk through the different ids
manually!

```
d" OR id =2; --
```

# Preventing SQL Injection

- Fixed input from user prior to injection of data
  - Blacklisting or Escaping Single Quotes (which is a start)
  - Prepared Statements
- Use input info on code base side of project
- using built in tools like the ORM in DJANGO which already has SQL injection prevention built in


# Attempting to escaping single quotes

This a good start to preventing SQL Injections, and fixes the
attempts previously shown examples, as they depend on ending the string and
then injecting the SQL. 

This does not prevent all sql injections though!

For our example, we are not too worried about it because we are still okay!
But, if we were in a different database system, we could still be vulnerable to this
attack by a different bit of sql injection!

If we had code in place to escape out double quotes in other sql dialects,
what we would do is this:

```
" -> \"
```

This can still leave us vulnerable by just not using double quotes. Instead,
we would do this:

Username: `\`
Password: `OR 1=1 --`

By escaping the actual string, we put the whole password in inside the username
string, so the password field just becomes a place to inject queries.

```
SELECT * FROM user WHERE user.username = "\" AND user.password = "OR 1=1;--";
```

Unfortunate fo SQLITE, it determines escaped quotes by using two double or single
quotes one after each other, so, you cannot escape the double quotes like this, and 
attempting to escape would require you to actually try to add more quotes, which won't work.


# Prepared Statements

We can also use the built-in prepared statement tools part of database tools.
These have SQL injection preventions, like escaping double quotes and comments and what not.

These are pretty reliable, and you can stop worrying about SQL Injection!

Typically, this works the same way as it does here in Python. You make ? where you want
things inserted, and then put what you what inserted in some type of parameter field.
