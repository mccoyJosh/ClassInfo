# Time

Time is a very important thing to know how to do in python, obviously.

Now, many things with time can be annoying to deal with.

Think for example of just trying to get the correct time for your location.
With the number of time zones on earth, this alone can be a tremendous task.
This is especially true as some places don't use the timezone they fall in and 
rather run with a time that is more politically/economically/culturally suited 
for them.

Due to this problem, it is best to teach yourself how 
to use the many, many tools at your disposal to manage time that are already made.

# Python datetime

One of the built-in packages in python is datetime.
As you might notice, it is used to get many, many things related to the time.

If you are trying to store a date, for instance, you can easily do this with the date object
that is part of the package:

```python
from datetime import date

today = date(2025, 2, 19)
```

You can then use the same date objects to do many, many things. For
instance, if you wanted to see the number of days that passed between two days, you
can simply subtract date objects from each other.

Also, note that you can more easily get today's date by calling another package datetime.
Another note: 

```python
from datetime import date, datetime

today = datetime.today().date()
new_years_day = date(2025, 1, 1)

print(today - new_years_day)
```

To convert simple strings to get the date, there is also code already made for
that too. It is also in the datetime package:

```
THIS WOULD CONVERT THE STRING WHICH SPECIFICALLY HAS THE MONTH FIRST, THEN DAY, THEN YEAR 
datetime.strptime(input_date_string, "%m/%d/%Y")
```

This package also has built in constraints  on days which have to be days.
So, for instance if you type in a date that can't exist like 13/40/2024,
you get an error. Again, saving us time. This checking also accounts for the
extra day on leap years, and MORE!

Here is an example of using it 

```python
from datetime import datetime

input_date_string = input('Please type in the date you want to know time since MM/DD/YYYY: ')

today = datetime.today().date()


# CONVERT TO DATE OBJECT
input_date = datetime.strptime(input_date_string, "%m/%d/%Y").date()

date_diff = today - input_date

print(f"Days since then: {date_diff.days}")
print(f"Months since then: ~{date_diff.days/30 : .2f}")
print(f"Years since then: ~{date_diff.days/365 : .2f}")
```


# Python time

Another very useful tool is the time package. It does 
alot of what the date package, but just for time!

The way computers can often store time is by starting
at a certain point in time and count seconds since then.

For instance, there is the VERY popular Unix time, which 
count the seconds since midnight of January 1, 1970 (this is 
often referred to as the EPOCH).

We can get this time using the TIME PACKAGE.
Here, we get it and print it out.

```python
import time
now = time.time()

print(now)
```

Now, typically this epoch number is stored as a single integer value. What 
this means is that, for some systems, this number since epoch will eventually get
too big for it to store. For instance, if you are on a 32 bit system, you most likely using
a 32 bit signed integer to store this unix time, which caps out
at 2,147,483,647. We reach more seconds than this on January 19, 2038.

Now, some computers have switched over to using UNSIGNED integers to help extend the lifetime to February 7, 2106, but
for most of us, this won't be a problem. The computer you are using is MOST LIKELY a 64 bit device, in which case, you
will not exceed this limit until 292 billion years from now. 

What is at risk are embedded systems. That is, devices which have hardware and software on them which
are produced and never updated. Think for instance, medical equipment. If a medical device uses a 32 bit
architecture, there is no REAL WAY to update its software to account for this bug, and it will most likely just break
after the 2038 mark.

Currently, smart people are fixing this bug from being TOO big of a deal, but it
is probably going to make some people go crazy like Y2K.

Anyways, here is a timer counting down to that moment:

```python
import time


lg = 2 ** 31

curr_diff = lg - int(time.time())

go_for_this = curr_diff - 100 # Only runs this for 100 seconds

while curr_diff > go_for_this:
    if curr_diff != lg - int(time.time()):
        print(curr_diff)
        curr_diff = lg - int(time.time())
```

Also, to get more example set of time, we can use "localtime()" instead
of time which gets us the number of hours, days, and years it is currently (like, the datetime object).

```python
import time

start_time = time.localtime()
print(start_time)
```

# Timer

With this package, we do a few tasks, for instance make a timer of sorts.

Here is a simple example of just counting to 10:

```python
import time

print("It has been NO seconds")

start_time = time.time()
end_time = start_time + (10)  # After 10 seconds

while time.time() < end_time:
    pass

print("It has been 10 seconds")
```




# Stopwatch

We can also utilize this same package for finding how long things take (time wise).

This is incredibly useful as it will allow us to see if our processes are faster/slower than 
other implementations of algorithms (we have some way to measure our performance).


Here is some code comparing going through every index of both
a list and a tuple and seeing which one performs better 
after 100 tests on average. Notice how implementing 
a stopwatch just quires us to make a start time and end time 
and then find the difference between them.

```python
import time

re = range(90000)
li = list(re)
tp = tuple(re)

look_for = -1

number_of_it = 100

time_total_tp = 0.0
time_total_li = 0.0


# Seeing how long to go through the entire tuple and list version of these objects:

for i in range(number_of_it):
    # LIST
    li_start = time.time()
    for index in re:
        if look_for == li[index]:
            print('I found it')
            break
    else:
        print('Did not find')
    li_end = time.time()

    list_time = li_end - li_start
    time_total_li += list_time

    # TUPLE
    tp_start = time.time()
    for index in re:
        if look_for == tp[index]:
            print('I found it')
            break
    else:
        print('Did not find')
    tp_end = time.time()

    tuple_time = tp_end - tp_start
    time_total_tp += tuple_time


print(f'Tuple Time: {time_total_tp/number_of_it:.5f}')
print(f'List Time:  {time_total_li/number_of_it:.5f}')

```


