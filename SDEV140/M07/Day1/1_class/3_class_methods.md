# Class Methods

So methods work just like all the functions we have seen up to this point, except, they
are contained and used with a class. To make it, it is as simple as making any other class, except
you need to put 'self'

```python
class class_name:
    def method_name(self):
        pass
```

Now, the method works the same as another other function! You can add parameters,
returns statements, they can be recursive, whatever. The only difference is the 'self' parameter.

----

## Self
Now the reason we have this 'self' variable is to have some access point for the object we are currently in.

Anytime we ever call a method, we need an object to call it from. Since we are coding inside the object we may want to call, it is 
not possible to have a reference to itself, not until we have the 'self' parameter.

From within the method, we can access the other methods and variables that are defined using self. This also
allows us to use the same name for variables/methods in a method without overwriting the actual value because
the variables within the scope of the method are different from the ones from `self.`, which will be seen in this next example:

```python
class math_obj:
    num: int
  
    def add_and_print(self, addition):
        num = self.num + addition
        print(num)

m = math_obj()
m.num = 7
m.add_and_print(10)  # Prints out 17
print(m.num)         # Prints out 7 (since num which was changed within the add_and_print() method was its own thing in its own scope)
```

Notice:
- When running these methods, we DO NOT NEED TO GIVE THE METHOD THE SELF PARAMETER. This is 'essentially' done automatically
  since it is an object. Thus, calling the add_and_print method just needed the 10 as a parameter.
- We are able to access the object's actual `num` in the add_and_print() method by using `self.num`.
- If you are familiar with Java or C++, instead of `self`, you would probably be using `this`, but it essentially works the same.


---
# `__<THING>__` Methods

Now most methods you are going to create are going to be unique for your object. But there are a bunch of methods
which are common across classes which help make python better at interpreting them. 

These methods all use the format of `__<Common Method Name>__`

The first and most important of these is the: 

## Initialization (AKA Constructor) Method (`__init__`)

This method will construct the object that you are desiring. Typically, this is initialing variables that are needed
and taking variables which need to be assigned. 

The init method is an alias in for whenever you call the class_name() constructor. 

Here is a simplified version of our math_obj from before:
```python
class math_obj:
    num: int
    
    def __init__(self, n):
        self.num = n
    
    def add_and_print(self, addition):
        num = self.num + addition
        print(num)

        
m = math_obj(7)
m.add_and_print(10) # Still prints 17
```

Notice how instead of needing to do `m.num = 7` after the object is made, we just give 7 to the constructor and it is done.

With this information, we can now redesign our Individual object to make it a bit easier to create a new Individual.

```python
class Individual:
    FName: str
    MI:    str
    LName: str
    Age:   int
    SSN:   int
    
    def __init__(self, FName, MI, LName, Age, SSN):
        self.FName = FName
        self.MI = MI
        self.LName = LName
        self.Age = Age
        self.SSN = SSN


i1 = Individual('John', 'L', "Smith", 90, 123456)
```

This will assign each of our class variables for us now, and we just need the supply the values!
This converts the 5 lines to assign values into 1, and it will be 1 line for all the objects we end up making from this point.
This code though can be further reduced. 

When assigning the class variables, we are now having all the values named from within the init method, meaning
we don't need to name them all from within the class, we can just do all that work within the init method.
Now, we do continue to use type hints, but this code will work just fine without it.


```python
class Individual:
    def __init__(self, FName : str, MI : str, LName : str, Age : int, SSN : int):
        self.FName = FName
        self.MI = MI
        self.LName = LName
        self.Age = Age
        self.SSN = SSN


i1 = Individual('John', 'L', "Smith", 90, 123456)
i2 = Individual('Bill', 'B', "Bob",   67, 000000)
```

Now with that in place, we can do whatever we need to do with the individual object!
Maybe we want to be able to print out the birth year of the individual, well, we have the age so calculating that shouldn't
be too bad!

```python
from datetime import datetime


class Individual:
    def __init__(self, FName : str, MI : str, LName : str, Age : int, SSN : int):
        self.FName = FName
        self.MI = MI
        self.LName = LName
        self.Age = Age
        self.SSN = SSN

    def print_birth_year(self):
        year = datetime.now().year.real
        print(year-self.Age, 'or', year-self.Age+1)


i1 = Individual('John', 'L', "Smith", 90, 123456)
i2 = Individual('Bill', 'B', "Bob",   67, 000000)

i1.print_birth_year()
i2.print_birth_year()
```

-----

## `__str__` method

Another 'built in' method for classes python is the `__str__` method. 
If you attempt to convert your object to a string for any reason, such as printing it out
or something similar, you are going to find that python does not automatically make it look nice... it is
going to be python's internal representation of the object.

