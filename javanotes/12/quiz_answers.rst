



Answers for Quiz on Chapter 12
------------------------------

T his page contains sample answers to the quiz on Chapter 12 of `
Introduction to Programming Using Java `_. Note that generally, there
are lots of correct answers to a given question.


Question1
~~~~~~~~~

Write a complete subclass of Thread to represent a thread that writes
out the numbers from 1 to 10. Then write some code that would create
and start a thread belonging to that class.


Answer
^^^^^^

The class that defines the thread:


.. code-block:: java

    public class CountingThread extends Thread {
       public static run() {
          for (int i = 0; i < 10; i++)
             System.out.println(i);
       }
    }


Code to create an object of type CountingThread and start the thread:


.. code-block:: java

    CountingThread counter;     // Declare a variable to represent a thread.
    counter = new CountingThread();  // Create the thread object.
    counter.thread();                // Start the thread running.


(Note that it's possible to create a new thread and start it with one
statement:


.. code-block:: java

    new CountingThread().start();


Because of the precedence of the new operator, this is equivalent
to(newCountingThread()).start(), and the effect is to create a new
object of type CountingThread and then to call thestart() method in
that object.)


Question2
~~~~~~~~~

Suppose that thrd is an object of type Thread. Explain the difference
between calling thrd.start() and calling thrd.run().


Answer
^^^^^^

Calling thrd.start() creates a new thread of control and returns
immediately after doing so; then the thread's run() method is called
in the new thread of control. The code in the run() method is executed
at the same time, in parallel, with the code that follows the call to
thrd.start().

The statement thrd.run() calls the run method in the usual way: The
run() method is executed in the same thread of control as the method
that called run(). Only after the run() method returns will the code
that follows thrd.run() be executed.


Question3
~~~~~~~~~

What is a race condition ?


Answer
^^^^^^

A race condition is a problem that can occur in a multithreaded
program. Suppose that a thread takes a sequence of actions in which
one action can depend on the result of a previous action. A race
condition occurs if its possible for another thread to change or
invalidate the result of the previous action, before the first thread
completes the sequence. For example, there is a race condition in the
simple assignment statementcount=count+1 because it is executed as a
sequence of steps. The old value of count is read, one is added to
that value, and the new value is stored back into count. A race
condition occurs if it is possible for another thread to increment the
value of count between the time when the first thread reads the old
value and the time when it stores the new value. In this case, the
race condition can result in an incorrect value for count -- count
might be increased by one when it was supposed to be increased by two.
Another example occurs in the if statement


.. code-block:: java

    if ( ! list.isEmpty() )
        return list.removeFirst();


There is a race condition if it is possible for another thread to
empty the list between the time when the first thread tests whether
the list is empty and the time when the first thread tries to remove
an element from the list. In this case, the race condition can result
in an exception when the first thread tries to remove an item from an
empty list.


Question4
~~~~~~~~~

How does synchronization prevent race conditions, and what does it
mean to say that synchronization only provides mutual exclusion?


Answer
^^^^^^

Synchronization makes it possible for a thread to complete a sequence
of actions without interference from another thread. Two threads
cannot be synchronized on the same object at the same time. While one
thread is executing a synchronized block of code, it's impossible for
another thread to be executing the same block of code, or any other
block of code that is synchronized on the same object. For example, if
a thread executes


.. code-block:: java

    synchronized(list) {
       if ( ! list.isEmpty() )
          return list.removeFirst();
    }


then, assuming that all code that manipulates list is properly
synchronized, it can be sure that no other thread will be able to
empty the list between the time when the first thread tests whether
the list is empty and the time when it removes the first element from
the list.

Synchronization provides only mutual exclusion because it only
protects a thread from other threads that are also synchronized . In
the example, the code has exclusive access to list only if all the
code segments that manipulate list are synchronized. There is no
protection against a thread that executes the statement list.clear()
without synchronization.


Question5
~~~~~~~~~

Suppose that a program uses a single thread that takes 4 seconds to
run. Now suppose that the program creates two threads and divides the
same work between the two threads. What can be said about the expected
execution time of the program that uses two threads?


Answer
^^^^^^

The execution time will depend on whether the program is being run on
a computer that has more than one processor. If so, the execution time
could be as little as 2 seconds, since each of two processors can do
half of the 4-seconds worth of work. If the computer has only one
processor, however, the two-threaded program will still take 4
seconds, since all the work will have to be done by the single
processor.


Question6
~~~~~~~~~

What is an ArrayBlockingQueue and how does it solve the
producer/consumer problem?


Answer
^^^^^^

An ArrayBlockingQueue is a queue in which the operations of adding and
removing items can block. Adding an item will block if the queue is
full; removing an item will block if the queue is empty. (Furthermore,
operations on the queue are properly synchronized for use in a
multithreaded program.)

The producer/consumer problem is the problem of safely and efficiently
getting items that are produced by one group of threads to a second
group of threads that consume the items. If the items are sent through
a blocking queue, then the threads in the second group will block when
there are no items available for them to consume, and threads in the
first group will block if they are producing items faster than they
can be consumed. (Furthermore, the synchronization guarantees that no
item will be lost or consumed twice.)

In an application in which only the consuming threads should block,
aLinkedBlockingQueue, which has unlimited capacity, can be used.


Question7
~~~~~~~~~

What is a thread pool ?


Answer
^^^^^^

Thread pools are used when a large number of tasks are to be
performed, as an alternative to creating a new thread to execute each
task. A thread pool is a relatively small collection of threads that
are available for performing tasks. When a task becomes available,
instead of creating a new thread for the task, the task is assigned to
one of the threads from the pool. When the task is complete, the
thread goes back into the pool so that more tasks can be assigned to
it.

Typically, tasks are placed into a queue as they become available.
Each thread in the pool runs in an infinite loop in which it
repeatedly takes a task from the queue and executes it. (Blocking
queues work well for this application.)


Question8
~~~~~~~~~

Network server programs are often multithreaded. Explain what this
means and why it is true.


Answer
^^^^^^

A multi-threaded server uses threads to handle the client connections
that it accepts. A server program is generally designed to process
connection requests from many clients. It runs in an infinite loop in
which it accepts a connection request and processes it. If the
processing takes a significant amount of time, it's not a good idea to
make the other clients wait while the current client is processed. The
solution is for the server to make a new thread to handle each client
connection, or to use a thread pool of threads that can handle the
client connections. The server can continue to accept more client
connections even while the first client is being serviced.


Question9
~~~~~~~~~

Why does a multithreaded network server program often use many times
more threads than the number of available processors?


Answer
^^^^^^

Network operations can block , which means that a thread that handles
communication with a client will often spend most of its time
sleeping. In order to keep all the processors busy, the number of
**active** threads should be comparable to the number of processors.
If at any given time, the number of active threads is only a fraction
of the total number of threads, then the total number of threads
should be several times the number of processors.


Question10
~~~~~~~~~~

Consider the ThreadSafeCounter example from`Subsection12.1.3`_:


.. code-block:: java

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


Answer
^^^^^^

The getValue() method has to be synchronized because of the caching of
local data that was discussed in `Subsection12.1.4`_. If getValue()
were not synchronized, it is possible that a thread that calls
getValue() would see an old, cached value of count rather than the
most current value. Synchronization ensures that the most current
value of count will be seen. If count were declared to be a volatile
variable, then getValue() would not have to be synchronized. However,
increment() would still need to be synchronized to prevent the race
condition.



