[ `Quiz Answers`_ | `Chapter Index`_ | `Main Index`_ ]





Quiz on Chapter 3
-----------------

T his page contains questions on Chapter 3 of ` Introduction to
Programming Using Java `_. You should be able to answer these
questions after studying that chapter. Sample answers to these
questions can be found `here`_.
Question1:
What is an algorithm ?
Question2:
Explain briefly what is meant by "pseudocode" and how is it useful in
the development of algorithms.
Question3:
What is a block statement? How are block statements used in Java
programs?
Question4:
What is the main difference between a while loop and a do..while loop?
Question5:
What does it mean to prime a loop?
Question6:
Explain what is meant by an animation and how a computer displays an
animation.
Question7:
Write a for loop that will print out all the multiples of 3 from 3 to
36, that is: 3 6 9 12 15 18 21 24 27 30 33 36.
Question8:
Fill in the followingmain() routine so that it will ask the user to
enter an integer, read the user's response, and tell the user whether
the number entered is even or odd. (You can use TextIO.getInt() to
read the integer. Recall that an integer n is even if n%2==0.)


::

    public static void main(String[] args) {
     
             // Fill in the body of this subroutine!
     
    }

Question9:
Suppose that s1 and s2 are variables of typeString, whose values are
expected to be string representations of values of type int. Write a
code segment that will compute and print the integer sum of those
values, or will print an error message if the values cannot
successfully be converted into integers. (Use a try..catch statement.)
Question10:
Show the exact output that would be produced by the following main()
routine:


::

    public static void main(String[] args) {
        int N;
        N = 1;
        while (N <= 32) {
           N = 2 * N;
           System.out.println(N);   
        }
    }

Question11:
Show the exact output produced by the following main() routine:


::

    public static void main(String[] args) {
       int x,y;
       x = 5;
       y = 1;
       while (x > 0) {
          x = x - 1;
          y = y * x;
          System.out.println(y);
       }
    }

Question12:
What output is produced by the following program segment? **Why?**
(Recall that name.charAt(i) is the i-th character in the string,
name.)


::

    String name;
    int i;
    boolean startWord;
    
    name = "Richard M. Nixon";
    startWord = true;
    for (i = 0; i < name.length(); i++) {
       if (startWord)
          System.out.println(name.charAt(i));
       if (name.charAt(i) == ' ')
          startWord = true;
       else
          startWord = false;
    }




[ `Quiz Answers`_ | `Chapter Index`_ | `Main Index`_ ]

.. _Chapter Index: http://math.hws.edu/javanotes/c3/index.html
.. _Quiz Answers: http://math.hws.edu/javanotes/c3/quiz_answers.html
.. _Main Index: http://math.hws.edu/javanotes/c3/../index.html


