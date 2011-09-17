



Answers for Quiz on Chapter 10
------------------------------

T his page contains sample answers to the quiz on Chapter 10 of `
Introduction to Programming Using Java `_. Note that generally, there
are lots of correct answers to a given question.


Question1
~~~~~~~~~

What is meant by generic programming and what is the alternative?


Answer
^^^^^^

Generic programming means writing data structures and subroutines that
can be used for many different types of data. The alternative would be
to write a new data structure or subroutine for each different type of
data, even when they would all be essentially identical except for the
type name. For example, a single generic sort routine can be used for
sorting lists that contain data of any type. The alternative is one
routine for sorting lists of integers, one for sorting lists of
strings, one for storing arrays of real numbers, and so on.


Question2
~~~~~~~~~

Why can't you make an object of type LinkedList<int>? What should you
do instead?


Answer
^^^^^^

LinkedList<int> is an attempt to use a generic class with a type
parameter of type int, which is a primitive type. Generic programming
in Java works only for objects, and not for the primitive types, so a
type parameter of primitive type is not allowed. However, it is
possible to use the wrapper class Integer in place of int. An object
of type LinkedList<Integer> can be used almost as if it were actually
a list of ints.


Question3
~~~~~~~~~

What is an iterator and why are iterators necessary for generic
programming?


Answer
^^^^^^

One of the principle features of Java's generic programming framework
is Collections. There are several types of collection (including
LinkedList, ArrayList, TreeSet, and HashSet). In order to deal with
all the different types of collection in a generic way, we need a
generic way to access all the elements in a collection. An iterator
makes this possible. An iterator is an object associated with a
collection that makes it possible to traverse the collection (that is,
to visit each of the items in the collection in turn). Code written
using iterators will work for any type of collection. (Note, however,
that explicit use of an iterator can often be avoided by using a for-
each loop.)


Question4
~~~~~~~~~

Suppose thatintegers is a variable of type Collection<Integer>. Write
a code segment that uses an iterator to compute the sum of all the
integer values in the collection. Write a second code segment that
does the same thing using a for-each loop.


Answer
^^^^^^

Using an iterator:


.. code-block:: java

    int sum = 0;
    Iterator<Integer>  iter = integers.iterator();
    while ( iter.hasNext() ) {
       sum += iter.next();
    }


The statement "sum += iter.next()" relies on the automatic conversion
from type Integer to type int. It could also be written "sum +=
iter.next().intValue()".

Using a for-each loop:


.. code-block:: java

    int sum = 0;
    for ( int number : integers ) {   // ( Could also use "Integer number : integers". )
       sum += number;
    }



Question5
~~~~~~~~~

Interfaces such asList, Set, and Map define abstract data types.
Explain what this means.


Answer
^^^^^^

An abstract data type is defined by the operations that can be
performed on it, not by the way the data is actually stored or by the
way the operations are implemented. An interface such as List defines
operations that can be performed, but says nothing about how they are
to be implemented. In fact, there can be many different
implementations. For example, both LinkedList and ArrayList implement
the List interface. They are different "concrete" data types that
implement the same abstract data type.


Question6
~~~~~~~~~

What is the fundamental property that distinguishes Sets from other
types ofCollections?


Answer
^^^^^^

A Set cannot contain duplicate elements. Adding an item to the set has
no effect if that item is already in the set. (Note that exactly what
it means to say that two items are the same depends on the type of
set. For HashSet, two items are tested for equality using the equals()
method. For a TreeSet, the test for equality uses thecompareTo()
method.)


Question7
~~~~~~~~~

What is the essential difference in functionality between a TreeMap
and aHashMap?


Answer
^^^^^^

The key/value pairs in aTreeMap are sorted so that the keys are in
ascending order. (For this reason, it must be possible to compare the
keys in a TreeMap, using a compareTo() method. Either the keys must
implement theComparable interface or a Comparator must be provided to
do the comparison.)


Question8
~~~~~~~~~

Explain what is meant by a hash code.


Answer
^^^^^^

The hash code of an object is an integer that tells where that object
should be stored in a hash table. A hash table is an array of linked
lists. When an object is stored in a hash table, it is added to one of
these linked lists. The object's hash code is the index of the
position in the array where the object is stored. All objects with the
same hash code go into the same linked list. In Java, every object obj
has a methodobj.hashCode() that is used to compute hash codes for the
object. If the object is to be stored in a hash table of size N, then
the hash code that is used for the object is
Math.abs(obj.hashCode())%N.


Question9
~~~~~~~~~

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



Answer
^^^^^^

