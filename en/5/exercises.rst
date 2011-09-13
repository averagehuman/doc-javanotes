[ `Chapter Index`_ | `Main Index`_ ]





Programming Exercises for Chapter 5
-----------------------------------



T his page contains several exercises for Chapter 5 in `Introduction
to Programming Using Java`_. For each exercise, a link to a possible
solution is provided. Each solution includes a discussion of how a
programmer might approach the problem and interesting points raised by
the problem or its solution, as well as complete source code of the
solution.




Exercise 5.1:
~~~~~~~~~~~~~

In all versions of thePairOfDice class in :doc:`Section 5.2</5/s2>`, the instance
variables die1 and die2 are declared to be public. They really should
be private, so that they would be protected from being changed from
outside the class. Write another version of the PairOfDice class in
which the instance variables die1 and die2 areprivate. Your class will
need "getter" methods that can be used to find out the values of die1
and die2. (The idea is to protect their values from being changed from
outside the class, but still to allow the values to be read.) Include
other improvements in the class, if you can think of any. Test your
class with a short program that counts how many times a pair of dice
is rolled, before the total of the two dice is equal to two.

`See the Solution`_




Exercise 5.2:
~~~~~~~~~~~~~

A common programming task is computing statistics of a set of numbers.
(A statistic is a number that summarizes some property of a set of
data.) Common statistics include the mean (also known as the average)
and the standard deviation (which tells how spread out the data are
from the mean). I have written a little class calledStatCalc that can
be used to compute these statistics, as well as the sum of the items
in the dataset and the number of items in the dataset. You can read
the source code for this class in the file `StatCalc.java`_. If calc
is a variable of type StatCalc, then the following methods are
defined:


+ calc.enter(item) whereitem is a number, adds the item to the
  dataset.
+ calc.getCount() is a function that returns the number of items that
  have been added to the dataset.
+ calc.getSum() is a function that returns the sum of all the items
  that have been added to the dataset.
+ calc.getMean() is a function that returns the average of all the
  items.
+ calc.getStandardDeviation() is a function that returns the standard
  deviation of the items.


Typically, all the data are added one after the other by calling
theenter() method over and over, as the data become available. After
all the data have been entered, any of the other methods can be called
to get statistical information about the data. The methods getMean()
andgetStandardDeviation() should only be called if the number of items
is greater than zero.

Modify the current source code, `StatCalc.java`_, to add instance
methods getMax() and getMin(). The getMax() method should return the
largest of all the items that have been added to the dataset, and
getMin() should return the smallest. You will need to add two new
instance variables to keep track of the largest and smallest items
that have been seen so far.

Test your new class by using it in a program to compute statistics for
a set of non-zero numbers entered by the user. Start by creating an
object of typeStatCalc:


.. code-block:: java

    StatCalc  calc;   // Object to be used to process the data.
    calc = new StatCalc();


Read numbers from the user and add them to the dataset. Use 0 as a
sentinel value (that is, stop reading numbers when the user enters 0).
After all the user's non-zero numbers have been entered, print out
each of the six statistics that are available from calc.

`See the Solution`_




Exercise 5.3:
~~~~~~~~~~~~~

This problem uses thePairOfDice class from `Exercise5.1`_ and the
StatCalc class from `Exercise5.2`_.

The program in `Exercise4.4`_ performs the experiment of counting how
many times a pair of dice is rolled before a given total comes up. It
repeats this experiment 10000 times and then reports the average
number of rolls. It does this whole process for each possible total
(2, 3, ..., 12).

Redo that exercise. But instead of just reporting the average number
of rolls, you should also report the standard deviation and the
maximum number of rolls. Use a PairOfDice object to represent the
dice. Use aStatCalc object to compute the statistics. (You'll need a
newStatCalc object for each possible total, 2, 3, ..., 12. You can use
a new pair of dice if you want, but it's not necessary.)

`See the Solution`_




Exercise 5.4:
~~~~~~~~~~~~~

The BlackjackHand class from `Subsection5.5.1`_ is an extension of
theHand class from :doc:`Section 5.4</5/s4>`. The instance methods in the Hand
class are discussed in that section. In addition to those methods,
BlackjackHand includes an instance method,getBlackjackValue(), that
returns the value of the hand for the game of Blackjack. For this
exercise, you will also need the Deck andCard classes from
:doc:`Section 5.4</5/s4>`.

A Blackjack hand typically contains from two to six cards. Write a
program to test the BlackjackHand class. You should create
aBlackjackHand object and a Deck object. Pick a random number between
2 and 6. Deal that many cards from the deck and add them to the hand.
Print out all the cards in the hand, and then print out the value
computed for the hand by getBlackjackValue(). Repeat this as long as
the user wants to continue.

In addition to `TextIO.java`_, your program will depend on
`Card.java`_, `Deck.java`_, `Hand.java`_, and `BlackjackHand.java`_.

`See the Solution`_




Exercise 5.5:
~~~~~~~~~~~~~

Write a program that lets the user play Blackjack. The game will be a
simplified version of Blackjack as it is played in a casino. The
computer will act as the dealer. As in the previous exercise, your
program will need the classes defined in `Card.java`_, `Deck.java`_,
`Hand.java`_, and `BlackjackHand.java`_. (This is the longest and most
complex program that has come up so far in the exercises.)

You should first write a subroutine in which the user plays one game.
The subroutine should return a boolean value to indicate whether the
user wins the game or not. Return true if the user wins, false if the
dealer wins. The program needs an object of class Deck and two objects
of type BlackjackHand, one for the dealer and one for the user. The
general object in Blackjack is to get a hand of cards whose value is
as close to 21 as possible, without going over. The game goes like
this.


+ First, two cards are dealt into each player's hand. If the dealer's
  hand has a value of 21 at this point, then the dealer wins. Otherwise,
  if the user has 21, then the user wins. (This is called a
  "Blackjack".) Note that the dealer wins on a tie, so if both players
  have Blackjack, then the dealer wins.
+ Now, if the game has not ended, the user gets a chance to add some
  cards to her hand. In this phase, the user sees her own cards and sees
  **one** of the dealer's two cards. (In a casino, the dealer deals
  himself one card face up and one card face down. All the user's cards
  are dealt face up.) The user makes a decision whether to "Hit", which
  means to add another card to her hand, or to "Stand", which means to
  stop taking cards.
