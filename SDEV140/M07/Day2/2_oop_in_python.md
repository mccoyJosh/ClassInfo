# Object Oriented programming

Object-oriented programming is the idea of modeling real world and abstract objects as code where we assign attributes and actions to them.
This is what we were doing last lecture, but
we are going to more go over conceptually what is the point and extend upon the idea of subclasses
and superclasses.

### The main 3 tenets of object-oriented programming are these three things:

- **Encapsulation**: Restricting the manipulation of an object's state by external user. This is idea of 'information hiding'.
- **Inheritance**: Allowing a (sub) class to automatically reuse and extend the code of another class. (this is idea when you extend a class)
- **Polymorphism**: Allowing (sub) classes to use the same (super) class' method.

*NOTE*: Python is considered an object-oriented language despite the fact actually encapsulation
is not necessarily supported by python by default since making something private just makes a
methods name something other than what it originally was, which doesn't actually restrict access to it.

Another huge part of an OOP Language is that it promotes **abstraction**, which we have talked about in our function discussion!

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


Let's say you had a class which describes a **Person**.
From this class, we can have a class that extends it which gets all of its functions/variables, such as **Student**.
We could also create a **Teacher** class which extends from **Person**.

Both **Teacher** and **Students** are types of '**Persons**', so their shared qualities can
all be represented/implemented within **Person**.



```python
from datetime import datetime


class Person:
    def __init__(self, f_name, l_name, gender, dob):
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        if '-' in dob:
            splits = dob.split('-')
            year_char = 'y'
            if len(splits[2]) == 4:
                year_char = 'Y'
            self.dob = datetime.strptime(dob, '%m-%d-%' + year_char)
        elif '/' in dob:
            splits = dob.split('/')
            year_char = 'y'
            if len(splits[2]) == 4:
                year_char = 'Y'
            self.dob = datetime.strptime(dob, '%m/%d/%' + year_char)
        else:
            print('INVALID DOB FORMAT: USE EITHER m/d/y or m-d-y')

    def get_age(self):
        time_rn = datetime.now()
        time_diff = time_rn.date().year.real - self.dob.date().year.real - 1
        if time_rn.month.real > self.dob.month.real:
            time_diff += 1
        elif time_rn.month.real == self.dob.month.real and time_rn.day.real >= self.dob.day.real:
            time_diff += 1
        return time_diff


class Student(Person):
    def __init__(self, name, gender, dob, id, year):
        super().__init__(name.split(' ')[0], name.split(' ')[len(name.split(' ')) - 1], gender, dob)
        self.id = id
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_grades(self):
        return list(self.grades)

    def calc_gpa(self):
        gpa = 0.0

        grades_num = len(self.grades)
        total = 0
        for g in self.grades:
            g = g.upper()
            if g == 'A':
                total += 4.0
            elif g == 'B':
                total += 3.0
            elif g == 'C':
                total += 2.0
            elif g == 'D':
                total += 1.0
        gpa = total / grades_num
        return gpa


class Teacher(Person):
    def __init__(self, name, gender, dob, id):
        super().__init__(name.split(' ')[0], name.split(' ')[len(name.split(' ')) - 1], gender, dob)
        self.id = id
        self.classes = []

    def add_clas(self, class_str):
        self.classes.append(class_str)

    def get_classes(self):
        return list(self.classes)  # Creates a copy of the classes


b = Student('Bing Bob', 'male', '1/2/2000', '1111112', 'Senior')

print(b.get_age())
b.add_grade('A')
b.add_grade('B')
b.add_grade('A')
b.add_grade('A')
b.add_grade('C')
print(b.calc_gpa())
```

What we can see here is an instance of **inheritance**.
The Student object can call the get_age() method just fine


We can further this hierarchy by perhaps getting more specific.
Maybe I need to represent Students specifically in this class SDEV140.



```python
class SDEV140Student(Student):
    def __init__(self, name, gender, dob, id, year):
        super().__init__(name, gender, dob, id, year)
        self.assignment_grades = []

    def add_new_assignment(self, assignment_grade):
        self.assignment_grades.append(assignment_grade)

    def get_grade(self):
        sum = reduce(lambda x, y: x + y, self.assignment_grades) / len(self.assignment_grades)
        if sum >= 90:
            return 'A'
        elif sum >= 80:
            return 'B'
        elif sum >= 70:
            return 'C'
        elif sum >= 60:
            return 'D'
        else:
            return 'F'

    def add_grade_to_student(self):
        self.add_grade(self.get_grade())
```

----
# Hierarchy

What we end up from these classes extending other classes is a hierarchy of classes.

- ## Person
    - ## Teacher
    - ## Student
        - ## SDEV140Student


What this hierarchy helps to show is a few things:
- As we move from the top down, the subclasses will
  get more and more functionality, as they are inherent the aspects of the superclasses.
- We can now easily create hierarchical structure utilizing classes, as shown here
- Hopefully this shows you how thie helps us save a tremendous amount of time aswell.
  We only had to implement the code about calculating the age once, and every class
  we are using here now has access to it.






-----

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