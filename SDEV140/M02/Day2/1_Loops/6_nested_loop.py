# You can put loops in loops; this is considered a nest loop
box_size = 10

# all this does is print out a box of x's
for i in range(box_size):
    for j in range(box_size):
        print('x', end='  ')
    print()

# Typically, this is done to go through 2-dimensional arrays (matrices)

