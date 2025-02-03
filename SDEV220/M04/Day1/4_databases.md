# Databases

Files are good storage, but, what if we need more data, and a fast way to access it

This is where databases come in.

## What are they: DBMS DataBase Management System

Database management systems are large scale data storage formats. They manage structuring, saving,
retrieving, and manipulating data for you. Many of times, these database
are independently running systems which is connected to like any other service.
Other times, it is a simple file. 

When comparing to simply saving information to a single file and calling it a day, databases
have many, MANY important benefits:

- allowing multiple users to access the data simultaneously
- have different levels of user, allowing some more privileges than others
- VERY quick, efficient methods to store and retrieve data.
- Data is explicitly defined to follow a certain set of rules (schemas and constraints)
- Easy to use methods to combine data
- A declarative query language: SQL (we will get to this later)

# Relational Tables

Relational tables are called such for two reasonsL

- they are tables; they have rows and columns, each column indicates a different type of value and every row defines 1 single instance of whatever the table represents
- is relational to other tables, as in there typically exists a connection to data within another table

In relational tables, there is typically one row that is referred to as the **PRIMARY KEY**.
This is a unique identifier for that row; it doesn't have to just be an ID of some sort.
The primary key can just be a combination of a few rows which creates a unique overall key.

Whatever the key is, it is **indexed** to allow a fast lookup; this is similar to hashing but NOT THE SAME!!
On whatever DBMS you use, the actual information in these tables is just stored on files; it is the system
around said file that really makes DBMS shine.

After having tables with primary keys, you can make your tables relational
by having other tables reference those primary keys. They are considered 'foreign keys'
in the other tables.


Here is a quick example:

### COMPANY Table

- ID acts as the primary key for company

| ID | Name             | Address                       |
|----|------------------|-------------------------------|
| 1  | Big Ads Company  | 123 Advertisement Way, LA, CA |
| 2  | Big Products LLC | 096 Make Money Avenue, LA, CA |


### EMPLOYEE Table

- ID acts as the primary key as well, and cmp_id is a foreign key to the company table.

- If an employee's cmp_id matches the one from the COMPANY table, it means they work for said company.

- Also note how, to ensure there is no null table entries, an employee is dependent on a company to exist first to populate it's cmp_id

- Also also note the usefulness of the ID, as despite there existing someone with the same name and dob as another employee, we can still distinguish between the users by a uniquely given id

| ID | CMP_ID | FIRST_NAME | LAST_NAME | DOB       |
|----|--------|------------|-----------|-----------|
| 1  | 1      | John       | Smith     | 1/1/1999  |
| 2  | 1      | John       | Smith     | 1/1/1999  |
| 3  | 2      | Bingus     | Smingus   | 2/11/1980 |
| 4  | 2      | Walter     | Halter    | 4/16/1987 |
| 5  | 1      | Cherish    | Clinton   | 9/12/1966 |


----

----

# SQL

For many, MANY database management systems, the fundamental way we
communicate to our database is through a language called **SQL**, i.e. **S**tructured **Q**uery **L**anguage

Unlike Python, Java and any other PROGRAMMING LANGUAGES (which are imperative),
SQL is a DECLARATIVE language. _Essentially, they are:_

> **_Imperative Language_**: A language where you explicitly define the steps to take to get the data you want (think of creating a loop to get the values in a list)

> **_Declarative Langauge_**: A langauge where you ask for a set of data, and it gathers it for you (essentially calling a function to gather the data you want without actually going through the list itself)

SQL is made this way as the underlying data structures of the DBMS is actually hidden from us as users of it. So, we simply need
a way to add/retrieve the data without us actually 'placing' the data.

SQL is different from the other programming languages since it is not 1 language.
Depending on the specific DBMS you are using, there may be some SQL statements
which are ever so slightly different compared to another DBMS. I will say, they are mostly the same,
but it is different enough where we refer each of these instances as an SQL Dialect.

Here are a few examples of these different DBMS:

### SQL Database Examples

- SQLite
- MySQL
- PostgreSQL
- Microsoft SQL Server
- Oracle DBMS

### NoSQL

- MongoDB

### Other

- Redis
  - Simple Key-Value Pair Database (think dictionary)

# General Structure

![db_struct.png](assets/db_struct.png)

-----

-----

# Basics of SQLite

For the sake of this class, we are going to use SQLite
(for now), as it is incredibly easy to set up and start using, 
AND doesn't require a constant server be running.

## Install (and how it is just a file tee hee)

There are a few ways to install it:

