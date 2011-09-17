



Answers for Quiz on Chapter 11
------------------------------

T his page contains sample answers to the quiz on Chapter 11 of `
Introduction to Programming Using Java `_. Note that generally, there
are lots of correct answers to a given question.


Question1
~~~~~~~~~

In Java, input/output is done using streams. Streams are an
abstraction. Explain what this means and why it is important.


Answer
^^^^^^

A stream represents a source from which data can be read or a
destination to which data can be written. A stream is an abstraction
because it represents the abstract idea of a source or destination of
data, as opposed to specific, concrete sources and destinations such
as a particular file or network connection. The stream abstraction is
important because it allows programmers to do input/output using the
same methods for a wide variety of data sources and destinations. It
hides the details of working with files, networks, and the screen and
keyboard.


Question2
~~~~~~~~~

Java has two types of streams: character streams and byte streams.
Why? What is the difference between the two types of streams?


Answer
^^^^^^

Character streams are for working with data in human-readable format,
that is, data expressed as sequences of characters. Byte streams are
for data expressed in the machine-readable format that is used
internally in the computer to represent the data while a program is
running. It is very efficient for a computer to read and write data in
machine format, since no translation of the data is necessary.
However, if a person must deal directly with the data, then character
streams should be used so that the data is presented in human-readable
form.


Question3
~~~~~~~~~

What is a file? Why are files necessary?


Answer
^^^^^^

A file is a collection of data that has been given a name and stored
on some permanent storage device such as a hard disk or USB memory
stick. Files are necessary because data stored in the computer's RAM
is lost whenever the computer is turned off. Data that is to be saved
permanently must be stored in a file. (Furthermore, RAM is very
expensive compared to space on a disk drive, so a computer's hard disk
can typically store much more data than would fit in the computer's
RAM, even if the computer were left turned on all the time.)


Question4
~~~~~~~~~

What is the point of the following statement?


.. code-block:: java

    out = new PrintWriter( new FileWriter("data.dat") );


Why would you need a statement that involves two different stream
classes,PrintWriter and FileWriter?


Answer
^^^^^^

The PrintWriter class is being used as a "wrapper" for the FileWriter
class. AFileWriter is a stream object that knows how to send
individual characters to a file. By wrapping this in a PrintWriter,
you get the ability to write other data types such as ints, doubles,
andStrings to the file using the PrintWriter's print() and println()
methods. Wrapping the FileWriter in aPrintWriter adds capabilities to
the file output stream but still sends the data to the same
destination.


Question5
~~~~~~~~~

The package java.io includes a class named URL. What does an object of
type URL represent, and how is it used?


Answer
^^^^^^

A url is an address for a web page (or other information) on the
Internet. For example, "http://math.hws.edu/javanotes/index.html" is a
url that refers to the main page of the current edition of this on-
line textbook. A URL object represents such an address. Once you have
a URL object, you can call its openConnection() method to access the
information at the web address that it represents.


Question6
~~~~~~~~~

What is the purpose of the JFileChooser class?


Answer
^^^^^^

An object of type JFileChooser represents a dialog box that can be use
in a GUI program to let the user select a file that is to be used for
input or for output.


Question7
~~~~~~~~~

Explain what is meant by the client / server model of network
communication.


Answer
^^^^^^

In the client/server model, a server program runs on a computer
somewhere on the Internet and "listens" for connection requests from
client programs. The server makes some service available. A client
program connects to the server to access that service. For example, a
Web server has a collection of Web pages. A Web browser acts as a
client for the Web server. It makes a connection to the server and
sends a request for one of its pages. The server responds by
transmitting a copy of the requested page back to the client.


Question8
~~~~~~~~~

What is a socket ?


Answer
^^^^^^

A socket represents one endpoint of a network connection. A program
uses a socket to communicate with another program over the network.
Data written by a program to the socket at one end of the connection
is transmitted to the socket on the other end of the connection, where
it can be read by the program at that end.


Question9
~~~~~~~~~

What is a ServerSocket and how is it used?


Answer
^^^^^^

