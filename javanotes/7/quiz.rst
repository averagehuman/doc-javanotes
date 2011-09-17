



Quiz on Chapter 7
-----------------

T his page contains questions on Chapter 7 of ` Introduction to
Programming Using Java `_. You should be able to answer these
questions after studying that chapter. Sample answers to these
questions can be found `here`_.


Question1
~~~~~~~~~

What does the computer do when it executes the following statement?
Try to give as complete an answer as possible.


.. code-block:: java

    Color[]  palette  =  new  Color[12];



Question2
~~~~~~~~~

What is meant by the basetype of an array?


Question3
~~~~~~~~~

What does it mean to sort an array?


Question4
~~~~~~~~~

What is the main advantage of binary search over linear search? What
is the main disadvantage?


Question5
~~~~~~~~~

What is meant by a dynamic array? What is the advantage of a dynamic
array over a regular array?


Question6
~~~~~~~~~

Suppose that a variable strlst has been declared as


.. code-block:: java

    ArrayList<String> strlst = new ArrayList<String>();


Assume that the list is not empty and that all the items in the list
are non-null. Write a code segment that will find and print the string
in the list that comes first in lexicographic order. How would your
answer change if strlst were declared to be of type ArrayList instead
of ArrayList<String>?


Question7
~~~~~~~~~

What is the purpose of the following subroutine? What is the meaning
of the value that it returns, in terms of the value of its parameter?


.. code-block:: java

    static String concat( String[] str ) {
       if (str == null)
          return "";
       String ans = "";
       for (int i = 0; i < str.length; i++) {
          ans = ans + str[i];
       return ans;
    }



Question8
~~~~~~~~~

Show the exact output produced by the following code segment.


.. code-block:: java

    char[][] pic = new char[6][6];
    for (int i = 0; i < 6; i++)
       for (int j = 0; j < 6; j++) {
          if ( i == j  ||  i == 0  ||  i == 5 )
             pic[i][j] = '*';
          else
             pic[i][j] = '.';
       }
    for (int i = 0; i < 6; i++) {
       for (int j = 0; j < 6; j++)
          System.out.print(pic[i][j]);
       System.out.println();
    }



Question9
~~~~~~~~~

Write a complete static method that finds the largest value in an
array of ints. The method should have one parameter, which is an array
of type int[]. The largest number in the array should be returned as
the value of the method.


Question10
~~~~~~~~~~

Suppose that temperature measurements were made on each day of 1999 in
each of 100 cities. The measurements have been stored in an array


.. code-block:: java

    int[][]  temps  =  new  int[100][365];


where temps[c][d] holds the measurement for city number c on the d th
day of the year. Write a code segment that will print out the average
temperature, over the course of the whole year, for each city. The
average temperature for a city can be obtained by adding up all 365
measurements for that city and dividing the answer by 365.0.


Question11
~~~~~~~~~~

Suppose that a class,Employee, is defined as follows:


.. code-block:: java

    class Employee {
       String lastName;
       String firstName;
       double hourlyWage;
       int yearsWithCompany;
    }


Suppose that data about 100 employees is **already** stored in an
array:


.. code-block:: java

    Employee[] employeeData = new Employee[100];


Write a code segment that will output the first name, last name, and
hourly wage of each employee who has been with the company for 20
years or more.


Question12
~~~~~~~~~~

Suppose that A has been declared and initialized with the statement


.. code-block:: java

    double[] A = new double[20];


and suppose that A has **already** been filled with 20 values. Write a
program segment that will find the average of all the **non-zero**
numbers in the array. (The average is the sum of the numbers, divided
by the number of numbers. Note that you will have to count the number
of non-zero entries in the array.) Declare any variables that you use.



