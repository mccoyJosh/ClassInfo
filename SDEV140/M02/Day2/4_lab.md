# Programming Problems


---

## Tax Like in a Store

> Create a calculator which adds on the tax from a purchase that displays up to two digits of precision using the round function.

```python
og_number = float(input("Please enter initial amount: $"))

tax_rate = 0.07

tax = og_number * tax_rate
total = og_number + tax
final_rounded_number = round(total, 2)
print("TAX: +$", tax)
print("Here is the number with tax: $", final_rounded_number)
```


---


## Sphere Calculations

(Straight up question 2-4 from book)

> Write a program that takes the radius of a sphere (FLOAT) as input 
> and then outputs the sphere's diameter, circumference, surface area, and volume
> 
```python
import math
radius = float(input("What is the radius of the sphere: "))

diameter = 2 * radius

pi = math.pi

circumference = 2 * radius * pi
surface_area = 4 * pi * (radius ** 2)
volume = (4/3) * pi * (radius ** 3)

print("Diameter: ", diameter)
print("Circumference: ", circumference)
print("Surface Area: ", surface_area)
print("Volume: ", volume)
```

Note: we could have imported math and use math.pi for this if we wanted greater accuracy!


-----
