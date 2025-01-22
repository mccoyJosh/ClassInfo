# Command Line

The command line is exactly what it sounds like... a 
line where you can put commands. These are commands to do things on a machine.
Typically, in your every day life, you do most things from a gui, whether
that be coding, watching videos, and what not. But before proper guis
were implemented, all you had was a command line to work with; simply characters
on a screen. While machines being only command line based is not really a common
thing anymore, the command line itself has a very important spot in your tools as a 
developers. It provides you easy access to running, well, commands, whether that 
be commands like 'python myfile.py' to run python code, or commands for git, it is
a simplistic tool that can do tons for you. 

There are also instances where you NEED to use a command line, for instance, connecting to a system which
only has a command line as part of it (whether that be a database system, device hosting a website, or anything else). Not every machine needs a gui, and having a gui run can often take resources which could be used to run whatever program a machine may be dedicated to, thus, the only access point you 
have to the device is going to be through a commandline.

While there are many commands to use, the most important ones are those that help you 
navigate through the file system (YOUR COMPUTER).

# File System Structure

Before working with the command line, 

- understand file system structure
  - organized as tree structure



# Different Types of "Command Lines" aka "Terminals"

Depending on your machine and operating system, you may have a different terminal. Due to this,
the commands you are going to run to navigate through your system may be a bit different, thus
the following guides has the alternatives depending what you are using:

## Windows

Depending on how your computer is configured, you may be set up to use either Command Prompt
or Windows Powershell as your terminal. Both of these have a different way of interacting with your
machine. Fortunately, Powershell works extremely similar to how bash/zsh works (the terminals
for unix based machines), so using it will probably be more helpful in learning as it can be used
for other OS's. Command Prompts commands are mostly unique per itself, so learning them may only help you
in windows. 

Just be aware of which one you are using, as one could prevent you from using the commands of the other!


## Mac

The default terminal application for macs utilizes zsh, which is kinda equivalent to bash
but with extra stuff on top. Due to this, both Mac's and Linux's commands are going to be VERY
SIMILAR!!!

## Linux

Depending on your flavor of linux, your terminal application may look a bit different,
but under the hood it is most likely bash. Obviously, you can change that, but if you are changing your terminal
to an alternative, you probably also know how to use it (hopefully),


# Command Line Guide

This tutorial should teach you how to navigate through directories and make them

https://tutorial.djangogirls.org/en/intro_to_command_line/

- make sure you check out move and copy commands!


----

We also need to know how to make and edit files too:

## Make Files

Windows
```
type nul > <filename>
```

Mac/Linux
```
touch <filename>
```

## Edit Files

One can always edit files from outside the command line with a text editor like
Notepad, but it may be useful to learn how to do so from within the terminal.

This is especially good to know whenever you are working with machines
where you only have access to the terminal and nothing else.

For tasks like this, you need some kind of terminal based text editor.
One that is installed on most machines is vim.

You can typically easily install it as well if you don't have it.

Mac/Linux/Windows
```
vim filename

or

vi filename
```

Show:
- the modes
  - ## Normal
    - ENTER BY pressing ESCAPE
    - Allows you to view file and apply a few commands
      - hjkl act as arrow keys (and so do your arrow keys)
      - w moves you forward a word
      - b moves you back a word
      - x removes the character under your cursor
      - dd removes an entire line
      - v starts and stops "Visual Mode" which allows you to select a portion of text
      - y copies (YANKS) a selected section
      - yy copies (YANKS) the line you are on
      - p pastes any copied text
  - ## Insert
    - ENTER BY be in normal mode and type 'I'
    - now you can type!
  - ## Executable
    - ENTER BY be in normal mode and type ':'
    - :q quits the file
    - :w writes to the file (saves it)
    - :wq will save the file and quit
    - :q! will quit without saving

Anther terminal based text editor is ***nano***!

## Move Files

Windows
```
move <filepath> <new-filepath>
```

Mac/Linux
```
mv <filepath> <new-filepath>
```


# Copy Files

Windows
```
copy <filepath> <filepath-to-copy-location>
```

Mac/Linux
```
cp <filepath> <filepath-to-copy-location>
```

# Using a terminal in IDE

There are terminal tools in (most likely) any IDE you use. They typically use your default shell as the terminal, so Windows this may be Powershell, and for linux it may be bash.

### In VSCode:
Go to top of window, find "terminal" and create new terminal. It should appear at bottom of window

### In Pycharm:
In the bottom left hand corner of the window, there are a few buttons on the side bar.

These include "Services", "Terminal", "Problems" and "Git"

Select "Terminal"

A terminal should open at the bottom of the screen!