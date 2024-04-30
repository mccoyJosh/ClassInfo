# Object Oriented programming

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


Let's say had a class which vaguely describes a person:

```python



```
