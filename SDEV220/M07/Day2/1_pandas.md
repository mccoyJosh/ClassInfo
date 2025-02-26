# [Pandas](https://pandas.pydata.org/)

Whenever you need to quickly analyze a set of data 
and do not want to worry yourself too much the details of code and
just need it to WORK, this is when we use pandas.

Pandas is an open source library to deal with sets of data and allows
you quick access to analyze, clean, search and manipulate the data within.

The way we access is very similar to how we mess with data in a database,
so pandas essentially creates for us an easy-to-use database access tool.

If you are looking into doing anything related to DATA SCIENCE, pandas is where you are going to want to look:

# Installation

Just like everything else we have installed, you can get pandas from pip:

```
pip install pandas
```

# Intro

So, let's start messing with stuff.
If you look inside the pandas example directory, there is a csv file we are going to
use as example!

To open up a csv file and bring all the data into our python file, we can use this
piece of code:

```python
import pandas as pd

df = pd.read_csv('data.csv')
```


With this now in our code, we can start accessing the data in many,
many ways.


This command here will retrieve for you first 5 values in your dataset!
This is the beginning of many, many ways to analyze data.
```python
df.head()
```

If you need more or less number of items from the top of our data, we can also pass 
a number into head. This would give us the top 10 values of our data:
```python
df.head(10)
```

If we want the last values in our list, we can use tail in just the same way!

```python
df.tail()
```

# Analyzing General Data

With our data in hand, we can begin looking at it:

We can see the columns of data we are working with 'columns':
```python
df.columns
```

And the data types help within ith 'dtypes'
```python
df.dtypes
```

It gives us this nice little look into how it is interpreting each column:
```
ID                                    int64
DOB                                  object
First Name                           object
Last Name                            object
Gender                               object
Net Worth                           float64
City                                 object
State                                object
Country                              object
Phone Number                          int64
IQ                                    int64
Height (FT)                         float64
Controversies                         int64
Highest Level Of Education           object
Number Of Children                    int64
Political Party                      object
Occupation                           object
Number Of Old Ladies Pushed Over      int64
EVILNESS                              int64
```

We can see that it considers things which are not like numbers "object" types instead
of something like Strings as to make it more universal.


Now with pandas, we can very quickly get some general statistics on our data!

By simply running `df.describe`, our data is immedielty evaluated in terms of
the count, mean, standard deviation, minimum and maximum values, and MORE.

Also, note that these values it is evaluating are only applicable to number based
values like integers and floating point numbers, as it doesn't make much
sense to get the mean of a first name!

```python
df.describe()
```

Although, there are things we can find out about our other data such as our strings
(which again, are considered objects):

So, if wanted these statistics for just strings, we would do this:
```python
df.describe(include='object')
```

This will give us information like how many unique values of strings there are, and what is the
most common and how many of that most common item there is.


Also, if we only wanted the described data for something like the 64 bit integers, we could also do that!

```python
df.describe(include='int64')
```

# How data is stored

I don't know if you have noticed, but all the data we have seen so far is stored as tables which are simple printed
out. This is known as a Data Frame, or specifically ```pandas.core.frame.DataFrame```.

This means that everything we create is going to be accessed the same. So, for instance, we could do something like this:
```python
df.describe(include='object').describe(include='object')
```
And it will describe the data found in the table produced from the description of the initial data.

This works because both the initial table and the resulting data (and the final table) are all the same
type: Data Frame.

So, we are about to see how to access specific columns and info in a table, but keep in mind that
the same techniques are also going to work for things like the describe table and head tables.


# Filtering Data (COLUMNS)

With all this data, we need to start shortening it and filtering out the stuff we don't need.

If just need a specific column of data (like Occupations) from our set of data, we can get it by
two ways:

- Like it is a class variable:
```python
df.Occupation
```

- Like it is a key in a dictionary
```python
df['Occupation']
```

Now, for column names which have spaces in them, you are required to address them as dictionary objects.

## Aside: Series (aka: `pandas.core.series.Series`)

The results from getting these columns is what's known as a Series (the first none Data Frame
object we have seen). Series are simpley a glorified array which is for pandas to 
utilize in its data manipulation.

If you think about it, a column of data is simply an array of data anyways.

Because of this, we can access specific row values in a Series just like a list/tuple/array.
For instance, this would get the second rows First Name and Occupation and print it out:

```python
print(df['First Name'][2], df.Occupation[2])
```


Within these series, we can ask for many things.
One such thing is the unique values within the series:

```python
df['Occupation'].unique()
```

Or we can ask for specific metrics on a column, like mean:
```python
df['IQ'].mean()
```


## Aside Over, back to filtering

