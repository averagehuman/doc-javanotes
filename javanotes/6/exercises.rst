[ `Chapter Index`_ | `Main Index`_ ]





Programming Exercises for Chapter 6
-----------------------------------



T his page contains several exercises for Chapter 6 in `Introduction
to Programming Using Java`_. For each exercise, a link to a possible
solution is provided. Each solution includes a discussion of how a
programmer might approach the problem and interesting points raised by
the problem or its solution, as well as complete source code of the
solution.




Exercise 6.1:
~~~~~~~~~~~~~

In the SimpleStamperPanel example from`Subsection6.4.2`_, a rectangle
or oval is drawn on the panel when the user clicks the mouse, except
that when the user shift-clicks, the panel is cleared instead. Modify
this class so that the modified version will continue to draw figures
as the user drags the mouse. That is, the mouse will leave a trail of
figures as the user drags. However, if the user shift-clicks, the
panel should simply be cleared and no figures should be drawn even if
the user drags the mouse after shift-clicking. Use your panel either
in an applet or in a stand-alone application (or both). Here is an
applet version of my solution:



The source code for the original panel class is
`SimpleStamperPanel.java`_. An applet that uses this class can be
found in `SimpleStamperApplet.java`_, and a main program that uses the
panel in a frame is in `SimpleStamper.java`_. See the discussion of
dragging in `Subsection6.4.4`_. (Note that in the original version, I
drew a black outline around each shape. In the modified version, I
decided that it would look better to draw a gray outline instead.)

If you want to make the problem a little more challenging, when
drawing shapes during a drag operation, make sure that the shapes that
are drawn are at least, say, 5 pixels apart. To implement this, you
have to keep track of the position of the last shape that was drawn.

`See the Solution`_




Exercise 6.2:
~~~~~~~~~~~~~

Write a panel that shows a small red square and a small blue square.
The user should be able to drag either square with the mouse. (You'll
need an instance variable to remember which square the user is
dragging.) The user can drag the square off the applet if she wants;
if she does this, there is no way to get it back. Use your panel in
either an applet or a stand-alone application. You can try the applet
version here:



Note that for this exercise, you should do all the drawing in
thepaintComponent() method (as indeed you should whenever possible).

`See the Solution`_




Exercise 6.3:
~~~~~~~~~~~~~

Write a panel that shows a pair of dice. When the user clicks on the
panel, the dice should be rolled (that is, the dice should be assigned
newly computed random values). Each die should be drawn as a square
showing from 1 to 6 dots. Since you have to draw two dice, its a good
idea to write a subroutine, "void drawDie(Graphics g, int val, int x,
int y)", to draw a die at the specified (x,y) coordinates. The second
parameter, val, specifies the value that is showing on the die. Assume
that the size of the panel is 100 by 100 pixels. Also write an applet
that uses your panel as its content pane. Here is a working version of
the applet:



`See the Solution`_




Exercise 6.4:
~~~~~~~~~~~~~

In `Exercise6.3`_, you wrote a pair-of-dice panel where the dice are
rolled when the user clicks on the panel. Now make a pair-of-dice
program in which the user rolls the dice by clicking a button. The
button should appear under the panel that shows the dice. Also make
the following change: When the dice are rolled, instead of just
showing the new value, show a short animation during which the values
on the dice are changed in every frame. The animation is supposed to
make the dice look more like they are actually rolling. Write your
program as a stand-alone application. Here is an applet version of the
program:



`See the Solution`_




Exercise 6.5:
~~~~~~~~~~~~~

In `Exercise3.6`_, you drew a checkerboard. For this exercise, write a
checkerboard applet where the user can select a square by clicking on
it. Highlight the selected square by drawing a colored border around
it. When the applet is first created, no square is selected. When the
user clicks on a square that is not currently selected, it becomes
selected (and the previously selected square, if any, is unselected).
If the user clicks the square that is selected, it becomes unselected.
Assume that the size of the applet is exactly 160 by 160 pixels, so
that each square on the checkerboard is 20 by 20 pixels. Here is a
working version of the applet:



`See the Solution`_




Exercise 6.6:
~~~~~~~~~~~~~

