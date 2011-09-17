

Answers for Quiz on Chapter 13
------------------------------

This page contains sample answers to the quiz on Chapter 13 of
Introduction to Programming Using Java. Note that generally, there
are lots of correct answers to a given question.


Question1
~~~~~~~~~

Describe the object that is created by the following statement, and
give an example of how it might be used in a program:


.. code-block:: java

    BufferedImage OSC = new BufferedImage(32,32,BufferedImage.TYPE_INT_RGB);



Answer
^^^^^^

A BufferedImage is a region in memory that can be used as a drawing
surface. In this statement, the image that is created is 32 pixels
wide and 32 pixels high, and the color of each pixel is an RGB color
that has red, green, and blue components in the range 0 to 255. The
picture in a BufferedImage can easily be copied into a graphics
context g by calling one of the ``g.drawImage`` methods. However, since the
image is so small in this case, it seems more likely that is going to
be used to define an ImageIcon or perhaps a Cursor.


Question2
~~~~~~~~~

Many programs depend on resource files . What is meant by a resource
in this sense? Give an example.


Answer
^^^^^^

In addition to the program code itself, programs often use other types
of data such as images and sounds. These are said to be resources for
the program. In order to run, the program must be able to locate and
load the resources. An example of a resource is a small image file
that will be used by the program to define a custom cursor.


Question3
~~~~~~~~~

What is the FontMetrics class used for?


Answer
^^^^^^

An object that belongs to the class FontMetrics can be used to obtain
information about the sizes of characters and strings that are drawn
in a specific font. The font is specified when the FontMetrics object
is created. If fm is a variable of type FontMetrics, then, for
example, ``fm.stringWidth(str)`` gives the width of the string str and
``fm.getHeight()`` is the usual amount of vertical space allowed for one
line of text. This information could be used, for example, for
positioning the string in a component.


Question4
~~~~~~~~~

If a Color, c, is created as ``c = new Color(0,0,255,125)``, what is the
effect of drawing with this color?


Answer
^^^^^^

When a color is constructed from four integers, the fourth parameter
is the alpha component of the color. When drawing, the alpha component
is interpreted as the degree of opaqueness of the color. If the alpha
component is less than its maximum possible value, 255, then the color
is partially transparent. In this case, c represents a blue color that
is about 50% transparent. When a pixel is colored withc, the pixel
does not become entirely blue. Instead, the new color of the pixel is
obtained by blending c with the previous color of the pixel. The
effect is like adding a blue tint to the pixel, or like looking at the
previous color of the pixel through blue-colored glass.


Question5
~~~~~~~~~

What is antialiasing ?


Answer
^^^^^^

Antialiasing is used to make shapes that are drawn look less "jagged."
The jaggedness is called "aliasing," and it arises because shapes have
to be drawn by coloring individual pixels. If antialiasing is off,
then the only decision is either to color a pixel or not to color it.
As a result, a boundary that should be a smooth curve will look like a
jagged staircase. When antialiasing is on, the amount of color that is
applied to a pixel depends on how much of that pixel is covered by the
ideal geometric shape. For pixels along the boundary of the shape, the
color of the shape will be blended with the previous color of the
pixel. Although antialiasing does not produce a perfect result, it
does tend to make pictures look better.


Question6
~~~~~~~~~

How is the ButtonGroup class used?


Answer
^^^^^^

A ButtonGroup object is used with a set of radio buttons (or radio
button menu items), to make sure that at most one of the radio buttons
in the group can be selected at any given time. To use the ButtonGroup
class, you have to create a ButtonGroup object,grp. Then each radio
button, ``rb``, that is supposed to be part of the group is added to the
group by calling ``grp.add(rb)``. Nothing further needs to be done with
the ButtonGroup object.


Question7
~~~~~~~~~

What does the acronym MVC stand for, and how does it apply to
the ``JTable`` class?


Answer
^^^^^^

MVC stands for "Model-View-Controller." In a JTable, the view is the
actual visible component on the screen. The model is the collection of
data that specifies, among other things, what appears in each cell of
the table and in the column headings. The model is represented by a
separate object from the object that represents the view. The
controller is responsible for interaction with the user. It consists
mostly of a bunch of listener objects that listen for events generated
when the user interacts with the table. The listeners respond by
making changes in the model, which will in turn cause a change in the
view.


Question8
~~~~~~~~~

Describe the picture that is produced by the following ``paintComponent()``
method:


.. code-block:: java

    
    public void paintComponent(Graphics g) {
       super.paintComponent(g);
       Graphics2D g2 = (Graphics2D)g;
       g2.translate( getWidth()/2, getHeight()/2 );
       g2.rotate( 30 * Math.PI / 180 );
       g2.fillRect(0,0,100,100);
    }



Answer
^^^^^^

This shows a filled black square that is 100-by-100 pixels in size.
The corner of the square is at the center of the component that is
being painted, and the top side of the square descends at a 30 degree
angle from that point. (The translate command moves the origin, ``(0,0)``
to the point ``(getWidth()/2, getHeight()/2)``, so that when the fillRect
command places the corner of the square at ``(0,0)``, the corner actually
appears at the center of the component. Furthermore, the rotate
command rotates the picture by 30 degrees in a clockwise direction
about the origin. This means that the top of the square is rotated
from the horizontal position onto a line that is 30 degrees clockwise
of the horizontal. That line descends at a 30 degree angle.


Question9
~~~~~~~~~

What is meant by Internationalization of a program?


Answer
^^^^^^

Internationalization refers to writing the program in a way that will
make it easy to adapt the program for use in a variety of "locales."
For example, it should be easy to translate all the strings that are
used in the program into other languages. To make this possible the
strings should not be hard coded into the program itself. Instead,
they are placed in a separate resource file, so that the program can
be translated into another language simply by writing a resource file
for that language. Internationalization also applies to the format
that is used for dates and numbers.)


Question10
~~~~~~~~~~

Suppose that the class that you are writing has an instance
method ``doOpen()`` (with no parameters) that is meant to be used to open a
file selected by the user. Write a code segment that creates anAction
that represents the action of opening a file. Then show how to create
a button and a menu item from that action.


Answer
^^^^^^

Here is the code for the three parts of the problem:


.. code-block:: java

    Action openAction = new AbstractAction( "Open..." ) {
       public void actionPerformed( ActionEvent e ) {
          doOpen();
       }
    };
    
    JButton openButton = new JButton( openAction );
       
    JMenuItem openCommand = new JMenuItem( openAction );


(Since Action is only an interface, the class AbstractAction has to be
used to create the action object. The most natural way to write the
code is to create an anonymous inner class that is a subclass
ofAbstractAction. This subclass must define the actionPerformed()
method -- which in this case only has to call the doOpen() method. As
an alternative to creating the JMenuItem, the action could have simply
been added directly to a JMenu. By the way, the "..." in the name of
the action is there, by convention, to tell the user that selecting
this command will cause a dialog box to pop up.)