Now, in the aside, this would be a very dumb way to get multiple values from a data set.
We can more easily get multiple columns of data utilizing the same
dictionary addressing format.

Since it is still KINDA being addressed like a dictionary, we still need to only 
pass it one value, but that value can be a list of the different columns we want:

```python
df[['First Name', 'Last Name', "Occupation", "IQ"]]
```

_DO NOTICE THAT THE VALUE WE ARE PASSING IS NOT SIMPLY THE ITEMS WE ARE LISTING,
BUT A LIST OF THEM!! SO, PLEASE ENSURE YOU USE 2 brackets: [[]]_

Also, the result from this is NOT a series, but rather a Data Frame. 
Whenever we are working with mutliple columns, we have a Data Frame.

A single column SHOULD just be a Series (unless we obtained it in a fashion we would normally get a Data Frame)

# Filtering Rows

Now with all this mind, we can being actually filtering our data based on the values inside.
If we only wanted to rows of data which are people employed as farmers, we could address that like this:

```python
df[df["Occupation"] == "Farmer"]
```

Now, there are a few things happening here, so lets walk through it.

When we just look at the different steps in this process, we can see that 

- Type of `df['Occupation']`: <class 'pandas.core.series.Series'>
- Type of `df['Occupation'] == 'Farmer'`: <class 'pandas.core.series.Series'>
- Type of `df[df['Occupation'] == 'Farmer']`: <class 'pandas.core.frame.DataFrame'>

So, we are:
- Firstly, getting a Series of data just like before
- Filtering the rows in the Series which are "Farmer"
  - This results in new series which only contain the id for the row, along with a boolean expression:
    - ```
      0       False
      1       False
      2       False
      3       False
      4       False
      ...  
      3595    False
      3596    False
      3597    False
      3598    False
      3599    False
      Name: Occupation, Length: 3600, dtype: bool
      ```
- This boolean series is used to remove the rows which are 'False' from our main set of data
- It produces a Data Frame with only the Farmers

What is allows us to do it finally start getting for specific data from our data set.
For instance now, we can see what the most common Education level of a Farmer is and what their mean IQ is:
```python
import pandas as pd
df = pd.read_csv('data.csv')


only_farmers = df[df['Occupation'] == 'Farmer']
print(only_farmers.describe())
print(only_farmers.describe(include='object'))
```

We could also query on things like number values. For instance, if we wanted to see
only the data on individuals with an IQ greater than 120, we could do that with this piece of code:

```python
import pandas as pd
df = pd.read_csv('data.csv')


result = df[df['IQ'] > 120]
print(result.describe())
print(result.describe(include='object'))
```

### Multiple Queries

If we wanted to filter our data by multiple parameters, we could do this easily with some boolean expressions.

This for instance would search for individuals who have an IQ greater than 120 **AND** whose
greatest level of education is High School.

We make sure to use the `&` symbol for AND queries:
```python
import pandas as pd

df = pd.read_csv('data.csv')

result = df[(df['IQ'] > 120) & (df['Highest Level Of Education'] == 'High School')]
print(result.describe())
print(result.describe(include='object'))
```

If we wanted to see all individuals who are EITHER a Gardener **OR** a Farmer we can run the following piece of code.

We make sure to use the `|` symbol for OR queries:
```python
import pandas as pd

df = pd.read_csv('data.csv')

query1 = df['Occupation'] == 'Gardener'
query2 = df['Occupation'] == 'Farmer'

result = df[query1 | query2]
print(result.describe())
print(result.describe(include='object'))
```

## Specific Rows  (iloc)

We can get a much nicer representation of a row with the iloc method as well.
For instance, if we want the 14 person in our data, we can run this set of commands:

```python
import pandas as pd

df = pd.read_csv('data.csv')

print(df.iloc[14])
```

This returns to us a Series object with the data from this specific row.

We can than access this just like a normal series, so if we wanted the just name,
we could ask for it by also asking for the col 3:

```python
import pandas as pd

df = pd.read_csv('data.csv')

print(df.iloc[14, 3])
```

We can also use this to get slices of our data. 
So, if we wanted to do exaclty what the head function does, we could run this piece of code:
```python
import pandas as pd

df = pd.read_csv('data.csv')

print(df.iloc[0:5])
```

What we are also given the ability to do is change what the id
of our Data Frame is. Currently and by default it is an integer. BUT, we can change that to any thing we would like.
For instance, we can make the Occupation the id for the rows, and this would then allow us to use LOC
to filter by only farmers:
```python
import pandas as pd

df = pd.read_csv('data.csv')

occu = df.copy()
occu.set_index('Occupation', inplace=True)
just_farmers = occu.loc['Farmer']
print(just_farmers)
```

