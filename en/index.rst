
Introduction to Programming Using Java
Version 6.0, June 2011

.. toctree::
   :hidden:

   1/index
   2/index
   3/index
   4/index
   5/index
   6/index
   7/index
   8/index
   9/index
   10/index
   11/index
   12/index
   13/index
   glossary

Preface
-------



Introduction to Programming Using Java is a free introductory
computer programming textbook that uses Java as the language of
instruction. It is suitable for use in an introductory programming
course and for people who are trying to learn programming on their
own. There are no prerequisites beyond a general familiarity with the
ideas of computers and programs. There is enough material for a full
year of college-level programming. Chapters 1 through 7 can be used as
a textbook in a one-semester college-level course or in a year-long
high school course. The remaining chapters can be covered in a second
course.

The Sixth Edition of the book covers "Java5.0", along with a few
features that were interoducted in Java6 and Java7. While Java5.0
introduced major new features that need to be covered in an
introductory programming course, Java6 and Java7 did not. Whenever the
text covers a feature that was not present in Java 5.0, that fact is
explicitly noted. Note that Java applets appear throughout the pages
of this book. Most of the applets require Java5.0 or higher.

The home web site for this book is `http://math.hws.edu/javanotes/`_.
The page at that address contains links for downloading a copy of the
web site and for downloading PDF versions of the book.




In style, this is a textbook rather than a tutorial. That is, it
concentrates on explaining concepts rather than giving step-by-step
how-to-do-it guides. I have tried to use a conversational writing
style that might be closer to classroom lecture than to a typical
textbook. You'll find programming exercises at the end of each
chapter, except for Chapter1. For each exercise, there is a web page
that gives a detailed solution for that exercise, with the sort of
discussion that I would give if I presented the solution in class. I
**strongly** advise that you read the exercise solutions if you want
to get the most out of this book.

This is certainly not a Java reference book, and it is not a
comprehensive survey of all the features of Java. It is **not**
written as a quick introduction to Java for people who already know
another programming language. Instead, it is directed mainly towards
people who are learning programming for the first time, and it is as
much about general programming concepts as it is about Java in
particular. I believe that Introduction to Programming using Java is
fully competitive with the conventionally published, printed
programming textbooks that are available on the market. (Well, all
right, I'll confess that I think it's better.)

There are several approaches to teaching Java. One approach uses
graphical user interface programming from the very beginning. Some
people believe that object oriented programming should also be
emphasized from the very beginning. This is **not** the approach that
I take. The approach that I favor starts with the more basic building
blocks of programming and builds from there. After an introductory
chapter, I cover procedural programming in Chapters 2, 3, and4.
Object-oriented programming is introduced in Chapter5. Chapter6 covers
the closely related topic of event-oriented programming and graphical
user interfaces. Arrays are covered in Chapter7. Chapter8 is a short
chapter that marks a turning point in the book, moving beyond the
fundamental ideas of programming to cover more advanced topics.
Chapter8 is about writing robust, correct, and efficient programs.
Chapters9 and 10 cover recursion and data structures, including the
Java Collection Framework. Chapter11 is about files and networking.
Chapter12 covers threads and parallel processing. Finally, Chapter13
returns to the topic of graphical user interface programming to cover
some of Java's more advanced capabilities.




Major changes were made for the **previous** (fifth) edition of this
book. Perhaps the most significant change was the use of parameterized
types in the chapter on generic programming. Parameterized types --
Java's version of templates -- were the most eagerly anticipated new
feature in Java5.0. Other new features in Java 5.0 were also
introduced in the fifth edition, including enumerated types, formatted
output, theScanner class, and variable arity methods. In addition,
Javadoc comments were covered for the first time.

The changes in this **sixth** edition are much smaller. The major
change is a new chapter on threads (`Chapter12`_). Material about
threads from the previous edition has been moved to this chapter, and
a good deal of new material has been added. Other changes include some
coverage of features added to Java in versions 6 and7 and the
inclusion of a glossary. There are also smaller changes throughout the
book.




The latest complete edition of Introduction to Programming using Java
is always available on line at`http://math.hws.edu/javanotes/`_. The
first version of the book was written in 1996, and there have been
several editions since then. All editions are archived at the
following Web addresses:


+ First edition: `http://math.hws.edu/eck/cs124/javanotes1/`_ (Covers
  Java 1.0.)
+ Second edition: `http://math.hws.edu/eck/cs124/javanotes2/`_ (Covers
  Java 1.1.)
+ Third edition: `http://math.hws.edu/eck/cs124/javanotes3/`_ (Covers
  Java 1.1.)
+ Fourth edition: `http://math.hws.edu/eck/cs124/javanotes4/`_ (Covers
  Java 1.4.)
+ Fifth edition: `http://math.hws.edu/eck/cs124/javanotes5/`_ (Covers
  Java 5.0.)
+ Sixth edition: `http://math.hws.edu/eck/cs124/javanotes6/`_ (Covers
  Java 5.0 and later.)


Introduction to Programming using Java is **free**, but it is not in
the public domain. As of Version 6.0, it is published under the terms
of the Creative Commons Attribution-NonCommercial-ShareAlike 3.0
License. To view a copy of this license, visit
`http://creativecommons.org/licenses/by-nc-sa/3.0/`_. For example, you
can:


+ Post an unmodified copy of the on-line version on your own Web site
  (including the parts that list the author and state the license under
  which it is distributed!).
+ Give away unmodified copies of this book or sell them at cost of
  production, as long as they meet the requirements of the license.
+ Make modified copies of the complete book or parts of it and post
  them on the web or otherwise distribute them non-commercially,
  provided that attribution to the author is given, the modifications
  are clearly noted, and the modified copies are distributed under the
  same license as the original. This includes translations to other
  languages.


For uses of the book in ways not covered by the license, permission of
the author is required.

While it is not actually required by the license, I do appreciate
hearing from people who are using or distributing my work.




**A technical note on production:** The on-line and PDF versions of
this book are created from a single source, which is written largely
in XML. To produce the PDF version, the XML is processed into a form
that can be used by the TeX typesetting program. In addition to XML
files, the source includes DTDs, XSLT transformations, Java source
code files, image files, a TeX macro file, and a couple of scripts
that are used in processing.

**I have made the complete source files available for download at the
following address:**

`http://math.hws.edu/eck/cs124/downloads/javanotes6-full-source.zip`_

These files were not originally meant for publication, and therefore
are not very cleanly written. Furthermore, it requires a fair amount
of expertise to use them effectively. However, I have had several
requests for the sources and have made them available on an "as-is"
basis. For more information about the source and how they are used see
the `README file`_ from the source download.




Professor David J. Eck
Department of Mathematics and Computer Science
Hobart and William Smith Colleges
300 Pulteney Street
Geneva, New York 14456, USA
Email: `eck@hws.edu`_
WWW: `http://math.hws.edu/eck/`_





`David Eck`_

.. _README file: http://math.hws.edu/javanotes/README-full-source.txt
.. _http://math.hws.edu/eck/cs124/javanotes3/: http://math.hws.edu/eck/cs124/javanotes3/
.. _http://math.hws.edu/eck/cs124/javanotes2/: http://math.hws.edu/eck/cs124/javanotes2/
.. _http://math.hws.edu/eck/cs124/downloads/javanotes6-full-source.zip: http://math.hws.edu/eck/cs124/downloads/javanotes6-full-source.zip
.. _eck@hws.edu: mailto:eck@hws.edu
.. _http://creativecommons.org/licenses/by-nc-sa/3.0/: http://creativecommons.org/licenses/by-nc-sa/3.0/
.. _http://math.hws.edu/eck/cs124/javanotes6/: http://math.hws.edu/eck/cs124/javanotes6/
.. _http://math.hws.edu/eck/cs124/javanotes5/: http://math.hws.edu/eck/cs124/javanotes5/
.. _http://math.hws.edu/eck/cs124/javanotes4/: http://math.hws.edu/eck/cs124/javanotes4/
.. _http://math.hws.edu/eck/cs124/javanotes1/: http://math.hws.edu/eck/cs124/javanotes1/
.. _12: http://math.hws.edu/javanotes/../c12/index.html
.. _http://math.hws.edu/eck/: http://math.hws.edu/eck/
.. _David Eck: http://math.hws.edu/eck/index.html
.. _http://math.hws.edu/javanotes/: http://math.hws.edu/javanotes/