The interface Comparable<Date> specifies the method"public int
compareTo(Date d)", which will be used to compare two objects of type
Date. ThecompareTo() method must be added to the class, and the class
must be declared to implement the interface. To compare two dates,
first try comparing the years. If the years are equal, try comparing
the months. If the months are also equal, compare the days.


.. code-block:: java

    class Date implements Comparable<Date> {
       int month;  // Month number in range 1 to 12.
       int day;    // Day number in range 1 to 31.
       int year;   // Year number.
       Date(int m, int d, int y) {
          month = m;
          day = d;
          year = y;
       }
       public int compareTo( Date otherDate ) {
               // Returns 1, 0, or -1 if this date is greater than, equal to,
               // or less than otherDate, respectively.
          if (year < otherDate.year)
             return -1;
          else if (year > otherDate.year)
             return 1;
          else { // Years are equal; compare months.
             if (month < otherDate.month)
                return -1;
             else if (month > otherDate.month)
                return 1;
             else { // Years and months are equal; compare days.
                if (day < otherDate.day)
                   return -1;
                else if (day > otherDate.day)
                   return 1;
                else 
                   return 0;
             }
          }
       }
    }



Question10
~~~~~~~~~~

Suppose thatsyllabus is a variable of type TreeMap<Date,String>, where
Date is the class from the preceding exercise. Write a code segment
that will write out the value string for every key that is in the
month of December, 2010.


Answer
^^^^^^

I will give two solutions. One of them simply looks up each date in
December, 2010 in the map and prints the corresponding value, if there
is one. The other iterates though a submap that contains all the
entries for dates in that month.


.. code-block:: java

    
    A solution using the map's get() method:
    
          for (int day = 1; day <= 31; day++) {
               // Get the info for one day in December, 2010
             Date date = new Date(12,day,2010); // The key.
             String info = syllabus.get(date); // Get the value for that key.
                                               // (Can be null if there is no
                                               // entry in the map for this date.)
             if (info != null)
                System.out.println("December " + day + ": " + info);
          }
    
    
    A solution using a submap (harder, but more efficient):
    
          Date startDate = new Date(12,1,2010); // Starting date for submap.
          Date endDate = new Date(1,1,2011);    // Ending date for submap.
                                                // (Remember that the end date
                                                // is not included.)
          Map<Date,String> decemberData = syllabus.subMap(startDate, endDate);
          for ( Map.Entry<Date,String> entry : decemberData ) {
             Date date = entry.getKey();
             String info = entry.getValue();
             System.out.println("December " + data.day + ": " + info);
          }



Question11
~~~~~~~~~~

Write a generic class Stack<T> that can be used to represent stacks of
objects of type T. The class should include methods push(), pop(),
andisEmpty(). Inside the class, use an ArrayList to hold the items on
the stack.


Answer
^^^^^^


.. code-block:: java

    public class Stack<T> {
       ArrayList<T> stack = new ArrayList<T>();
       public void push( T newItem ) {
          stack.add(newItem);
       }  
       public T pop() {
          int top = stack.size() - 1;  // location of top item
          return stack.remove(top);    // remove and return top item
       }
       public boolean isEmpty() {
          return stack.size() == 0;
       }
    }



Question12
~~~~~~~~~~

Write a generic method, using a generic type parameter <T>, that
replaces every occurrence in a ArrayList<T> of a specified item with a
specified replacement item. The list and the two items are parameters
to the method. Both items are of type T. Take into account the fact
that the item that is being replaced might be null. For a non-null
item, use equals() to do the comparison.


Answer
^^^^^^

Since the method operates on ArrayLists, it can use indexed access
with the get(i) and set(i,item) methods. These operations are
efficient for array lists. I also give a second version of the method
that uses a list iterator and is efficient for any type of list.


.. code-block:: java

    public static <T> void replaceAll(ArrayList<T> list, T oldItem, T newItem) {
       if (oldItem == null) {
          for (int i = 0; i < list.size(); i++) {
             if ( null == list.get(i) )
                list.set( i, newItem );
          }
       }
       else {
          for (int i = 0; i < list.size(); i++) {
             if ( oldItem.equals(list.get(i)) )
                list.set( i, newItem );
          }
       }
    }
    
    
    public static <T> void replaceAll(List<T> list, T oldItem, T newItem) {
       ListIterator<T> iter = list.listIterator();
       while (iter.hasNext()) {
          T listItem = iter.next();
          if ( oldItem == null ) {
             if ( listItem == null )
                iter.set(newItem);
          }
          else {
             if ( oldItem.equals(listItem) )
                iter.set(newItem);
          }
       }
    }


(Note, by the way, that a replaceAll method is already defined as a
static method in class Collections.)



