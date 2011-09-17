



Answers for Quiz on Chapter 7
-----------------------------

T his page contains sample answers to the quiz on Chapter 7 of `
Introduction to Programming Using Java `_. Note that generally, there
are lots of correct answers to a given question.


Question1
~~~~~~~~~

What does the computer do when it executes the following statement?
Try to give as complete an answer as possible.


.. code-block:: java

    Color[]  palette  =  new  Color[12];



Answer
^^^^^^

This is a declaration statement, that declares and initializes a
variable named palette of typeColor[]. The initial value of this
variable is a newly created array that has space for 12 items. To be
specific about what the computer does: It creates a new 12-element
array object on the heap, and it fills each space in that array with
null. It allocates memory space for the variable,palette. And it
stores a pointer to the new array object in that memory space.


Question2
~~~~~~~~~

What is meant by the basetype of an array?


Answer
^^^^^^

The base type of an array refers to the type of the items that can be
stored in that array. For example, the base type of the array in the
previous problem is Color.


Question3
~~~~~~~~~

What does it mean to sort an array?


Answer
^^^^^^

To sort an array means to rearrange the items in the array so that
they are in increasing or decreasing order (according to some
criterion).


Question4
~~~~~~~~~

What is the main advantage of binary search over linear search? What
is the main disadvantage?


Answer
^^^^^^

The advantage of binary search is that it is much faster. On a list of
one million items, linear search would take an average of five hundred
thousand steps to find an item, whereas binary search would take only
20 steps. The disadvantage is that binary search only works on a
sorted list, so some extra work must be done to keep the sort the list
or to keep the list in sorted order as it is created.


Question5
~~~~~~~~~

What is meant by a dynamic array? What is the advantage of a dynamic
array over a regular array?


Answer
^^^^^^

A dynamic array is like an array in that it is a data structure that
stores a sequence of items, all of the same type, in numbered
locations. It is different from an array in that there is no preset
upper limit on the number of items that it can contain. This is an
advantage in situations where a reasonable value for the size of the
array is not known at the time it is created.


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


Answer
^^^^^^

Strings can be compared for lexicographic order using the compareTo
instance method in the String class. We can find the smallest string
as follows:


.. code-block:: java

    String smallest = strlst.get(0);
    for (int i = 1; i < strlist.size(); i++) {
       String nextString = strlst.get(i);
       if ( nextString.compareTo(smallest) < 0 ) 
           smallest = nextString;
    }
    System.out.println("The smallest string lexicographically is " + smallest);


If strlst were declared to be of type ArrayList, then the return type
of strlst.get(i) would be Object instead of String, and a type-cast
would be necessary to convert the returned value to type String:


.. code-block:: java

    String smallest = (String)strlst.get(0);
    for (int i = 1; i < strlist.size(); i++) {
       String nextString = (String)strlst.get(i);
       if ( nextString.compareTo(smallest) < 0 ) 
           smallest = nextString;
    }
    System.out.println("The smallest string lexicographically is " + smallest);


Furthermore, it now has to be **assumed** that every item in the list
is in fact a string, since objects of any type could now be legally
stored in strlst.


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



Answer
^^^^^^

The purpose of the subroutine is to chain all the strings in an array
of strings into one long string. If the array parameter is null, then
there are no strings, and the empty string is returned. Otherwise, the
value returned is the string made up of all the strings from the
array. For example, if stringList is an array declared as


.. code-block:: java

    String[] stringList = { "Put 'em ",  "all", " together" };


then the value of concat(stringList) is "Put 'em all together".


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



Answer
^^^^^^

The output consists of six lines, with each line containing six
characters. In the first line, i is 0, so all the characters are *'s.
In the last line, i is 5, so all the characters are *'s. In each of
the four lines in the middle, one of the characters is a * and the
rest are periods. The output is


.. code-block:: java

    ******
    .*....
    ..*...
    ...*..
    ....*.
    ******


It might help to look at the array items that are printed on each
line. Note that pic[row][col] is '*' if row is 0 or if row is 5 or if
row and col are equal.


