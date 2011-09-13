[ `Chapter Index`_ | `Main Index`_ ]





Programming Exercises for Chapter 7
-----------------------------------



T his page contains several exercises for Chapter 7 in `Introduction
to Programming Using Java`_. For each exercise, a link to a possible
solution is provided. Each solution includes a discussion of how a
programmer might approach the problem and interesting points raised by
the problem or its solution, as well as complete source code of the
solution.




Exercise 7.1:
~~~~~~~~~~~~~

An example in `Subsection7.2.4`_ tried to answer the question, How
many random people do you have to select before you find a duplicate
birthday? The source code for that program can be found in the
file`BirthdayProblemDemo.java`_. Here are some related questions:


+ How many random people do you have to select before you find
  **three** people who share the same birthday? (That is, all three
  people were born on the same day in the same month, but not
  necessarily in the same year.)
+ Suppose you choose 365 people at random. How many different
  birthdays will they have? (The number could theoretically be anywhere
  from 1 to 365).
+ How many different people do you have to check before you've found
  at least one person with a birthday on each of the 365 days of the
  year?


Write **three** programs to answer these questions. Each of your
programs should simulate choosing people at random and checking their
birthdays. (In each case, ignore the possibility of leap years.)

`See the Solution`_




Exercise 7.2:
~~~~~~~~~~~~~

Write a program that will read a sequence of positive real numbers
entered by the user and will print the same numbers in sorted order
from smallest to largest. The user will input a zero to mark the end
of the input. Assume that at most 100 positive numbers will be
entered.

`See the Solution`_




Exercise 7.3:
~~~~~~~~~~~~~

A polygon is a geometric figure made up of a sequence of connected
line segments. The points where the line segments meet are called
thevertices of the polygon. The Graphics class includes commands for
drawing and filling polygons. For these commands, the coordinates of
the vertices of the polygon are stored in arrays. Ifg is a variable of
type Graphics then


+ g.drawPolygon(xCoords, yCoords, pointCt) will draw the outline of
  the polygon with vertices at the points(xCoords[0],yCoords[0]),
  (xCoords[1],yCoords[1]), ...,(xCoords[pointCt-1],yCoords[pointCt-1]).
  The third parameter,pointCt, is an int that specifies the number of
  vertices of the polygon. Its value should be 3 or greater. The first
  two parameters are arrays of type int[]. Note that the polygon
  automatically includes a line from the last point,
  (xCoords[pointCt-1],yCoords[pointCt-1]), back to the starting point
  (xCoords[0],yCoords[0]).
+ g.fillPolygon(xCoords, yCoords, pointCt) fills the interior of the
  polygon with the current drawing color. The parameters have the same
  meaning as in the drawPolygon() method. Note that it is OK for the
  sides of the polygon to cross each other, but the interior of a
  polygon with self-intersections might not be exactly what you expect.


Write a panel class that lets the user draw polygons, and use your
panel as the content pane in an applet (or standalone application). As
the user clicks a sequence of points, count them and store their x-
and y-coordinates in two arrays. These points will be the vertices of
the polygon. Also, draw a line between each consecutive pair of points
to give the user some visual feedback. When the user clicks near the
starting point, draw the complete polygon. Draw it with a red interior
and a black border. The user should then be able to start drawing a
new polygon. When the user shift-clicks on the applet, clear it.

For this exercise, there is no need to store information about the
contents of the applet. Do the drawing directly in the mousePressed()
routine, and use the getGraphics() method to get a Graphics object
that you can use to draw the line. (Remember, though, that this is
considered to be bad style.) You will not need a paintComponent()
method, since the default action of filling the panel with its
background color is good enough.

You can try my solution here. Note that as the user is drawing the
polygon, lines are drawn between the points that the user clicks.
Click within two pixels of the starting point to see a filled polygon.



`See the Solution`_




Exercise 7.4:
~~~~~~~~~~~~~

