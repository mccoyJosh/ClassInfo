def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average


vals = []
average = calculate_average(vals)
print("The average is:", average)