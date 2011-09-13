
11. Advanced Input/Output: Streams, Files, and Networking
---------------------------------------------------------


Computer programs are only useful if they interact with the rest of
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
which were covered in :doc:`Chapter 8</8>`. Many of the subroutines that are
used can throw exceptions that require mandatory exception handling.
This generally means calling the subroutine in atry..catch statement
that can deal with the exception if one occurs. Effective network
communication also requires the use of threads, which will be covered
in the :doc:`Chapter 12</12>`. We will look at the basic networking API in this
chapter, but we will return to the topic of threads and networking in
:doc:`Section 12.4</12/s4>`.


.. toctree::

   s1
   s2
   s3
   s4
   s5
   exercises
   quiz

