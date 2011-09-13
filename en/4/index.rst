[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]





Chapter 4
~~~~~~~~~


Programming in the Large I: Subroutines
---------------------------------------



O ne way to break up a complex program into manageable pieces is to
use subroutines. A subroutine consists of the instructions for
carrying out a certain task, grouped together and given a name.
Elsewhere in the program, that name can be used as a stand-in for the
whole set of instructions. As a computer executes a program, whenever
it encounters a subroutine name, it executes all the instructions
necessary to carry out the task associated with that subroutine.

Subroutines can be used over and over, at different places in the
program. A subroutine can even be used inside another subroutine. This
allows you to write simple subroutines and then use them to help write
more complex subroutines, which can then be used in turn in other
subroutines. In this way, very complex programs can be built up step-
by-step, where each step in the construction is reasonably simple.

As mentioned in `Section3.8`_, subroutines in Java can be either
static or non-static. This chapter covers static subroutines only.
Non-static subroutines, which are used in true object-oriented
programming, will be covered in the next chapter.





Contents of Chapter 4:
~~~~~~~~~~~~~~~~~~~~~~


+ Section 1: `Black Boxes`_
+ Section 2: `Static Subroutines and Static Variables`_
+ Section 3: `Parameters`_
+ Section 4: `Return Values`_
+ Section 5: `APIs, Packages, and Javadoc`_
+ Section 6: `More on Program Design`_
+ Section 7: `The Truth About Declarations`_
+ `Programming Exercises`_
+ `Quiz on This Chapter`_




[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]

.. _Quiz on This Chapter: http://math.hws.edu/javanotes/c4/quiz.html
.. _Static Subroutines and Static Variables: http://math.hws.edu/javanotes/c4/s2.html
.. _Previous Chapter: http://math.hws.edu/javanotes/c4/../c3/index.html
.. _Next Chapter: http://math.hws.edu/javanotes/c4/../c5/index.html
.. _Return Values: http://math.hws.edu/javanotes/c4/s4.html
.. _APIs, Packages, and Javadoc: http://math.hws.edu/javanotes/c4/s5.html
.. _Programming Exercises: http://math.hws.edu/javanotes/c4/exercises.html
.. _3.8: http://math.hws.edu/javanotes/c4/../c3/s8.html
.. _Main Index: http://math.hws.edu/javanotes/c4/../index.html
.. _Parameters: http://math.hws.edu/javanotes/c4/s3.html
.. _First Section: http://math.hws.edu/javanotes/c4/s1.html
.. _More on Program Design: http://math.hws.edu/javanotes/c4/s6.html
.. _The Truth About Declarations: http://math.hws.edu/javanotes/c4/s7.html


