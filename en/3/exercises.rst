[ `Chapter Index`_ | `Main Index`_ ]





Programming Exercises for Chapter 3
-----------------------------------



T his page contains several exercises for Chapter 3 in `Introduction
to Programming Using Java`_. For each exercise, a link to a possible
solution is provided. Each solution includes a discussion of how a
programmer might approach the problem and interesting points raised by
the problem or its solution, as well as complete source code of the
solution.




Exercise 3.1:
~~~~~~~~~~~~~

How many times do you have to roll a pair of dice before they come up
snake eyes? You could do the experiment by rolling the dice by hand.
Write a computer program that simulates the experiment. The program
should report the number of rolls that it makes before the dice come
up snake eyes. (Note: "Snake eyes" means that both dice show a value
of 1.) `Exercise2.2`_ explained how to simulate rolling a pair of
dice.

`See the Solution`_




Exercise 3.2:
~~~~~~~~~~~~~

Which integer between 1 and 10000 has the largest number of divisors,
and how many divisors does it have? Write a program to find the
answers and print out the results. It is possible that several
integers in this range have the same, maximum number of divisors. Your
program only has to print out one of them. An example
in`Subsection3.4.2`_ discussed divisors. The source code for that
example is `CountDivisors.java`_.

You might need some hints about how to find a maximum value. The basic
idea is to go through all the integers, keeping track of the largest
number of divisors that you've seen so far . Also, keep track of the
integer that had that number of divisors.

`See the Solution`_




Exercise 3.3:
~~~~~~~~~~~~~

Write a program that will evaluate simple expressions such as 17 + 3
and 3.14159 * 4.7. The expressions are to be typed in by the user. The
input always consist of a number, followed by an operator, followed by
another number. The operators that are allowed are +, -, *, and /. You
can read the numbers with TextIO.getDouble() and the operator with
TextIO.getChar(). Your program should read an expression, print its
value, read another expression, print its value, and so on. The
program should end when the user enters 0 as the first number on the
line.

`See the Solution`_




Exercise 3.4:
~~~~~~~~~~~~~

Write a program that reads one line of input text and breaks it up
into words. The words should be output one per line. A word is defined
to be a sequence of letters. Any characters in the input that are not
letters should be discarded. For example, if the user inputs the line


::

    He said, "That's not a good idea."


then the output of the program should be


::

    He
    said
    That
    s
    not
    a
    good
    idea


An improved version of the program would list "that's" as a single
word. An apostrophe can be considered to be part of a word if there is
a letter on each side of the apostrophe.

To test whether a character is a letter, you might use (ch >= 'a'&& ch
<= 'z') || (ch >= 'A' && ch <= 'Z'). However, this only works in
English and similar languages. A better choice is to call the standard
function Character.isLetter(ch), which returns a boolean value of true
if ch is a letter and false if it is not. This works for any Unicode
character.

`See the Solution`_




Exercise 3.5:
~~~~~~~~~~~~~

Suppose that a file contains information about sales figures for a
company in various cities. Each line of the file contains a city name,
followed by a colon(:) followed by the data for that city. The data is
a number of type double. However, for some cities, no data was
available. In these lines, the data is replaced by a comment
explaining why the data is missing. For example, several lines from
the file might look like:


::

    San Francisco:  19887.32
    Chicago:  no report received
    New York: 298734.12


Write a program that will compute and print the total sales from all
the cities together. The program should also report the number of
cities for which data was not available. The name of the file is
"sales.dat".

To complete this program, you'll need one fact about file input with
TextIO that was not covered in `Subsection2.4.5`_. Since you don't
know in advance how many lines there are in the file, you need a way
to tell when you have gotten to the end of the file. When TextIO is
reading from a file, the function TextIO.eof() can be used to test for
end of file. This boolean-valued function returns true if the file has
been entirely read and returns false if there is more data to read in
the file. This means that you can read the lines of the file in a loop
while(TextIO.eof()==false).... The loop will end when all the lines of
the file have been read.

Suggestion: For each line, read and ignore characters up to the colon.
Then read the rest of the line into a variable of type String. Try to
convert the string into a number, and use try..catch to test whether
the conversion succeeds.

`See the Solution`_




Exercise 3.6:
~~~~~~~~~~~~~

