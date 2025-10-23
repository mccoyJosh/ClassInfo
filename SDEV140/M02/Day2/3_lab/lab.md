# Lab

(Inspired heavily from chapter 3 in the textbook)

------

> Implement a guessing game where the computer makes up a number from a provided range and the user is expected to guess that value. 
> Have the user the ability to continuously guess until they get the number while letting them know if each guess is greater or less than the
> number they are guess. When they found the correct number, let them know and print out the number of guesses they tried.
> 
> Please validate the users input and limit the user to guess only log(range_diff)*1.5 (as an integer)

Good example of allowing a user to keep doing 'something' and validating the user input!

```python
import random
import math

# Get input from the user
lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))

# Initializes the number being guessed and counting variable to print out number of tries at the end
secret_number = random.randint(lower_range, upper_range)
guesses_count = 0
number_of_guesses = int(math.log(upper_range - lower_range) * 1.5)

# Repeats until the user guesses the number or exceeds limit
while guesses_count < number_of_guesses:
    # Gets a new guess
    user_guess = input("Enter your guess: ")
    
    # Validates user's input
    
    # Ensures a number was entered
    if user_guess.isnumeric():
        user_guess = int(user_guess)
        
        # Ensures the guess was within range
        if lower_range > user_guess or user_guess > upper_range:
            print("Your guess was outside the range!")
            continue
    else:
        print("Please type in a number!")
        continue
    
    # Only updates count if provided a valid guess
    # (we are not penalizing for a not-real guess, but we could if we wanted to)
    guesses_count += 1
    
    # Determines if they found the number or not
    if user_guess < secret_number:
        print("Too small!")
    elif user_guess > secret_number:
        print("Too large!")
    else:
        print(f"You have found the number! You guessed {guesses_count} times!")
        break
else:
    print(f"Ran out of guesses! The correct answer was {secret_number}")
```


----------