.. code-block:: java

    pic[0][0] pic[0][1] pic[0][2] pic[0][3] pic[0][4] pic[0][5] 
    pic[1][0] pic[1][1] pic[1][2] pic[1][3] pic[1][4] pic[1][5] 
    pic[2][0] pic[2][1] pic[2][2] pic[2][3] pic[2][4] pic[2][5] 
    pic[3][0] pic[3][1] pic[3][2] pic[3][3] pic[3][4] pic[3][5] 
    pic[4][0] pic[4][1] pic[4][2] pic[4][3] pic[4][4] pic[4][5] 
    pic[5][0] pic[5][1] pic[5][2] pic[5][3] pic[5][4] pic[5][5]



Question9
~~~~~~~~~

Write a complete static method that finds the largest value in an
array of ints. The method should have one parameter, which is an array
of type int[]. The largest number in the array should be returned as
the value of the method.


Answer
^^^^^^

One possible answer is:


.. code-block:: java

    public static int getMax(int[] list) {
       
       int max = list[0];  // This is the largest item seen so far.
       
       for (int i = 1; i < list.length; i++) {
             // Look at each item in the array.  If the item is
             // bigger than max, then set max equal to the item.
           if (list[i] > max)
              max = list[i];
       }
       
       // At this point, max is the largest item in the whole array.
       
       return max;
       
    } // end getMax


(Note that this method throws an exception if the parameter list is
null or if it is an array of length0. The exception is thrown by the
line "intmax=list[0];". The reference to list[0] causes a
NullPointerException if list is null and an
ArrayIndexOutOfBoundsException if the array has lenght zero.)


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


Answer
^^^^^^

A pseudocode outline of the answer is


.. code-block:: java

    For each city {
       Add up all the temperatures for that city
       Divide the total by 365 and print the answer
    }


Adding up all the temperatures for a given city itself requires a for
loop, so the code segment looks like this:


.. code-block:: java

    for (int city = 0; city < 100; city++) {
        int total = 0;  // total of temperatures for this city
        for (int day = 0; day < 365; day++)
           total = total + temps[city][day];
        double avg = total / 365.0;  // average temp for this city
        System.out.println("Average temp for city number " 
                 + city + " is " + avg);
    }



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


Answer
^^^^^^

(The data for the i-th employee is stored in an object that can be
referred to as employeeData[i]. The four pieces of data about that
employee are members of this object and can be referred to as:


+ employeeData[i].firstName
+ employeeData[i].lastName
+ employeeData[i].hourlyWage
+ employeeData[i].yearsWithCompany


The code segment uses a for loop to consider each employee in the
array.)


.. code-block:: java

    for (int i=0; i < 100; i++) {
        if ( employeeData[i].yearsWithCompany >= 20 )
            System.out.println(employeeData[i].firstName + " " +
                          employeeData[i].lastName + ": " +
                          employeeData[i].hourlyWage);
    }


A for-each loop would also work:


.. code-block:: java

    for ( Employee emp : employeeData ) {
        if ( emp.yearsWithCompany >= 20 )
            System.out.println(emp].firstName + " " +
                          emp.lastName + ": " +
                          emp.hourlyWage);
    }



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


Answer
^^^^^^

(There is one problem with this question. What happens if all the
entries in the array A are zero? In that case, the number of non-zero
entries is zero, and the average of non-zero entries is undefined. In
my answer, I assign the "undefined" value, Double.NaN, to the average
in this case, but this is somewhat arbitrary.)


.. code-block:: java

    int nonzeroCt = 0; // The number of non-zero entries in the array.
    double total = 0;  // The total of all the grades in the array.
    double average;    // The average of the non-zero entries in the array.
    
    for (int i = 0; i < 20; i++) {
       if (A[i] != 0) {       // Process this non-zero entry.
           total += A[i]; // Add it to the total.
           nonzeroCt++;   // Count it.
       }
    }
    
    if (nonzeroCt > 0)
       average = total / nonzeroCt;
    else   // (The average is undefined in this case)
       average = Double.NaN;




