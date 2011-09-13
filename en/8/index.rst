[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]





Chapter 8
~~~~~~~~~


Correctness, Robustness, Efficiency
-----------------------------------



I n previous chapters, we have covered the fundamentals of
programming. The chapters that follow this one will cover more
advanced aspects of programming. The ideas that are presented will
generally be more complex and the programs that use them a little more
complicated. This relatively short chapter is a kind of turning point
in which we look at the problem of getting such complex programs right
.

Computer programs that fail are much too common. Programs are fragile.
A tiny error can cause a program to misbehave or crash. Most of us are
familiar with this from our own experience with computers. And we've
all heard stories about software glitches that cause spacecraft to
crash, telephone service to fail, and, in a few cases, people to die.

Programs don't have to be as bad as they are. It might well be
impossible to guarantee that programs are problem-free, but careful
programming and well-designed programming tools can help keep the
problems to a minimum. This chapter will look at issues of correctness
and robustness of programs. It also looks more closely at exceptions
and the try..catch statement, and it introduces assertions, another of
the tools that Java provides as an aid in writing correct programs.

We will also look at another issue that is important for programs in
the real world: efficiency. Even a completely correct program is not
very useful if it takes an unreasonable amount of time to run. The
last section of this chapter introduces techniques for analyzing the
run time of algorithms.





Contents of Chapter 8:
~~~~~~~~~~~~~~~~~~~~~~


+ Section 1: `Introduction to Correctness and Robustness`_
+ Section 2: `Writing Correct Programs`_
+ Section 3: `Exceptions and try..catch`_
+ Section 4: `Assertions and Annotations`_
+ Section 5: `Analysis of Algorithms`_
+ `Programming Exercises`_
+ `Quiz on This Chapter`_




[ `First Section`_ | `Previous Chapter`_ | `Next Chapter`_ | `Main
Index`_ ]

.. _Assertions and Annotations: http://math.hws.edu/javanotes/c8/s4.html
.. _First Section: http://math.hws.edu/javanotes/c8/s1.html
.. _Programming Exercises: http://math.hws.edu/javanotes/c8/exercises.html
.. _Main Index: http://math.hws.edu/javanotes/c8/../index.html
.. _Analysis of Algorithms: http://math.hws.edu/javanotes/c8/s5.html
.. _Writing Correct Programs: http://math.hws.edu/javanotes/c8/s2.html
.. _Exceptions and try..catch: http://math.hws.edu/javanotes/c8/s3.html
.. _Previous Chapter: http://math.hws.edu/javanotes/c8/../c7/index.html
.. _Quiz on This Chapter: http://math.hws.edu/javanotes/c8/quiz.html
.. _Next Chapter: http://math.hws.edu/javanotes/c8/../c9/index.html


