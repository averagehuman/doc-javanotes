
Glossary
--------



abstract class. A class that cannot be used to create objects, and
that exists only for the purpose of creating subclasses. Abstract
classes in Java are defined using the modifier abstract.

abstract data type (ADT). A data type for which the possible values of
the type and the permissible operations on those values are specified,
without specifying how the values and operations are to be
implemented.

access specifier. A modifier used on a method definition or variable
specification that determines what classes can use that method or
variable. The access specifiers in Java are public, protected,
andprivate. A method or variable that has no access specifier is said
to have "package" visibility.

activation record. A data structure that contains all the information
necessary to implement a subroutine call, including the values of
parameters and local variables of the subroutine and the return
address to which the computer will return when the subroutine ends.
Activation records are stored on a stack, which makes it possible for
several subroutine calls to be active at the same time. This is
particularly important for recursion, where several calls to the same
subroutine can be active at the same time.

actual parameter. A parameter in a subroutine call statement, whose
value will be passed to the subroutine when the call statement is
executed. Actual parameters are also called "arguments".

address. Each location in the computer's memory has an address, which
is a number that identifies that location. Locations in memory are
numbered sequentially. In modern computers, each byte of memory has
its own address. Addresses are used when information is being stored
into or retrieved from memory.

algorithm. An unambiguous, step-by-step procedure for performing some
task, which is guaranteed to terminate after a finite number of steps.

alpha color component. A component of a color that says how
transparent or opaque that color is. The higher the alpha component,
the more opaque the color.

API. Application Programming Interface. A specification of the
interface to a software package or "toolbox." The API says what
classes or subroutines are provided in the toolbox and how to use
them.

applet. A type of Java program that is meant to run on a Web page in a
Web browser, as opposed to a stand-alone application.

animation. An apparently moving picture created by rapidly showing a
sequence of still images, called frames, one after the other. In Java,
animations are often driven by Timer objects; a new frame of the
animation is shown each time the timer fires.

antialiasing. Adjusting the color of pixels to reduce the "jagged"
effect that can occur when shapes and text are represented by pixels.
For antialiased drawing, when the shape covers only part of a pixel,
the color of the shape is blended with the previous color of the
pixel. The degree of blending depends on how much of the pixel is
covered.

array. A list of items, sequentially numbered. Each item in the list
can be identified by its index, that is, its sequence number. In Java,
all the items in array must have the same type, called the base type
of the array. An array is a random access data structure; that is, you
can get directly at any item in the array at any time.

array type. A data type whose possible values are arrays. If Type is
the name of a type, then Type[] is the array type for arrays that have
base type Type.

assignment statement. A statement in a computer program that retrieves
or computes a value and stores that value in a variable. An assignment
statement in Java has the form: variable-name = expression;

asynchronous event. An event that can occur at an unpredictable time,
outside the control of a computer program. User input events, such as
pressing a button on the mouse, are asynchronous.

ASCII. American Standard Code for Information Interchange. A way of
encoding characters using 7 bits for characters. ASCII code only
supports 128 characters, with no accented letters, non-English
alphabets, special symbols, or ideograms for non-alphabetic languages
such as Chinese. Java uses the much larger and more complete Unicode
code for characters.

base case. In a recursive algorithm, a simple case that is handled
directly rather than by applying the algorithm recursively.

binary number. A number encoded as a sequence of zeros and ones. A
binary number is represented in the "base2" in the same way that
ordinary numbers are represented in the "base10."

binary tree. A linked data structure that is either empty or consists
of a root node that contains pointers to two smaller (possibly empty)
binary trees. The two smaller binary trees are called the left subtree
and the right subtree.

bit. A single-digit binary number, which can be either 0 or 1.

black box. A system or component of a system that can be used without
understanding what goes on inside the box. A black box has an
interface and an implementation. A black box that is meant to be used
as a component in a system is called a module.

