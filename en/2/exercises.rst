[ `Chapter Index`_ | `Main Index`_ ]





Programming Exercises for Chapter 2
-----------------------------------



T his page contains several exercises for Chapter 2 in `Introduction
to Programming Using Java`_. For each exercise, a link to a possible
solution is provided. Each solution includes a discussion of how a
programmer might approach the problem and interesting points raised by
the problem or its solution, as well as complete source code of the
solution.




Exercise 2.1:
~~~~~~~~~~~~~

Write a program that will print your initials to standard output in
letters that are nine lines tall. Each big letter should be made up of
a bunch of *'s. For example, if your initials were "DJE", then the
output would look something like:


.. code-block:: java

    ******           *************        **********
    **    **                **            **
    **     **               **            **
    **      **              **            **
    **      **              **            ********
    **      **       **     **            **
    **     **         **    **            **
    **    **           **  **             **
    *****               ****              ********** 


`See the Solution`_




Exercise 2.2:
~~~~~~~~~~~~~

Write a program that simulates rolling a pair of dice. You can
simulate rolling one die by choosing one of the integers 1, 2, 3, 4,
5, or 6 at random. The number you pick represents the number on the
die after it is rolled. As pointed out in :doc:`Section 2.5</2/s5>`, The
expression


.. code-block:: java

    (int)(Math.random()*6) + 1


does the computation you need to select a random integer between 1 and
6. You can assign this value to a variable to represent one of the
dice that are being rolled. Do this twice and add the results together
to get the total roll. Your program should report the number showing
on each die as well as the total roll. For example:


.. code-block:: java

    The first die comes up 3
    The second die comes up 5
    Your total roll is 8


`See the Solution`_




Exercise 2.3:
~~~~~~~~~~~~~

Write a program that asks the user's name, and then greets the user by
name. Before outputting the user's name, convert it to upper case
letters. For example, if the user's name is Fred, then the program
should respond "Hello, FRED, nice to meet you!".

`See the Solution`_




Exercise 2.4:
~~~~~~~~~~~~~

Write a program that helps the user count his change. The program
should ask how many quarters the user has, then how many dimes, then
how many nickels, then how many pennies. Then the program should tell
the user how much money he has, expressed in dollars.

`See the Solution`_




Exercise 2.5:
~~~~~~~~~~~~~

If you have N eggs, then you have N/12 dozen eggs, with N%12 eggs left
over. (This is essentially the definition of the / and % operators for
integers.) Write a program that asks the user how many eggs she has
and then tells the user how many dozen eggs she has and how many extra
eggs are left over.

A gross of eggs is equal to 144 eggs. Extend your program so that it
will tell the user how many gross, how many dozen, and how many left
over eggs she has. For example, if the user says that she has 1342
eggs, then your program would respond with


.. code-block:: java

    Your number of eggs is 9 gross, 3 dozen, and 10


since 1342 is equal to 9*144 + 3*12 + 10.

`See the Solution`_




Exercise 2.6:
~~~~~~~~~~~~~

Suppose that a file named "testdata.txt" contains the following
information: The first line of the file is the name of a student. Each
of the next three lines contains an integer. The integers are the
student's scores on three exams. Write a program that will read the
information in the file and display (on standard output) a message the
contains the name of the student and the student's average grade on
the three exams. The average is obtained by adding up the individual
exam grades and then dividing by the number of exams.

`See the Solution`_



[ `Chapter Index`_ | `Main Index`_ ]

.. _2.5: http://math.hws.edu/javanotes/c2/../c2/s5.html
.. _See the Solution: http://math.hws.edu/javanotes/c2/ex3-ans.html
.. _Main Index: http://math.hws.edu/javanotes/c2/../index.html
.. _See the Solution: http://math.hws.edu/javanotes/c2/ex6-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c2/ex4-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c2/ex1-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c2/ex5-ans.html
.. _Chapter Index: http://math.hws.edu/javanotes/c2/index.html
.. _See the Solution: http://math.hws.edu/javanotes/c2/ex2-ans.html


