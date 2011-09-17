


Answers for Quiz on Chapter 2
-----------------------------

This page contains sample answers to the quiz on Chapter 2 of
Introduction to Programming Using Java. Note that generally, there
are lots of correct answers to a given question.


Question1
~~~~~~~~~

Briefly explain what is meant by the syntax and the semantics of a
programming language. Give an example to illustrate the difference
between a syntax error and a semantics error.


Answer
^^^^^^

The syntax of a language is its grammar, and the semantics is its
meaning. A program with a syntax error cannot be compiled. A program
with a semantic error can be compiled and run, but gives an incorrect
result. A missing semicolon in a program is an example of a syntax
error, because the compiler will find the error and report it. If N is
an integer variable, then the statement ``frac = 1/N;`` is probably an
error of semantics. The value of ``1/N`` will be ``0`` for any ``N` greater than
``1``. It's likely that the programmer meant to say ``1.0/N``.


Question2
~~~~~~~~~

What does the computer do when it executes a variable declaration
statement. Give an example.


Answer
^^^^^^

A variable is a "box", or location, in the computer's memory that has
a name. The box holds a value of some specified type. A variable
declaration statement is a statement such as


.. code-block:: java

    int x;


which creates the variable x. When the computer executes a variable
declaration, it creates the box in memory and associates a name (in
this case, x) with that box. Later in the program, that variable can
be referred to by name.


Question3
~~~~~~~~~

What is a type, as this term relates to programming?


Answer
^^^^^^

A ``type`` represents a set of possible values. When you specify that a
variable has a certain type, you are saying what values it can hold.
When you say that an expression is of a certain type, you are saying
what values the expression can have. For example, to say that a
variable is of type int says that integer values in a certain range
can be stored in that variable.


Question4
~~~~~~~~~

One of the primitive types in Java is boolean. What is the boolean
type? Where are boolean values used? What are its possible values?


Answer
^^^^^^

The only values of type boolean are true and false. Expressions of
type boolean are used in places where true/false values are expected,
such as the conditions inwhile loops and if statements.


Question5
~~~~~~~~~

Give the meaning of each of the following Java operators:


::

    a)    ++
    
    b)    &&
    
    c)    !=



Answer
^^^^^^

The operator ++ is used to add 1 to the value of a variable. For
example, ``count++`` has the same effect as ``count = count + 1``.

The operator && represents the word **and**. It can be used to combine
two boolean values, as in ``(x > 0 && y > 0)``, which means, "x is greater
than ``0`` **and** ``y`` is greater than ``0``."

The operation != means ``is not equal to``, as in ``if (x != 0)``, meaning
``if x is not equal to zero.``.


Question6
~~~~~~~~~

Explain what is meant by an assignment statement, and give an example.
What are assignment statements used for?


Answer
^^^^^^

An assignment statement computes a value and stores that value in a
variable. Examples include:


.. code-block:: java

    x = 17;          // Assign a constant value to the variable, x.
    newRow = row;    // Copy the value from the variable, row,
                     //             into the variable, newRow.
    ans = 17*x + 42; // Compute the value of the expression 
                     //     17*x + 42, and store that value in ans.


An assignment statement is used to change the value of a variable as
the program is running. Since the value assigned to the variable can
be another variable or an expression, assignments statements can be
used to copy data from one place to another in the computer, and to do
complex computations.


Question7
~~~~~~~~~

What is meant by precedence of operators?


Answer
^^^^^^

If two or more operators are used in an expression, and if there are
no parentheses to indicate the order in which the operators are to be
evaluated, then the computer needs some way of deciding which operator
to evaluate first. The order is determined by the precedence of the
operators. For example, * has higher precedence than+, so the
expression ``3 + 5 * 7`` is evaluated as if it were written
``3 + (5 * 7)``.


Question8
~~~~~~~~~

What is a literal ?


Answer
^^^^^^

A literal is a sequence of characters used in a program to represent a
constant value. For example, ``'A'`` is a literal that represents the value
``A``, of type char, and ``17L`` is a literal that represents the number ``17`` as
a value of type long. A literal is a way of writing a value, and should
not be confused with the value itself.


Question9
~~~~~~~~~

In Java, classes have two fundamentally different purposes. What are
they?


Answer
^^^^^^

A class can be used to group together variables and subroutines that
are contained in the class. These are called the static members of the
class. For example, the subroutine ``Math.sqrt`` is a static member of the
class called ``Math``. Also, the main routine in any program is a static
member of a class. The second possible purpose of a class is to
describe and create objects. The class specifies what variables and
subroutines are contained in those objects. In this role, classes are
used in object-oriented programming (which we haven't studied yet in
any detail.)


Question10
~~~~~~~~~~

What is the difference between the statement ``x = TextIO.getDouble();``
and the statement ``x = TextIO.getlnDouble();``


Answer
^^^^^^

Either statements will read a real number input by the user, and store
that number in the variable, ``x``. They would both read and return
exactly the same value. The difference is that in the second statement
(using ``getlnDouble``), after reading the value the computer will
continue reading characters from input up to and including the next
carriage return. These extra characters are discarded.


Question11
~~~~~~~~~~

Explain why the value of the expression 2+3+"test" is the string
``5test`` while the value of the expression "test"+2+3 is the string
``test23``. What is the value of "test"+2*3?


Answer
^^^^^^

The reason is somewhat technical. The difference is due to the order
of evaluation. When several + operators are used in a row, with no
parentheses, they are evaluated from left to right. 2+3+"test" is
interpreted as (2+3)+"test", so 2 and 3 are added together, giving 5,
and then the 5 is concatenated onto the string "test". On the other
hand, "test"+2+3 is interpreted as ("test"+2)+3, so the 2 is first
concatenated onto the "test", giving "test2", and then the 3 is
concatenated onto that. In the case of "test"+2*3, the precedence
rules for + and * come into play. Since * has higher precedence, this
expression is interpreted as "test"+(2*3), which evaluates to "test6".


Question12
~~~~~~~~~~

Integrated Development Environments such as Eclipse often use syntax
coloring, which assigns various colors to the characters in a program
to reflect the syntax of the language. A student notices that Eclipse
colors the word String differently from int, double, and boolean. The
student asks why String should be a different color, since all these
words are names of types. What's the answer to the student's question?


Answer
^^^^^^

(This was a real question from a real student.)

Although String, like int, double, and boolean, is a type name, there
is a fundamental difference between String and the other types. String
is the name of a **class**, while int, double, and boolean are
primitive types. Eclipse colors all class names in the same way that
it does String, and it uses a different color for the primitive types.
(Although the difference between classes and primitive types might not
seem very important to you now, it really is an important distinction
and it's reasonable for Eclipse to use different colors for the two
concepts.)



