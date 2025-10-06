# Other Things


## Dead Paths

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



## Missed Boundary

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

