
# Computer Intro

This info is literally in the beginning of almost all computer courses, so this
is not going to be the first time this will be drilled into ya head:


> **Computer System:** A combination of all the components required to process and store data and using a computer, which is composed of multiple pieces of hardware and software

## Hardware v. Software

> *Hardware* is the physical equipment and devices that make up one's computer. This is the
> keyboard, mouse, speakers, printers, mic, camera, RAM, CPU, storage and all the internal
> bits in a computer.

> *Software* is what is __on__ the hardware; to be more specific: it is the
> instructions on these devices and systems which tell the device/system how to
> operate.


These instructions to make the computer do *something* is called a __program__.

If you write these instructions, these programs, you are __programming__ and doing the tasks of a __programmer__.

These programs often need to be carried out in a specific manner or set
of instructions to actually produce a desired solution...
this set of instructions would be the __logic__ of a program.

MUCH of this class if simply focused on *logically* solving problems.

What you will hopefully learn is that the same problem can be solved in multiple 
different ways OR (more importantly for our sakes here), in multiple different environments/(programming) languages.


-------

## Types of Software

### System Software

> **_System Software:_** the programs that are part of the OS you are running to ensure it works. Often used to manage the system's resources, provide GUI interfaces, delegate tasks, organize files, and much, much more. Contrast with application software.

### Application Software

> **_Application Software:_** the programs that help users with tasks (e.g., accounting or word processing). Contrast with system software.

-------

## Types of Hardware

### Input Devices
Devices/components which GIVE the system information. Think mouse, keyboard, mic, camera.

### Processing Devices
Devices/components which take info and transform/process it. Think ram, cpu, controllers.

### Output devices
Devices/components which take data and GIVE IT BACK TO THE USER. Think monitor/screen, speakers, lights.


-------

## How do we get software to tell the computer how to do... well... anything

(generally, obviously elaborate)
COMPUTER <--- MACHINE CODE <---- ASSEMBLY CODE (low level lang) <---- HIGH LEVEL CODE

High Level Programming Languages:
- Java
- Visual Basic
- C++
- C#
- Python
- Javascript


Low Level Programming Languages (assembly):
- NASM



## Compilers and Interpreters and Binary

Basically, we do NOT want to be manually writing 0's and 1's, so
we make the computer translate human readable stuff to less human readable stuff

The most important task of a compiler or an interpreter is to translate a 
programming language (which we can read and understand) into machine language (which
the computer can read and understand)


# Some real code which prints "Hello world!" to your screen

## Example Low Level Programming languages (NASM, x86, 32-bit)

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


## Example High Level Programming Language

```python
print("Hello world!")
```

