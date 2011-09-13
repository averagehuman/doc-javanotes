[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]





Chapter 6
~~~~~~~~~


Introduction to GUI Programming
-------------------------------



C omputer users today expect to interact with their computers using a
graphical user interface (GUI). Java can be used to write GUI programs
ranging from simple applets which run on a Web page to sophisticated
stand-alone applications.

GUI programs differ from traditional "straight-through" programs that
you have encountered in the first few chapters of this book. One big
difference is that GUI programs are event-driven. That is, user
actions such as clicking on a button or pressing a key on the keyboard
generate events, and the program must respond to these events as they
occur. Event-driven programming builds on all the skills you have
learned in the first five chapters of this text. You need to be able
to write the methods that respond to events. Inside those methods, you
are doing the kind of programming-in-the-small that was covered in
`Chapter2`_ and `Chapter3`_.

And of course, objects are everywhere in GUI programming. Events are
objects. Colors and fonts are objects. GUI components such as buttons
and menus are objects. Events are handled by instance methods
contained in objects. In Java, GUI programming is object-oriented
programming.

This chapter covers the basics of GUI programming. The discussion will
continue in `Chapter13`_ with more details and with more advanced
techniques.





Contents of Chapter 6:
~~~~~~~~~~~~~~~~~~~~~~


+ Section 1: `The Basic GUI Application`_
+ Section 2: `Applets and HTML`_
+ Section 3: `Graphics and Painting`_
+ Section 4: `Mouse Events`_
+ Section 5: `Timers, KeyEvents, and State Machines`_
+ Section 6: `Basic Components`_
+ Section 7: `Basic Layout`_
+ Section 8: `Menus and Dialogs`_
+ `Programming Exercises`_
+ `Quiz on This Chapter`_




[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]

.. _Menus and Dialogs: http://math.hws.edu/javanotes/c6/s8.html
.. _13: http://math.hws.edu/javanotes/c6/../c13/index.html
.. _2: http://math.hws.edu/javanotes/c6/../c2/index.html
.. _Applets and HTML: http://math.hws.edu/javanotes/c6/s2.html
.. _Programming Exercises: http://math.hws.edu/javanotes/c6/exercises.html
.. _Next Chapter: http://math.hws.edu/javanotes/c6/../c7/index.html
.. _Basic Components: http://math.hws.edu/javanotes/c6/s6.html
.. _Basic Layout: http://math.hws.edu/javanotes/c6/s7.html
.. _3: http://math.hws.edu/javanotes/c6/../c3/index.html
.. _Previous Chapter: http://math.hws.edu/javanotes/c6/../c5/index.html
.. _Main Index: http://math.hws.edu/javanotes/c6/../index.html
.. _Quiz on This Chapter: http://math.hws.edu/javanotes/c6/quiz.html
.. _First Section: http://math.hws.edu/javanotes/c6/s1.html
.. _Graphics and Painting: http://math.hws.edu/javanotes/c6/s3.html
.. _Mouse Events: http://math.hws.edu/javanotes/c6/s4.html
.. _Timers, KeyEvents, and State Machines: http://math.hws.edu/javanotes/c6/s5.html


