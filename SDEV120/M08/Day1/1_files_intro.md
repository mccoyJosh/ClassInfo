# Files Intro


# Memory Types

Up to now, all of our programs have been just running and dealing with 
data as it comes.

Everything we have done has been within RAM space,

Per Wiktionary:
> **RAM (Random Access Memory)**: Computer memory that dynamically stores program and data values during operation and in which each byte of memory may be directly accessed.

Per me:
> Memory which is **volatile**, that is, temporary on your device while it is running. Once you turn on your device, it is gone.

If you ever have been using Microsoft Word and started writing a piece of work, and your computer turns off in the middle of you
working or you have closed the program, you have experienced volatile memory. Everything currently RUNNING on your computer is within RAM space.

This is fine for our simple programs, but eventually we need to actually keep data even if we turn
off our device. 

This is where forms of PERMANENT STORAGE DEVICES come in!

Permanent, nonvolatile, storage stays on your computer even when it is turned off. 

Per book:
> **Permanent Storage Device**: a hardware device that holds nonvolatile data; examples include hard disks, DVDs, Zip disks, USB drives, reels of magnetic tape and MORE

If you are on a computer right now, you probably have all of your data saved on some sort of hard drive, whether that be
a solid-state drive (SSD) or hard disk.

# Files

On your device, everything on it is typically saved as files; these are pieces of data stored on your permanent system.

Per the book:
> Computer File: a collection of data stored on a nonvolatile device in a computer system.

When you want to edit it, view it, or run the file, it will be read into RAM memory to be processed.


When looking at any file, it is made of two parts:

1. FILENAME
2. FILE EXTENSION

They are arranged like this:

```
filename.extension
```

This is to say, first comes the file name, and ends with the extension, which comes after a period

The file name tells the computer the unique identifier for this piece of data.

The file extension tells the computer how to access the file.
Depending on the file extension, your computer may try to 
- run the program
- run a specific program to open the file
- not know the extension and ask you how to deal with it

Here are few extensions and how computers typically deal with them:

## Text File (.txt)

Probably the simplest type of file. These just store characters.

If you are on Windows, Notepad will probably open the text file.
If you are on Mac, the Text Editor will probably open the text file.
If you are on Linux, the built-in text editor app will open.

For these and any other extension, you can always tell the computer to use an alternative application to deal
with these types of files.

## Binary Files

Typically they

Binary Files can be many things:
- music
- images
- executable files
  - The extension for executable files depends on the system
    - Windows typically use .ex, or sometimes .com
    - Linux uses .pkg alot of times
    - Apple uses .dmg and .app a lot of times for different types of executables
    - REALLY, most computers can execute a file as long as it is set in the systems as an executable with permissions

## More:

- Python Files (.py)
- Java (.java)
- .pdf
- Pictures: .jpg.png .gif (kinda)


# File Info:

Typically, files will also contain a bunch of data about it on the device you are on, such as:
- creation time
- last time modified

Probably should go look at "File Properties" on a file at this point.


# Reading/Writing to Files

When referring to files, if we are using them or viewing them, this is considered "**READING**" them

When referring to files, if we are editing them or adding to them, this is considered "**WRITING**" to them


# Default Input

The default input of most, if not all devices is the keyboard.

# Default Output

The default output of most programs is your terminal output screen