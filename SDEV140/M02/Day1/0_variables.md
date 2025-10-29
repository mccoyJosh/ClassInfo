# Variables
assigns a value to a identifiable name
typically in this fashion:
<variable name> = <expression>

example:

```python
variable = 1
```

the word variable can be used here on out to refer to the value of 1
anything you could have done with 1, you can do with variable




## TYPES
in other languages, you need to explicitly tell the code what type
of value you are using the variable for


python is smart, as in you only NEED to provide an expression, and it can assume the type of the variable
```python
var_1 = 10
print(type(var_1))

var_2 = "cat"
print(type(var_2))
```

if you know the type of variable you would like, you can tell python what a variable type is going to be:
string_variable: str
this doesn't prevent you to reassigning it to another type, but it cant help make your code readable



## NAMING
you should make your variables named properly as to what they do

```python
val_1 = 10
val_2 = 10
val_3 = 10
```

DON'T NAME IT SOMETHING LIKE X
```python
x = val_1 + val_2 + val_3
```

If this variable is holding the sum, name it sum:

```python
sum = val_1 + val_2 + val_3

```

Name the variables based off of its purpose in the code



