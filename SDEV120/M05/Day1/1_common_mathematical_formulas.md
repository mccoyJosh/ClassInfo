# Math

Honestly, many of these concepts are going to be
review, but many parts of the IT field and especially
coding is very much math based. So, we are going to
cover just the basics of some math formulas:

------

# Data Set Calculation (Statistics)

Much of what programs do is deal with calculating statistics.

We have lots of data in the world to go through, and having computers do it is very important.

So, before we get into coding these type of problems (which
typically deal with arrays and lists of sorts), we should understand how these calculations work!

## Minimum

The minimum value of set of numbers is the smallest.
To make sure you find the smallest value in a randomly
ordered set of values, you NEED to go through every value to
ensure you find the smallest.

Example:

```
6, 7, 2, 7, 1, 10, -20, 1, 4 , 5
```

The minimum value is -20.

Even if there were two -20's in set of data, we could still
say that -20 is the minimum value.


## Maximum

The maximum value is the LARGEST number in a data set. Again, SAME THING ABOUT SEARCHING EVERY VALUE.


Example:

```
6, 7, 2, 7, 1, 10, -20, 1, 4 , 5
```

The max value is 10 in this set of data.


## Sum

The sum of set of data is the value from adding all of the numbers in that set.

Even though we are adding, the result can still be less than an individual value, since we can add
negative values to each other.


Example:

```
1, 2, 3
```

the sum would be 6!

Summation can also be represetented with the sigma symbol and some identifiers:

![Sum](assets/sum.png)

Here, there are a few things to note:
- the number below the sigma sign (Σ) is the starting value (inclusive)
- the number above the Σ is the ending value (inclusive)
- the 'i' is simply the variable which takes on the value of every value between the starting and end values (working almost as indices)

All the values within the range are then added together!

See example above!


## Count

So the number of items in a set of data is it's count.
It can also be called it's size or length.


Example:

```
6, 7, 2, 7, 1, 10, -20, 1, 4 , 5
```

This set of data has 10 items, so its count is 10.



## Mean

The mean, or average, is the sum of all the values 
divided by the count.

i.e. SUM / COUNT

This gives us the CENTER of all the data in a set.
This can helps us locate generally what this data set is getting.



![Mean](assets/mean.png)


Example:

```
5, 1, 0, 4, 3

SUM = 5 + 1 + 0 + 4 + 3 = 13
COUNT = 5
MEAN = 13 / 5  = 2.6 
```

## Median

The median is the middle number in an ordered set of data.

Now, if this is an odd numbered set of data, this is pretty easy.
Just, put em in order and get the one in the middle.

Only thing to even note is when there is an even numbered set of data.
In this case, located the two middle most values, add em together, and divide by 2.
This is basically just finding the mean/average of the two numbers.

Odd Example:
```
1, 5, 7, 9, 19

      ^
      |
      This value is in the middle: 7
```


Even Example:
```
5, 8, 10, 12, 14, 55
      ^    ^
      |    |
      These two values are in the middle.

      To find the median, you
      median = 10 + 12 / 2
      median =  22 / 2
      median = 11

```


## Mode

The mode is the most common value found within a set of data.

If there are multiple numbers which all have the same number of appearances,
then they are all the modes.

Example:
```
1, 4, 6, 3, 78, 1 , 3, 22, 3, 2, 1, 1

mode: 1
It appears the most
```

Example 2:

```
7, 9, 6, 11, 20, 20, 41, 3, 9

Modes: 9, 29

```


## Range

The range is the difference between the maximum and minimum value.
The range shows how far spread a set of data is.

Example:

```
188, 64, 23, 34, 66, 124, 223

min value: 23
max value: 223

range = max - min
      = 223 - 23
      = 200
```


## Variance (?)



## Standard Deviation



-------
# Others

## Converting between Celcius and Fahrenheit

![Temperature Conversions](assets/temp.png)

- F -> C
- C -> F

show if you just know one of them,
you can find the other


## Converting units

Being able to convert from 
one type of data to another is very important in many situations..

Understanding the basics is important.

Here we are using inches to centimeters.

1 in  =  2.54 cm

When you have one of the two types, you need to set up
a small equation where you are 'getting rid of' your type in a
dision problem.

Just look at this example and understand:

Example 1:

```
8 in

I want it in cm


8 in      2.54 cm
     *   --------- = 20.32 cm
            1 in
```

Example 2:

```
8 cm

I want it in inches


8 cm       1 in
     *   --------- =  3.14 in
          2.54 cm  
```

## Sorting set of data

There are multiple ways or sorting data.

The following sorting method is called bubble sort and
it is pretty ineffcient.

But it is a simple way to understand sorting

![Bubble Sort](assets/bubble_sort.png)

