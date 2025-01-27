# Objects and classes, what are they, generally?

Classes and Objects are often used interchangeably in software development because they
are basically the same thing.

To be clear though, technically, they aren't.

A class is a definition for how a thing operates and what variables it holds.

An object is an instance of said class.

For example, if we make a class which holds a single number, the instance of the class (the object) will
actually have an assigned value to that number.

# Classes in Python

```python
class class_name:


    def a_function(self):
        print('This is the only function in this class')
```


# Common Things For Classes

Most programming languages have support for making classes and objects by extension, and languages that do this are considered
"object-oriented programming" languages (OOP).

Some similar things you see between these languages are as follows:

### A constructor and class variables:
> the constructor is a method which is called to create an instance of a class and define exactly how it is initialized

> class variables are variables which are available anywhere within the given class (and outside the class if you so choose). Like shown here, they are often initialized within the constructor of a class

> This example also shows an example of a method. This method is being used outside of the class itself, but if we are to use it within the class, we still need an object to call it from. That's where the self keyword comes in handy as it gives us access to the object itself

```python
class Square:
    def __init__(self, input_side_length):
        self.side_length = input_side_length
    
    def calculate_perimeter(self):
        return self.side_length ** 2


my_square_object = Square(12)
print(my_square_object.calculate_perimeter())
```


# Other Common Methods

## Getters and Setter

## _Protected Objects

## __Private Objects



# Object Oriented Programming

Object-oriented programming is the idea of modeling real world ideas, systems a objects as, well
objects in code. This is what we were doing last lecture, but
we are going to more go over conceptually what is the point and extend upon the idea of subclasses
and superclasses.

### The main 3 tenets of object-oriented programming are these three things:

- **Encapsulation**: Restricting the manipulation of an object's state by external user. This is idea of 'information hiding'.
- **Inheritance**: Allowing a (sub) class to automatically reuse and extend the code of another class. (this is idea when you extend a class)
- **Polymorphism**: Allowing (sub) classes to use the same (super) class' method.

*NOTE*: Python is considered an object oriented language despite the fact actually encapsulation
is not necessarily supported by python by default since making something private just makes a
methods name something other than what it originally was, which doesn't actually restrict access to it.

Now, we have not really talked too much about extending classes, so lets go over an example
before we begin actually discussing inheritance and polymorphism.

-----

# EXTENSION

When we make one class extend another, it means a few things:
- A subclass extends a superclass
- the subclass gets access to all public and protect methods/variables within the super class (INHERITANCE)
- the subclass is an instance of the super class and SHOULD initilize the superclass in its __init__
- the subclass can over-load methods of the super classes (sometimes) (POLYMORPHISM)

To do extension, all we need to do is add the super class within the deifinition of a class with ()

```
GENERAL FORMAT:

class subclass_name(superclass_name):
    ...

```

