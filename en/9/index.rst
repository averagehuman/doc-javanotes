[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]





Chapter 9
~~~~~~~~~


Linked Data Structures and Recursion
------------------------------------



I n this chapter, we look at two advanced programming techniques,
recursion and linked data structures, and some of their applications.
Both of these techniques are related to the seemingly paradoxical idea
of defining something in terms of itself. This turns out to be a
remarkably powerful idea.

A subroutine is said to be recursive if it calls itself, either
directly or indirectly. What this means is that the subroutine is used
in its own definition. Recursion can often be used to solve complex
problems by reducing them to simpler problems of the same type.

A reference to one object can be stored in an instance variable of
another object. The objects are then said to be "linked." Complex data
structures can be built by linking objects together. An especially
interesting case occurs when an object contains a link to another
object that belongs to the same class. In that case, the class is used
in its own definition. Several important types of data structures are
built using classes of this kind.





Contents of Chapter 9:
~~~~~~~~~~~~~~~~~~~~~~


+ Section 1: `Recursion`_
+ Section 2: `Linked Data Structures`_
+ Section 3: `Stacks, Queues, and ADTs`_
+ Section 4: `Binary Trees`_
+ Section 5: `A Simple Recursive Descent Parser`_
+ `Programming Exercises`_
+ `Quiz on This Chapter`_




[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]

.. _Programming Exercises: http://math.hws.edu/javanotes/c9/exercises.html
.. _Quiz on This Chapter: http://math.hws.edu/javanotes/c9/quiz.html
.. _Next Chapter: http://math.hws.edu/javanotes/c9/../c10/index.html
.. _Main Index: http://math.hws.edu/javanotes/c9/../index.html
.. _First Section: http://math.hws.edu/javanotes/c9/s1.html
.. _Stacks, Queues, and ADTs: http://math.hws.edu/javanotes/c9/s3.html
.. _Previous Chapter: http://math.hws.edu/javanotes/c9/../c8/index.html
.. _Linked Data Structures: http://math.hws.edu/javanotes/c9/s2.html
.. _A Simple Recursive Descent Parser: http://math.hws.edu/javanotes/c9/s5.html
.. _Binary Trees: http://math.hws.edu/javanotes/c9/s4.html


