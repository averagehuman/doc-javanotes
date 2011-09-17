



Answers for Quiz on Chapter 3
-----------------------------

T his page contains sample answers to the quiz on Chapter 3 of
Introduction to Programming Using Java. Note that generally, there
are lots of correct answers to a given question.


Question1
~~~~~~~~~

What is an algorithm ?


Answer
^^^^^^

An algorithm is an unambiguous, step-by-step procedure for performing
a certain task, which is guaranteed to finish after a finite number of
steps. (An algorithm is not the same thing as a program, but it can be
the idea behind a program.)


Question2
~~~~~~~~~

Explain briefly what is meant by "pseudocode" and how is it useful in
the development of algorithms.


Answer
^^^^^^

Pseudocode refers to informal descriptions of algorithms, written in a
language that imitates the structure of a programming language, but
without the strict syntax. Pseudocode can be used in the process of
developing an algorithm with stepwise refinement. You can start with a
brief pseudocode description of the algorithm and then add detail to
the description through a series of refinements until you have
something that can be translated easily into a program written in an
actual programming language.


Question3
~~~~~~~~~

What is a block statement? How are block statements used in Java
programs?


Answer
^^^^^^

A block statement is just a sequence of Java statements enclosed
between braces, ``{`` and ``}``. The body of a subroutine is a block
statement. Block statements are often used in control structures. A
block statement is generally used to group together several statements
so that they can be used in a situation that only calls for a single
statement. For example, the syntax of a while loop calls for a single
statement: ``while (condition) do statement``. However, the statement
can be a block statement, giving the structure: ``while (condition) {
statement; statement;...}``.


Question4
~~~~~~~~~

What is the main difference between a ``while`` loop and a ``do...while`` loop?


Answer
^^^^^^

Both types of loop repeat a block of statements until some condition
becomes false. The main difference is that in a while loop, the
condition is tested at the beginning of the loop, and in a do..while
loop, the condition is tested at the end of the loop. It is possible
that the body of a while loop might not be executed at all. However,
the body of a do..while loop is executed at least once since the
condition for ending the loop is not tested until the body of the loop
has been executed.


Question5
~~~~~~~~~

What does it mean to prime a loop?


Answer
^^^^^^

The condition at the beginning of a while loop has to make sense even
the first time it is tested, before the body of the loop is executed.
To prime the loop is to set things up before the loop starts so that
the test makes sense (that is, the variables that it contains have
reasonable values). For example, if the test in the loop is "while the
user's response is yes," then you will have to prime the loop by
getting a response from the user (or making one up) before the loop.


Question6
~~~~~~~~~

Explain what is meant by an animation and how a computer displays an
animation.


Answer
^^^^^^

An animation consists of a series of "frames." Each frame is a still
image, but there are slight differences from one frame to the next.
When the images are displayed rapidly one frame after another, the eye
perceives motion. A computer displays an animation by showing one
image on the screen, then replacing it with the next image, then the
next, and so on.


Question7
~~~~~~~~~

Write a for loop that will print out all the multiples of 3 from 3 to
36, that is: ``3 6 9 12 15 18 21 24 27 30 33 36``.


Answer
^^^^^^

Here are two possible answers. Assume that ``N`` has been declared to be a
variable of type int:


.. code-block:: java

            for ( N = 3;  N <= 36;  N = N + 3 ) {
                System.out.println( N );
            }
      
    or
            for ( N = 3;  N <= 36;  N++ ) {
                if ( N % 3 == 0 )
                    System.out.println( N );
            }



Question8
~~~~~~~~~

Fill in the following main() routine so that it will ask the user to
enter an integer, read the user's response, and tell the user whether
the number entered is even or odd. (You can use ``TextIO.getInt()`` to
read the integer. Recall that an integer ``n`` is even if ``n % 2 == 0``.)


.. code-block:: java

    public static void main(String[] args) {
     
             // Fill in the body of this subroutine!
     
    }



Answer
^^^^^^

