



Quiz on Chapter 6
-----------------

T his page contains questions on Chapter 6 of ` Introduction to
Programming Using Java `_. You should be able to answer these
questions after studying that chapter. Sample answers to these
questions can be found `here`_.


Question1
~~~~~~~~~

Programs written for a graphical user interface have to deal with
"events." Explain what is meant by the term event. Give at least two
different examples of events, and discuss how a program might respond
to those events.


Question2
~~~~~~~~~

Explain carefully what therepaint() method does.


Question3
~~~~~~~~~

What is HTML?


Question4
~~~~~~~~~

Java has a standard class called JPanel. Discuss **two** ways in which
JPanels can be used.


Question5
~~~~~~~~~

Draw the picture that will be produced by the following
paintComponent() method:


.. code-block:: java

    public static void paintComponent(Graphics g) {
        super.paintComponent(g);
        for (int i=10; i <= 210; i = i + 50)
           for (int j = 10; j <= 210; j = j + 50)
              g.drawLine(i,10,j,60);
    }



Question6
~~~~~~~~~

Suppose you would like a panel that displays a green square inside a
red circle, as illustrated. Write a paintComponent() method for the
panel class that will draw the image.




Question7
~~~~~~~~~

Java has a standard class called MouseEvent. What is the purpose of
this class? What does an object of type MouseEvent do?


Question8
~~~~~~~~~

One of the main classes in Swing is the JComponent class. What is
meant by a component? What are some examples?


Question9
~~~~~~~~~

What is the function of aLayoutManager in Java?


Question10
~~~~~~~~~~

What type of layout manager is being used for each of the three panels
in the following illustration from :doc:`Section 6.7</6/s7>`?




Question11
~~~~~~~~~~

Explain how Timers are used to do animation.


Question12
~~~~~~~~~~

What is a JCheckBox and how is it used?



