# Time Complexity


# STRESS THAT "LESS EXECUTIONS = MORE EFFICIENT CODE (obviously)"

# No loop example
```python
val = 10
val = val ** 2
print(10)
```
This line has 3 lines of execution
A single statement is typically considered an execution


----

# Loop example

```python
numbers = [1, 2, 3]
sum = 0

for num in numbers:
    sum = sum + num

print(sum)
```

What is the number of executions for this code?

```python
numbers = [1, 2, 3]   # 1 execution
sum = 0               # 1 executions

for num in numbers:   # 4 (3 for each num it gathers and then 1 for the final 'check')
    sum = sum + num   # 3 (1 for each loop iteration)

print(sum)            # 1 execution
```

Total number of executions: 1 + 1 + 4 + 3 + 1 = 10

If we add 1 more item to the numbers list, the loop will iterate 1 more time

If there are 10 items in the list, the loop would have this many executions
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
sum = 0              

for num in numbers:   # 11 
    sum = sum + num   # 10
```

We are starting to see a pattern. The number of executions is tied to that of the numbers list input size
If we abstract the list out just a bit and say instead of it having '10', or '5' values, lets just say it has N values

If that is the case, how many executions will this loop have?
```python
for num in numbers:   # n + 1 
    sum = sum + num   # n
```

This is considered a 'linear problem'. As the input size increase, the number of executions increases with it
linearly.
If we add up all the exeuctions (1 + 1 + n + 1 + n + 1) we get 2n+4.


This equation will give us the exact number of times the code we have created will execute depending on
the size of the list.


-----

# Nested loop example

If we look at the nested loop code we had previously created, what would its time complexity be?

```python
box_size = 2                   # 1

for i in range(box_size):      # (2 + 1)
    for j in range(box_size):  # (2 + 1) * 2 
        print('x', end='  ')   # 2 * 2
    print()                    # 2
```

the box size variable here is our input size (N)
If we again generalize the problem and say that we have a box size of 'n', what would be the number of executions


```python
box_size = N                   # 1

for i in range(box_size):      # (N + 1)
    for j in range(box_size):  # (N + 1) * N
        print('x', end='  ')   # N * N
    print()                    # N
```

What we see is that the inner loop must perform its own actions N number of times, and the whole inner loop must be ran
N number of time due to the outer loop. Thus, we find the inner loop being N^2 or (N^2 + N).
Let's get an equation from this:

1 + N + 1 + N(N+1) + N(N) + N
2 + 2N + N^2 + N + N^2
2N^2 + 3N + 2


----

# Graph of time complexities

The whole point try to get across is that the way in which you design your code can make it take longer to run
(i.e. make more executions). There are many ways to solve specific coding problems, and some of these solutions
are slower when compared to others. So, just keep in mind what you are coding.

We looked at linear time and exponential time, but, there are worse (and better) rates of code. We don't
really get to get too deep into time complexity in the course due to time restraints, but this should be
an alright introduction.




------

# Compare Binary Search vs Non-Binary Search
