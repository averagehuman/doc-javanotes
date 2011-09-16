[ `Chapter Index`_ | `Main Index`_ ]





Programming Exercises for Chapter 13
------------------------------------



T his page contains several exercises for Chapter 13 in `Introduction
to Programming Using Java`_. For each exercise, a link to a possible
solution is provided. Each solution includes a discussion of how a
programmer might approach the problem and interesting points raised by
the problem or its solution, as well as complete source code of the
solution.




Exercise 13.1:
~~~~~~~~~~~~~~

The sample program `PaintWithOffScreenCanvas.java`_ from
:doc:`Section 13.1</13/s1>` is a simple paint program. Make two improvements to
this program: First, add a "File" menu that lets the user open an
image file and save the current image in either PNG or JPEG format.
Second, add a basic one-level "Undo" command that lets the user undo
the most recent operation that was applied to the image. (Do not try
to make a multilevel Undo, which would allow the user to undo several
operations.)

When you read a file into the program, you should copy the image that
you read into the program's off-screen canvas. Since the canvas in the
program has a fixed size, you should scale the image that you read so
that it exactly fills the canvas.

`See the Solution`_




Exercise 13.2:
~~~~~~~~~~~~~~

For this exercise, you should continue to work on the program from the
`previous exercise`_. Add a "StrokeWidth" menu that allows the user to
draw lines of varying thicknesses. Make it possible to use different
colors for the interior of a filled shape and for the outline of that
shape. To do this, change the "Color" menu to "StrokeColor" and add a
"FillColor" menu. (My solution adds two new tools, "Stroked Filled
Rectangle" and "Stroked Filled Oval", to represent filled shapes that
are outlined with the current stroke.) Add support for filling shapes
with transparent color. A simple approach to this is to use a
JCheckboxMenuItem to select either fully opaque or 50% opaque fill.
(Don't try to apply transparency to stokes -- it's very difficult to
make transparency work correctly for the Curve tool, and in any case,
shape outlines look better if they are opaque.) Finally, make the
menus more user friendly by adding some keyboard accelerators to some
commands and by using JRadioButtonMenuItems where appropriate, such as
in the color and tool menus. This exercise takes quite a bit of work
to get it all right, so you should tackle the problem in pieces.

Here is an applet version of my solution to the program. Since an
applet does not have access to files on the computer where it is
running, the "File" menu is non-functional in this applet. Keyboard
accelerators for menu commands are probably also non-functional in the
applet.



`See the Solution`_




Exercise 13.3:
~~~~~~~~~~~~~~

The StopWatchLabel component from `Subsection13.4.5`_ displays the
text "Timing..." when the stop watch is running. It would be nice if
it displayed the elapsed time since the stop watch was started. For
that, you need to create aTimer. (See `Subsection6.5.1`_.) Add a Timer
to the original source code, `StopWatchLabel.java`_, to drive the
display of the elapsed time in seconds. Create the timer in the
mousePressed() routine when the stop watch is started. Stop the timer
in the mousePressed() routine when the stop watch is stopped. The
elapsed time won't be very accurate anyway, so just show the integral
number of seconds. You only need to set the text a few times per
second. For my Timer method, I use a delay of 200 milliseconds for the
timer. Here is an applet that tests my solution to this exercise:



`See the Solution`_




Exercise 13.4:
~~~~~~~~~~~~~~

The custom component example `MirrorText.java`_, from
`Subsection13.4.5`_, uses an off-screen canvas to show mirror-reversed
text in a JPanel. An alternative approach would be to draw the text
after applying a transform to the graphics context that is used for
drawing. (See `Subsection13.2.5`_.) With this approach, the custom
component can be defined as a subclass of JLabel in which the
paintComponent() method is overridden. Write a version of the
MirrorText component that takes this approach. The solution is very
short, but tricky. Note that the scale transform g2.scale(-1,1) does a
left-right reflection through the left edge of the component.

`See the Solution`_




Exercise 13.5:
~~~~~~~~~~~~~~

The sample program `PhoneDirectoryFileDemo.java`_ from
`Subsection11.3.2`_ keeps data for a "phone directory" in a file in
the user's home directory. `Exercise11.5`_ asked you to revise that
program to use an XML format for the data. Both programs have a simple
command-line user interface. For this exercise, you should provide a
GUI interface for the phone directory data. You can base your program
either on the original sample program or on the modified version from
the exercise. Use a JTable to hold the data. The user should be able
to edit all the entries in the table. Also, the user should be able to
add and delete rows. Include either buttons or menu commands that can
be used to perform these actions. The delete command should delete the
selected row, if any. New rows should be added at the end of the
table. For this program, you can use a standard DefaultTableModel.