A SeverSocket is used by a server program to listen for connection
requests from client programs. Iflistener refers to an object that
belongs to Java'sServerSocket class, then calling the
functionlistener.accept() will wait for a connection request and will
return aSocket object that can be used to communicate with the client
that made the request.


Question10
~~~~~~~~~~

What is meant by an element in an XML document?


Answer
^^^^^^

An element consists of a tag (possibly containing attributes), a
matching end-tag, and everything in between. There are also empty
elements where an empty element consists of a single self-closing tag.
An element can contain textual content and nested elements. For
example, in the XML fragment


.. code-block:: java

    
    <testresult score="82"><name>Joe Smith</name><subject>Math</subject></testresult>


the entire fragment is an element, while <name>Joe Smith</name> and
<subject>Math</subject> are nested elements inside the <testresult>
element. "Joe Smith" and "Math" are examples of textual content, and
score is an attribute with value 82.


Question11
~~~~~~~~~~

What is it about XML that makes it suitable for representing almost
any type of data?


Answer
^^^^^^

XML is a syntax for building data representation languages. In XML,
the names of tags and the structure of a document can be chosen to be
whatever is most appropriate for the type of data that is being
represented. The tag names can be chosen to give meaningful
descriptions of the data. This contrasts with HTML documents, which
can include only a certain fixed set of tags. (XML also has the
advantage of being a widely accepted standard that is supported in
just about every programming language.)


Question12
~~~~~~~~~~

Write a complete program that will display the first ten lines from a
text file. The lines should be written to standard output, System.out.
The file name is given as the command-line argument args[0]. You can
assume that the file contains at least ten lines. Don't bother to make
the program robust. Do not useTextIO to process the file; use a
FileReader to access the file.


Answer
^^^^^^

I will give three different solutions. The first uses the non-
standardTextReader class from `Subsection11.1.4`_ to read the lines
from the file. The other two solutions the standard
classesBufferedReader and Scanner. All of these classes make it easy
to read a line of text from an input stream.

For each program, I do everything in one big try statement. If
anything goes wrong, an error message is printed in the catch clause
of the try statement. For example, if the program is run with no
command-line argument, an IndexOutOfBoundsException will be generated
when the program refers to args[0]. If a file is specified, but it
doesn't exist, then a FileNotFoundException will occur. (The exercise
says to assume that the file has at least ten lines, but if there are
fewer than ten lines in the file, TextReader and Scanner will throw an
exception, while BufferedReader will just print a null for each
missing line.)

Note, by the way, that the Scanner in the third program could have
been constructed from a File instead if from a FileReader.


.. code-block:: java

    import java.io.*;
    // (TextReader.class must be made available to this program.)
    public class TenLinesWithTextReader {
    
       public static void main(String[] args) {
          try {
             TextReader in = new TextReader( new FileReader(args[0]) );
             for (int lineCt = 0; lineCt < 10; lineCt++)) {
                String line = in.getln();
                System.out.println(line);
             }
          }
          catch (Exception e) {
             System.out.println("Error: " + e);
          }
       }
       
    }  // end class TenLinesWithTextReader
    
    //-----------------------------------------------------------------   
       
    import java.io.*;
    public class TenLinesWithBufferedReader {
    
       public static void main(String[] args) {
          try {
             BufferedReader in = new BufferedReader( new FileReader(args[0]) );
             for (int lineCt = 0; lineCt < 10; lineCt++)) {
                String line = in.readLine();
                System.out.println(line);
             }
          }
          catch (Exception e) {
             System.out.println("Error: " + e);
          }
       }
       
    }  // end clsss TenLinesWithBufferedReader
    
    //-----------------------------------------------------------------   
    
    import java.io.*;
    import java.util.Scanner;
    public class TenLinesWithScanner {
    
       public static void main(String[] args) {
          try {
             Scanner scanner = new Scanner( new FileReader(args[0]) );
             for (int lineCt = 0; lineCt < 10; lineCt++)) {
                String line = scanner.nextLine();
                System.out.println(line);
             }
          }
          catch (Exception e) {
             System.out.println("Error: " + e);
          }
       }
       
    }  // end clsss TenLinesWithScanner




