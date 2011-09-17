

Answers for Quiz on Chapter 4
-----------------------------

This page contains sample answers to the quiz on Chapter 4 of
Introduction to Programming Using Java. Note that generally, there
are lots of correct answers to a given question.


Question1
~~~~~~~~~

A "black box" has an interface and an implementation. Explain what is
meant by the terms interface and implementation .


Answer
^^^^^^

The interface of a black box is its connection with the rest of the
world, such as the name and parameters of a subroutine or the dial for
setting the temperature on a thermostat. The implementation refers to
internal workings of the black box. To use the black box, you need to
understand its interface, but you don't need to know anything about
the implementation.


Question2
~~~~~~~~~

A subroutine is said to have a contract . What is meant by the
contract of a subroutine? When you want to use a subroutine, why is it
important to understand its contract? The contract has both
"syntactic" and "semantic" aspects. What is the syntactic aspect? What
is the semantic aspect?


Answer
^^^^^^

The contract of a subroutine says what must be done to call the
subroutine correctly and what it will do when it is called. It is, in
short, everything a programmer needs to know about the subroutine in
order to use it correctly. (It does not include the "insides," or
implementation, of the subroutine.)

The syntactic component of a subroutine's contract includes the name
of the subroutine, the number of parameters, and the type of each
parameter. This is the information needed to write a subroutine call
statement that can be successfully compiled. The semantic component of
the contract specifies the meaning of the subroutine, that is, the
task that the subroutine performs. It might also specify limitations
on what parameter values the subroutine can process correctly. The
semantic component is not part of the program. It is generally
expressed in comments.


Question3
~~~~~~~~~

Briefly explain how subroutines can be useful in the top-down design
of programs.


Answer
^^^^^^

Top-down refers to starting from the overall problem to be solved, and
breaking it up into smaller problems that can be solved separately.
When designing a program to solve the problem, you can simply make up
a subroutine to solve each of the smaller problems. Then you can
separately design and test each subroutine.


Question4
~~~~~~~~~

Discuss the concept of parameters. What are parameters for? What is
the difference between formal parameters and actual parameters ?


Answer
^^^^^^

Parameters are used for communication between a subroutine and the
part of the program that calls the subroutine. If a subroutine is
thought of as a black box, then parameters are part of the interface
to that black box. Formal parameters are found in the subroutine
definition. Actual parameters are found in subroutine call statements.
When the subroutine is called, the values of the actual parameters are
assigned to the formal parameters before the body of the subroutine is
executed.


Question5
~~~~~~~~~

Give two different reasons for using named constants (declared with
the final modifier).


Answer
^^^^^^

A constant has a meaningful name, which makes the program easier to
read. It's easier to understand what a name like INTEREST_RATE is for
than it is to figure out how a literal number like 0.07 is being used.

A second reason for using named constants is that it's easy to modify
the value of the constant if that becomes necessary. If a literal
value is used throughout the program, the programmer has to track down
each occurrence of the value and change it. When a constant is used
correctly, it is only necessary to change the value assigned to the
constant at one point in the program.

A third reason is that using the final modifier protects the value of
a variable from being changed. This is especially important for member
variables that are accessible from outside the class where they are
declared.


Question6
~~~~~~~~~

What is an API? Give an example.


Answer
^^^^^^

An API is an Applications Programming Interface. It is the interface
to a "toolbox" of subroutines that someone has written. It tells you
what routines are available, how to call them, and what they do, but
it does not tell you how the subroutines are implemented. An example
is the standard Java API which describes the interfaces of all the
subroutines in all the classes that are available in such packages as
java.lang and java.awt.


Question7
~~~~~~~~~

Write a subroutine named "stars" that will output a line of stars to
standard output. (A star is the character ``*``.) The number of stars
should be given as a parameter to the subroutine. Use a for loop. For
example, the command ``stars(20)`` would output


.. code-block:: java

    ********************



Answer
^^^^^^

The subroutine could be written as follows:


.. code-block:: java

    static void stars(int numberOfStars) {
         // output a line containing the specified number of stars
       for (int i = 0; i < numberOfStars; i++) {
           System.out.print('*');
       }
       System.out.println();  // output carriage return after the *'s
    }



Question8
~~~~~~~~~

Write a main() routine that uses the subroutine that you wrote for
Question 7 to output 10 lines of stars with 1 star in the first line,
2 stars in the second line, and so on, as shown below.


.. code-block:: java

    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********



Answer
^^^^^^

The main() routine can use a for loop that calls the stars()
subroutine ten times, once to produce each line of output. (An
occasional beginner's mistake in this problem is to rewrite the body
of the subroutine inside the main() routine, instead of just calling
it by name.) Here is the main routine -- which would, of course, have
to be put together with the subroutine in a class in order to be used.


.. code-block:: java

    public static void main(String[] args) {
        int line;  // Line number, and also the number of stars on that line.
        for ( line = 1;  line <= 10;  line++ ) {
            stars( line );
        }
    }



Question9
~~~~~~~~~

Write a function named countChars that has a String and a char as
parameters. The function should count the number of times the
character occurs in the string, and it should return the result as the
value of the function.


Answer
^^^^^^

The returned value will be of type int. The function simply uses a for
loop to look at each character in the string. When the character in
the string matches the parameter value, it is counted.


.. code-block:: java

    static int countChars( String str, char searchChar ) {
          // Count the number of times searchChar occurs in
          // str and return the result.
        int i;     // A position in the string, str.
        char ch;   // A character in the string.
        int count; // Number of times searchChar has been found in str.
        count = 0;
        for ( i = 0;  i < str.length();  i++ ) {
            ch = str.charAt(i);  // Get the i-th character in str.
            if ( ch == searchChar )
               count++;
        }
        return count;
    }



Question10
~~~~~~~~~~

Write a subroutine with three parameters of type int. The subroutine
should determine which of its parameters is smallest. The value of the
smallest parameter should be returned as the value of the subroutine.


Answer
^^^^^^

I'll call the subroutine smallest and the three parameters x, y, andz.
The value returned by the subroutine has to be either x ory or z. The
answer will be x if x is less than or equal to both y and z. The
correct syntax for checking this is "if(x<=y&&x<= z)". Similarly fory.
The only other remaining possibility is z, so there is no necessity
for making any further test before returning z. (In fact, doing so
would be an error in Java, since with no "else" clause in the if
statement, the compiler cannot determine that the function definitely
returns a value in all possible cases.)


.. code-block:: java

    static int smallest(int x, int y, int z) {
       if (x <= y && x <= z) {
          return x;
       }
       else if (y <= x && y <= z) {
          return y;
       }
       else
          return z;
    }


Note: Since a return statement causes the computer to terminate the
execution of a subroutine anyway, this could also be written as
follows, without the elses:


.. code-block:: java

    static int smallest(int x, int y, int z) {
       if (x <= y && x <= z) {
          return x;
       }
       if (y <= x && y <= z) {
          return y;
       }
       return z;
    }