For this exercise, you should modify the SubKiller game from
`Subsection6.5.4`_. You can start with the existing source code, from
the file `SubKillerPanel.java`_. Modify the game so it keeps track of
the number of hits and misses and displays these quantities. That is,
every time the depth charge blows up the sub, the number of hits goes
up by one. Every time the depth charge falls off the bottom of the
screen without hitting the sub, the number of misses goes up by one.
There is room at the top of the panel to display these numbers. To do
this exercise, you only have to add a half-dozen lines to the source
code. But you have to figure out what they are and where to add them.
To do this, you'll have to read the source code closely enough to
understand how it works.

`See the Solution`_




Exercise 6.7:
~~~~~~~~~~~~~

`Exercise5.2`_ involved a class, `StatCalc.java`_, that could compute
some statistics of a set of numbers. Write a program that uses the
StatCalc class to compute and display statistics of numbers entered by
the user. The panel will have an instance variable of type StatCalc
that does the computations. The panel should include a JTextField
where the user enters a number. It should have four labels that
display four statistics for the numbers that have been entered: the
number of numbers, the sum, the mean, and the standard deviation.
Every time the user enters a new number, the statistics displayed on
the labels should change. The user enters a number by typing it into
theJTextField and pressing return. There should be a "Clear" button
that clears out all the data. This means creating a new StatCalc
object and resetting the displays on the labels. My panel also has an
"Enter" button that does the same thing as pressing the return key in
the JTextField. (Recall that a JTextField generates an ActionEvent
when the user presses return, so your panel should register itself to
listen forActionEvents from the JTextField.) Write your program as a
stand-alone application. Here is an applet version of my solution to
this problem:



`See the Solution`_




Exercise 6.8:
~~~~~~~~~~~~~

Write a panel with aJTextArea where the user can enter some text. The
panel should have a button. When the user clicks on the button, the
panel should count the number of lines in the user's input, the number
of words in the user's input, and the number of characters in the
user's input. This information should be displayed on three labels in
the panel. Recall that if textInput is aJTextArea, then you can get
the contents of the JTextArea by calling the function
textInput.getText(). This function returns aString containing all the
text from the text area. The number of characters is just the length
of this String. Lines in theString are separated by the new line
character, '\n', so the number of lines is just the number of new line
characters in the String, plus one. Words are a little harder to
count. `Exercise3.4`_ has some advice about finding the words in a
String. Essentially, you want to count the number of characters that
are first characters in words. Don't forget to put yourJTextArea in a
JScrollPane, and add the scroll pane to the container, not the text
area. Scrollbars should appear when the user types more text than will
fit in the available area. Here is an applet version of my solution:



`See the Solution`_




Exercise 6.9:
~~~~~~~~~~~~~

Write a GUI Blackjack program that lets the user play a game of
Blackjack, with the computer as the dealer. The applet should draw the
user's cards and the dealer's cards, just as was done for the
graphical HighLow card game in `Subsection6.7.6`_. You can use the
source code for that game, `HighLowGUI.java`_, for some ideas about
how to write your Blackjack game. The structures of the HighLow panel
and the Blackjack panel are very similar. You will certainly want to
use thedrawCard() method from the HighLow program.

You can find a description of the game of Blackjack in `Exercise5.5`_.
Add the following rule to that description: If a player takes five
cards without going over 21, that player wins immediately. This rule
is used in some casinos. For your program, it means that you only have
to allow room for five cards. You should assume that the panel is just
wide enough to show five cards, and that it is tall enough show the
user's hand and the dealer's hand.

Note that the design of a GUI Blackjack game is very different from
the design of the text-oriented program that you wrote for
`Exercise5.5`_. The user should play the game by clicking on "Hit" and
"Stand" buttons. There should be a "New Game" button that can be used
to start another game after one game ends. You have to decide what
happens when each of these buttons is pressed. You don't have much
chance of getting this right unless you think in terms of the states
that the game can be in and how the state can change.

Your program will need the classes defined in
`Card.java`_,`Hand.java`_,`Deck.java`_, and`BlackjackHand.java`_.

Here is an applet version of the program for you to try:



`See the Solution`_




Exercise 6.10:
~~~~~~~~~~~~~~

In the Blackjack game from `Exercise6.9`_, the user can click on the
"Hit", "Stand", and "NewGame" buttons even when it doesn't make sense
to do so. It would be better if the buttons were disabled at the
appropriate times. The "New Game" button should be disabled when there
is a game in progress. The "Hit" and "Stand" buttons should be
disabled when there is not a game in progress. The instance variable
gameInProgress tells whether or not a game is in progress, so you just
have to make sure that the buttons are properly enabled and disabled
whenever this variable changes value. I strongly advise writing a
subroutine that can be called whenever it is necessary to set the
value of the gameInProgress variable. Then the subroutine can take
responsibility for enabling and disabling the buttons. Recall that if
bttn is a variable of type JButton, thenbttn.setEnabled(false)
disables the button andbttn.setEnabled(true) enables the button.