block. In Java programming, a sequence of statements enclosed between
a pair of braces, { and }. Blocks are used to group several statements
into a single statement. A block can also be empty, meaning that it
contains no statements at all and consists of just an empty pair of
braces.

blocking operation. An operation, such as reading data from a network
connection, is said to "block" if it has to wait for some event to
occur. A thread that performs a blocking operation can be "blocked"
until the required event occurs. A thread cannot execute any
instructions while it is blocked. Other threads in the same program,
however, can continue to run.

blocking queue. A queue in which the dequeue operation will block if
the queue is empty, until an item is added to the queue. If the
blocking queue has a limited capacity, the enqueue operation can also
block, if the queue is full.

bottom-up design. An approach to software design in which you start by
designing basic components of the system, then combine them into more
complex components, and so on.

BufferedImage. A class representing "off-screen canvases," that is,
images that are stored in the computer's memory and that can be used
for drawing images off-screen.

branch. A control structure that allows the computer to choose among
two or more different courses of action. Java has two branch
statements: if statements and switch statements.

byte. A unit of memory that consists of eight bits. One byte of memory
can hold an eight-bit binary number.

bytecode. "Java bytecode" is the usual name for the machine language
of the Java Virtual Machine. Java programs are compiled into Java
bytecode, which can then be executed by the JVM.

charset. A particular encoding of character data into binary form.
Examples include UTF-8 and ISO-8859-1.

checked exception. An exception in Java that must be handled, either
by a try..catch statement or by a throws clause on the method that can
throw he exception. Failure to handle a checked exception in one way
or the other is a syntax error.

class. The basic unit of programming in Java. A class is a collection
of static and non-static methods and variables. Static members of a
class are part of the class itself; non-static, or "instance," members
constitute a blueprint for creating objects, which are then said to
"belong" to the class.

client/server. A model of network communication in which a "server"
waits at a known address on the network for connection requests that
are sent to the server by "clients." This is the basic model for
communication using the TCP/IP protocol.

command-line interface. A way of interacting with the computer in
which the user types in commands to the computer and the computer
responds to each command.

comment. In a computer program, text that is ignored by the computer.
Comments are for human readers, to help them understand the program.

compiler. A computer program that translates programs written in some
computer language (generally a high-level language) into programs
written in machine language.

component. General term for a visual element of a GUI, such as a
window, button, or menu. A component is represented in Java by an
object belonging to a subclass of the class java.awt.Component.

constructor. A special kind of subroutine in a class whose purpose is
to construct objects belonging to that class. A constructor is called
using the new operator, and is not considered to be a "method."

container. A component, such as a JPanel, that can contain other GUI
components. Containers have add() methods that can be used to add
components.

contract of a method. The semantic component of the method's
interface. The contract specifies the responsibilities of the method
and of the caller of the method. It says how to use the method
correctly and specifies the task that the method will perform when it
is used correctly. The contract of a method should be fully specified
by its Javadoc comment.

control structure. A program structure such as an if statement or a
while loop that affects the flow of control in a program (that is, the
order in which the instructions in the program are executed).

CPU. Central Processing Unit. The CPU is the part of the program that
actually performs calculations and carries out programs.

data structure. An organized collection of data, that can be treated
as a unit in a program.

deadlock. A situation in which several threads hang indefinitely, for
example because each of them is waiting for some resource that is
locked by one of the other threads.

default package. The unnamed package. A class that does not declare
itself to be in a named package is considered to be in the default
package.

definite assignment. Occurs at a particular point in a program if it
is definitely true that a given variable must have been assigned a
value before that point in the program. It is only legal to use the
value of a local variable if that variable has "definitely" been
assigned a value before it is used. For this to be true, the compiler
must be able to verify that **every** path through the program from
the declaration of the variable to its use must pass through a
statement that assigns a value to that variable.

deprecated. Considered to be obsolete, but still available for
backwards compatibility. A deprecated Java class or method is still
part of the Java language, but it is not advisable to use it in new
code. Deprecated items might be removed in future versions of Java.

