[ `Quiz Answers`_ | `Chapter Index`_ | `Main Index`_ ]





Quiz on Chapter 5
-----------------

T his page contains questions on Chapter 5 of ` Introduction to
Programming Using Java `_. You should be able to answer these
questions after studying that chapter. Sample answers to these
questions can be found `here`_.
Question1:
Object-oriented programming uses classes and objects . What are
classes and what are objects? What is the relationship between classes
and objects?
Question2:
Explain carefully what null means in Java, and why this special value
is necessary.
Question3:
What is a constructor? What is the purpose of a constructor in a
class?
Question4:
Suppose thatKumquat is the name of a class and that fruit is a
variable of type Kumquat. What is the meaning of the statement "fruit
= new Kumquat();"? That is, what does the computer do when it executes
this statement? (Try to give a complete answer. The computer does
several things.)
Question5:
What is meant by the terms instance variable and instance method ?
Question6:
Explain what is meant by the terms subclass and superclass.
Question7:
Modify the following class so that the two instance variables are
private and there is a getter method and a setter method for each
instance variable:


.. code-block:: java

    public class Player {
       String name;
       int score;
    }

Question8:
Explain why the class Player that is defined in the previous question
has an instance method named toString(), even though no definition of
this method appears in the definition of the class.
Question9:
Explain the term polymorphism.
Question10:
Java uses "garbage collection" for memory management. Explain what is
meant here by garbage collection. What is the alternative to garbage
collection?
Question11:
For this problem, you should write a very simple but complete class.
The class represents a counter that counts 0, 1, 2, 3, 4,.... The name
of the class should be Counter. It has one private instance variable
representing the value of the counter. It has two instance methods:
increment() adds one to the counter value, and getValue() returns the
current counter value. Write a complete definition for the class,
Counter.
Question12:
This problem uses theCounter class from the previous question. The
following program segment is meant to simulate tossing a coin 100
times. It should use two Counter objects, headCount and tailCount, to
count the number of heads and the number of tails. Fill in the blanks
so that it will do so:


.. code-block:: java

    Counter headCount, tailCount;
    tailCount = new Counter();
    headCount = new Counter();
    for ( int flip = 0;  flip < 100;  flip++ ) {
       if (Math.random() < 0.5)    // There's a 50/50 chance that this is true.
       
           ______________________ ;   // Count a "head".
           
       else
       
           ______________________ ;   // Count a "tail".
    }
    
    System.out.println("There were " + ___________________ + " heads.");
    
    System.out.println("There were " + ___________________ + " tails.");




[ `Quiz Answers`_ | `Chapter Index`_ | `Main Index`_ ]

.. _Chapter Index: http://math.hws.edu/javanotes/c5/index.html
.. _Main Index: http://math.hws.edu/javanotes/c5/../index.html
.. _Quiz Answers: http://math.hws.edu/javanotes/c5/quiz_answers.html


