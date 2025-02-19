# Processes

Whenever you run your program, the machine you are using (or more accurately, the operating 
system you are using) will create for your program a process, which is allocated a small
section of the cpi, diskspace, memory, and things like your network if need be.  

There are number of things that the machine saves about your process, such as
an id identifying it, the directory it is working in (current working directory), the usage
of the resources on your computer, how long it has existed, the user who made the process, and more!

You can see alot of this information from your devices task manager (or the command `top` on a linux machine).

More so, this information can also be gathered from python programs yourself:

```python
import os

print(os.getpid())

print(os.getcwd())
```


### Subprocess

When making a program, we are not restricted to only making a single one, but can initiate additional programs
as SUBPROCESS.

For instance, if you need to run a command from the commandline from your
python program, you can!

```python
import subprocess

output = subprocess.getoutput('pwd')

print(output)
```

This can include running another python file:

```python
import subprocess

output = subprocess.getoutput('python ex.py')

print(f'HERE IS THE OUTPUT OF THE OTHER FILE: "{output}"')
```

This very quickly begins to give us the ability to make some sort of program to control and run other programs!

In these examples of using subprocesses though, our program is dependent on the
subprocess to actually finish before it can keep on going, which we are 
going to see a solution for SOON.

If you want to call the process but not capture its input, you can just use
the 'call' method instead of 'getoutput':

```python
import subprocess

subprocess.call('pwd')
```

## Multiprocessing

We can also BEGIN the process of kinda doing concurrent programs, that
is, programs running at the same time. Now, before we get into concurrent programming, we kinda
need to talk about its cousin, multiprocessing.

> Multiprocessing is running more than one process on a single processor, but can be on multiple processors

Within python, we can easily do this with the `multiprocessing` package.
Each process we are going to create is going to run an instance of a function.

Here is a small example:
(highly inspired from the text book)

```python
import multiprocessing
import os


def whoami(what):
    print(f"Process {os.getpid()} what's: {what}")


if __name__ == "__main__":
    whoami("MAIN PROGRAM")
    for n in range(5):
        p = multiprocessing.Process(target=whoami, args=(f"function call {n}",))
        p.start()
    print('DONE')
```

When running this, you may notice that "DONE" is (most of the time) printed out before we see the
last message of the last process. That is because these new processes are separate and NOT subprocesses of
the original call.

That means they are running at the same time, technically, and the original process 
was not held up waiting for the created processes to finish.

This is the beginning of understanding programs running in conjunction to each other.


### Killing Processes

Whenever we start creating these multiple processes, it is probably in our best interest to kill them when we
no longer want them to exist.

There are two main ways to do this:

Easiest is to use the reference to the process that we have
from the previous program. All we need to do is call the terminate method from
the object and that is it!

So, here is the same piece of code but now each process is killed immediately.

Obviously this is kinda dumb, but it is just showing off the method.
```python
import multiprocessing
import os


def whoami(what):
    print(f"Process {os.getpid()} what's: {what}")


if __name__ == "__main__":
    whoami("MAIN PROGRAM")
    for n in range(5):
        p = multiprocessing.Process(target=whoami, args=(f"function call {n}",))
        p.start()
        p.terminate()
    print('DONE')
```

The second way is to do it from the operating system itself (or, from python, the os package).

There is an aptly named 'kill' function which takes two parameters, those being
the process id (pid) and signal to send it. Typically, when terminating a process, you
would want to use the signal code 0 for SIGTERM, which the typical way of exiting a process.

SIGTERM gives the program the opportunity to kill itself, which results in the program 
properly ending and the life of its subprocesses. This ensures the resources are correctly
reallocated back the device.

Using something like SIGKILL will kill a process IMMEDIATELY, which can result in subprocess lingering around
as 'zombie' processes, which are still allocated resources and then have to be ended in some fancy fashion.

In python, using the function looks like this:

```python
import os

os.kill(os.getpid(), 0)
```