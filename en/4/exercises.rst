[ `Chapter Index`_ | `Main Index`_ ]





Programming Exercises for Chapter 4
-----------------------------------



T his page contains several exercises for Chapter 4 in `Introduction
to Programming Using Java`_. For each exercise, a link to a possible
solution is provided. Each solution includes a discussion of how a
programmer might approach the problem and interesting points raised by
the problem or its solution, as well as complete source code of the
solution.




Exercise 4.1:
~~~~~~~~~~~~~

To "capitalize" a string means to change the first letter of each word
in the string to upper case (if it is not already upper case). For
example, a capitalized version of "Now is the time to act!" is "Now Is
The Time To Act!". Write a subroutine namedprintCapitalized that will
print a capitalized version of a string to standard output. The string
to be printed should be a parameter to the subroutine. Test your
subroutine with a main() routine that gets a line of input from the
user and applies the subroutine to it.

Note that a letter is the first letter of a word if it is not
immediately preceded in the string by another letter. Recall that
there is a standardboolean-valued function Character.isLetter(char)
that can be used to test whether its parameter is a letter. There is
another standardchar-valued function, Character.toUpperCase(char),
that returns a capitalized version of the single character passed to
it as a parameter. That is, if the parameter is a letter, it returns
the upper-case version. If the parameter is not a letter, it just
returns a copy of the parameter.

`See the Solution`_




Exercise 4.2:
~~~~~~~~~~~~~

The hexadecimal digits are the ordinary, base-10 digits '0' through
'9' plus the letters 'A' through 'F'. In the hexadecimal system, these
digits represent the values 0 through 15, respectively. Write a
function named hexValue that uses aswitch statement to find the
hexadecimal value of a given character. The character is a parameter
to the function, and its hexadecimal value is the return value of the
function. You should count lower case letters 'a' through 'f' as
having the same value as the corresponding upper case letters. If the
parameter is not one of the legal hexadecimal digits, return -1 as the
value of the function.

A hexadecimal integer is a sequence of hexadecimal digits, such as
34A7, FF8, 174204, or FADE. If str is a string containing a
hexadecimal integer, then the corresponding base-10 integer can be
computed as follows:


::

    value = 0;
    for ( i = 0; i < str.length();  i++ )
       value = value*16 + hexValue( str.charAt(i) );


Of course, this is not valid if str contains any characters that are
not hexadecimal digits. Write a program that reads a string from the
user. If all the characters in the string are hexadecimal digits,
print out the corresponding base-10 value. If not, print out an error
message.

`See the Solution`_




Exercise 4.3:
~~~~~~~~~~~~~

Write a function that simulates rolling a pair of dice until the total
on the dice comes up to be a given number. The number that you are
rolling for is a parameter to the function. The number of times you
have to roll the dice is the return value of the function. The
parameter should be one of the possible totals: 2, 3, ..., 12. The
function should throw an IllegalArgumentException if this is not the
case. Use your function in a program that computes and prints the
number of rolls it takes to get snake eyes. (Snake eyes means that the
total showing on the dice is 2.)

`See the Solution`_




Exercise 4.4:
~~~~~~~~~~~~~

This exercise builds on `Exercise4.3`_. Every time you roll the dice
repeatedly, trying to get a given total, the number of rolls it takes
can be different. The question naturally arises, what's the average
number of rolls to get a given total? Write a function that performs
the experiment of rolling to get a given total 10000 times. The
desired total is a parameter to the subroutine. The average number of
rolls is the return value. Each individual experiment should be done
by calling the function you wrote for`Exercise4.3`_. Now, write a main
program that will call your function once for each of the possible
totals (2, 3, ..., 12). It should make a table of the results,
something like:


::

    Total On Dice     Average Number of Rolls
    -------------     -----------------------
           2               35.8382
           3               18.0607
           .                .
           .                .


`See the Solution`_




Exercise 4.5:
~~~~~~~~~~~~~

The sample program`RandomMosaicWalk.java`_ from`Section4.6`_ shows a
"disturbance" that wanders around a grid of colored squares. When the
disturbance visits a square, the color of that square is changed. The
applet at the bottom of `Section4.7`_ shows a variation on this idea.
In this applet, all the squares start out with the default color,
black. Every time the disturbance visits a square, a small amount is
added to the green component of the color of that square. Write a
subroutine that will add 25 to the green component of one of the
squares in the mosaic. The row and column numbers of the square should
be given as parameters to the subroutine. Recall that you can discover
the current green component of the square in row r and column c with
the function callMosaic.getGreen(r,c). Use your subroutine as a
substitute for thechangeToRandomColor() subroutine in the program
`RandomMosaicWalk2.java`_. (This is the improved version of the
program from `Section4.7`_ that uses named constants for the number of
rows, number of columns, and square size.) Set the number of rows and
the number of columns to 80. Set the square size to 5.

