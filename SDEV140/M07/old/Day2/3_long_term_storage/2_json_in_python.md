### Example JSON Object:
Here we load in an object into python using json.


# THE DATA
```json
{
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "hobbies": ["reading", "swimming", "coding"]
}
```



# THE CODE

```python
import json

json_file = open('Day2/assets/file.json', 'r')
json_data = json_file.read()
json_file.close()

person_dict = json.loads(json_data)

print(f"Name: {person_dict['name']}")
print(f"Age: {person_dict['age']}")
print(f"City: {person_dict['city']}")
print(f"Hobbies: {', '.join(person_dict['hobbies'])}")
```