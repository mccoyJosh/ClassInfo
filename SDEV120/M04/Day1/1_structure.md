# Structured Code

As code sets get larger, things can get very complicated 
and unwieldy. 

If we go ahead and start writing code and planning how everything connects and works, what we
can end up with is code that is

- confusing
- repeating portions of code
- impossible to reuse/modularize
- hard to organize your solutions
- prone to error
- hard to fix errors

What these programs OFTEN don't include is structure

> **Spaghetti Code:** unstructured program logic. See also unstructured programs.

> **Unstructured programs:** programs that do not follow the rules of structured logic

So, often when talking about programming, a lot of work and discussion is about
just getting things to work, and then calling a day.

Taking a step back though and looking into the proper rules of 
designing code is super important.

That is what today is really going to be: talking about the rules for how
code should be written, i.e. how it should be arranged, i.e. how it should be structured

# Why do structured code?

Before we get into these specific rules for arrangement, why should we even care? 

We JUST talked about the bad reasons for unstructured code, which
some of these are going to be parallels for, but not all.
So, why?

-----

## Clarity

When code is structured, it is made in an expected
way which people who write code recognize. When we work
with familiar structures over time, we can quickly look at a piece
of code and understand it far easier than unstructured code.

Also, many of these structuring techniques make it precisely clear in what it is
trying to accomplish. This is especially true for things like loops.

-----

## Professionalism

When working with others in the field, if you are making wild code
that lacks common types of structure, people are not going to take you seriously.

Many pre-established structures for codes exist to solve a wide variety of problems, and
it is common to use most of them. If you are using some novel invention-type-structure 
to solve a common problem
- it is actually probably worse
- you are wasting time

It also may look like you don't know the common solution, and look kinda dumb.

Otherwise, all other programmers expect your programs to be structured... and will be
disappointed if they aren't.

-----

## Efficiency

Most programming languages today have these structures 
built into the language. Knowing the proper uses will
allow you to efficiently write code and utilize it.

Even if the programming language doesn't support it (like in the instance of
older programming languages), you can typically recreate these within 
the tools the language does give you.


-----

## Maintenance

When structured, we can easily modify programs to work
a bug is introduced.

With a common format, we can easily locate the lines within it
that are just not either following that structure, or if a logical error exists
within the context of the structure.


-----

## Modularity

By following structures, we easily group large portions of our code into
their respective structures, or combination of structures. If we need to move around the order
of our code, we can just move the larger structure!

Also, we can group these structures into modules, and re-use the code in multiple places.


-----
