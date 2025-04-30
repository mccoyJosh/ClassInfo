# Polymorphic Methods

Now the idea behind creating subclasses and extending other classes
is become the subclasses are close enough to each other in nature to have a 
need to utilize the same super class for some reason.

But, obviously, subclasses are different... otherwise they wouldn't
be separate classes. 

In some cases, different subclasses may want to both override a method in its super class.

This can happen when the super class is something more like an interface that it's subclasses
all need to follow. 

# Simple Example:

```python
class Animal:
    def make_sound(self):
        pass  

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

def animal_sounds(animal):
    print(f"{animal.__class__.__name__} says: {animal.make_sound()}")

dog = Dog()
cat = Cat()
bird = Bird()

animal_sounds(dog)  
animal_sounds(cat)  
animal_sounds(bird)
```

This is a simple example of polymorphism. We can see each subclass of animal filling in the 
method 'make_sound' and then the animal_sounds method just needs to expect an animal
type object, and it can be rest assured that the .make_sound() method is implemented.

Keep in mind that the way we made the in method in the super class was just using pass, as in we had it do nothing.

We could have made a default response for the method if we had chose.
For instance, maybe we want the animals which lacked the implementation of sound to just say 'Nothing'.
We can do that just fine!

```python
class Animal:
    def make_sound(self):
        return "Nothing"

class Dog(Animal):
    pass
```

-----

# Better Example:



Think for example like a superclass being a general idea like "**Shape**"
and the subclasses being '**Circle**' and '**Square**'. We may want the ability to compare said shapes
(whether that be by area or perimeter), but the **Circle** and **Square** classes would need to have their
own methods on how to find area and perimeter. SO, the **Shape** superclass would simply have 
some interface for 'get_area' and 'get_perimeter', FORCING the subclasses to implement them,
and then the **Circle** and Square **classes** just implement them. This would then allow
for a method in the super class to override something like the < symbol to compare two objects.

The overriding of the get_area and get_perimeter methods would be an example of polymorphism in action.

Here is that example:

```python
class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __lt__(self, other):
        return self.get_area() < other.get_area()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

    def get_perimeter(self):
        return 2 * 3.14 * self.radius


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

    def get_perimeter(self):
        return 4 * self.side_length


circle1 = Circle(radius=5)
circle2 = Circle(radius=3)
square1 = Square(side_length=1)

print(f"Is circle1 smaller than circle2? {circle1 < circle2}")

# Compare squares based on area
print(f"Is square1 smaller than square2? {square1 < circle1}")

```

This shows the Shape method as more of an interface, ready for its subclasses to 
do most of the implementation and really just ready to describe how to compare
shapes in general!


----

# THIS IS SUPER IMPORTANT IN OTHER PROGRAMMING LANGUAGES WHERE YOU ARE REQUIRED TO 
# PUT THE TYPES OF VARIABLES BEFORE USIN' THEM

For instance, by using subclassing, you could make
a list which holds the type of a super class, and that list would
allow the subclasses to be stored within it. Otherwise though,
you could not store different types in a list.