dialog box. A window that is dependent on another window, called its
parent. Dialog boxes are usually popped up to get information from the
user or to display a message to the user. Dialog boxes in the Swing
API are represented by objects of typeJDialog.

distributed computing. A kind of parallel processing in which several
computers, connected by a network, work together to solve a problem.

dummy parameter. Identifier that is used in a subroutine definition to
stand for the value of an actual parameter that will be passed to the
subroutine when the subroutine is called. Dummy parameters are also
called "formal parameters" (or sometimes just "parameters," when the
term "argument" is used instead of actual parameter).

enum. Enumerated type. A type that is defined by listing every
possible value of that type. An enum type in Java is a class, and the
possible values of the type are objects.

event. In GUI programming, something that happens outside the control
of the program, such as a mouse click, and that the program must
respond to when it occurs.

exception. An error or exceptional condition that is outside the
normal flow of control of a program. In Java, an exception can be
represented by an object of type Throwable that can be caught and
handled in a try..catch statement.

fetch-and-execute cycle. The process by which the CPU executes machine
language programs. It fetches (that is, reads) an instruction from
memory and carries out (that is, executes) the instruction, and it
repeats this over and over in a continuous cycle.

flag. A boolean value that is set to true to indicate that some
condition or event is true. A single bit in a binary number can also
be used as a flag.

formal parameter. Another term for "dummy parameter."

frame. One of the images that make up an animation. Also used as
another name for activation record.

function. A subroutine that returns a value.

garbage collection. The automatic process of reclaiming memory that is
occupied by objects that can no longer be accessed.

generic programming. Writing code that will work with various types of
data, rather than with just a single type of data. The Java Collection
Framework, and classes that use similar techniques, are examples of
generic programming in Java.

getter. An instance method in a class that is used to read the value
of some property of that class. Usually the property is just the value
of some instance variable. By convention, a getter is named getXyz()
wherexyz is the name of the property.

global variable. Another name for member variable, emphasizing the
fact that a member variable in a class exists outside the methods of
that class.

graphics context. The data and methods necessary for drawing to some
particular destination. A graphics context in Java is an object
belonging to the Graphics class.

GUI. Graphical User Interface. The modern way of interacting with a
computer, in which the computer displays interface components such as
buttons and menus on a screen and the user interacts with them -- for
example by clicking on them with a mouse.

hash table. A data structure optimized for efficient search,
insertion, and deletion of objects. A hash table consists of an array
of locations, and the location in which an object is stored is
determined by that object's "hash code," an integer that can be
efficiently computed from the contents of the object.

heap. The section of the computer's memory in which objects are
stored.

high level language. A programming language, such as Java, that is
convenient for human programmers but that has to be translated into
machine language before it can be executed.

HSB. A color system in which colors are specified by three numbers (in
Java, real numbers in the range 0.0 to 1.0) giving the hue,
saturation, and brightness.

IDE. Integrated Development Environment. A programming environment
with a graphical user interface that integrates tools for creating,
compiling, and executing programs.

identifier. A sequence of characters that can be used as a name in a
program. Identifiers are used as names of variables, methods, and
classes.

index. The position number of one item in an array.

implementation. The inside of a black box, such as the code that
defines a subroutine.

infinite loop. A loop that never ends, because its continuation
condition always evaluates to true.

inheritence. The fact that one class can extend another. It then
inherits the data and behavior of the class that it extends.

instance of a class. An object that belongs to that class (or a
subclass of that class). An object belongs to a class in this sense
when the class is used as a template for the object when the object is
created by a constructor defined in that class.

instance method. A non-static method in a class and hence a method in
any object that is an instance of that class.

instance variable. A non-static variable in a class and hence a
variable in any object that is an instance of that class.

