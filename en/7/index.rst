[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]





Chapter 7
~~~~~~~~~


Arrays
------



C omputers get a lot of their power from working with data structures.
A data structure is an organized collection of related data. An object
is a data structure, but this type of data structure -- consisting of
a fairly small number of named instance variables -- is just the
beginning. In many cases, programmers build complicated data
structures by hand, by linking objects together. We'll look at these
custom-built data structures in `Chapter9`_. But there is one type of
data structure that is so important and so basic that it is built into
every programming language: the array.

An array is a data structure consisting of a numbered list of items,
where all the items are of the same type. In Java, the items in an
array are always numbered from zero up to some maximum value, which is
set when the array is created. For example, an array might contain 100
integers, numbered from zero to 99. The items in an array can belong
to one of Java's primitive types. They can also be references to
objects, so that you could, for example, make an array containing all
the buttons in a GUI program.

This chapter discusses how arrays are created and used in Java. It
also covers the standard class java.util.ArrayList. An object of
typeArrayList is very similar to an array of Objects, but it can grow
to hold any number of items.





Contents of Chapter 7:
~~~~~~~~~~~~~~~~~~~~~~


+ Section 1: `Creating and Using Arrays`_
+ Section 2: `Programming With Arrays`_
+ Section 3: `Dynamic Arrays and ArrayLists`_
+ Section 4: `Searching and Sorting`_
+ Section 5: `Multi-dimensional Arrays`_
+ `Programming Exercises`_
+ `Quiz on This Chapter`_




[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]

.. _Main Index: http://math.hws.edu/javanotes/c7/../index.html
.. _Quiz on This Chapter: http://math.hws.edu/javanotes/c7/quiz.html
.. _Programming  With Arrays: http://math.hws.edu/javanotes/c7/s2.html
.. _Next Chapter: http://math.hws.edu/javanotes/c7/../c8/index.html
.. _9: http://math.hws.edu/javanotes/c7/../c9/index.html
.. _Dynamic Arrays and ArrayLists: http://math.hws.edu/javanotes/c7/s3.html
.. _First Section: http://math.hws.edu/javanotes/c7/s1.html
.. _Multi-dimensional Arrays: http://math.hws.edu/javanotes/c7/s5.html
.. _Previous Chapter: http://math.hws.edu/javanotes/c7/../c6/index.html
.. _Programming Exercises: http://math.hws.edu/javanotes/c7/exercises.html
.. _Searching and Sorting: http://math.hws.edu/javanotes/c7/s4.html


