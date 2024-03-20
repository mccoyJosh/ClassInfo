
# "a data type consists of a set of values and a set of operations that can be performed on those values"


# use the type() function to get the type of any object
print(type('an object'))






class example_defined_type:
    val: str

    def __init__(self, string):
        self.val = string


var = example_defined_type('example')
print(type(var))