interface. As a general term, how to use a black box such as a
subroutine. Knowing the interface tells you nothing about what goes on
inside the box. "Interface" is also a reserved word in Java; in this
sense, an interface is a type that specifies one or more abstract
methods. An object that implements the interface must provide
definitions for those methods.

interpreter. A computer program that executes program written in some
computer language by reading instructions from the program, one-by-
one, and carrying each one out (by translating it into equivalent
machine language instructions).

I/O. Input/Output, the way a computer program communicates with the
rest of the world, such as by displaying data to the user, getting
information from the user, reading and writing files, and sending and
receiving data over a network.

iterator. An object associated with a collection, such a list or a
set, that can be used to traverse that collection. The iterator will
visit each member of the collection in turn.

Java Collection Framework (JCF). A set of standard classed that
implement generic data structures, including ArrayList and TreeSet,
for example.

JDK. Java Development Kit. Basic software that supports both compiling
and running Java programs. A JDK includes a command-line programming
environment as well as a JRE. You need a JDK if you want to compile
Java source code, as well as executing pre-compiled programs.

JRE. Java Runtime Environment. Basic software that supports running
standard Java programs that have already been compiled. A JRE includes
a Java Virtual Machine and all the standard Java classes.

just-in-time compiler. A kind of combination interpreter/compiler that
compiles parts of a program as it interprets them. This allows
subsequent executions of the same parts of the program to be executed
more quickly than they were the first time. This can result is greatly
increased speed of execution. Modern JVMs use a just-in-time compiler.

JVM. Java Virtual Machine. The imaginary computer whose machine
language is Java bytecode. Also used to refer to computer programs
that act as interpreters for programs written in bytecode; to run Java
programs on your computer, you need a JVM.

layout manager. An object whose to function is to lay out the
components in a container, that is, to set their sizes and locations.
Different types of layout managers implement different policies for
laying out components.

linked data structure. A collection of data consisting of a number of
objects that are linked together by pointers which are stored in
instance variables of the objects. Examples include linked lists and
binary trees.

linked list. A linked data structure in which nodes are linked
together by pointers into a linear chain.

listener. In GUI programming, an object that can be registered to be
notified when events of some given type occur. The object is said to
"listen" for the events.

literal. A sequence of characters that is typed in a program to
represent a constant value. For example, 'A' is a literal that
represents the constant char value, A, when it appears in a Java
program.

location (in memory). The computer's memory is made up of a sequence
of locations. These locations are sequentially numbered, and the
number that identifies a particular location is called the address of
that location.

local variable. A variable declared within a method, for use only
inside that method. A variable declared inside a block is valid from
the point where it is declared until the end of block in which the
declaration occurs.

loop. A control structure that allows a sequence of instructions to be
executed repeatedly. Java has three kinds of loops: for loops, while
loops, and do loops

loop control variable. A variable in a for loop whose value is
modified as the loop is executed and is checked to determine whether
or not to end the loop.

machine language. A programming language consisting of instructions
that can be executed directed by a computer. Instructions in machine
language are encoded as binary numbers. Each type of computer has its
own machine language. Programs written in other languages must be
translated into a computer's machine language before they can be
executed by that computer.

main memory. Programs and data can be stored in a computer's main
memory, where they are available to the CPU. Other forms of memory,
such as a disk drive, also store information, but only main memory is
directly accessible to the CPU. Programs and data from a disk drive
have to be copied into main memory before they can be used by the CPU.

map. An associative array; a data structure that associates an object
from some collection to each object in some set. In Java, maps are
represented by the generic interface Map<T,S>

member variable. A variable defined in a class but not inside a
method, as opposed to a local variable, which is defined inside some
method.

memory. Memory in a computer is used to hold programs and data.

method. Another term for subroutine , used in the context of object-
oriented programming. A method is a subroutine that is contained in a
class or in an object.

module. A component of a larger system that interacts with the rest of
the system in a simple, well-defined, straightforward manner.

