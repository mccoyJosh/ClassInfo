# Syntax and Logic and CODE

Put simply: *code* (aka an *algorithm)* is __set of instructions to complete a task__.

This definition is broad enough to not limit itself to only computer code.
Any set of instructions to do *anything* is a type of code or algorithm.

The class example of a piece of 'code' in the real world is a cooking recipe.
Recipes are typically instructions to complete the task of making some type of
food, and looking at one can help us actually see the many aspects of a real
piece of code... so let's look at a *simplified* recipe:

```
# To Bake A Cake
1. preheat oven to 320°F
2. get mixing bowl
3. add flour and baking powder to mixing bowl
4. sift flour and baking powder together
5. mix in sugar, butter, milk, and vanilla
6. get cake tin
7. grease cake tin
8. pour mixture into cake tin
9. put cake bin into oven
10. allow cake to bake for 45-50 minutes
11. remove cake from oven
12. let cool
13. EAT
```

With just this example, we can see many of the basics of all programs/code/algorithms.

# It works!

Obviously, the first thing we notice is that if we follow this algorithm,
we will end up with the desired result... a cake!

The idea you should understand from this is that a piece of code
should complete a task/series of task. If a piece of code is not doing
the desired task, you have an issue (obviously).

If something is preventing us from completing the task, whether that be
an issue with the written instructions, or the correct instructions being unable to
be followed for some reason, this is known as an __error__ or a __bug__.

There are many ways a piece of code can have an error.


# Syntax

Typically, programming languages are specific in the way in which the code is written.
The way in which a programming language is written is called its **_syntax_**.\

### Formal Syntax Definition:

> **_Syntax:_** the rules of a language

Another way of thinking about it is that it is like the grammar of a language.
In out recipe example, it's "syntax" is to be formatted as a chronological list in english.


# Syntax Error

A *syntax error* is a type of error that results from a piece of code
being unable to be read/understood/compiled, i.e., there being some sort of problem in its syntax.

If our cooking recipe looked like this instead:

```
# Coquere Libum
5. Misce saccharum, butyrum, lac, et vanillam
1. Praecale furnum ad 320°F
4. Cribra farinam et fermentum simul
12. Sine refrigerari
2. Accipe crateram miscendi
6. Accipe formam libi
7. Unge formam libi
9. Pone formam libi in furnum
10. Sine libum coqui per 45-50 minuta
3. Adde farinam et fermentum in crateram miscendi
11. Remove libum e furno
13. Consume
8. Infunde mixturam in formam libi
```

We would have a huge problem: we can't even read this!
We can not even begin to understand what the recipe would look like
because the expected syntax (english... and in a chronological list)

This would be a syntax error!

If we quickly looked at a real piece of code, we can see this actually in action:

```c
#include <stdio.h>
int main() {
   printf("Hello, World!");
   return 0;
}
```

This code works just fine! This code is written in C, and
just prints out to the screen "hello world".
C is not the simplest language, and part of it is because
it has stricterish syntax. One instance of this is
each line of code needs to end with a semicolon (;).

If we forget this, and run the code, it will result in a
syntax error as the computer cannot figure out what to do with
this code because IT CANNOT FULLY READ IT!

If we remove the semicolon after the line "return 0;", and try
running the code, we get this message:

```
file.c: In function ‘main’:
file.c:5:12: error: expected ‘;’ before ‘}’ token
    5 |    return 0
      |            ^
      |            ;
    6 | }
      | ~
```

The compiler is even smart enough to explain where the error is!

When writing algorithms and coding, we need to think like a computer (unfortunately).
Computers don't know how we intend to end instructions all by themselves. They are
like a baby following our every move, not knowing where we are leading it or what it
is even accomplishing, just doing "tasks".

Side not: please don't make your baby do tasks like you would a computer.

Consider this example:

```c
#include <stdio.h>
int main() {
   printf("Hello, World!")
   return 0;
}
```

In this previous example, by removing the semicolon, suddenly our baby computer doesn't know
when 1 line ends and the next line starts and assumes (because we didn't say otherwise) that they are the same line. 
When it tries to read it as the same line, it fails, because it is not familiar with one instruction being "printf("Hello, World!")return 0;"

Follow a language's rules and you will have correct syntax!

# Logic

As was already discussed, logic is "what" the code is trying to do or express.

### Formal Logic Definition

> **_Logic:_** the complete sequence of instructions that lead to a problem solution.

In our cake example, the logic is just DOING each step.

# Logical Error

If these instructions are incorrect or lead to something other
than our intended solution, this would be a logical error.

### Formal Logic Definition:

> **_Logical Errors:**_ errors that occur when incorrect instructions are performed, or when instructions are performed in the wrong order.

This would be if our instructions had a step where you got on your roof.
This would not help you bake a cake.

Or if it read to:
1. preheat oven to 100,000,000°F
   this would be too hot!

Typically, logical errors still allow a piece of code to run and even
get done, but you probably won't end up with the correct result.

Since these errors are (typically) ones that don't stop the program,
these can be a lot harder to pin down.

Returning back to the C language, if we were writing a program to say "Hello World" and we instead had this
piece of code:

```c
#include <stdio.h>
int main() {
   printf(87);
   return 0;
}
```


.... well, we would have a logic error. This code DOES follow the rules of the language and should run
just fine, but we will not reach out goal, instead we get some random other answer.