# Class

----

# What is a class, generally

We have used classes in the previous section when discussing GUI's, as 
the proper way to set up our GUI program was to create a class. But, we will actually
talk about specifically what a class is and how to make one.

A class is an abstraction tool to represent objects and structures.
At this point in time, abstractions we've seen have been 
- functions
- modules
- classes (aka objects)


Before the introduction of classes, if we wanted to represent something like information for an individual, 
the best way to go about this may have been to use a dictionary like this:

```python
info = {
    'FName': 'John',
    'MI': 'L',
    'LName': 'Smith',
    'Age': 90,
    'SSN': 123456,
}
```

Now, much like many of the other abstraction tools, this works just fine, technically. 
But, there is a better way to represent this OBJECT.

In a sense, information about an individual can be considered an object, as in, within it, 
all the information about an individual can be found. Maybe you want to use all this info in one place,
like comparing it to another individual, or adding it to a list, but all of these ideas 
is simplifying the idea of a individual and their specific attributes to one whole object.
Now, again, technicality, this dictionary DOES hold all this info and can be used as an 
'object' to do everything state above. But, classes have the functionality to simplify and 
abstract away the actual implementation and information of said object, which can help us
SO MUCH as developers.


So, how do we go about making a class?


# Creating a class

Making a class is as easy as using the class keyword!

```python
class class_name:
    pass
    
    # Variables
    
    # And Functions
```

Now, if we wanted to represent the individual before, we need to add some variables!

