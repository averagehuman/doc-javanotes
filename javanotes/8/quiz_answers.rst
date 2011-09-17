



Answers for Quiz on Chapter 8
-----------------------------

T his page contains sample answers to the quiz on Chapter 8 of `
Introduction to Programming Using Java `_. Note that generally, there
are lots of correct answers to a given question.


Question1
~~~~~~~~~

What does it mean to say that a program is robust ?


Answer
^^^^^^

A robust program is one that can handle errors and other unexpected
conditions in some reasonable way. This means that the program must
anticipate possible errors and respond to them if they occur.


Question2
~~~~~~~~~

Why do programming languages require that variables be declared before
they are used? What does this have to do with correctness and
robustness?


Answer
^^^^^^

It's a little inconvenient to have to declare every variable before it
is used, but its much safer. If the compiler would accept undeclared
variables, then it would also accept misspelled names and treat them
as valid variables. This can easily lead to incorrect programs. When
variables must be declared, the unintentional creation of a variable
is simply impossible, and a whole class of possible bugs is avoided.


Question3
~~~~~~~~~

What is a precondition ? Give an example.


Answer
^^^^^^

A precondition is a condition that has to hold at given point in the
execution of a program, if the execution of the program is to continue
correctly. For example, the statement "x=A[i];" has two preconditions:
that A is not null and that 0<=i <A.length. If either of these
preconditions is violated, then the execution of the statement will
generate an error.

Also, a precondition of a subroutine is a condition that has to be
true when the subroutine is called in order for the subroutine to work
correctly.


Question4
~~~~~~~~~

Explain how preconditions can be used as an aid in writing correct
programs.


Answer
^^^^^^

Suppose that a programmer recognizes a precondition at some point in a
program. This is a signal to the programmer that an error might occur
if the precondition is not met. In order to have a correct and robust
program, the programmer must deal with the possible error. There are
several approaches that the programmer can take. One approach is to
use an if statement to test whether the precondition is satisfied. If
not, the programmer can take some other action such as printing an
error message and terminating the program. Another approach is to use
atry statement to catch and respond to the error. This is really just
a cleaner way of accomplishing the same thing as the first approach.
The best approach, when it is possible, is to ensure that the
precondition is satisfied as a result of what has already been done in
the program. For example, if the precondition is that x>=0, and the
preceding statement is "x=Math.abs(y);", then we know that the
precondition is satisfied, since the absolute value of any number is
greater than or equal to zero.


Question5
~~~~~~~~~

Java has a predefined class called Throwable. What does this class
represent? Why does it exist?


Answer
^^^^^^

The class Throwable represents all possible objects that can be thrown
by a throw statement and caught by a catch clause in a try..catch
statement. That is, the thrown object must belong to the
classThrowable or to one of its (many) subclasses such asException and
RuntimeException. The object carries information about an exception
from the point where the exception occurs to the point where it is
caught and handled.


Question6
~~~~~~~~~

Write a method that prints out a 3N+1 sequence starting from a given
integer, N. The starting value should be a parameter to the method. If
the parameter is less than or equal to zero, throw an
IllegalArgumentException. If the number in the sequence becomes too
large to be represented as a value of typeint, throw an
ArithmeticException.


Answer
^^^^^^

The problem of large values in a3N+1 sequence was discussed in
`Section8.1`_. In that section, it is pointed out that the test
"if(N>2147483646/3)" can be used to test whether the value of N has
become too large. This test is used in the following method.


.. code-block:: java

    /** Print the 3N+1 sequence starting from N.  If N
     * is not greater than 0 or if the value of N exceeds
     * the maximum legal value for ints, than an
     * exception will be thrown.
     */
    static void printThreeNSequence(int N) {
       if (N < 1) {
          throw new IllegalArgumentException(
                      "Starting value for 3N+1 sequence must be > 0.");
       }
       System.out.println("3N+1 sequence starting from " + N " is: ");
       System.out.println(N);
       while (N > 1) {
          if (N % 2 == 0) {  // N is even.  Divide by 2.
              N = N / 2;
          }
          else {  // N is odd.  Multiply by 3 and add 1.
              if (N > 2147483646/3) {
                 throw new ArithmeticError("Value has exceeded the largest int.");
              }
              N = 3 * N + 1;
          }
          System.out.println(N);
       }
    }


