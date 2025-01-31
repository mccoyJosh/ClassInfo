# Data Formats &/|| Encodings

When using computers, how we store and translate data, is VERY important.

The way we store data can often vary its
- memory use
- efficiency
- simplicity
- how versatile and adaptable it is
- how structured it is

## Binary
Technically the most bare version to encode data. This is just straight up what
the computer stores. This is not super useful for most of our high level applications though, so

- VERY good for memory use
- VERY efficient
- not very simple (for us)
- not very versatile
- not super structured


## Text

Text is one of the simplest data format.

We have already talked about how text is represented by ASCII values on the computer, and those ASCII numbers are actually represented as binary on the hardware. 

Simply characters on a screen organized however we may like.

This is exactly the problem with characters being used as a data format!
Most of the time, we do not want characters organized in any which way, and instead 
be in a specific structure to match the object or data we need them to represent.

- very simple
- very versatile
- has no structure

The rest of these data types are going to be built on characters in different ways, but just uses
them to organize differently.

The full process looks like this:

[data format] -> Characters -> Numbers (in ASCII) -> Binary

## CSV (Comma Separated Values)

The first data format is CSV.

This data format is:

- simple
- pretty versatile
- has some structure

We can store data within a table like structure by separating every value with a comma. Its that simple
Most CSV files will reserve the first line (row) in the file for headers as to explain what each column is.

Here is a simple example:
```
id,first name,last name,age,amount
1231,Jim,Bim,53,100235
212,George,Lorez,23,3
981,Francis,Jumper,45,42234
```

Most csv files also have support for any table-like software, like Excel or Numbers. The should allow you to import/export
data in this format, which makes it very versatile between programs.

There are only a few downsides:

no unique data, since every row must have the same number of columns to line up with the header.
You could always insert unique data at the end, but you will then be adding complexity on top of what's suppose to be
a simple data structure.

Also, using commas within what's suppose to be the data can be complicated, since they SHOULD be distinguishing 
when data should begin and end. Typically to avoid the comma's deliminator nature, you can surround the field with double quotes to indicate that is a string. Also, to then use double quotes as the double quotes characters instead of a deliminator, you use 4 double quotes. Also also, this can change with different implementations of CSV files, so beware.

Also, you only know what the data means with the help of the header. Other data formats has built in tags with every value you store.

## JSON (JavaScript Object Notation)

The **J**ava**S**cript **O**bject **N**otation (JSON) format is a human-readable way to represent objects
of any language. It does this by utilizing key value pairs for values of variables and by containing whole objects
within {}.

This can look EXTREMELY similar to Python's dictionary.


### EXAMPLE 1
```JSON
{
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "hobbies": ["reading", "swimming", "coding"]
}
```

As can be seen by hobbies, you can also represent lists using []s

In this second example, we see a list of books, each being their own unique object

### EXAMPLE 2

```JSON
{
  "books": [
    {
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "year": 1925
    },
    {
      "title": "To Kill a Mockingbird",
      "author": "Harper Lee",
      "year": 1960
    },
    {
      "title": "1984",
      "author": "George Orwell",
      "year": 1949
    }
  ]
}

```


---

## XML (eXtensible Markup Language)

The e**X**tensible **M**arkup **L**anguage (XML) is also a human readble way to store data for any object.
The way it does this is VERY similar to HTMl, if you have seen that. 

The key value pairs we saw before have been converted to opening and closing tags of said values.
A list now just becomes saying what the object is over and over again instead of just using []


### EXAMPLE 1

Here is that same JSON object in XML

```XML
<person>
  <name>John Doe</name>
  <age>30</age>
  <city>New York</city>
  <hobbies>
    <hobby>reading</hobby>
    <hobby>swimming</hobby>
    <hobby>coding</hobby>
  </hobbies>
</person>
```

### EXAMPLE 2

```XML
<fruits>
  <fruit>
    <name>Apple</name>
    <color>Red</color>
    <calories>95</calories>
  </fruit>
  <fruit>
    <name>Banana</name>
    <color>Yellow</color>
    <calories>105</calories>
  </fruit>
  <fruit>
    <name>Orange</name>
    <color>Orange</color>
    <calories>62</calories>
  </fruit>
</fruits>
```

## HTML (HyperText Markup Language)


XML is extremely similar to HTML!
HTML is mainly use in webpages.

We will get to rendering webpages later, but it also utilizes this same format of
tags delimitating the beginning and the end of a section.