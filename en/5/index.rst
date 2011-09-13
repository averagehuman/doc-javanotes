[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]





Chapter 5
~~~~~~~~~


Programming in the Large II: Objects and Classes
------------------------------------------------



W hereas a subroutine represents a single task, an object can
encapsulate both data (in the form of instance variables) and a number
of different tasks or "behaviors" related to that data (in the form of
instance methods). Therefore objects provide another, more
sophisticated type of structure that can be used to help manage the
complexity of large programs.

This chapter covers the creation and use of objects in Java.
`Section5.5`_ covers the central ideas of object-oriented programming:
inheritance and polymorphism. However, in this textbook, we will
generally use these ideas in a limited form, by creating independent
classes and building on existing classes rather than by designing
entire hierarchies of classes from scratch. `Section5.6`_ and
`Section5.7`_ cover some of the many details of object oriented
programming in Java. Although these details are used occasionally
later in the book, you might want to skim through them now and return
to them later when they are actually needed.





Contents of Chapter 5:
~~~~~~~~~~~~~~~~~~~~~~


+ Section 1: `Objects, Instance Methods, and Instance Variables`_
+ Section 2: `Constructors and Object Initialization`_
+ Section 3: `Programming with Objects`_
+ Section 4: `Programming Example: Card, Hand, Deck`_
+ Section 5: `Inheritance, Polymorphism, and Abstract Classes`_
+ Section 6: `this and super`_
+ Section 7: `Interfaces, Nested Classes, and Other Details`_
+ `Programming Exercises`_
+ `Quiz on This Chapter`_




[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]

.. _Constructors and Object Initialization: http://math.hws.edu/javanotes/c5/s2.html
.. _Previous Chapter: http://math.hws.edu/javanotes/c5/../c4/index.html
.. _Quiz on This Chapter: http://math.hws.edu/javanotes/c5/quiz.html
.. _Interfaces, Nested Classes, and Other Details: http://math.hws.edu/javanotes/c5/s7.html
.. _Next Chapter: http://math.hws.edu/javanotes/c5/../c6/index.html
.. _Programming Example: Card, Hand, Deck: http://math.hws.edu/javanotes/c5/s4.html
.. _this and super: http://math.hws.edu/javanotes/c5/s6.html
.. _5.5: http://math.hws.edu/javanotes/c5/../c5/s5.html
.. _First Section: http://math.hws.edu/javanotes/c5/s1.html
.. _Programming Exercises: http://math.hws.edu/javanotes/c5/exercises.html
.. _Main Index: http://math.hws.edu/javanotes/c5/../index.html
.. _Inheritance, Polymorphism, and Abstract Classes: http://math.hws.edu/javanotes/c5/s5.html
.. _5.7: http://math.hws.edu/javanotes/c5/../c5/s7.html
.. _5.6: http://math.hws.edu/javanotes/c5/../c5/s6.html
.. _Programming with Objects: http://math.hws.edu/javanotes/c5/s3.html


