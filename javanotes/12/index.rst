
12. Threads and Multiprocessing
-------------------------------

In the classic programming model, there is a single central
processing unit that reads instructions from memory and carries them
out, one after the other. The purpose of a program is to provide the
list of instructions for the processor to execute. This is the only
type of programming that we have considered so far.

However, this model of programming has limitations. Modern computers
have multiple processors, making it possible for them to perform
several tasks at the same time. To use the full potential of all those
processors, you will need to write programs that can do parallel
processing. For Java programmers, that means learning aboutthreads. A
single thread is similar to the programs that you have been writing up
until now, but more than one thread can be running at the same time,
"in parallel." What makes things more interesting -- and more
difficult -- than single-threaded programming is the fact that the
threads in a parallel program are rarely completely independent of one
another. They usually need to cooperate and communicate. Learning to
manage and control cooperation among threads is the main hurdle that
you will face in this chapter.

There are several reasons to use parallel programming. One is simply
to do computations more quickly by setting several processors to work
on them simultaneously. Just as important, however, is to use threads
to deal with "blocking" operations, where a process can't proceed
until some event occurs. In the`previous chapter`_, for example, we
saw how programs can block while waiting for data to arrive over a
network connection. Threads make it possible for one part of a program
to continue to do useful work even while another part is blocked,
waiting for some event to occur. In this context, threads are a vital
programming tool even for a computer that has only a single processing
unit.

.. toctree::

   s1
   s2
   s3
   s4
   s5
   exercises
   quiz
   quiz_answers

