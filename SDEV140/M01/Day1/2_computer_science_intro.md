
# **Algorithms**

Def: _A finite sequence of instructions that, when applied to a problem, will solve it_

- Not a computer-only type problem. A person doing a step by step task is an example of an algorithm
- Really any type of step-by-step process is an algorithm
- **Computing Agent**: the one performing the algorithm
    - Typically, the computing agent is the computer running your algorithm. But, if you are performing some set of tasks, you would be considered a computing agent

### **Typical processing of algorithms**

- takes input
- transforms the information according to wel-defined rules
- produces output

- **EXAMPLES**
    - thinking about this as a person
        - cooks food: input is raw ingredients -> utilize cooking recipe to transform food -> output is yummy food :)
    - thinking about this as computers
        - login page: input is your username and password -> computer validates it -> output is entry into website

---

### Hardware VS Software

Hardware:
- the physical devices required to execute algorithms

Software:
- the set of algorithms, represented as programing in particular programming languages

Some main parts of a computer:
- Input/Output Devices
    - Mice, Screens, Keyboards, Headphones
- CPU
    - "A major hardware component that consists of the arithmetic/logic unit and the control unit"
- Memory
    - "The ordered sequence of storage cells that can be accessed by address. Instructions and variables of an executing program are temporarily held"

---

### Bits, Bytes and what-nots:

- Inside computers are billions maybe trillions of what are known as binary switches, having two modes, being on or off. Being on is typically just when electricity is being passed through them, and off is when it doesn't
- Computers store information on these components as binary values (1's and 0's). Think of 0s as being off, and 1s as being on.
- As far as the computer is concerned, all it "knows" are these 0s and 1s (**bits**)

- now, typically, we want to be able to store more than 0s and 1s. So, what we do is string along a few bits together to form bytes.
- Byte: 8 bits
    - Examples:
        - 00000000
        - 01010101

With arrangements like these, we can start holding BIG NUMBERS (atleast bigger than 0 and 1).
For instance, the computer can interpret
- (binary) 00000010 as (decimal) 2
- (binary) 0000011 as (decimal) 3.

With one byte, we can hold only values from
- 0 (with the binary being 00000000) to
- 255 (with the binary being 11111111)

Now, obviously we need to be able to work with more than 256 numbers.
hat why modern computers often use 64 bit based systems. This gives the possibility of holding
numbers as large as 1.84467 * 10^19.

Now for things that are not numbers, we often just store them as numbers and convert them to our needed us case when the time comes.
For instance, letters (and symbols).

In ASCII, we assign each symbol a number, and just store the number. When we want to display a previously stored message,
we have the computer reads these numbers, convert them to symbols that it displays for us.

![ascii.png](../Day2/assets/ascii.png)

This is an example of encoding: "converting data from one form into a proper form required for a certain process"

----

### Software

When you run something on your device, whether that be the web browser to access this class or some type of video game, all the computer
knows it is doing is processing a very long string of 0's and 1's. These strings of 1s and 0s that the computer execute is known as **_machine code_**.

To load in these machine codes into their proper places, the computer utilizes a program called the **loader**.
It is "a software program that copies program code and data from secondary memory into primary memory before the program execution begins".
This is better than the alternative, manually putting the 1s and 0s into the correct place by hand for the computer to understand it.

Now, obviously, in this class we are not about to write millions upon millions of 0s and 1s to attempt to tell the computer what to do.

What we do instead is write in programming languages!


----

# Programming Languages

A programming language is a set of human-readable instructions (algorithm) for the computer.

The computer does not instinctually know what a given programming language means or does.
What happens is that the code is converted from a human-readable format to machine code (i.e. binary i.e. 1s and 0s aka binary aka 1s and 0s).

So, for instance, we can write:
```python
print("Hello World")
```
and this human-readable programming language code is converted into binary for the computer to understand, and it then will know to print out "hello world"

Not all programming languages are created equal!
There are low level and high level programming languages.
Some are awesome and cool and fun to work with. And then there's NASM, which is considered a low-level assembly language.

## Low Level Programming Languages
Low level programming languages look and are closer to machine code than higher level programming language.
In these languages, you are often call specific registers from CPUs and instruct the computer to work within them.
A Hello World program in the Netwide Assembly programming language (NASM) would look like this:

