# Numbers

We have already briefly talked about numbers in python, specifically integers
and floating point values, and conventionally, they are not hard to understand. 

One is simply whole numbers.

One can hold numbers with decimals (for precision)

So, we are going to move on to how these types are interacted with:

## Operations

- Addition
  ```python
  # Pretty straight forward -> use + sign to add two numbers together:

  print(10 + 10) # Integer Example
  print(1.5 + 1.4) # Floating Point Example
  print(1.5 + 1) # Int + Float Example (results in floating point value)
  ```
- Subtraction
  ```python
  # Again, pretty simple; works as subtraction normally does 

  print(10 - 10) # Integer Example
  print(1.5 - 1.4) # Floating Point Example
  print(1.5 - 1) # Int & a Float Example (results in floating point as well!)
  ```
- Multiplication
  ```python
  # Multiplication :)
  print(5 * 6)
  print(1.5 * 8.9)
  print(7.3 * 3) # RESULTS IN A floating point value (see pattern?)
  ```
- (Floating Point) Division
  ```python
  # With just a single /, we are doing normal division, AND, the result will always
  # be a floating point value, even if it is a whole number
  print(1/3)
  print(6/3)
  print(4.5/1.5)
  ```
- Integer (truncating) division
  ```python
  print(6//2) # results in an integer
  print(8.0//2.0) # results in a floating point value
  print(33//10)  # results in an integer... that is not the answer??

  # so, here, we see the truncating in process. It does the division like normal, but truncates (cuts it off) to the whole number.

  print(5//2)

  # Even in this situation, the code results in 2 despite the result being 3 if we rounded. WE ARE NOT ROUNDING THE RESULT; simply removing the values after the decimal

  ```
- Modulus
  ```python
  # This kinda does the opposite of the integer division.
  # This results to us the remainder from the integer division

  # For instance, 3/2 would be 1.5, but integer division would result in 1 and a remainder of 1
  # Thus, our result should be 1 from the following code:

  print(3%2)


  # Or here where 10%7 results in 3 because 7 goes into 10 once, and we end up with a remainder of 3
  
  print(10%7)

  # This is particularly helpful in determining if a number is even or not:
  
  # 10 is the number we are checking is even! (this results in true)
  print(10 % 2 == 0)

  ```
- Exponent (just a matter of using **)
  ```python
  # Finally, we get to exponents, which is what it sounds like... exponents:
  print(2**3) # this would be 2 to the power of 3, i.e., 2 * 2 * 2 which equals 8

  ```

## Bases

- Binary (Base 2)
  ```python
  # Use 0b or 0B before value


  # Convert to binary using bin(<number>)


  ```
- Octal (Base 8)
  ```python
  # Use 0o or 0O before value
  

  # Convert t0 octal using oct(<number>)

  ```
- Hexadecimal (Base 6)
  ```python
  # Use 0x or 0X before value


  # Convert to hexadecimal using hex(<number>)

  
  ```


## Ascii values conversions

EXPLAIN ASCII ENCODING
-> computer only knows 1s and 0s
-> we can easily represent numbers with binary values
-> to write text, we can assign every character a corresponding number
-> boom bang we have ascii, the characters which correspond to numbers so that the computer only needs to store numbers and some sort of text editor/viewer can translate those to letters on a screen!

show ascii chart

chr(NUMBER) -> 'LETTER'

ord('LETTER') -> NUMBER




