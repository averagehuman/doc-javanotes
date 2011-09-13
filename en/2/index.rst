[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]





Chapter 2
~~~~~~~~~


Programming in the Small I: Names and Things
--------------------------------------------



O n a basic level (the level of machine language), a computer can
perform only very simple operations. A computer performs complex tasks
by stringing together large numbers of such operations. Such tasks
must be "scripted" in complete and perfect detail by programs.
Creating complex programs will never be really easy, but the
difficulty can be handled to some extent by giving the program a clear
overall structure. The design of the overall structure of a program is
what I call "programming in the large."

Programming in the small, which is sometimes called coding, would then
refer to filling in the details of that design. The details are the
explicit, step-by-step instructions for performing fairly small-scale
tasks. When you do coding, you are working fairly "close to the
machine," with some of the same concepts that you might use in machine
language: memory locations, arithmetic operations, loops and branches.
In a high-level language such as Java, you get to work with these
concepts on a level several steps above machine language. However, you
still have to worry about getting all the details exactly right.

This chapter and the next examine the facilities for programming in
the small in the Java programming language. Don't be misled by the
term "programming in the small" into thinking that this material is
easy or unimportant. This material is an essential foundation for all
types of programming. If you don't understand it, you can't write
programs, no matter how good you get at designing their large-scale
structure.

The last section of this chapter discusses programming environments.
That section contains information about how to compile and run Java
programs, and you might want to take a look at it before trying to
write and use your own programs.





Contents of Chapter 2:
~~~~~~~~~~~~~~~~~~~~~~


+ Section 1: `The Basic Java Application`_
+ Section 2: `Variables and the Primitive Types`_
+ Section 3: `Strings, Objects, Enums, and Subroutines`_
+ Section 4: `Text Input and Output`_
+ Section 5: `Details of Expressions`_
+ Section 6: `Programming Environments`_
+ `Programming Exercises`_
+ `Quiz on This Chapter`_




[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]

.. _Strings, Objects, Enums, and Subroutines: http://math.hws.edu/javanotes/c2/s3.html
.. _Main Index: http://math.hws.edu/javanotes/c2/../index.html
.. _Programming Environments: http://math.hws.edu/javanotes/c2/s6.html
.. _Details of Expressions: http://math.hws.edu/javanotes/c2/s5.html
.. _Programming Exercises: http://math.hws.edu/javanotes/c2/exercises.html
.. _First Section: http://math.hws.edu/javanotes/c2/s1.html
.. _Quiz on This Chapter: http://math.hws.edu/javanotes/c2/quiz.html
.. _Next Chapter: http://math.hws.edu/javanotes/c2/../c3/index.html
.. _Text Input and Output: http://math.hws.edu/javanotes/c2/s4.html
.. _Previous Chapter: http://math.hws.edu/javanotes/c2/../c1/index.html
.. _Variables and the Primitive Types: http://math.hws.edu/javanotes/c2/s2.html