(Note that it would be possible to declare that this routine can throw
exceptions by adding a "throws" clause to the heading:


.. code-block:: java

    static void printThreeNSequence(int N)
               throws IllegalArgumentException, ArithmeticException {


However, this is not required since IllegalArgumentExceptions
andArithmeticExceptions are not checked exceptions.)


Question7
~~~~~~~~~

Rewrite the method from the previous question, using assert statements
instead of exceptions to check for errors. What is the difference
between the two versions of the method when the program is run?


Answer
^^^^^^

We can replace the if statements that check for errors with assert
statements that give the same error messages:


.. code-block:: java

    /** Print the 3N+1 sequence starting from N.
      * Precondition:  N > 0 and the 3N+1 sequence for N does not contain
      * any numbers that are too big to be represented as 32-bit ints.
      */
    static void printThreeNSequence(int N) {
       
       assert  N > 0 : "Starting value for 3N+1 sequence must be > 0.";
    
       System.out.println("3N+1 sequence starting from " + N " is: ");
       
       System.out.println(N);
       while (N > 1) {
          if (N % 2 == 0) {  // N is even.  Divide by 2.
              N = N / 2;
          }
          else {  // N is odd.  Multiply by 3 and add 1.
              assert  N <= 2147483646/3 : "Value has exceeded the largest int.";
              N = 3 * N + 1;
          }
          System.out.println(N);
       }
       
    }


The first version of the method will always check for errors when the
program is run. The second version, on the other hand, does not
actually do any error checking when the program is run in the ordinary
way. In order for assert statements to be executed, the program must
be run with assertions enabled. The assert statements are really there
only to do error-checking during debugging and testing. (In this
particular case, I would say that an exception should definitely be
thrown whenN exceeds the maximum legal value, but that it's reasonable
to use an assert to check whether N>0.)


Question8
~~~~~~~~~

Some classes of exceptions are checked exceptions that require
mandatory exception handling. Explain what this means.


Answer
^^^^^^

Subclasses of the classException which are not subclasses of
RuntimeException are checked exceptions. This has two consequences:
First, if a method can throw such an exception, then it must declare
this fact by adding a throws clause to the method heading. Second, if
a routine includes any code that can generate such an exception, then
the routine must deal with the exception. It can do this by including
the code in a try statement that has a catch clause to handle the
exception. Or it can add a throws clause to the method definition to
declare that calling the method might throw the exception.


Question9
~~~~~~~~~

Consider a subroutine processData() that has the header


.. code-block:: java

    static void processData() throws IOException


Write a try..catch statement that calls this subroutine and prints an
error message if an IOException occurs.


Answer
^^^^^^


.. code-block:: java

    try {
       processData();
    }
    catch (IOException e) {
       System.out.println("An IOException occurred while processing the data.");
    }



Question10
~~~~~~~~~~

Why should a subroutine throw an exception when it encounters an
error? Why not just terminate the program?


Answer
^^^^^^

Terminating the program is too drastic, and this tactic certainly
doesn't lead to robust programs! It's likely that the subroutine
doesn't know what to do with the error, but that doesn't mean that it
should abort the whole program. When the subroutine throws an
exception, the subroutine is terminated, but the program that called
the subroutine still has a chance to catch the exception and handle
it. In effect, the subroutine is saying "Alright, I'm giving up. Let's
hope someone else can deal with the problem."


Question11
~~~~~~~~~~

Suppose that you have a choice of two algorithms that perform the same
task. One has average-case run time that is Θ(n 2 ) while the run time
of the second algorithm has an average-case run time that is
Θ(n*log(n)). Suppose that you need to process an input of size n=100.
Which algorithm would you choose? Can you be certain that you are
choosing the fastest algorithm for the input that you intend to
process.


Answer
^^^^^^

In the absence of other information, the second algorithm, with run
time Θ(n*log(n)), is the better choice, since n*log(n) is much smaller
than n 2 . However, it's not completely certain that the second
algorithm is the better choice in a particular case. First of all,
although the n*log(n) algorithm is certainly better than the n 2
algorithm for large enough values of n, that is not necessarily true
for n=100. Second, there is the issue of "average-case" run time. Even
if the n*log(n) algorithm is better for most inputs of size 100, it
might not be better for all such inputs.


Question12
~~~~~~~~~~

Analyze the run time of the following algorithm. That is, find a
function f(n) such that the run time of the algorithm is O(f(n)) or,
better, Θ(f(n)). Assume that A is an array of integers, and use the
length of the array as the input size, n.


.. code-block:: java

    
    int total = 0;
    for (int i = 0; i < A.length; i++) {
       if (A[i] > 0)
          total = total + A[i];
    }



Answer
^^^^^^

The run time of this algorithm is Θ(n). There are several things in
the code that are evaluated n times: the test "i<A.length", the
increment "i++", and the test in the if statement. The initialization
is done once, and nothing is executed more than n times. It follows
that both the worst-case and the average case run times are Θ(n).