For this problem, you will need to use an array of objects. The
objects belong to the classMovingBall, which I have already written.
You can find the source code for this class in the file
`MovingBall.java`_. A MovingBall represents a circle that has an
associated color, radius, direction, and speed. It is restricted to
moving inside some rectangle in the (x,y) plane. It will "bounce back"
when it hits one of the sides of this rectangle. AMovingBall does not
actually move by itself. It's just a collection of data. You have to
call instance methods to tell it to update its position and to draw
itself. The constructor for the MovingBall class takes the form


.. code-block:: java

    new MovingBall(xmin, xmax, ymin, ymax)


where the parameters are integers that specify the limits on the x and
y coordinates of the ball. (This sets the rectangle inside which the
ball will stay.) In this exercise, you will want balls to bounce off
the sides of the applet, so you will create them with the constructor
call


.. code-block:: java

    new MovingBall(0, getWidth(), 0, getHeight())


The constructor creates a ball that initially is colored red, has a
radius of 5 pixels, is located at the center of its range, has a
random speed between 4 and 12, and is headed in a random direction.
There is one **problem** here: You can't use this constructor until
the width and height of the component are known. It would be OK to use
it in the init() method of an applet, but not in the constructor of an
applet or panel class. If you are using a panel class to display the
ball, one slightly messy solution is to create the MovingBall objects
in the panel's paintComponent() method the first time that method is
called. You can be sure that the size of the panel has been determined
beforepaintComponent() is called. This is what I did in my own
solution to this exercise.

If ball is a variable of typeMovingBall, then the following methods
are available:


+ ball.draw(g) -- draw the ball in a graphics context. The parameter,
  g, must be of type Graphics. (The drawing color in g will be changed
  to the color of the ball.)
+ ball.travel() -- change the(x,y)-coordinates of the ball by an
  amount equal to its speed. The ball has a certain direction of motion,
  and the ball is moved in that direction. Ordinarily, you will call
  this once for each frame of an animation, so the speed is given in
  terms of "pixels per frame". Calling this routine does not move the
  ball on the screen. It just changes the values of some instance
  variables in the object. The next time the object's draw() method is
  called, the ball will be drawn in the new position.
+ ball.headTowards(x,y) -- change the direction of motion of the ball
  so that it is headed towards the point(x,y). This does not affect the
  speed.


These are the methods that you will need for this exercise. There are
also methods for setting various properties of the ball, such as
ball.setColor(color) for changing the color andball.setRadius(radius)
for changing its size. See the source code for more information. A
nice variation on the exercise would be to use random colors and sizes
for the balls.

For this exercise, you should create an applet that shows an animation
of balls bouncing around on a black background. Use a Timer to drive
the animation. (See `Subsection6.5.1`_.) Use an array of type
MovingBall[] to hold the data for the balls. In addition, your program
should listen for mouse and mouse motion events. When the user presses
the mouse or drags the mouse, call each of the ball's headTowards()
methods to make the balls head towards the mouse's location. My
solution uses 50 balls and a time delay of 50 milliseconds for the
timer.

Here is my solution. Try clicking and dragging on the applet:



`See the Solution`_




Exercise 7.5:
~~~~~~~~~~~~~

The sample program `RandomArtPanel.java`_ from`Subsection6.5.1`_ shows
a different random "artwork" every four seconds. There are three types
of "art", one made from lines, one from circles, and one from filled
squares. However, the program does not save the data for the picture
that is shown on the screen. As a result, the picture cannot be
redrawn when necessary. In fact, every time paintComponent() is
called, a new picture is drawn.

Write a new version of `RandomArtPanel.java`_ that saves the data
needed to redraw its pictures. The paintComponent() method should
simply use the data to draw the picture. New data should be recomputed
only every four seconds, in response to an event from the timer that
drives the program.

To make this interesting, write a separate class for each of the three
different types of art. Also write an abstract class to serve as the
common base class for the three classes. Since all three types of art
use a random gray background, the background color can be defined in
their superclass. The superclass also contains a draw() method that
draws the picture; this is an abstract method because its
implementation depends on the particular type of art that is being
drawn. The abstract class can be defined as:


.. code-block:: java

    
    private abstract class ArtData {
       Color backgroundColor;  // The background color for the art.
       ArtData() {  // Constructor sets background color to be a random gray.
          int x = (int)(256*Math.random());
          backgroundColor = new Color( x, x, x, );
       }
       abstract void draw(Graphics g);  // Draws this artwork.
    }


Each of the three subclasses of ArtData must define its own draw()
method. It must also define instance variables to hold the data
necessary to draw the picture. I suggest that you should create random
data for the picture in the constructor of the class, so that
constructing the object will automatically create the data for the
random artwork. (One problem with this is that you can't create the
data until you know the size of the panel, so you can't create an
artdata object in the constructor of the panel. One solution is to
create an artdata object at the beginning of the paintComponent()
method, if the object has not already been created.) In all three
subclasses, you will need to use several arrays to store the data.

The file `RandomArtPanel.java`_ only defines a panel class. A main
program that uses this panel can be found in `RandomArt.java`_, and an
applet that uses it can be found in `RandomArtApplet.java`_. You only
need to modify RandomArtPanel.

`See the Solution`_




Exercise 7.6:
~~~~~~~~~~~~~

Write a program that will read a text file selected by the user, and
will make an alphabetical list of all the different words in that
file. All words should be converted to lower case, and duplicates
should be eliminated from the list. The list should be written to an
output file selected by the user. As discussed in `Subsection2.4.5`_,
you can use TextIO to read and write files. Use a variable of type
ArrayList<String> to store the words. (See `Subsection7.3.4`_.) It is
not easy to separate a file into words as you are reading it. You can
use the following method:


.. code-block:: java

    /**
     * Read the next word from TextIO, if there is one.  First, skip past
     * any non-letters in the input.  If an end-of-file is encountered before 
     * a word is found, return null.  Otherwise, read and return the word.
     * A word is defined as a sequence of letters.  Also, a word can include
     * an apostrophe if the apostrophe is surrounded by letters on each side.
     * @return the next word from TextIO, or null if an end-of-file is 
     * encountered
     */
    private static String readNextWord() {
       char ch = TextIO.peek(); // Look at next character in input.
       while (ch != TextIO.EOF && ! Character.isLetter(ch)) {
              // Skip past non-letters.
          TextIO.getAnyChar();  // Read the character.
          ch = TextIO.peek();   // Look at the next character.
       }
       if (ch == TextIO.EOF) // Encountered end-of-file
          return null;
       // At this point, we know the next character is a letter, so read a word.
       String word = "";  // This will be the word that is read.
       while (true) {
          word += TextIO.getAnyChar();  // Append the letter onto word.
          ch = TextIO.peek();  // Look at next character.
          if ( ch == '\'' ) {
                // The next character is an apostrophe.  Read it, and
                // if the following character is a letter, add both the
                // apostrophe and the letter onto the word and continue
                // reading the word.  If the character after the apostrophe
                // is not a letter, the word is done, so break out of the loop.
             TextIO.getAnyChar();   // Read the apostrophe.
             ch = TextIO.peek();    // Look at char that follows apostrophe.
             if (Character.isLetter(ch)) {
                word += "\'" + TextIO.getAnyChar();
                ch = TextIO.peek();  // Look at next char.
             }
             else
                break;
          }
          if ( ! Character.isLetter(ch) ) {
                // If the next character is not a letter, the word is
                // finished, so break out of the loop.
             break;
          }
          // If we haven't broken out of the loop, next char is a letter.
       }
       return word;  // Return the word that has been read.
    }


Note that this method will return null when the file has been entirely
read. You can use this as a signal to stop processing the input file.

`See the Solution`_




Exercise 7.7:
~~~~~~~~~~~~~

The game of Go Moku (also known as Pente or Five Stones) is similar to
Tic-Tac-Toe, except that it played on a much larger board and the
object is to get five squares in a row rather than three. Players take
turns placing pieces on a board. A piece can be placed in any empty
square. The first player to get five pieces in a row -- horizontally,
vertically, or diagonally -- wins. If all squares are filled before
either player wins, then the game is a draw. Write a program that lets
two players play Go Moku against each other.