Your program should load data from the file when it starts and save
data to the file when it ends, just as the two previous programs do.
For a GUI program, you can't simply save the data at the end of the
main() routine, since main() terminates as soon as the window shows up
on the screen. You want to save the data when the user closes the
window and ends the program. There are several approaches. One is to
use a WindowListener to detect the event that occurs when the window
closes. Another is to use a "Quit" command to end the program; when
the user quits, you can save the data and close the window (by calling
its dispose() method), and end the program. If you use the "Quit"
command approach, you don't want the user to be able to end the
program simply by closing the window. To accomplish this, you should
call


.. code-block:: java

    frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);


where frame refers to the JFrame that you have created for the
program's user interface. When using aWindowListener, you want the
close box on the window to close the window, not end the program. For
this, you need


.. code-block:: java

    frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);


When the listener is notified of a window closed event, it can save
the data and end the program.

Most of the JTable and DefaultTableModel methods that you need for
this exercise are discussed in `Subsection13.4.3`_, but there are a
few more that you need to know about. To determine which row is
selected in a JTable, calltable.getSelectedRow(). This method returns
the row number of the selected row, or returns -1 if no row is
selected. To specify which cell is currently being edited, you can
use:


.. code-block:: java

    table.setRowSelectionInterval(rowNum, rowNum);  // Selects row number rowNum. 
    table.editCellAt( rowNum, colNum ); // Edit cell at position (rowNum,colNum).
    phoneTable.getEditorComponent().requestFocus();  // Put input cursor in cell.


One particularly troublesome point is that the data that is in the
cell that is currently being edited is not in the table model. The
value in the edit cell is not put into the table model until after the
editing is finished. This means that even though the user sees the
data in the cell, it's not really part of the table data yet. If you
lose that data, the user would be justified in complaining. To make
sure that you get the right data when you save the data at the end of
the program, you have to turn off editing before retrieving the data
from the model. This can be done with the following method:


.. code-block:: java

    private void stopEditing() {
       if (table.getCellEditor() != null)
          table.getCellEditor().stopCellEditing();
    }


This method must also be called before modifying the table by adding
or deleting rows; if such modifications are made while editing is in
progress, the effect can be very strange.

`See the Solution`_



[ `Chapter Index`_ | `Main Index`_ ]

.. _PhoneDirectoryFileDemo.java: http://math.hws.edu/javanotes/c13/../source/PhoneDirectoryFileDemo.java
.. _Chapter Index: http://math.hws.edu/javanotes/c13/index.html
.. _11.5: http://math.hws.edu/javanotes/c13/../c11/ex5-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c13/ex4-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c13/ex5-ans.html
.. _13.4.3: http://math.hws.edu/javanotes/c13/../c13/s4.html#GUI2.4.3
.. _See the Solution: http://math.hws.edu/javanotes/c13/ex3-ans.html
.. _13.4.5: http://math.hws.edu/javanotes/c13/../c13/s4.html#GUI2.4.5
.. _PaintWithOffScreenCanvas.java: http://math.hws.edu/javanotes/c13/../source/PaintWithOffScreenCanvas.java
.. _See the Solution: http://math.hws.edu/javanotes/c13/ex1-ans.html
.. _See the Solution: http://math.hws.edu/javanotes/c13/ex2-ans.html
.. _Main Index: http://math.hws.edu/javanotes/c13/../index.html
.. _MirrorText.java: http://math.hws.edu/javanotes/c13/../source/MirrorText.java
.. _6.5.1: http://math.hws.edu/javanotes/c13/../c6/s5.html#GUI1.5.1
.. _previous exercise: http://math.hws.edu/javanotes/c13/../c13/ex1-ans.html
.. _13.1: http://math.hws.edu/javanotes/c13/../c13/s1.html
.. _11.3.2: http://math.hws.edu/javanotes/c13/../c11/s3.html#IO.3.2
.. _13.2.5: http://math.hws.edu/javanotes/c13/../c13/s2.html#GUI2.2.5
.. _StopWatchLabel.java: http://math.hws.edu/javanotes/c13/../source/StopWatchLabel.java


