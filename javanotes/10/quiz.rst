[ `Quiz Answers`_ | `Chapter Index`_ | `Main Index`_ ]





Quiz on Chapter 10
------------------

T his page contains questions on Chapter 10 of ` Introduction to
Programming Using Java `_. You should be able to answer these
questions after studying that chapter. Sample answers to these
questions can be found `here`_.
Question1:
What is meant by generic programming and what is the alternative?
Question2:
Why can't you make an object of type LinkedList<int>? What should you
do instead?
Question3:
What is an iterator and why are iterators necessary for generic
programming?
Question4:
Suppose thatintegers is a variable of type Collection<Integer>. Write
a code segment that uses an iterator to compute the sum of all the
integer values in the collection. Write a second code segment that
does the same thing using a for-each loop.
Question5:
Interfaces such asList, Set, and Map define abstract data types.
Explain what this means.
Question6:
What is the fundamental property that distinguishes Sets from other
types ofCollections?
Question7:
What is the essential difference in functionality between a TreeMap
and aHashMap?
Question8:
Explain what is meant by a hash code.
Question9:
Modify the followingDate class so that it implements the interface
Comparable<Date>. The ordering on objects of type Date should be the
natural, chronological ordering.


.. code-block:: java

    class Date {
       int month;  // Month number in range 1 to 12.
       int day;    // Day number in range 1 to 31.
       int year;   // Year number.
       Date(int m, int d, int y) { 
          month = m;
          day = d;
          year = y;
       }
    }

Question10:
Suppose thatsyllabus is a variable of type TreeMap<Date,String>, where
Date is the class from the preceding exercise. Write a code segment
that will write out the value string for every key that is in the
month of December, 2010.
Question11:
Write a generic class Stack<T> that can be used to represent stacks of
objects of type T. The class should include methods push(), pop(),
andisEmpty(). Inside the class, use an ArrayList to hold the items on
the stack.
Question12:
Write a generic method, using a generic type parameter <T>, that
replaces every occurrence in a ArrayList<T> of a specified item with a
specified replacement item. The list and the two items are parameters
to the method. Both items are of type T. Take into account the fact
that the item that is being replaced might be null. For a non-null
item, use equals() to do the comparison.



[ `Quiz Answers`_ | `Chapter Index`_ | `Main Index`_ ]

.. _Chapter Index: http://math.hws.edu/javanotes/c10/index.html
.. _Quiz Answers: http://math.hws.edu/javanotes/c10/quiz_answers.html
.. _Main Index: http://math.hws.edu/javanotes/c10/../index.html