Your program will be simpler than the Checkers program
from`Subsection7.5.3`_. Play alternates strictly between the two
players, and there is no need to highlight the legal moves. You will
only need two classes, a short panel class to set up the interface and
a Board class to draw the board and do all the work of the game.
Nevertheless, you will probably want to look at the source code for
the checkers program,`Checkers.java`_, for ideas about the general
outline of the program.

The hardest part of the program is checking whether the move that a
player makes is a winning move. To do this, you have to look in each
of the four possible directions from the square where the user has
placed a piece. You have to count how many pieces that player has in a
row in that direction. If the number is five or more in any direction,
then that player wins. As a hint, here is part of the code from my
applet. This code counts the number of pieces that the user has in a
row in a specified direction. The direction is specified by two
integers, dirX and dirY. The values of these variables are 0, 1, or
-1, and at least one of them is non-zero. For example, to look in the
horizontal direction, dirX is 1 and dirY is 0.


.. code-block:: java

    int ct = 1;  // Number of pieces in a row belonging to the player.
    
    int r, c;    // A row and column to be examined
    
    r = row + dirX;  // Look at square in specified direction.
    c = col + dirY;
    while ( r >= 0 && r < 13 && c >= 0 && c < 13 
                                      && board[r][c] == player ) {
            // Square is on the board, and it 
            // contains one of the players's pieces.
       ct++;
       r += dirX;  // Go on to next square in this direction.
       c += dirY;
    }
    
    r = row - dirX;  // Now, look in the opposite direction.
    c = col - dirY;
    while ( r >= 0 && r < 13 && c >= 0 && c < 13 
                                     && board[r][c] == player ) {
       ct++;
       r -= dirX;   // Go on to next square in this direction.
       c -= dirY;
    }


Here is an applet version of my program It uses a 13-by-13 board. You
can do the same or use a normal 8-by-8 checkerboard.



`See the Solution`_



[ `Chapter Index`_ | `Main Index`_ ]

.. _Chapter Index: http://math.hws.edu/javanotes/c7/index.html
.. _7.3.4: http://math.hws.edu/javanotes/c7/../c7/s3.html#arrays.3.4
.. _Main Index: http://math.hws.edu/javanotes/c7/../index.html
.. _MovingBall.java: http://math.hws.edu/javanotes/c7/../source/MovingBall.java
.. _See the Solution: http://math.hws.edu/javanotes/c7/ex2-ans.html
.. _7.5.3: http://math.hws.edu/javanotes/c7/../c7/s5.html#arrays.5.3
.. _2.4.5: http://math.hws.edu/javanotes/c7/../c2/s4.html#basics.4.5
.. _See the Solution: http://math.hws.edu/javanotes/c7/ex4-ans.html
.. _7.2.4: http://math.hws.edu/javanotes/c7/../c7/s2.html#arrays.2.4
.. _RandomArtPanel.java: http://math.hws.edu/javanotes/c7/../source/RandomArtPanel.java
.. _Checkers.java: http://math.hws.edu/javanotes/c7/../source/Checkers.java
.. _RandomArtApplet.java: http://math.hws.edu/javanotes/c7/../source/RandomArtApplet.java
.. _See the Solution: http://math.hws.edu/javanotes/c7/ex1-ans.html
.. _6.5.1: http://math.hws.edu/javanotes/c7/../c6/s5.html#GUI1.5.1
.. _See the Solution: http://math.hws.edu/javanotes/c7/ex7-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c7/ex5-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c7/ex3-ans.html
.. _RandomArt.java: http://math.hws.edu/javanotes/c7/../source/RandomArt.java
.. _BirthdayProblemDemo.java: http://math.hws.edu/javanotes/c7/../source/BirthdayProblemDemo.java
.. _See the Solution: http://math.hws.edu/javanotes/c7/ex6-ans.html