Don't forget that you will need `Mosaic.java`_ and
`MosaicCanvas.java`_ to compile and run your program, since they
define non-standard classes that are required by the program.

`See the Solution`_




Exercise 4.6:
~~~~~~~~~~~~~

For this exercise, you will do something even more interesting with
the Mosaic class that was discussed in `Section4.6`_. (Again, don't
forget that you will need `Mosaic.java`_ and `MosaicCanvas.java`_.)

The program that you write for this exercise should start by filling a
mosaic with random colors. Then repeat the following until the user
closes the mosaic window: Select one of the rectangles in the mosaic
at random. Then select one of the neighboring rectangles -- above it,
below it, to the left of it, or to the right of it. Copy the color of
the originally selected rectangle to the selected neighbor, so that
the two rectangles now have the same color.

As this process is repeated over and over, it becomes more and more
likely that neighboring squares will have the same color. The result
is to build up larger color patches. On the other hand, once the last
square of a given color disappears, there is no way for that color to
ever reappear (extinction is forever!). If you let the program run
long enough, eventually the entire mosaic will be one uniform color.

Here is an applet version of the program. In the applet version -- but
not in the version that you will write -- you can double-click the
applet to reset all the rectangles to random colors.



After doing each color conversion, your program should insert a very
short delay. You can try running the program without the delay; it
will work, but it might be a little glitchy.

`See the Solution`_




Exercise 4.7:
~~~~~~~~~~~~~

This is another Mosaic exercise, (using `Mosaic.java`_ and
`MosaicCanvas.java`_ as discussed in `Section4.6`_). While the program
does not do anything particularly interesting, it's interesting as a
programming problem. The program will do the same thing as the
following applet:



The program will show a square that grows from the center of the
applet to the edges. As it grows, the part added around the edges gets
brighter, so that in the end the color of the square fades from white
at the edges to dark gray at the center.

The whole picture is made up of the little rectangles of a mosaic. You
should first write a subroutine that draws the outline of a rectangle
on a Mosaic window. More specifically, write a subroutine named
outlineRectangle such that the subroutine call statement


::

    outlineRectangle(top,left,height,width,r,g,b);


will call Mosaic.setColor(row,col,r,g,b) for each little square that
lies on the outline of a rectangle. The topmost row of the rectangle
is specified by top. The number of rows in the rectangle is specified
byheight (so the bottommost row is top+height-1). The leftmost column
of the rectangle is specified by left. The number of columns in the
rectangle is specified by width (so the rightmost column
isleft+width-1.) For the specific program that you are writing, the
width and the height of the rectangle will always be equal, but it's
nice to have the more general-purpose routine.

The animation loops through the same sequence of steps over and over.
In each step, the outline of a rectangle is drawn in gray (that is,
with all three color components having the same value). There is a
pause of 200 milliseconds so the user can see the picture. Then the
variables giving the top row, left column, size, and color level of
the rectangle are adjusted to get ready for the next step. In my
applet, the color level starts at 50 and increases by 10 after each
step. When the rectangle gets to the outer edge of the applet, the
loop ends, and the picture is erased by filling the mosaic with black.
Then, after a delay of one second, the animation starts again at the
beginning of the loop. You might want to make an additional subroutine
to do one loop through the steps of the basic animation.

The main() routine simply opens a Mosaic window and then does the
animation loop over and over until the user closes the window. There
is a 1000 millisecond delay between one animation loop and the next.
Use a Mosaic window that has 41 rows and 41 columns. (I advise you
**not** to used named constants for the numbers of rows and columns,
since the problem is complicated enough already.)

`See the Solution`_



[ `Chapter Index`_ | `Main Index`_ ]

.. _See the Solution: http://math.hws.edu/javanotes/c4/ex4-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c4/ex6-ans.html
.. _Mosaic.java: http://math.hws.edu/javanotes/c4/../source/Mosaic.java
.. _RandomMosaicWalk.java: http://math.hws.edu/javanotes/c4/../source/RandomMosaicWalk.java
.. _See the Solution: http://math.hws.edu/javanotes/c4/ex7-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c4/ex5-ans.html
.. _4.3: http://math.hws.edu/javanotes/c4/../c4/ex3-ans.html
.. _Chapter Index: http://math.hws.edu/javanotes/c4/index.html
.. _See the Solution: http://math.hws.edu/javanotes/c4/ex1-ans.html
.. _4.6: http://math.hws.edu/javanotes/c4/../c4/s6.html
.. _MosaicCanvas.java: http://math.hws.edu/javanotes/c4/../source/MosaicCanvas.java
.. _RandomMosaicWalk2.java: http://math.hws.edu/javanotes/c4/../source/RandomMosaicWalk2.java
.. _Main Index: http://math.hws.edu/javanotes/c4/../index.html
.. _4.7: http://math.hws.edu/javanotes/c4/../c4/s7.html
.. _See the Solution: http://math.hws.edu/javanotes/c4/ex3-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c4/ex2-ans.html


