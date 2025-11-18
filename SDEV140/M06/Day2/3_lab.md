# Lab

----

----

> Have code perform the Caesar Cipher on any string of text. The code needs to give the option to
> encrypt or decrypt the code based on an inputted distance value.

This code lacks a lot of input checking!

If we write the pseudocode for both processes for encrypting and decrypting, they would look like this:

Encrypting:
- Get Plain Text
- Get Distance
- Add Distance to Each Character To Get Cipher Text
- Print Cipher Text


Decrypting:
- Get Cipher Text
- Get Distance
- Subtract Distance to Each Character To Get Plain Text
- Print Plain Text


These are very similar, and really, to reduce our code, we can combine many of these actions into
the same action. For instance, instead of writing two different loops to apply the encrypting/decrypting, we
can combine them into one loop which just changes the value we add, which we will see.

```python
users_choice = input("Do you want to Decrypt (d) or Encrypt (e) text: ")
users_choice = users_choice.lower()[0]

text_type = "ciphertext" if users_choice == 'd' else "plaintext"
text = input(f"Please input {text_type}: ")
distance = int(input("Please input distance: "))

if users_choice == 'd':
    # Only difference between encryption and decryption IS decryption is the subtraction of the distance
    distance = distance * -1

resulting_text = ''
resulting_type = "plaintext" if users_choice == 'd' else "ciphertext"
for char in text:
    resulting_text += chr(ord(char) + distance)

print(f"{resulting_type}: {resulting_text}")
```


-----

-----

> Write code which takes two files and combines them into one file

```python
# Get File Names
file_name_1 = input('Please input the first file name: ')
file_name_2 = input('Please input the second file name: ')

# Create file objects
file_1 = open(file_name_1, 'r')
file_2 = open(file_name_2, 'r')
output_file = open('output.txt', 'w')

# Get Contents, Combine Them, and Write to new file
file_1_contents = file_1.read()
file_2_contents = file_2.read()
output_file.write(file_1_contents + file_2_contents)

# Close Files
file_1.close()
file_2.close()
output_file.close()
```