Most times, we don't want this. So, instead, we are going to want to implement the `__str__` method.
This method tells python how it should convert this type of object to a string.
Once implemented, anytime this object is maybe used as a string, it will call this method to get
said string.

Here we use it to properly display information concerning an individual:

```python
from datetime import datetime


class Individual:
    def __init__(self, FName: str, MI: str, LName: str, Age: int, SSN: int):
        self.FName = FName
        self.MI = MI
        self.LName = LName
        self.Age = Age
        self.SSN = SSN

    def print_birth_year(self):
        year = datetime.now().year.real
        print(year - self.Age, 'or', year - self.Age + 1)

    def __str__(self):
        return f'-----------------------------\nNAME: {self.FName} {self.MI} {self.LName}\n\tAGE: {self.Age}\n\tSNN: {self.SSN}\n-----------------------------'


i1 = Individual('John', 'L', "Smith", 90, 123456)
i2 = Individual('Bill', 'B', "Bob", 67, 000000)

print(i1)
print(i2)
```

What we will end up seeing from this point forwards is that these special methods will convert our object to
some sort of python inherit object or functionality. For instance, comparing two objects:

---

# Comparison Methods

When using > < == != or any other python keyword to compare objects, python needs to know how to interpret the
object's rationally to even compare them. So, these methods exist to allow us as developers to tell python
exactly how an object may compare to other objects of the same kind.

- ## `__eq__` method
  - This is used to tell python how to see if two objects are the same (using the == operator)
Here is an example of using it:
```python
from datetime import datetime


class Individual:
    def __init__(self, FName: str, MI: str, LName: str, Age: int, SSN: int):
        self.FName = FName
        self.MI = MI
        self.LName = LName
        self.Age = Age
        self.SSN = SSN

    def print_birth_year(self):
        year = datetime.now().year.real
        print(year - self.Age, 'or', year - self.Age + 1)

    def __str__(self):
        return f'-----------------------------\nNAME: {self.FName} {self.MI} {self.LName}\n\tAGE: {self.Age}\n\tSNN: {self.SSN}\n-----------------------------'

    def __eq__(self, other):
        return other.SSN == self.SSN




i1 = Individual('John', 'L', "Smith", 90, 123456)
i2 = Individual('Bill', 'B', "Bob", 67, 999999)
i3 = Individual('Billy', 'C', "Cob", 68, 999999)

print(i1 == i2)
print(i2 == i3)
```

In the example, we defined equality solely off of the SSN, so, despite other values being different between i2 & i3,
they are in fact equal since they have the same SSN.

- ## Other Comparison Types
  - ### `__ne__` method (Not Equals aka !=)
  - ### `__lt__` method (Less than aka <)
  - ### `__le__` method (Less than or equal aka <=)
  - ### `__gt__` method (Greater than aka >)
  - ### `__ge__` method (Greater than of equal aka >=)
  
For some things, you need to implement one of these methods for it to work properly.
For instance, if you had a list of items, and wants to sort them, you need `__lt__` (<) implemented, as
this is the operation used to do the sorting.

If we wanted to be able to sort a list of individuals by last name, we would need this code:

```python
from datetime import datetime


class Individual:
    def __init__(self, FName: str, MI: str, LName: str, Age: int, SSN: int):
        self.FName = FName
        self.MI = MI
        self.LName = LName
        self.Age = Age
        self.SSN = SSN

    def print_birth_year(self):
        year = datetime.now().year.real
        print(year - self.Age, 'or', year - self.Age + 1)

    def short_hand_str(self):
        return f'"{self.FName} {self.MI} {self.LName}"'

    def __str__(self):
        return f'-----------------------------\nNAME: {self.FName} {self.MI} {self.LName}\n\tAGE: {self.Age}\n\tSNN: {self.SSN}\n-----------------------------'

    def __eq__(self, other):
        return other.SSN == self.SSN

    def __lt__(self, other):
        return self.LName < other.LName


def print_list(l):
    print('[', end='')
    for i, item in enumerate(l):
        print(item.short_hand_str(), end='')
        if i != len(l) - 1:
            print(', ', end='')
    print("]")


i1 = Individual('John', 'L', "Smith", 90, 123456)
i2 = Individual('Bill', 'B', "Bob", 67, 999999)
i3 = Individual('Billy', 'C', "Cob", 68, 823822)

i_list = [i1, i2, i3]
print_list(i_list)
i_list.sort()
print_list(i_list)

```

### For a more comprehensive list of these special methods, check out this [link!](https://devopedia.org/magic-methods-in-python)

----

----

# Accessors and Mutators

### What are they and why use em

Accessor and mutator methods are all about working with the variables contained within a class.

Accessor methods allow you to access variables while
mutator methods allow you to change em

Sometimes you do not want to give complete control to who ever is using your class access to 
change and do what they'd like with all variables. In this case, it is smart to use accessor and mutator methods
to control these actions.

