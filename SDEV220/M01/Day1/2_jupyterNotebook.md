# Jupyter Notebook

----

# What is it?

Jupyter notebooks is made specifically for data analysis, so that you can run 
your code, add your explanation, show the actual result from your code all in
the same convenient place/

Typically, with any 'normal' IDE, you would have your code and maybe some comments.

If you want anything formatted in code, it would require you to just make second file with some formatting (like markdown); even in that situation, your file with actual code would still be in a different place.

Instead of acting as a true file of code, the Jupyter notebook is more like
a fancy interactive shell, as you run the code line by line with documentation i
n between. Technically, it is not a true IDE, and rather a REPL 
(read-eval-print loop i.e. an interactive shell, cause thats what is is :/)
That being said, that is how python already works so it is not really that big 
of a deal.

----

# Installation

There are a few ways to install jupyter notebook defined here:
https://jupyter.org/install

The easiest way to install the notebook is through pip (which should come with python)

```pip instal notebook```


Alternatively, you can use Anaconda and/or conda:

```conda install anaconda::notebook```

If you want to use conda gui (Anaconda), it should come pre-installed with jupyter notebook. Here is an example of doing that:

https://www.youtube.com/watch?v=bkOEYmyMtEU


-----

# Running

To run jupyter notebook from the commandline, use:

```jupyter notebook```

If you installed jupyter notebook with Anaconda, you should be able to launch it straight from the gui window.

Once it is running, it is essentially just running a local server for you to edit from within your browser (a website).

This will open the editor from within the directory you run this in, so make sure you run it in a good place!

----

# How to code in it

> run it

> code something

> show results

> do some documentation


----

# Documentation in Jupyter (is MARKDOWN)

The documentation section of jupyter is just markdown.

Markdown is a simple way to encode some formatting on to your text. 
Instead of using some sort of gui to like, make some text a header (like in microsoft word),
you simply code the formatting with some simple syntax. This has the added
benefit of having these files be saved as simple text files. 

All of my notes for this class are in markdown, so, you can see from these how it kinda works.

On top of this, I have left a link to a handy guide to some simple Markdown in the Resources tab on Ivy Learn


----

# Importing/Exporting

## Exporting:

This will export your file into the Downloads folder on your computer (or where ever the browser you are using downloads files to)

**From within an open notebook:**

> File -> Download


## Importing:

This will import the jupyter file into your notebook's directory, at
which point you can open the notebook like any other one

**From within the Home menu of jupyter notebook:**

> Upload -> Find & Select Jupyter File


-----

# There is a jupyter notebook plugin for VS Code which allows you to work on notebooks from within the IDE, FYI!!!

https://www.youtube.com/watch?v=suAkMeWJ1yE

