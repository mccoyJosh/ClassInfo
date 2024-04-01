
# What is and why do we use encryption (and decryption)

We are familiar with computers, right? Everything on them is stored and transferred as 1's and 0's.
Some of those 1's and 0's tell the computer to run Chrome. Some of those 1's and 0's tell the computer
how to display and image. AND some of the data we store on the computer is important. Think bank account info,
SSN, information about your family, etc.

Now, if you just had a personal machine that ran at home and wasn't connected to any other computer in any
way shape or form, your information is probably fine. But that is not the case for most people, as we are all
connected to the internet. When connected to the internet and any other kinda of network, when you
want to connect to another computer, the data you transfer to the other computer is vulnerable. 


You may think that when connecting to another computer, it is just a direct connect, but nope, it is not

![1.png](..%2Fassets%2F1.png)


What is really happening is you are connecting to a network and then connecting to that other 
computer by sending packets of info over that network, and technically anyone else on the network is able
to see those packets

![2.png](..%2Fassets%2F2.png)

So you may just be trying to send your friend a funny picture of a cat, but that message can be intercepted by someone.
Typically, the third individual would be using a type of sniffing software which constantly is reading for packets
over a network to see if it can them and find potentially useful information.

Now, it doesn't matter too much if the person also got your cat picture, but if it was, for example, you're sending
your SSN to a website over the internet, you don't want the information being read and stolen.
There needs to be some sort of way to prevent the interceptor from reading your message
while also allowing the desired user to read it. 

## Encryption
All that encryption means is to transform the data in a way where the original message is (hopefully) unreadable.

This unreadable text is called a 'cipher text'.

Typically, if it is a good encryption process, there is a way to get the original message back from the cipher text. 
This process is called 'decryption'. When you decrypt a cipher text, you end up with the plain text. Decryption often 
involves utilizes a key to tell us specifically how to get back to the original solution


![process.png](..%2Fassets%2Fprocess.png)


If we are able to encrypt the packet and send it out to the network, and the desired individual had the means to
decrypt the packet to get the original message, then we can be rest assured that the packet gets to the desired user
while the individual intercepting the packet DOES get the packet, but cannot read it as it is unreadable.

![3.png](..%2Fassets%2F3.png)


This is basis for sending information securely over a network. This is essentially what is happening whenever you
connect to the internet. If you have ever seen Hypertext Transfer Protocol Secure, aka, HTTPS, this is the 
encryption protocol that internet traffic uses to ensure your data isn't stolen.

Now we are not going to talk about how to encrypt data like HTTPS does, as it can get complicated, but
we will learn a basic type of encryption: the caesar cipher!

# Caesar Cipher

The way the Caesar Cipher works is by shifting the letters in the alphabet by a specific distance. 
For example, if we shifted by a distance of 4, we get this Caesar cipher:

Plain text:  a b c d e f g h i j k l m n o p q r s t u v w x y z
Cipher text: e f g h i j k l m n o p q r s t u v w x y z a b c d

So, when we want to encrypt a word using this cipher, we would start at the top with the plain text and
see what letter it translates to.
For example, lets translate the word "lady":

```
PLAIN     CIPHER
  l   --->  p
  a   --->  e
  d   --->  h
  y   --->  c
```

"lady" gets translated to "pehc", which, is now our cipher text. 
If we wanted to decrypt the message, all we would need to do is go backwards! So, we start at the cipher letters
and see what plan letters they line up with. Doing this will get 'pehc' back to 'lady'.

Now, if we were given a cipher text, getting back to the original would be a lot harder if we didn't
have the distance which was used to create the cipher text letters. The distance here is essentially our
key to being able to decrypt the message. 

Now, the Caesar Cipher is a simple cipher, and it can be decrypted even if you don't know the key.
There are only 26 different offsets of the alphabet you can make, so anyone who is attempting to decrypt a Caesar cipher
only has 26 different string to look at to see if it is the correct one.

This code here will print out all the possible caesar ciphers. Running it will show us one of them is the correct
plaintext
```python
str = "pehc"

str = str.lower()
for i in range(26):
    for j in range(len(str)):
        print(chr( (((ord(str[j]) - ord('a')) + i) % 26) + ord('a')), end='')
    print()
```
When you don't know the key, decrypting the message is SIGNIFICANTLY HARDER than encrypting. That's exactly
what you want from an encrypting process. Again, the caesar cipher is not that complicated, but more complicated
more processes of encryption, decrypting can literally take years to accomplish.



# Potential Problems

Now, if encryption works by decrypting an encrypted message, how do you give someone the key that doesn't allow 
for anyone on a network to also take the key to decrypt the message????

One solution is end-to-end encryption.

In end-to-end encryption, everyone gets a private key and public key. Only you as a user knows your private key, 
but everyone knows your public key.

The public key can encrypt messages while the private key can decrypt messages made by the public key

![4.png](..%2Fassets%2F4.png)

If user 2 here wanted to send a message to user 1, they would first get u1's public key. 
They will encrypt their message using it.

![5.png](..%2Fassets%2F5.png)

Now that the message is encrpyted, it is safe to send over a network, or server in this case.
Even if it is intercepted, the intercepter has no access to the private key to know what the message
says.

![6.png](..%2Fassets%2F6.png)

Now, user 1 can decrypt the message and see what user 2 wanted to say to them:

![7.png](..%2Fassets%2F7.png)