Here is an example of adding mutator and accessor methods to the Individual class.

```python

class Individual:
    def __init__(self, FName: str, MI: str, LName: str, Age: int, SSN: int):
        self.FName = FName
        self.MI = MI
        self.LName = LName
        self.Age = Age
        self.SSN = SSN

    def get_FName(self):
        return self.FName

    def get_MI(self):
        return self.MI

    def get_LName(self):
        return self.LName
    
    def get_Age(self):
        return self.Age
    
    def get_SSN(self):
        return self.SSN

    def set_FName(self, FName):
        self.FName = FName

    def set_MI(self, MI):
        self.MI = MI

    def set_LName(self, LName):
        self.LName = LName
    
    def set_Age(self, Age):
        if Age > 0:
            self.Age = Age
    
    def set_SSN(self, SSN):
        if SSN > -1:
            self.SSN = SSN


i1 = Individual('John', 'L', "Smith", 90, 123456)
i2 = Individual('Bill', 'B', "Bob", 67, 999999)
i3 = Individual('Billy', 'C', "Cob", 68, 823822)
```

Most of these mutators and accessors are inconsequential in nature, as having the mutators and accessors
does not add functionality/limits to the actual object.

This is not the case for the mutator methods for age and ssn though; Age shouldn't be less than 0 so it ensures this before being change,
along with social security number, as you can't have a negative SSN.

----

# DocStrings

Obviously comments are super important regardless, but here we are talking about a special kind of comment:  **a docstring**
This is simply a longer comment at the beginning of a method explaining what it does. They use three " to denote the docstring

Here is out individual class with docstrings added.

```python

class Individual:
    def __init__(self, FName: str, MI: str, LName: str, Age: int, SSN: int):
        """Constructor for Individual class 
        taking in all variables as parameters"""
        self.FName = FName
        self.MI = MI
        self.LName = LName
        self.Age = Age
        self.SSN = SSN

    def get_FName(self):
        """Function to get FName"""
        return self.FName

    def get_MI(self):
        """Function to get MI"""
        return self.MI

    def get_LName(self):
        """Function to get LName"""
        return self.LName

    def get_Age(self):
        """Function to get Age"""
        return self.Age

    def get_SSN(self):
        """Function to get SSN"""
        return self.SSN

    def set_FName(self, FName):
        """Function to set FName"""
        self.FName = FName

    def set_MI(self, MI):
        """Function to set MI"""
        self.MI = MI

    def set_LName(self, LName):
        """Function to set LName"""
        self.LName = LName

    def set_Age(self, Age):
        """Function to set Age, barring Age must be greater than 0"""
        if Age > 0:
            self.Age = Age

    def set_SSN(self, SSN):
        """Function to set SSN, as positive value"""
        if SSN > -1:
            self.SSN = SSN




i1 = Individual('John', 'L', "Smith", 90, 123456)
i2 = Individual('Bill', 'B', "Bob", 67, 999999)
i3 = Individual('Billy', 'C', "Cob", 68, 823822)

```

-----


# Objects lifetime

So, we have talked about this before, but this code shows how that an object exists as long as there is some 
reference to it. In the example, even though i1 becomes None, the object is still referenced by the list, and is 
therefore still alive, but once we pop the list, the item is gone with no reference. What happens after it loses all reference is
that the python garbage collector will eventually come and pick it up so that the space can be used for something else.

```python

class Individual:
    def __init__(self, FName: str, MI: str, LName: str, Age: int, SSN: int):
        """Constructor for Individual class
        taking in all variables as parameters"""
        self.FName = FName
        self.MI = MI
        self.LName = LName
        self.Age = Age
        self.SSN = SSN

    def get_FName(self):
        """Function to get FName"""
        return self.FName

    def get_MI(self):
        """Function to get MI"""
        return self.MI

    def get_LName(self):
        """Function to get LName"""
        return self.LName

    def get_Age(self):
        """Function to get Age"""
        return self.Age

    def get_SSN(self):
        """Function to get SSN"""
        return self.SSN

    def set_FName(self, FName):
        """Function to set FName"""
        self.FName = FName

    def set_MI(self, MI):
        """Function to set MI"""
        self.MI = MI

    def set_LName(self, LName):
        """Function to set LName"""
        self.LName = LName

    def set_Age(self, Age):
        """Function to set Age, barring Age must be greater than 0"""
        if Age > 0:
            self.Age = Age

    def set_SSN(self, SSN):
        """Function to set SSN, as positive value"""
        if SSN > -1:
            self.SSN = SSN




i1 = Individual('John', 'L', "Smith", 90, 123456)

i_list = [i1]
print(i_list)

print(i1)

i1 = None

print(i_list)
i_list.pop()

print(i1)
print(i_list)
```