The problem already gives an outline of the program. The last step,
telling the user whether the number is even or odd, requires an if
statement to decide between the two possibilities.


.. code-block:: java

    public static void main (String[] args) {
    
       int n;  // the number read from the user
    
       TextIO.put("Type an integer: ");  // ask the use to enter an integer
     
       n = TextIO.getInt();   // read the user's response
     
       if (n % 2 == 0)        // tell the user whether the number is even or odd
          System.out.println("That's an even number.");
       else
          System.out.println("That's an odd number.");
    }



Question9
~~~~~~~~~

Suppose that s1 and s2 are variables of typeString, whose values are
expected to be string representations of values of type int. Write a
code segment that will compute and print the integer sum of those
values, or will print an error message if the values cannot
successfully be converted into integers. (Use a try..catch statement.)


Answer
^^^^^^

The function Integer.parseInt can be used to convert the strings into
integers. This function will throw an exception of type
NumberFormatException if the conversion fails. A try..catch statement
can catch this exception and print an error message. So, the code
segment can be written:


.. code-block:: java

    try {
       int n1, n2;  // The values of s1 and s2 as integers.
       int sum;     // The sum of n1 and n2.
       n1 = Integer.parseInt(s1);
       n2 = Integer.parseInt(s2);
       sum = n1 + n2;   // (If an exception occurs, we don't get to this point.)
       System.out.println("The sum is " + sum);
    }
    catch ( NumberFormatException e ) {
        System.out.println("Error!  Unable to convert strings to integers.);  
    }



Question10
~~~~~~~~~~

Show the exact output that would be produced by the following main()
routine:


.. code-block:: java

    public static void main(String[] args) {
        int N;
        N = 1;
        while (N <= 32) {
           N = 2 * N;
           System.out.println(N);   
        }
    }



Answer
^^^^^^

The exact output printed by this program is:


.. code-block:: java

    2
    4
    8
    16
    32
    64


(The hard part to get right is the 64 at the end. The value of N
doubles each time through the loop. For the final execution of the
loop, N starts out with the value 32, but N is doubled to 64 before it
is printed.)


Question11
~~~~~~~~~~

Show the exact output produced by the following main() routine:


.. code-block:: java

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



Answer
^^^^^^

The way to answer this question is to trace exactly what the program
does, step-by-step. The output is shown below on the right. On the
left is a table that shows the values of the variables ``x`` and ``y`` as the
program is being executed.


.. code-block:: java

     value of x   |   value of y                 OUTPUT
    --------------|--------------             -------------
          5       |     1  [ before loop]
          4       |     4  [ = 1*4 ]               4
          3       |    12  [ = 4*3 ]               12
          2       |    24  [ = 12*2 ]              24
          1       |    24  [ = 24*1 ]              24
          0       |     0  [ = 24*0 ]              0



Question12
~~~~~~~~~~

What output is produced by the following program segment? **Why?**
(Recall that ``name.charAt(i)`` is the ``i``-th character in the string,
name.)


.. code-block:: java

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



Answer
^^^^^^

This is a tough one! The output from this program consists of the
three lines:


.. code-block:: java

        R
        M
        N


As the for loop in this code segment is executed,name.charAt(i)
represents each of the characters in the string ``"Richard M. Nixon"`` in
succession. The statement ``System.out.println(name.charAt(i))`` outputs
the single character ``name.charAt(i)`` on a line by itself. However, this
output statement occurs inside an if statement, so only some of the
characters are output. The character is output if startWord is true.
This variable is initialized to true, so when i is 0, startWord is
true, and the first character in the string, 'R', is output. Then,
since 'R' does not equal ' ',startWorld becomes false, so no more
characters are output until startWord becomes true again. This happens
when ``name.charAt(i)`` is a space, that is, just before the 'M' is
processed and again just before the 'N' is processed. In fact whatever
the value of name, this for statement would print the first character
in name and every character in name that follows a space. (It is
almost true that this for statement prints the first character of each
word in the string, but something goes wrong when the first character
is a space or when there are two spaces in a row. What happens in
these cases?)