Write an applet that draws a checkerboard. Write your solution as a
subclass ofAnimationBase, even though all the frames that it draws
will be the same. Assume that the size of the applet is 160 by 160
pixels. Each square in the checkerboard is 20 by 20 pixels. The
checkerboard contains 8 rows of squares and 8 columns. The squares are
red and black. Here is a tricky way to determine whether a given
square should be red or black: If the row number and the column number
are either both even or both odd, then the square is red. Otherwise,
it is black. Note that a square is just a rectangle in which the
height is equal to the width, so you can use the
subroutineg.fillRect() to draw the squares. Here is an image of the
checkerboard:



(To run an applet, you need a Web page to display it. A very simple
page will do. Assume that your applet class is called Checkerboard, so
that when you compile it you get a class file named Checkerboard.class
Make a file that contains only the lines:


::

    <applet code="Checkerboard.class" width=160 height=160>
    </applet>


Call this file Checkerboard.html. This is the source code for a simple
Web page that shows nothing but your applet. The compiled class
file,Checkerboard.class, must be in the same directory with the Web-
page file, Checkerboard.html. Furthermore, since your program depends
on the non-standard class AnimationBase, you also have to make that
class available to your program. To do this, you should compile the
source code, `AnimationBase.java`_. The result will be **two** class
files, AnimationBase.class andAnimationBase$1.class. Place **both** of
these class files in the same directory, together with
Checkerboard.html and Checherboard.class. Now, to run the applet,
simply open Checkerboard.html in a web browser. Alternatively, on the
command line, you can use the command


::

    appletviewer Checkerboard.html


The appletviewer command, like java and javac is part of a standard
installation of the JDK.

If you are using the Eclipse Integrated Development Environment, you
should add`AnimationBase.java`_ to the project where you want to
writeCheckerboard.java. You can then simply right-click the name of
the source code file in the Package Explorer. In the pop-up menu, go
to "RunAs" then to "Java Applet". This will open the window in which
the applet appears. The default size for the window is bigger than
160-by-160, so the drawing of the checkerboard will not fill the
entire window.)

`See the Solution`_




Exercise 3.7:
~~~~~~~~~~~~~

Write an animation applet that shows a checkerboard pattern in which
the even numbered rows slide to the left while the odd numbered rows
slide to the right. You can assume that the applet is 160 by 160
pixels. Each row can be offset towards the left or right from its
usual position by the amount getFrameNumber()%40. Hints: Anything you
draw outside the boundaries of the applet will be invisible, so you
can draw more than 8 squares in a row. You can use negative values of
x ing.fillRect(x,y,w,h). Here is a working solution to this exercise:



As with `Exercise3.6`_, you can write your class as a subclass
ofAnimationBase. Compile and run the program in the same way, as
described in that exercise. Assuming that the name of your class is
SlidingCheckerboard, then the source file for the Web page this time
should contain the lines:


::

    <applet code="SlidingCheckerboard.class" width=160 height=160>
    </applet>


`See the Solution`_



[ `Chapter Index`_ | `Main Index`_ ]

.. _3.6: http://math.hws.edu/javanotes/c3/../c3/ex6-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c3/ex7-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c3/ex5-ans.html
.. _Chapter Index: http://math.hws.edu/javanotes/c3/index.html
.. _See the Solution: http://math.hws.edu/javanotes/c3/ex3-ans.html
.. _CountDivisors.java: http://math.hws.edu/javanotes/c3/../source/CountDivisors.java
.. _See the Solution: http://math.hws.edu/javanotes/c3/ex4-ans.html
.. _2.4.5: http://math.hws.edu/javanotes/c3/../c2/s4.html#basics.4.5
.. _Main Index: http://math.hws.edu/javanotes/c3/../index.html
.. _AnimationBase.java: http://math.hws.edu/javanotes/c3/../source/AnimationBase.java
.. _See the Solution: http://math.hws.edu/javanotes/c3/ex2-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c3/ex6-ans.html
.. _2.2: http://math.hws.edu/javanotes/c3/../c2/ex2-ans.html
.. _3.4.2: http://math.hws.edu/javanotes/c3/../c3/s4.html#control.4.2
.. _See the Solution: http://math.hws.edu/javanotes/c3/ex1-ans.html