multitasking. Performing multiple tasks at once, either by switching
rapidly back and forth from one task to another or by literally
working on multiple tasks at the same time.

multiprocessing. Multitasking in which more than one processor is
used, so that multiple tasks can literally be worked on at the same
time.

mutual exclusion. Prevents two threads from accessing the same
resource at the same time. In Java, this only applies to threads that
access the resource in synchronized methods or synchronized
statements. Mutual exclusion can prevent race conditions but
introduces the possibility of deadlock.

MVC pattern. The Model/View/Controller pattern, a strategy for
dividing responsibility in a GUI component. The model is the data for
the component. The view is the visual presentation of the component on
the screen. The controller is responsible for reacting to events by
changing the model. According to the MVC pattern, these
responsibilities should be handled by different objects.

NaN. Not a Number. Double.NaN is a special value of typedouble that
represents an undefined or illegal value.

node. Common term for one of the objects in a linked data structure.

null. A special pointer value that means "not pointing to anything."

numerical analysis. The field that studies algorithms that use
approximations, such as real numbers, and the errors that can result
from such approximation.

off-by-one error. A common type of error in which one too few or one
too many items are processed, often because counting is not being
handled correctly or because the processing stops too soon or
continues too long for some other reason.

object. An entity in a computer program that can have data (variables)
and behaviors (methods). An object in Java must be created using some
class as a template. The class of an object determines what variables
and methods it contains.

object type. A type whose values are objects, as opposed to primitive
types. Classes and interfaces are object types.

OOP. Object-Oriented Programming. An approach to the design and
implementation of computer programs in which classes and objects are
created to represent concepts and entities and their interactions.

operating system. The basic software that is always running on a
computer, without which it would not be able to function. Examples
include Linux, MacOS, and Windows Vista.

operator. A symbol such as "+", "<=", or "++" that represents an
operation that can be applied to one or more values in an expression.

overloading (of operators). The fact that the same operator can be
used with different types of data. For example, the "+" operator can
be applied to both numbers and strings.

overloading (of method names). The fact that several methods that are
defined in the same class can have the same name, as long as they have
different signatures.

overriding. Redefining in a subclass. When a subclass provides a new
definition of a method that is inherited from a superclass, the new
definition is said to override the original definition.

package. In Java, a named collection of related classes and sub-
packages, such asjava.awt and javax.swing.

parallel processing. When several tasks are being performed
simultaneously, either by multiple processors or by one processor that
switches back and forth among the tasks.

parameter. Used to provide information to a subroutine when that
subroutine is called. Values of "actual parameters" in the subroutine
call statement are assigned to the "dummy parameters" in the
subroutine definition before the code in the subroutine is executed.

parameterized type. A type such as ArrayList<String> that includes one
or more type parameters (String in the example).

parsing. Determining the syntactical structure of a string in some
language. To parse a string is to determine whether the string is
legal according to the grammar of the language, and if so, how it can
be created using the rules of the grammar.

partially full array. An array that is used to store varying numbers
of items. A partially full array can be represented as a normal array
plus a counter to keep track of how many items are actually stored.

pixel. A "picture element" on the screen or in an image. A picture
consists of rows and columns of pixels. The color of each pixel can be
individually set.

polymorphism. The fact that the meaning of a call to an instance
method can depend on the actual type of the object that is used to
make the call at run time. That is, if var is a variable of object
type, then the method that is called by a statement such as
var.action() depends on the type of the object to whichvar refers when
the statement is executed at run time, not on the type of variable
var.

pointer. A value that represents an address in the computer's memory,
and hence can be thought of as "pointing" to the location that has
that address. A variable in Java can never hold an object; it can only
hold a pointer to the location where the object is stored. A pointer
is also called a "reference."

pragmatics. Rules of thumb that describe what it means to write a good
program. For example, style rules and guidelines about how to
structure a program are part of the pragmatics of a programming
language.

precedence. The precedence of operators determines the order in which
they are applied, when several operators occur in an expression, in
the absence of parentheses.

