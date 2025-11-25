# Types of progrmaming

----

These definitions of imperative/procedural/functional programming styles
are taken from the book.

In these definitions, they treat each type as their own 
exclusive type of programming, where every
other reference on this earth lays it out differently.

See the geeksforgeeks reference at the end, but really imperative programming is
a broader term to describe a slew of other types of programming types, which both
procedural and OOP are under, while functional programming is within the
declarative programming schema.

So, take this with a grain of salt!

----

## **Imperative programming**:
is an approach where code consists of commands for input, 
output, assignments, and control flow, suitable for simple 
tasks and short code sequences 

Think short programs which just some input, some if statements

-------

## **Procedural programming**:
an approach where complex problems are broken down 
into simpler subproblems, each solved by separate subprograms. 
These subprograms reduce the need to track
numerous program components and minimize dependencies among them.

This would be separating your problem out into multiple different
methods, for instance, and calling said methods for each
part of your programming.


----

## **Functional programming**:
an approach where a program is composed of cooperating functions. 
Each function is a highly restricted subprogram, solely responsible 
for transforming data in its arguments into other data 
(its returned value). 

**_Unlike imperative programming, functional programming avoids 
assignment and relies on expression evaluation and function 
calls for computations_**. It simplifies program complexity 
but may not conveniently model scenarios where data objects 
need to change state

This would be like when we used reduce to get the sum of values
in a list.


---
# **Object-oriented programming (OOP)** 
an approach that manages program complexity while 
modeling data that change state. In OOP, data is divided 
into small units called objects. Each object is responsible 
for managing its own data. Objects can collaborate by calling 
methods defined in their superclass or relying on other objects. 
The goal is to divide responsibilities among independent components, 
reducing the risk of system breakage during changes

----

# Overuse of OOP

Object-Oriented Programming Can Sometimes get overused...
Do not think about these different types of programming as
like a hierarchy of better and better ways to program...

Sometimes it is better to NOT use an object, and it is entirely dependent on
your problem.

### Object-Oriented Programming (OOP) – Best Use Cases:

1. **Complex Systems with Interrelated Entities:**
   - **Example**: Building a simulation of an ecosystem with animals, plants, and environmental factors.
   - **Reason**: OOP allows modeling entities as objects with properties (attributes) and behaviors (methods). Relationships between entities can be represented using inheritance and composition.

2. **Software Reusability and Maintainability:**
   - **Example**: Developing a large-scale application with reusable components.
   - **Reason**: OOP promotes modularity, encapsulation, and code organization. Reusable classes (objects) can be easily extended or modified without affecting other parts of the system.

3. **Graphical User Interfaces (GUIs):**
   - **Example**: Creating a desktop application with buttons, menus, and interactive elements.
   - **Reason**: OOP aligns well with GUI development. Widgets (buttons, text fields, etc.) can be represented as objects, and event-driven programming simplifies handling user interactions.

### Object-Oriented Programming (OOP) – Not Ideal Use Cases:

1. **Performance-Critical Systems:**
   - **Example**: Real-time simulations, or embedded systems with strict resource constraints.
   - **Alternative**: **Procedural programming** is better for fine-grained control over memory and performance optimization.

2. **Functional Transformations and Pipelines:**
   - **Example**: Data processing pipelines, map-reduce tasks, or functional transformations.
   - **Alternative**: **Functional programming** excels in these scenarios. Functions as first-class citizens and immutability simplify data transformations.


# Here are some websites which really explain this well:

- https://www.scoutapm.com/blog/functional-vs-procedural-vs-oop
- https://www.geeksforgeeks.org/what-is-imperative-programming/