# convert between types (TYPE CASTING)
7.0  # obviously a float but maybe we want it as an int
int(7.0)

# TYPICALLY, it is done using this format:
#       <type>(<value you want to cast>)

# You may lose data when converting between types though, for instance:
int(7.5)  # results in 7






print("here is a number: " + str(5))  # this would result in an error if 5 was not casted to a string