precondition. A condition that must be true at some point in the
execution of a program, in order for the program to proceed correctly
from that point. A precondition of a subroutine is something that must
be true when the subroutine is called, in order for the subroutine to
function properly. Subroutine preconditions are often restrictions on
the values of the actual parameters that can be passed into the
subroutine.

postcondition. A condition that is known to be true at some point in
the execution of a program, as a result of the computation that has
come before that point. A postcondition of a subroutine is something
that must be true after the subroutine finishes its execution. A
postcondition of a function often describe the return value of the
function.

primitive type. One of the eight basic built-in data types in Java,
double,float, long, int, short,byte, boolean, and char. A variable of
primitive type holds an actual value, as opposed to a pointer to that
value.

priority of a thread. An integer associated with a thread that can
affect the order in which threads are executed. A thread with greater
priority is executed in preference to a thread with lower priority.

producer/consumer. A classic pattern in parallel programming in which
one or more producers produce items that are consumed by one or more
consumers, and the producers and consumers are meant to run in
parallel. The problem is to get items safely and efficiently from the
producers to the consumers. In Java, the producer/consumer pattern is
implemented by blocking queues.

program. A set of instructions to be carried out by a computer,
written in an appropriate programming language. Used as a verb, it
means to create such a set of instructions.

programming language. A language that can be used to write programs
for a computer. Programming languages range in complexity from machine
language to high-level languages such as Java.

protocol. A specification of what constitutes legal communication in a
give context. A protocol specifies the format of legal messages, when
they can be sent, what kind of reply is expected, and so on.

pseudocode. Informal specification of algorithms, expressed in
language that is closer to English than an actual programming
language, and usually without filling in every detail of the
procedure.

queue. A data structure consisting of a list of items, where items can
only be added at one end and removed at the opposite end of the list.

race condition. A source of possible errors in parallel programming,
where one thread can cause an error in another thread by changing some
aspect of the state of the program that the second thread is depending
on (such as the value of variable).

RAM. Random Access Memory. This term is often used as a synonym for
the main memory of a computer. Technically, however, it means memory
in which all locations are equally accessible at any given time. The
term also implies that data can be written to the memory as well as
read from it.

recursion. Defining something in terms of itself. In particular, a
recursive subroutine is one that calls itself, either directly, or
indirectly through a chain of other subroutines. Recursive algorithms
work by reducing a complex problem into smaller problems which can
solved either directly or by applying the same algorithm
"recursively."

RGB. A color system in which colors are specified by three numbers (in
Java, integers in the range 0 to 255) giving the red, green, and blue
components of the color.

reference. Another term for "pointer."

return type of a function. The type of value that is returned by that
function.

reserved word. A sequence of characters that looks like an identifier
but can't be used as an identifier because it has a special meaning in
the language. For example, class, public, and if are reserved words in
Java.

resource. An image, sound, text, or other data file that is part of a
program. Resource files for Java programs are stored on the same class
path where the compiled class files for the program are stored.

robust program. A program is robust if it is not only correct, but
also is capable of handling errors such as a non-existent file or a
failed network connection in a reasonable way.

set. A collection of objects which contains no duplicates. In Java,
sets are represented by the generic interface Set<T>

scope. The region in a program where the declaration of an identifier
is valid.

semantics. Meaning. The semantics rules of a language determine the
meaning of strings of symbols (such as sentences or statements) in
that language.

sentinel value. A special value that marks the end of a sequence of
data values, to indicate the end of the data.

setter. An instance method in a class that is used to set the value of
some property of that class. Usually the property is just the value of
some instance variable. By convention, a setter is named setXyz()
wherexyz is the name of the property.

signature of a method. The name of the method, the number of formal
parameters in its definition, and the type of each formal parameter.
Method signatures are the information needed by a compiler to tell
which method is being called by a given subroutine call statement.

