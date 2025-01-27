# Function (reminder)

When doing anything, it is annoying to do something twice.
Now, specifically for coding, we do already have a solution for this: loops!
Loops allow us to iterate through a problem as many times as we need to.

Problem is, any time there is some sort of change to said problem, or if
we need to code a solution to a technical problem that is required to be found in multiple
locations in our code, loops are not going to cut it.

For this sake, we have functions: repeated chunks of code which can fit different problem sets (when we use
different input parameters).

Functions allow us to break up problems into smaller problems and build up to fixing larger issues.

Instead of trying to solve problems like "running a social media website"
with a very large script, you can break up your code into smaller fragments which, altogether
create the website. A function handling URL request, functions building specific assets
for your pages, and whatever else you need. It is a major part in abstracting out
problems into solutions.

# Functions in general and in python


Functions are found in nearly every language and are defined in various ways.
In Java, a function can be defined as followed:
```java
public class class_name {
    public static int add_one(int num) {
        return num + 1;
    }

}

```

In Golang, a function looks like this

```golang
func add_one(num int) int {
    return a + 1
}

```

**AN IMPORTANT NOTE:** These languages require you to specify the type that the method returns, along
with the type of the variables that the function must accept.

Python sure doesn't require the same things from you!


In python, to create a function, it would look like the following:
```python
def add_one(num):
    return num
```

Python will, just like most things, interpret the type.


Generally the format looks like this:

```
def <METHOD_NAME>(<PARAMETER_1> , <PARAMETER_2> ... <PARAMETER_N>):
    ...code...
    return <MAYBE SOMETHING TO RETURN YOU DON'T HAVE TO RETURN ANYTHING TECHNICALLY>


```

# Parameters
For most problems, you need different info (wouldn't be a very good problem solver if it only ever solved one problem).

That is why you can input any number of items into your function that you want!
To do so, it is just a matter of ascribing a variable name to the 
method header of your method. Here is an example of a function taking two parameters and
multiplying them together.

```python
def multiply(num_1, num_2):
    return num_1 * num_2
```



## Default Parameters
Sometimes when you have a function with many parameters, it can
become inconvenient to use as you HAVE to fill every parameter every time.

For instance, take a look at this piece of code to initialize a matrix:
```python
def init_matrix(rows, columns, init_value):
    r_list = []
    for r in range(rows):
        r_list.append([])
        for c in range(columns):
            r_list[r].append(init_value)
    return r_list


print(init_matrix(2, 2, 0))
```

In most instances, you will probably want to initialize the 
matrix with the value 0, but you don't want to remove the parameter as
to give the option to the user to initialize it to whatever they would like.

To keep both the customizability of a parameter and the
ease of just not inputting a value every time, we can use a DEFAULT PARAMETER:

To use a default parameter, just put an equal sign (=) after your parameter and put the value you want it to be by default.

Here is the same piece of code but using a default value:
```python
def init_matrix(rows, columns, init_value = 0):
    r_list = []
    for r in range(rows):
        r_list.append([])
        for c in range(columns):
            r_list[r].append(init_value)
    return r_list


print(init_matrix(2, 2))
print(init_matrix(2, 2, 100))
```
Now initializing a matrix is easier in most cases, but
it can be initialized to any value given the opportunity.


Something to note:
- cannot put a default parameter before a non-default parameter.

# Recursive Functions

Sometimes, it is useful to call a function from within it self.

When this occurs, it is referenced as a "recursive function"

Not all languages support doing recursive functions, but python is on that does!

Here is a VERY simple example of a recursive function:

```python
def rec_function();
    rec_function()
```

In this example, we can see the VERY basics of a recursive function, as in,
somewhere within itself, it calls itself. This function will also call itself, and
the function within it will call itself.

The code presented theoretically is an infinite loop of sorts.

Now, if we run this code, python will stop it. 
This is because there is a cost in using recursive functions: the stack.
Whenever a function is called, the function from which it was called still needs to exist for when
the function is called ends so that it can finish it's own execution.
This can more easily be seen here:

```python
def example_count_function(num):
    print(num)
    example_count_function(num + 1)

example_count_function(0)
```
This code will print 0 to 998. This shows python's hard limit on 999
recursive steps on the stack. There are ways to increase this limit, but
what you NEED to realize is that right before this code errors out and dies, 
there existed 998 functions "executing" in memory that the computer has
to account for.

This is one the costs of using recursive functions.


----

To outline the few other aspects of recursive functions, we should look at this function:

```python
def rec_add_list(li, index):
    if index < 0:
        return 0
    return li[index] + rec_add_list(li, index - 1)

ex_list = [1, 5, 7, 2, 9, 2, 4]
sum = rec_add_list(ex_list, len(ex_list) - 1)
print(sum)
```

Note these things:
- this does not go on forever; this is because it reaches the BASE CASE!
  - The base case is what your code should be getting closer to
  - In this case, it is the index less than 0 (-1). This is a universal case so that regardless of the size of the list, it will be done working whenever the base case it reached
- We have code pushing us towards the base case (found within the parameters)
  - In our case, is is the index-1 portion of the code.
- Our solution is built and contained within the return statements
  - Unlike an iterative solution where we would create a variable like "sum" to start at 0 and add on to to get the sum through a list, we add up the sum as the functions end
- It is annoying to start the function because we are forced to insert `len(ex_list) - 1` into the function call every time we want to use this function. This doesn't even change between function calls of different lists. This would be a time to introduce a HELPER METHOD
  - It would look like this and we would just call this instead of the other function:
```python
def helper_function_add(ex_list):
    return rec_add_list(ex_list, len(ex_list) - 1)
```

## TRACE RECURSIVE STEPS

Now, if they have this cost to memory and are kinda
more confusing to make compared to just using lists and whatnot,
then why use em?

Well, in some situations, they provide us with elegant solutions where we
are better off using them than a list. This will become very evident whenever we look
at binary trees, but just as a rule of thumb:
if there is a problem where we need to remember a state, it might be
easier to use a recursive function and store everything in a "state" inside of a functions execution!