This just gives us another way to filter.

# Getting Specific Rows

If wanted to start getting specific data, we already have all the 
tools we need. If we for instance want to get the smarted person (based
on IQ), we can with this simple query:
```python
import pandas as pd

df = pd.read_csv('data.csv')

smartest_people = df[df['IQ'] == df['IQ'].max()]
print(smartest_people)
print(smartest_people.iloc[0])
```

Now, in the provided data set, we only have 1 person who fits this example, but 
we could have ended up with multiple people.


# Updating Data

Now, once we have data, we are not limited to keep EVERYTHING as is.
We can add and remove data as we please.


### Removing Rows

So, for instance, if we were trying to reduce our data down to individuals who were the most evil,
(top 10% EVILNESS) we can do this with the drop function.
We just drop the lower 90%, and the remove them by getting their indices.

```python
import pandas as pd

df = pd.read_csv('data.csv')

df.drop(df[df.EVILNESS < 90].index, inplace=True)
print(df)
```

### Remove Columns

If we have too many columns, for instance, we could also cut down on its size using drop aswell.
For instance, if we were really trying to narrow in on the people who are pushing over old ladies and how evil they are, we
would want to remove a lot of the identifiers as they are irrelevant, so, we could remove them by running code like this:
```python
import pandas as pd

df = pd.read_csv('data.csv')

df.drop('ID', axis=1, inplace=True)
df.drop('City', axis=1, inplace=True)
df.drop('State', axis=1, inplace=True)
df.drop('Country', axis=1, inplace=True)
df.drop('Phone Number', axis=1, inplace=True)
df.drop('Controversies', axis=1, inplace=True)
df.drop('Political Party', axis=1, inplace=True)
df.drop('Number Of Children', axis=1, inplace=True)
df.drop('Height (FT)', axis=1, inplace=True)

print(df)
```

Now, keep in mind, the 'inplace=True' simply applied this change to df. If we didn't do that
and wanted to keep these changes, we would have to do:
```python
df = df.drop('Height (FT)', axis=1)
```

They work the same way!


### Adding Columns

Adding a new column to the data set is actually fairly easy. All we need
to do is address it like a dictionary and tell it what to put there.

For instance, if we wanted to save on to this a ratio of the number of old ladies pushed over
and how 'evil' someone was, we could in a new row where we make that simple calculation:

```python
import pandas as pd

df = pd.read_csv('data.csv')

df['Evil Pushing Ratio'] = df['Number Of Old Ladies Pushed Over'] / df['EVILNESS']

print(df)
```


### Change Whole Column

We could then change that data to anything we would like by just re-assigning it.
Updating the entire column works exactly the same as adding it in the first place.

```python
import pandas as pd

df = pd.read_csv('data.csv')

df['Evil Pushing Ratio'] = df['Number Of Old Ladies Pushed Over'] / df['EVILNESS']
df['Evil Pushing Ratio'] = .99

print(df)
```

### Updating on specific parameters

We can start changing specific rows based on conditions using many, many different techniques.
One such technique is the apply function in conjunction with lambda functions.

Here, we are going through and making all the most evil people unemployed, because they are evil,
I guess.

Do note axis = 1, as we need access to the specific columns of this data piece.

```python
import pandas as pd

df = pd.read_csv('data.csv')

df["Occupation"] = df.apply(lambda x: 'Unemployed' if x.EVILNESS == 100 else x.Occupation, axis=1)

print(df[df['EVILNESS'] == 100].head())
print(df.head())
```


-----

# Output

When we are finally done working with our data, we can easily convert it to a data format
and create a file.

This works like the opposite of reading the data in, so
instead of 'from_format', we use 'to_format' and give it a filename.

To convert it to a csv file, we can do that like this:
```python
df.to_csv("new_data.csv")
```

If we wanted it to be JSON, we could do this:

```python
df.to_json('new_data.json')
```

This also means we can EASILY read in and convert to any data format we need!

This also include HTML, which will allow us to view this data in the browser:
```python
df.to_html('data.html')
```


# Delete it when you're done and don't need it

When you are finally done working on your dataset, it is probably wise to delete it from your
program so those resources can be reused elsewhere!

```python
del df
```

------

# Not Just CSV

I know we looked at using csv in this example, but pandas can also be used to analyze many, many other forms of
data, including:

- SQL
- EXCEL
- HTML
- JSON
- Pickle
- XML
- Feather
- Clipboard
- Parquet
- Orc
- Hdf
- Gbq

What this results in is a very easy way to transfer between
and manipulate different data types with very similar code,


Here is an example of reading a json file
```python
import pandas as pd

df = pd.read_json('data.json')
print(df.head())

```
