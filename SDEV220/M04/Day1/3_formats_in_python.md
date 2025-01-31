# Using different formats in Python

# CSV

[example_here](https://www.geeksforgeeks.org/working-csv-files-python/)

THE DATA
```
name,department,birthday_month
John Smith,HR,July
Alice Johnson,IT,October
Bob Williams,Finance,January
```


THE CODE
This places all of the csv data into a dictionary.

You could also EASILY read this data yourself
```python
import csv

with open('employees.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)

    data_list = []

    for row in csv_reader:
        data_list.append(row)

for data in data_list:
    print(data)
```



# JSON

THE DATA
```json
{
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "hobbies": ["reading", "swimming", "coding"]
}
```



THE CODE

```python
import json

json_file = open('person.json', 'r')
json_data = json_file.read()
json_file.close()

person_dict = json.loads(json_data)

print(f"Name: {person_dict['name']}")
print(f"Age: {person_dict['age']}")
print(f"City: {person_dict['city']}")
print(f"Hobbies: {', '.join(person_dict['hobbies'])}")
```


# pandas

Pandas is an all-in-one tool which allows you to not only read in
data from many of these formats, but manipulate said data, and convert it
into whatever data format you need!

Here is a good [tutorial](https://www.datacamp.com/tutorial/pandas)