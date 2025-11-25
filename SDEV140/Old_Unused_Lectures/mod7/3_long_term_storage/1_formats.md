# Data Formatting

Here we are going over more complicated ways to save our data.
With these organizations of data, we can
much more effectively store different types of objects.

----

## CSV
The data format we are talking about is CSV, aka, Comma Seperated
Values.

This format is what it sounds like... a set of values
seperated by commas.

This is the simplest data format. This format is especically good
for representing tables, as each line can be a row, and each comma
seperated value can be a column. 

Microsoft Excel and other datasheet type programs will even allow you
to export/import CSV files of tables.

### EXAMPLE

```
Name, Age, Grade
Alice, 20, A
Bob, 22, B
Charlie, 19, C
```


----

## JSON

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

## XML   

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


----
## Others

- YAML 
```yaml
name: John Doe
age: 30
hobbies:
  - reading
  - swimming
  - coding
```

- Protobuf
```protobuf
syntax = "proto3";
message Person {
  string name = 1;
  int32 age = 2;
  repeated string hobbies = 3;
}
```

Protobuf is a highly effiecient communication method as it can send lots of data without much data.
This is only possible because both sides know what 1, 2, and 3 means, as they are mapped on both sides,
so you only need to send the map value for the data to be properly saved/loaded


------
------
# Cross Language Communication
Since these formats are generalized, as long as you can read a file and properly comb through these
data types, you are able to utilize JSON/XML/CSV/WHATEVER to communicate between different programming languages.

As long as both sides of the communication are expecting/sending the same type of object, one language
can send/save JSON file, and another language can read/load it and utilize this for however may need.

This is how front ends and backends communicate with one another. 

This is where you would utilize communication methods like REST, but we are not going to talk about that today.



