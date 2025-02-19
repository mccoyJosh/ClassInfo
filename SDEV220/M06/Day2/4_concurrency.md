# Concurrency 

> Concurrency is running a process on more than one processor

This allows you to not only have programs run in parallel with each other, but
also typically includes sharing of assets and resources to make sure different processes are
wasting time, and / or affecting the ability to work of another process.

Concurrent programming in python is still going to be us using multiprocessing but, we are also going to
learn some typically concurrent ideas.

Now, when making concurrent programs, each individual process that is created is often referred to
as a worker. Also, in some implementation to concurrent programs, these processes are
referred to as threads, but that is technically confined to what is known as parallel programming.

# Is it worth it?

Now you may think that the more processes you are putting to a task, the better, right?

Well, not in all cases.

Some problems are small enough where having only X number of concurrent programs is more than enough.
For instance, if we were incrementing 4 places in an array all at once, there is no need to have 5,6 or more processes, as
we cover all needs with just 4.

Moreover, even in larger problems where there is potentially an infinite set of problems to solve
and more workers would help, we can often find that the overhead of keeping all the subprocesses in line
may be too much for our machine to handle, and we will reach a point of no gains to efficiency. This may even
present as not only dwindling gains, but loss of performance. In these situations, the handling of all of these workers
is literally more costly than the work they are trying to do.

The best time to use a concurrent or parallel programming solution is for process which are going to be doing
the same exact thing in multiple different address places.

If we think of something matrix multiplication, we could EASILY convert it to a faster
program using concurrent programs. We can assign each space in the resulting matrix to a process, and they
just have to share reading the two matrices being multiplied together.



# [Parallel and Current programming is TECHNICALLY different](https://www.baeldung.com/cs/concurrency-vs-parallelism)

# [Different types of parallelism / concurrent programming](https://www.cac.cornell.edu/education/training/ParallelMay2012/ParallelProgramming.pdf)


# Problems Which Can Occur 

### Sharing the same resource at the same time

In most cases, you want a singular processioning a single memory space at a time.
When multiple processes start to use the same space, unexpected outcomes can occur.

SO, what we typically do is put some lock in place to allow only one process to access a resource at a
time. So, the other resources just need to wait until the other process unlocks it and allows the
other process to go ahead and lock it itself.

### Deadlock

One problem that can occur due to this is [deadlock](https://medium.com/@parvjn616/understanding-deadlocks-in-concurrent-programming-799d78ebe7a8).

This is when one process is holding resource A and needs resource B to finish its process, BUT
there is a second process that is holding resource B and needs resource A to finish its process.

With locks in place, both are stuck holding on the resource that would allow for them both to end.
This makes the lock, dead, and our program gets stuck up. 

Common ways to prevent this is to 

- allows shared read access and not write access, so another process just needing to read a resources doesn't get stopped up.
- Implement a lock timer so that it will let go of the resource (gracefully) and allow the other process to access it.
- creating a tracker / data structure of sorts of who has access to what and using that to know when a deadlock occurs and then stopping it there.



