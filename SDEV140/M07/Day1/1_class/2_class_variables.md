## Class Variables

To add some variables to a class, all we need to do is create them within the class

```python
class Individual:
    FName = ''
    MI = ''
    LName = ''
    Age = 0
    SSN = 0


i1 = Individual()
i1.FName = 'John'
i1.MI = 'L'
i1.LName= 'Smith'
i1.Age = 90
i1.SSN = 123456


print('Name: ', i1.FName, i1.LName)
```

First off, this is a terrible way to **_CONSTRUCT_** an object (we will fix this in a second).
But I want a few things to be spcifically noticed here:

- Within the class, we can see that all the variables are initially declared. The current implementation
  essentially defines default values for these class variables just in case they are not used. 
  This also sets up what type each variable is, even though technically that can be changed.
- `i1 = Individual()` This line here creates for us an instance of the Individual object by calling the CONSTRUCTOR METHOD, which, we can name `i1`. 
  With the object made, we can access and change the variables from within it.
- We can see that we can assign each variable by doing `<object name>.<variable> = <new value>`. In general, we can access
  an object's variable by doing: `<object name>.<variable>` and this can be used to not only change the value, but get the value, as
  can be seen with `print('Name: ', i1.FName, i1.LName)`


Along having all the same fields as the dictionary, a object being made with a class
as a opposed to a dictionary is that we have a strict definition as to what this object should contain.
A dictionary is a mutable object and one could easily add a variable to one
individual and no one else which may cause problems as to how the objects are read.

### By making a class, we say that X object must have THESE variables, so we force all the objects to follow our interface so that each one will for sure all have the same information.

-----

# Type Hints

If you do not desire to give these variables default values, you can instead use
a type hint. This is just telling python what type of object 
your variable should be:

```python
class Individual:
    FName: str
    MI:    str
    LName: str
    Age:   int
    SSN:   int


i1 = Individual()
i1.FName = 'John'
i1.MI = 'L'
i1.LName = 1
i1.Age = 90
i1.SSN = 123456

print(type(i1.LName))
```

## NOTE:
> THIS DOES NOT ACTUALLY STOP YOU FROM PUTTING THE INCORRECT TYPE OF VARIABLE IT JUST SAYS TO PYTHON THAT THIS VARIABLE SHOULD EXIST! See example above.

### If you want to ensure variable use the type that you assign it, you could use something like the package [mypy](https://pypi.org/project/mypy/)


---

# Now, the way we are assigning the variable kinda sucks. It takes up so much room, and is annoying to look up, but we can greatly reduce this, although we first must talk about methods!