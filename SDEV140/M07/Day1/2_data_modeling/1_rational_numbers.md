
# Rational Numbers

Rational numbers are simply numbers which can be represented using a numerator and a denominator (like this: numerator/denominator). 
Python does not have a built-in type for rational numbers, but maybe making one would be good :)

```python
class Rational(object):
    def __init__(self, numerator, denominator):
        self.__n = numerator
        self.__d = denominator
        self._reduce()

    def numerator(self):
        return self.__n

    def denominator(self):
        return self.__d

    def _gcd(self, a, b):
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    def _reduce(self):
        divisor = self._gcd(self.__n, self.__d)
        self.__n = self.__n // divisor
        self.__d = self.__d // divisor

    def __str__(self):
        return f"{self.__n}/{self.__d}"


    def __add__(self, other):
        new_numerator = self.__n * other.__d + other.__n * self.__d
        new_denominator = self.__d * other.__d
        return Rational(new_numerator, new_denominator)


r = Rational(3, 10)
r2 = Rational(5, 20)

print(f"{r} + {r2} = {r + r2}")
```

