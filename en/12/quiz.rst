[ `Quiz Answers`_ | `Chapter Index`_ | `Main Index`_ ]





Quiz on Chapter 12
------------------

T his page contains questions on Chapter 12 of ` Introduction to
Programming Using Java `_. You should be able to answer these
questions after studying that chapter. Sample answers to these
questions can be found `here`_.
Question1:
Write a complete subclass of Thread to represent a thread that writes
out the numbers from 1 to 10. Then write some code that would create
and start a thread belonging to that class.
Question2:
Suppose that thrd is an object of type Thread. Explain the difference
between calling thrd.start() and calling thrd.run().
Question3:
What is a race condition ?
Question4:
How does synchronization prevent race conditions, and what does it
mean to say that synchronization only provides mutual exclusion?
Question5:
Suppose that a program uses a single thread that takes 4 seconds to
run. Now suppose that the program creates two threads and divides the
same work between the two threads. What can be said about the expected
execution time of the program that uses two threads?
Question6:
What is an ArrayBlockingQueue and how does it solve the
producer/consumer problem?
Question7:
What is a thread pool ?
Question8:
Network server programs are often multithreaded. Explain what this
means and why it is true.
Question9:
Why does a multithreaded network server program often use many times
more threads than the number of available processors?
Question10:
Consider the ThreadSafeCounter example from`Subsection12.1.3`_:


::

    public class ThreadSafeCounter {
       
       private int count = 0;  // The value of the counter.
       
       synchronized public void increment() {
          count = count + 1;
       }
       
       synchronized public int getValue() {
          return count;
       }
       
    }


The increment() method is synchronized so that the caller of the
method can complete the three steps of the operation "Get value of
count," "Add 1 to value," "Store new value in count" without being
interrupted by another thread. But getValue() consists of a single,
simple step. Why is getValue() synchronized? (This is a deep and
tricky question.)



[ `Quiz Answers`_ | `Chapter Index`_ | `Main Index`_ ]

.. _Chapter Index: http://math.hws.edu/javanotes/c12/index.html
.. _Quiz Answers: http://math.hws.edu/javanotes/c12/quiz_answers.html
.. _12.1.3: http://math.hws.edu/javanotes/c12/../c12/s1.html#threads.1.3
.. _Main Index: http://math.hws.edu/javanotes/c12/../index.html