- Their [website](https://www.sqlite.org/download.html)
- Through your package manager:
  - [Chocolatey](https://community.chocolatey.org/packages/SQLite)
  - [Homebrew](https://formulae.brew.sh/formula/sqlite)
  - Linux (plz look it up for your distro): ```sudo [ur package manage] install sqlite```

## Manage Database

When making a database, keep in mind that what we are actually
creating is just a file (which will store all of our tables within it)

### Create Database: 

> Through command ```sqlite3 database_name.db```

> From SQL File: ```sqlite3 database_name.db -init file_name.sql```

The benefit of using a sql file over using just the commands is that you include as many
commands as needed for the initiation of your database, which can include code to initialize
your tables as well. This is especially a good idea when you are likely to change where your database is run,
as creating an SQL file will automatically create the SAME database on whatever device you are utilizing.


### CRUD (Create, Read, Update, and Delete)

CRUD API is the term to describe how we interact with the database (how we Create, Read, Update, and Delete
the information we need).
Whenever you are working with a system like this, you want to learn how to do this simple actions:

# CRUD TABLES

## Create Table

> These next few commands can also be done from a SQL file 

To create a table, you use the 'CREATE TABLE table_name' to BEGIN creating table.

You then follow this by the columns you want in your table.

There are many identifiers you can use, which you can see where to place them below.
They really follow the format of starting with the name of the column, then the type, and then 'extra' information like 'NOT NULL'.

A few things to explain:
- `PRIMARY KEY` designates this value as the primary key to the table
- `AUTOINCREMENT` will automatically make values for this field (starting from 0 and incrementing to 1, 2 and so on). No need to insert this later
- `NOT NULL` this makes sure that the user adding an entry actually puts a value for this column. One could leave a column as NULL (or nothing) if NOT NULL is there
- In the employee table, `FOREIGN KEY (cmp_id) REFERENCES company(id)` actually connects the cmp_id to the company table on the key it is suppose to be associated with


```SQL
CREATE TABLE company (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL
);



CREATE TABLE employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cmp_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob DATE NOT NULL,
    FOREIGN KEY (cmp_id) REFERENCES company(id) 
);

```

Also, you may notice that all the keywords for SQL are all capitalized. This is merely 
a very very very common way to write SQL code, but not NECESSARY for it to run. Most sql
interpreters are not case-sensitive.

## Read Tables

You can view all your tables using 
```
.tables
```

## Update Tables

If you want to change a table once it has been created, you can use the ALTER command. Here is an example:
```SQL
ALTER TABLE table_name ADD COLUMN column_name TYPE;
```

## Delete Tables

To remove a table, you use this command:
```SQL
DROP TABLE table_name;
```



or more something like this

```SQL
ALTER TABLE employees ADD COLUMN created_time DATETIME;
```


# CRUD DATA

With tables created, we should now add data.

## Create Data

To insert a single entry, use:
```
INSERT INTO table_name (column1, column2,...) VALUES (value1, value2,...)
```
The values correspond to the column position, so value1 is filling the space with column1.

You have the option to also not put the column names... it just means you need to insert every column in the table,
otherwise it will not work. Both of these work:

```sql
INSERT INTO company VALUES (1,'Big Ads Company', '123 Advertisement Way, LA, CA');
INSERT INTO company(name,address)  VALUES ('Big Products LLC', '096 Make Money Avenue, LA, CA');
```

To add multiple values at the same time, it is just a matter of listing every entry after each other with a comma in between.
Like this:

```sql
INSERT INTO employee (cmp_id, first_name, last_name, dob)
VALUES (1, 'John', 'Smith', '1/1/1999'),
       (1, 'John', 'Smith', '1/1/1999'),
       (2, 'Bingus', 'Smingus', '1/1/1999'),
       (2, 'Walter', 'Halter', '1/1/1999'),
       (1, 'Cherish', 'Clinton', '1/1/1999');
```


## Read Data

The easiest command and the way to see all the 
content within a table is with the following command:

```SQL
SELECT * FROM table_name;
```

We will continue to see the SELECT keyword be used to read data from our tables.
There is ALOT we are not going to cover here, but just as a basic overview:

### Specific Columns

If you want to, perhaps, just get a single column, it is just a matter of
replacing * from the last command with said column name. For instance this will get
all the names of all the employees from various companies

```sql
SELECT first_name FROM employee;
```

### WHERE command

Sometimes you only need certain values meeting a set of criteria.
If you just want the employees working at the company id of 1, you would do this:

```sql
SELECT first_name, last_name FROM employee WHERE cmp_id = 1;
```

If you only wanted the users whose first name is not Cherish and from the same company, do this:

```sql
SELECT * FROM employee WHERE cmp_id = 1 and first_name != 'Cherish';
```

## Searching across tables

So, sometimes, you don't know the id's of things we are searchign for.
For instance, if all we knew was the company's name was Big Products LLC and you
wanted the employees names from that company.

Problem is, the information we need to search by (company name) is in
a different table.

What we do is join the tables.

By joining the tables, it is essentially combining the entries on the
specified ids that match.

Here is the code that accomplishes that initial task.

It joins the tables 'on' the cmp_id in the employees table
and the id in the company table.

ALSO, notice that we are table to abbreviate the table names using the `as` keyword.

```sql
SELECT e.first_name, e.last_name FROM employee as e 
    INNER JOIN company c on c.id = e.cmp_id 
    WHERE c.name = 'Big Products LLC';
```


## Update Data

Here is how you update information in a table

```sql
UPDATE table
SET column_1 = new_value_1,
    column_2 = new_value_2
WHERE
    search_condition;
```

## Delete Data

Here is how you delete data in a table

```sql
DELETE FROM table
WHERE search_condition;
```

------

------

# SQLite3 Package

SQLite can be used within python by using the SQLite3 package.
It allows you to simply use sql commands within python and call it a day.

See database_example/sqlite_pack_example.py

# SQLAlchemy and ORM

Sometimes, things like SQLite packages do not cut it. 
That's when we move to an ORM (Object Relational Mapper). They have many benefits,
but first and foremost, they kinda make it easier to communicate to a database, ESPECIALLY
if you don't know SQL.

Essentially, it adds an extra layer of abstraction where you only need to worry about
your types and code instead.

Also, specifically for SQLAlchemy, the ORM we are going to be using in python, it is also compatible
to other databases. SO, if you wanted to change the type of database you wanted to use a different one, you
can easily transfer over.

To use it, first we need to install it:

```
pip install sqlalchemy
```

To see the code in use, see

database_example/sqlalchemy_example.py


-----

-----

# Database Access in Jetbrains Products

If you are using IntelliJ or Pycharm or any other Jetbrains IDE's, you
should have access to the database tool on the right-side of the screen.

By opening up, adding a data source and connecting it to your existing SQLite,
you will be able to see the available tables in your database and the values within!
