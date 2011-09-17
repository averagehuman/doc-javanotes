



Quiz on Chapter 8
-----------------

T his page contains questions on Chapter 8 of ` Introduction to
Programming Using Java `_. You should be able to answer these
questions after studying that chapter. Sample answers to these
questions can be found `here`_.


Question1
~~~~~~~~~

What does it mean to say that a program is robust ?


Question2
~~~~~~~~~

Why do programming languages require that variables be declared before
they are used? What does this have to do with correctness and
robustness?


Question3
~~~~~~~~~

What is a precondition ? Give an example.


Question4
~~~~~~~~~

Explain how preconditions can be used as an aid in writing correct
programs.


Question5
~~~~~~~~~

Java has a predefined class called Throwable. What does this class
represent? Why does it exist?


Question6
~~~~~~~~~

Write a method that prints out a 3N+1 sequence starting from a given
integer, N. The starting value should be a parameter to the method. If
the parameter is less than or equal to zero, throw an
IllegalArgumentException. If the number in the sequence becomes too
large to be represented as a value of typeint, throw an
ArithmeticException.


Question7
~~~~~~~~~

Rewrite the method from the previous question, using assert statements
instead of exceptions to check for errors. What is the difference
between the two versions of the method when the program is run?


Question8
~~~~~~~~~

Some classes of exceptions are checked exceptions that require
mandatory exception handling. Explain what this means.


Question9
~~~~~~~~~

Consider a subroutine processData() that has the header


.. code-block:: java

    static void processData() throws IOException


Write a try..catch statement that calls this subroutine and prints an
error message if an IOException occurs.


Question10
~~~~~~~~~~

Why should a subroutine throw an exception when it encounters an
error? Why not just terminate the program?


Question11
~~~~~~~~~~

Suppose that you have a choice of two algorithms that perform the same
task. One has average-case run time that is Θ(n 2 ) while the run time
of the second algorithm has an average-case run time that is
Θ(n*log(n)). Suppose that you need to process an input of size n=100.
Which algorithm would you choose? Can you be certain that you are
choosing the fastest algorithm for the input that you intend to
process.


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