```nasm
SECTION .DATA
	hello:     db 'Hello world!',10
	helloLen:  equ $-hello

SECTION .TEXT
	GLOBAL _start 

_start:
	mov eax,4            ; 'write' system call = 4
	mov ebx,1            ; file descriptor 1 = STDOUT
	mov ecx,hello        ; string to write
	mov edx,helloLen     ; length of string to write
	int 80h              ; call the kernel

	; Terminate program
	mov eax,1            ; 'exit' system call
	mov ebx,0            ; exit with error code 0
	int 80h              ; call the kernel
```

This is kinda human-readable, but it reads more like a human sending a text message to a CPU more than anything else.

Now, this code is very particular for the devices it can work on. specifically being
devices with CPUs of x86 architecture. Furthermore, this specific NASM code
on linux systems due to the different system calls made from the Linux OS compared to that of mac/windows.
This is ALSO dependent on if you are working with a 32 bit machine, compared to a 64 bit machine.

Running it on Mac would look something like this (in 64 bit):
```nasm
          global    _start

section   .text

_start:   mov       rax, 0x2000004          ; system call for write
          mov       rdi, 1                  ; file handle 1 is stdout
          mov       rsi, msg                ; address the string message
          mov       rdx, msg.len            ; number of bytes
          syscall                           ; invoke operating system to do the write

          mov       rax, 0x2000001          ; system call for exit
          mov       rdi, 0                  ; exit code 0
          syscall                           ; invoke operating system to exit

section   .data

 msg:     db        "Hello, World!", 10      ; note the newline at the end
.len:     equ        $ - msg
```

Notice the different registries (rax, instead of eax, for instance) for the 64 bit machine
and notice the different system calls for Mac.

Now, this would be VERY annoying to do and make work for all computers.

It is a very good thing that we are not messing with this type of coding in this class.

## High Level Programming Languages

High level programming languages make operating and creating programs for the masses far more accessible.
High level programming languages are TYPICALLY machine agnostic, as they should run the same irregardless of the machine
you are working on.

This is accomplished through a number of steps, but this usually involves running the much simpler
code through a compiler/interpreter into assembly code (or something similar) which corresponds to the
machine you are one, and THEN making the executable file.

In any high level programming language, printing hello world is far easier.

### Python
```python
print("Hello World")
```

### Java
```java
public class example {
  public static void main(String[] args) {
    System.out.println("Hello World");
  }
}
```

### C++
```cpp
#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}
```

### Golang
```go
package main

import "fmt"

func main() {
    fmt.Println("Hello World")
}
```

These are far more readable.
They can look very different across languages, but do the same thing. They all get converted to machine code to tell the computer to write "Hello World" to the screen.
How exactly these high level programming languages get converted into machine code can vary greatly from language to language.

Two main difference is whether they are interpreted or compiled.

### Interpreter vs Compiler

Compiled languages first go through the entire process of getting converted to machine runnable files
and then can typically be executed through some executable file.

Think of any exe file on a windows computer; those could have been generated through a compiled language.

On the other hand, we have interpreted languages. They are typically ran singular lines at time. Python is one of these languages.
Also, since these languages do not typically produce an executable file, they need to be run in an "environment" (really, a program to run our program).

- Example interpreter vs compiler using C++ and Python

- General difference discussed between compiler and interpreter
    - Interpreter runs code slower than compiled code
    - MORE Debugging is possible before code is ran with a compiler
    - Compilation may take more time initially than interpreted code to get converted to running code, especially for large code bases
    - Interpreter DOES NOT SAVE the machine code (runs on the fly and doesn’t keep it around), while compiled code produces a reusable executable file

----

# Application Software Vs System Software

## System Software

This is the underlying programs that communicates to the hardware.

> These are the programs that write and execute other programs including operating systems

### Operating System

> Large programs that allow the user to communicate with the hardware and perform various management risks, such as Windows, macOS, linux, and Android

Typically, computers are shipped with these operating systems so that users have no need to figure out how to actually talk to the hardware,
and can simply work within the framework of the OS.

Sometimes this might come in the form of Drivers. For instance, if you get a new graphics card, your given operating system may not
in it of itself know how to communicate the hardware, so you download specialized software for that said system, which is typically called a driver.


## Application Software

> AKA applications or apps

> Programs that allow human users to accomplish specialized tasks, such as word processing or database management.

Think of Microsoft Word, or Chrome, or Firefox, or the calculator app on your phone.
These can often be specific per operating system, as the executable file created may have specifically been made to communicate
specifically with like the Windows operating system.

Most operating systems come with a whole slew of applications, but a lot of them are not necessary to communicate with the hardware.
----