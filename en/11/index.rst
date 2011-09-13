[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]





Chapter 11
~~~~~~~~~~


Advanced Input/Output: Streams, Files, and Networking
-----------------------------------------------------



C omputer programs are only useful if they interact with the rest of
the world in some way. This interaction is referred to asinput/output,
or I/O. Up until now, this book has concentrated on just one type of
interaction: interaction with the user, through either a graphical
user interface or a command-line interface. But the user is only one
possible source of information and only one possible destination for
information. We have already encountered one other type of
input/output, sinceTextIO can read data from files and write data to
files. However, Java has an input/output framework that provides much
more power and flexibility than does TextIO, and that covers other
kinds of I/O in addition to files. Most importantly, it supports
communication over network connections. In Java, input/output
involving files and networks is based onstreams, which are objects
that support I/O commands that are similar to those that you have
already used. In fact, standard output (System.out) and standard input
(System.in) are examples of streams.

Working with files and networks requires familiarity with exceptions,
which were covered in `Chapter8`_. Many of the subroutines that are
used can throw exceptions that require mandatory exception handling.
This generally means calling the subroutine in atry..catch statement
that can deal with the exception if one occurs. Effective network
communication also requires the use of threads, which will be covered
in the `Chapter12`_. We will look at the basic networking API in this
chapter, but we will return to the topic of threads and networking in
`Section12.4`_.





Contents of Chapter 11:
~~~~~~~~~~~~~~~~~~~~~~~


+ Section 1: `Streams, Readers, and Writers`_
+ Section 2: `Files`_
+ Section 3: `Programming With Files`_
+ Section 4: `Networking`_
+ Section 5: `A Brief Introduction to XML`_
+ `Programming Exercises`_
+ `Quiz on This Chapter`_




[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]

.. _8: http://math.hws.edu/javanotes/c11/../c8/index.html
.. _Quiz on This Chapter: http://math.hws.edu/javanotes/c11/quiz.html
.. _Programming With Files: http://math.hws.edu/javanotes/c11/s3.html
.. _Networking: http://math.hws.edu/javanotes/c11/s4.html
.. _12.4: http://math.hws.edu/javanotes/c11/../c12/s4.html
.. _Files: http://math.hws.edu/javanotes/c11/s2.html
.. _Next Chapter: http://math.hws.edu/javanotes/c11/../c12/index.html
.. _Previous Chapter: http://math.hws.edu/javanotes/c11/../c10/index.html
.. _Main Index: http://math.hws.edu/javanotes/c11/../index.html
.. _Programming Exercises: http://math.hws.edu/javanotes/c11/exercises.html
.. _A Brief Introduction to XML: http://math.hws.edu/javanotes/c11/s5.html
.. _First Section: http://math.hws.edu/javanotes/c11/s1.html


