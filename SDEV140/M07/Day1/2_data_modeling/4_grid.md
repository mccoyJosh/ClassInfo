# Grid Example:

This is good example for the construction of a data type.
In most data types you need to tell python how you want the data
gotten from it, and we use python's built in __getitem__ method to utilize the
default use of the brackets.

See EXAMPLE:

```python
class Grid:
    def __init__(self, rows, columns, fill_value=None):
        self.data = []
        for rows in range(rows):
            data_in_row = []
            for column in range(columns):
                data_in_row.append(fill_value)
            self.data.append(data_in_row)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += f"{str(self.data[row][col]):3s} "
            result += "\n"
        return result

    def __getitem__(self, index):
        return self.data[index]

    def find(self, value):
        for _row in range(self.get_height()):
            for _col in range(self.get_width()):
                if self[_row][_col] == value:
                    return _row, _col
        return None


rows = 25
cols = 25

gr = Grid(rows, cols)

for row in range(rows):
    for col in range(cols):
        gr[row][col] = row * col


print(gr)

```