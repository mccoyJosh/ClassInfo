# Selection Range



## Range Check

> the comparison of a variable to a series of values that mark the limiting ends of ranges.



-------


So, AND/OR statements are great for comparing ranges:

Here is how the book shows it off:


![selection_range.png](assets/selection_range.png)

This would be a good way to bread down grades in a class ranges.

## THIS IS BETTER FOR A BINARY RANGE

Here is how you would do it with OR... and it be wrong:

```
num = input()
if  num >= 0 OR num <= 100:
    output "It is between 0 and 100"
endif
```

This is a bad way to do it, since it wouldn't work, so you should probably use AND

Here is how you would do it with AND:

```
num = input()
if num >= 0 AND num <= 100:
    output "It is between 0 and 100"
endif
```


# The general rule of thumb is, if you need a range between values, use an AND statement; if you need to include number outside of a range of values, use an OR statement.

Like we saw, if we want to check if an input is between 0 and 100, we can use an AND statement to do so:

```
if num >= 0 AND num <= 100:
...
```

and if we wanted to check if something falls outside that range, i.e. less than 0 and greater than 100, we can use OR:
```
if num < 0 OR num > 100:
...
```

Technically, you can also get these by negating whatever it is you are trying to exclude

# Dead Paths

Sometimes, in a series of nested if statements, there can exist a path which does not execute.
For instance, check out this piece of code:

```
num = input

if num > 100 then
    print("thingy")
else
    if num == 204 then
        print("Another thing")  // This line/path is a dead path since we would only be in the outer ELSE if the num was less then 100, which 204 is not.
    endif
endif

```



# Missed Boundary

When coding to make sure all cases are covered.
Sometimes you forget to include a number or range of numbers within your checks

For instance, here:

```
isPositive num

result = ""

if num > 0 then
    result = "Positive!"
endif

if num < 0 then
    result = "Negative!"
endif

return result
```

In this example, we cover every value except 0 itself. In
this case, if 0 is our number, an empty string is returned.

This is our missed boundary; we would want to make sure all values are included,
so we would want to add a check for 0 as well!