As a second (and more difficult) improvement, make it possible for the
user to place bets on the Blackjack game. When the applet starts, give
the user $100. Add a JTextField to the strip of controls along the
bottom of the applet. The user can enter the bet in this JTextField.
When the game begins, check the amount of the bet. You should do this
when the game begins, not when it ends, because several errors can
occur: The contents of the JTextField might not be a legal number. The
bet that the user places might be more money than the user has, or it
might be <= 0. You should detect these errors and show an error
message instead of starting the game. The user's bet should be an
integral number of dollars.

It would be a good idea to make the JTextField uneditable while the
game is in progress. If betInput is the JTextField, you can make it
editable and uneditable by the user with the
commandsbetInput.setEditable(true) and betInput.setEditable(false).

In the paintComponent() method, you should include commands to display
the amount of money that the user has left.

There is one other thing to think about: Ideally, the applet should
not start a new game when it is first created. The user should have a
chance to set a bet amount before the game starts. So, in the
constructor for the drawing surface class, you should not call
doNewGame(). You might want to display a message such as "Welcome to
Blackjack" before the first game starts.

Here is an applet version of my program:



`See the Solution`_



[ `Chapter Index`_ | `Main Index`_ ]

.. _See the Solution: http://math.hws.edu/javanotes/c6/ex1-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c6/ex3-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c6/ex7-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c6/ex8-ans.html
.. _6.3: http://math.hws.edu/javanotes/c6/../c6/ex3-ans.html
.. _5.5: http://math.hws.edu/javanotes/c6/../c5/ex5-ans.html
.. _SubKillerPanel.java: http://math.hws.edu/javanotes/c6/../source/SubKillerPanel.java
.. _See the Solution: http://math.hws.edu/javanotes/c6/ex5-ans.html
.. _Main Index: http://math.hws.edu/javanotes/c6/../index.html
.. _Hand.java: http://math.hws.edu/javanotes/c6/../source/Hand.java
.. _See the Solution: http://math.hws.edu/javanotes/c6/ex6-ans.html
.. _3.4: http://math.hws.edu/javanotes/c6/../c3/ex4-ans.html
.. _6.4.4: http://math.hws.edu/javanotes/c6/../c6/s4.html#GUI1.4.4
.. _6.4.2: http://math.hws.edu/javanotes/c6/../c6/s4.html#GUI1.4.2
.. _Deck.java: http://math.hws.edu/javanotes/c6/../source/Deck.java
.. _6.5.4: http://math.hws.edu/javanotes/c6/../c6/s5.html#GUI1.5.4
.. _SimpleStamperApplet.java: http://math.hws.edu/javanotes/c6/../source/SimpleStamperApplet.java
.. _6.9: http://math.hws.edu/javanotes/c6/../c6/ex9-ans.html
.. _StatCalc.java: http://math.hws.edu/javanotes/c6/../source/StatCalc.java
.. _See the Solution: http://math.hws.edu/javanotes/c6/ex4-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c6/ex9-ans.html
.. _HighLowGUI.java: http://math.hws.edu/javanotes/c6/../source/HighLowGUI.java
.. _Chapter Index: http://math.hws.edu/javanotes/c6/index.html
.. _6.7.6: http://math.hws.edu/javanotes/c6/../c6/s7.html#GUI1.7.6
.. _See the Solution: http://math.hws.edu/javanotes/c6/ex10-ans.html
.. _SimpleStamperPanel.java: http://math.hws.edu/javanotes/c6/../source/SimpleStamperPanel.java
.. _3.6: http://math.hws.edu/javanotes/c6/../c3/ex6-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c6/ex2-ans.html
.. _BlackjackHand.java: http://math.hws.edu/javanotes/c6/../source/BlackjackHand.java
.. _SimpleStamper.java: http://math.hws.edu/javanotes/c6/../source/SimpleStamper.java
.. _5.2: http://math.hws.edu/javanotes/c6/../c5/ex2-ans.html
.. _Card.java: http://math.hws.edu/javanotes/c6/../source/Card.java


