
# Project Specification:

I wanted to briefly go over what is expected for the final project:
[Link to it here!](https://ivylearn.ivytech.edu/courses/1248721/assignments/19828609?module_item_id=48058273)

----

## Code

> A working GUI tkinter application with at least two windows

This can be either one of two things and I will accept both:
- Your project has two windows on the screen at some point, so this could
  be the 'main' window of your project and then maybe a pop up window.
- Your project removes all items from your window to then repopulate it with a
  'new' window. 

We will see how to do both of these today!

----


> Implementing a modular approach in your application

This means that you utilize methods in splitting up the functionality of your code. 
If you use the format for tkinter projects, you have not choice
but to use functions so


-----

> Consistent clear navigation throughout the GUI application

This doesn't necessarily mean you need a header, but a header of some kind
is a good idea to maintain a clear navigation. As long as you
don't get stuck in a window with no way out, it should be alright!

-----

> Include at least three call-back functions for the buttons, including the exit button

A callback function is just the function that is part of a buttons command.
So, we have already used these up to this point!
```
        tk.Button(self, text="Exit", command=self.exit).grid(row=0, column=0, sticky="NSEW")
```
In this little example here, we are using self.exit as the method that will be
executed upon clicking the button. THIS is our callback function in this case.

All this requirement is really getting at is that you SHOULDN'T just use
the same function for all of your buttons. Make your buttons do different actions!


----

> Implement secure coding best practices, including input validation to check if the user entered the correct data type, make sure the entry box is not empty, etc. 

This requirement is not saying that you need to take input from the user,
but, if you do, do make sure you do input validation. This requirement is speaking
more generally that you do in fact know your code can run regardless how the user may interact with it!

This goes hand in hand with testing your own code to ensure it is working properly.


---

# Validation Testing

_See page_

---

# README.md

_See page_

---

# Documentation of source code 

> A brief explanation of the purpose of each module (Sub) at the beginning of each Sub. (A header's comment)

This is just a per-file comment. So, if your entire project was in one file,
you would have a comment at the very top talking about how the file initializes the project
and how the code is structured.

----

> Line by line, or at least section by section comments within the code, explaining what the line/section does. 

I am not REALLY expecting line by line comments, but I very much do want section by section comments.
Like if you are declaring a few labels all at once, you don't need to say "declaring another label" before each one.
Just leave a comment about how you are adding these labels to be the content for said page. 

What I will take points off for is if there are methods with no comments, so do that at the very least.



----


# IF YOU HAVE ANY QUESTIONS ABOUT THE REQUIREMENTS OF THIS PROJECT PLEASE REACH OUT TO ME!