socket. An abstraction representing one end of a connection between
two computers on a network. A socket represents a logical connection
between computer programs, not a physical connection between
computers.

stack. A data structure consisting of a list of items where items can
only be added and removed at one end of the list, which is known as
the "top" of the stack. Adding an item to a stack is called "pushing,"
and removing an item is called "popping." The term stack also refers
to the stack of activation records that is used to implement
subroutine calls.

state machine. A model of computation where an abstract "machine" can
be in any of some finite set of different states. The behavior of the
machine depends on its state, and the state can change in response to
inputs or events. The basic logical structure of a GUI program can
often be represented as a state machine.

step-wise refinement. A technique for developing an algorithm by
starting with a general outline of the procedure, often expressed in
pseudocode, and then gradually filling in the details.

stream. An abstraction representing a source of input data or a
destination for output data. Java has four basic stream classes
representing input and output of character and binary data. These
classes form the foundation for Java's input/output API.

source code. Text written in a high-level programming language, which
must be translated into a machine language such as Java bytecode
before it can be executed by a computer.

subclass. A class that extends another class, directly or indirectly,
and therefore inherits its data and behaviors. The first class is said
to be a subclass of the second.

subroutine. A sequence of program instructions that have been grouped
together and given a name. The name can then be used to "call" the
subroutine. Subroutines are also called methods in the context of
object-oriented programming.

subroutine call statement. A statement in a program that calls a
subroutine. When a subroutine call statement is executed, the computer
executes the code that is inside the subroutine.

super. A special variable, automatically defined in any instance
method, that refers to the object that contains the method, but
considered as belonging to the superclass of the class in which the
method definition occurs.super gives access to members of the
superclass that are hidden by members of the same name in the
subclass.

syntax. Grammar. The syntax rules of a language determine what strings
of symbols are legal -- that is, grammatical -- in that language.

TCP/IP. Protocols that are used for network communication on the
Internet.

this. A special variable, automatically defined in any instance
method, that refers to the object that contains the method.

thread. An abstraction representing a sequence of instructions to be
executed one after the other. It is possible for a computer to execute
several threads in parallel.

thread pool. A collection of "worker threads" that are available to
perform tasks. As tasks become available, they are assigned to threads
in the pool. A thread pool is often used with a blocking queue that
holds the tasks.

top-down design. An approach to software design in which you start
with the problems, as a whole, subdivide it into smaller problems,
divide those into even smaller problems, and so on, until you get to
problems that can be solved directly.

type. Specifies some specific kind of data values. For example, the
typeint specifies integer data values that can be represented as
32-bit binary numbers. In Java, a type can be a primitive type, a
class names, or an interface name. Type names are used to specify the
types of variables, of dummy parameters in subroutines, and of return
values of subroutines.

type cast. Forces the conversion of a value of one type into another
type. For example, in (int)(6*Math.random()), the (int) is a type-cast
operation that converts the double value (6*Math.random()) into an
integer by discarding the fractional part of the real number.

Unicode. A way of encoding characters as binary numbers. The Unicode
character set includes characters used in many languages, not just
English. Unicode is the character set that is used internally by Java.

URL. Universal Resource Locator; an address for a resource on the
Internet, such as a web page.

variable. A named memory location (or sequence of locations) that can
be used to store data. A variable is created in a program, and a name
is assigned to the variable, in a variable declaration statement. The
name can then be used in that program to refer to the memory location,
or to the data stored in that memory location, depending on context.
In Java, a variable has a type , which specifies what kind of data it
can hold.

wrapper class. A class such as Double or Integer that makes it
possible to "wrap" a primitive type value in an object belonging to
the wrapper class. This allows primitive type values to be used in
contexts were objects are required, such as with the Java Collection
Framework.

XML. eXtensible Markup Language. A very common and well-supported
standard syntax for creating text-based data-representation languages.



`David Eck`_, June 2011

.. _David Eck: http://math.hws.edu/eck/index.html


