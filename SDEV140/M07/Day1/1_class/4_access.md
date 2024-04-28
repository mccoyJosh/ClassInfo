# Access From Within class

Sometimes you need to restrict access to outside users as to what they can control as far as the object goes.
We briefly talked about mutators and accessors, but we didn't talk about how we can prevent the user from
actually changing the variables from within inside a class.

We do this by setting its access level, of which there is (typically) 3:
- public
- protected
- private


----

# PUBLIC
By default, every variable and method within a class is set to public. This allows anyone to use
that variable from any context. This is why we were allowed to do stuff like i1.FName, as FName was public, 
and we accessed from outside the implementation of the class.


----

# PRIVATE
Making a variable or method private will only allow it to be access from within the class itself.
Anyone trying to access it outside the class will be met with an error. To convert a variable to be private, 
you just need to **add two underscores** before it. Before: `var` -> After: `__var`.

If we wanted to make SSN private, as it shouldn't need to be changed and shouldn't be messed with by the user, 
we just need to add __ before it.

```python

class Individual:
    def __init__(self, FName: str, MI: str, LName: str, Age: int, SSN: int):
        """Constructor for Individual class
        taking in all variables as parameters"""
        self.FName = FName
        self.MI = MI
        self.LName = LName
        self.Age = Age
        self.__SSN = SSN


i1 = Individual('John', 'L', "Smith", 90, 123456)


i1.Age = 10  # is public
print(i1.__SSN) # is private
```

Now, this does in fact work. __SSN is now private and can only be access from within the class.
Although, the way python does this is kind of dumb...
they just rename the variable, and you are expected to essentially not use it.

Finding the renamed variable name is also relatively easy:
```python

class Individual:
    def __init__(self, FName: str, MI: str, LName: str, Age: int, SSN: int):
        """Constructor for Individual class
        taking in all variables as parameters"""
        self.FName = FName
        self.MI = MI
        self.LName = LName
        self.Age = Age
        self.__SSN = SSN


i1 = Individual('John', 'L', "Smith", 90, 123456)


i1.Age = 10  # is public
print(i1.__dict__.keys()) # prints out the variable names
print(i1._Individual__SSN) # is private, supposedly
```

----

# PROTECTED

Protected items are ones which can only can be accessed by sub-classes of the class it was made in. To create
a 'protected' method or variable in python, you just need to use one underscore. Before: `var` -> After: `_var`.

Now, it doesn't seem like protected actually 'works' in python, as it just allows one to access a variable even if it is protected,
but in other languages it would simply not allow this.



----

# Conclusion for this,

In python, public, private, and protected a more or less for the sake of yourself as developer and less about actual security per se. 
