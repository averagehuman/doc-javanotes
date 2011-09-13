[ `Quiz Answers`_ | `Chapter Index`_ | `Main Index`_ ]





Quiz on Chapter 13
------------------

T his page contains questions on Chapter 13 of ` Introduction to
Programming Using Java `_. You should be able to answer these
questions after studying that chapter. Sample answers to these
questions can be found `here`_.
Question1:
Describe the object that is created by the following statement, and
give an example of how it might be used in a program:


.. code-block:: java

    BufferedImage OSC = new BufferedImage(32,32,BufferedImage.TYPE_INT_RGB);

Question2:
Many programs depend on resource files . What is meant by a resource
in this sense? Give an example.
Question3:
What is the FontMetrics class used for?
Question4:
If a Color, c, is created asc=newColor(0,0,255,125), what is the
effect of drawing with this color?
Question5:
What is antialiasing ?
Question6:
How is the ButtonGroup class used?
Question7:
What does the acronym MVC stand for, and how does it apply to
theJTable class?
Question8:
Describe the picture that is produced by the followingpaintComponent()
method:


.. code-block:: java

    
    public void paintComponent(Graphics g) {
       super.paintComponent(g);
       Graphics2D g2 = (Graphics2D)g;
       g2.translate( getWidth()/2, getHeight()/2 );
       g2.rotate( 30 * Math.PI / 180 );
       g2.fillRect(0,0,100,100);
    }

Question9:
What is meant by Internationalization of a program?
Question10:
Suppose that the class that you are writing has an instance
methoddoOpen() (with no parameters) that is meant to be used to open a
file selected by the user. Write a code segment that creates anAction
that represents the action of opening a file. Then show how to create
a button and a menu item from that action.



[ `Quiz Answers`_ | `Chapter Index`_ | `Main Index`_ ]

.. _Chapter Index: http://math.hws.edu/javanotes/c13/index.html
.. _Main Index: http://math.hws.edu/javanotes/c13/../index.html
.. _Quiz Answers: http://math.hws.edu/javanotes/c13/quiz_answers.html