+ If the user Hits, there is a possibility that the user will go over
  21. In that case, the game is over and the user loses. If not, then
  the process continues. The user gets to decide again whether to Hit or
  Stand.
+ If the user Stands, the game will end, but first the dealer gets a
  chance to draw cards. The dealer only follows rules, without any
  choice. The rule is that as long as the value of the dealer's hand is
  less than or equal to 16, the dealer Hits (that is, takes another
  card). The user should see all the dealer's cards at this point. Now,
  the winner can be determined: If the dealer has gone over 21, the user
  wins. Otherwise, if the dealer's total is greater than or equal to the
  user's total, then the dealer wins. Otherwise, the user wins.


Two notes on programming: At any point in the subroutine, as soon as
you know who the winner is, you can say "return true;" or "return
false;" to end the subroutine and return to the main program. To avoid
having an overabundance of variables in your subroutine, remember that
a function call such as userHand.getBlackjackValue() can be used
anywhere that a number could be used, including in an output statement
or in the condition of an if statement.

Write a main program that lets the user play several games of
Blackjack. To make things interesting, give the user 100 dollars, and
let the user make bets on the game. If the user loses, subtract the
bet from the user's money. If the user wins, add an amount equal to
the bet to the user's money. End the program when the user wants to
quit or when she runs out of money.

Here is an applet that simulates the program you are supposed to
write. It would probably be worthwhile to play it for a while to see
how it works.



`See the Solution`_




Exercise 5.6:
~~~~~~~~~~~~~

`Subsection5.7.6`_ discusses the possibility of representing the suits
and values of playing cards as enumerated types. Rewrite the Card
class from `Subsection5.4.2`_ to use these enumerated types. Test your
class with a program that prints out the 52 possible playing cards.
Suggestions: You can modify the source code file`Card.java`_, but you
should leave out support for Jokers. In your main program, use nested
for loops to generated cards of all possible suits and values; the for
loops will be "for-each" loops of the type discussed in
`Subsection3.4.4`_. It would be nice to add a toString() method to the
Suit class from `Subsection5.7.6`_, so that a suit prints out as
"Spades" or "Hearts" instead of "SPADES" or "HEARTS".

`See the Solution`_



[ `Chapter Index`_ | `Main Index`_ ]

.. _See the Solution: http://math.hws.edu/javanotes/c5/ex2-ans.html
.. _Chapter Index: http://math.hws.edu/javanotes/c5/index.html
.. _5.1: http://math.hws.edu/javanotes/c5/../c5/ex1-ans.html
.. _5.4.2: http://math.hws.edu/javanotes/c5/../c5/s4.html#OOP.4.2
.. _TextIO.java: http://math.hws.edu/javanotes/c5/../source/TextIO.java
.. _Hand.java: http://math.hws.edu/javanotes/c5/../source/Hand.java
.. _5.7.6: http://math.hws.edu/javanotes/c5/../c5/s7.html#OOP.7.6
.. _Deck.java: http://math.hws.edu/javanotes/c5/../source/Deck.java
.. _5.2: http://math.hws.edu/javanotes/c5/../c5/s2.html
.. _Main Index: http://math.hws.edu/javanotes/c5/../index.html
.. _5.2: http://math.hws.edu/javanotes/c5/../c5/ex2-ans.html
.. _BlackjackHand.java: http://math.hws.edu/javanotes/c5/../source/BlackjackHand.java
.. _5.4: http://math.hws.edu/javanotes/c5/../c5/s4.html
.. _3.4.4: http://math.hws.edu/javanotes/c5/../c3/s4.html#control.4.4
.. _5.5.1: http://math.hws.edu/javanotes/c5/../c5/s5.html#OOP.5.1
.. _Card.java: http://math.hws.edu/javanotes/c5/../source/Card.java
.. _4.4: http://math.hws.edu/javanotes/c5/../c4/ex4-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c5/ex3-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c5/ex5-ans.html
.. _StatCalc.java: http://math.hws.edu/javanotes/c5/../source/StatCalc.java
.. _See the Solution: http://math.hws.edu/javanotes/c5/ex1-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c5/ex6-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c5/ex4-ans.html


