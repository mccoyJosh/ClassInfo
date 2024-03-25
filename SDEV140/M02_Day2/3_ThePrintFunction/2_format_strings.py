# In many circumstances, you will need to format your strings so the data being presented can be more easily read
# For instance, lets say we were printing out a chart of data
l = [(0, 122), (1, 21), (2, 325), (3, 0), (10, 2444), (11, 223)]

print("| ID | Number of hours |")
for e_id, hours in l:
    print("| ", id, " | ", hours, " |", sep="")
# When this prints out, it looks bad
# Only if there was some way to make the data appear uniform... oh wait there is!

print()

# FORMATTING STRINGS









#  Now we can fix our chart
print("| ID | Number of hours |")
for e_id, hours in l:
    print("| ", "%2s" % e_id, " | ", "%-15s" % hours, " |", sep="")





