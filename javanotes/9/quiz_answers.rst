



Answers for Quiz on Chapter 9
-----------------------------

T his page contains sample answers to the quiz on Chapter 9 of `
Introduction to Programming Using Java `_. Note that generally, there
are lots of correct answers to a given question.


Question1
~~~~~~~~~

Explain what is meant by a recursive subroutine.


Answer
^^^^^^

A recursive subroutine is simply one that calls itself either directly
or through a chain of calls involving other subroutines.


Question2
~~~~~~~~~

Consider the following subroutine:


.. code-block:: java

    static void printStuff(int level) {
        if (level == 0) {
           System.out.print("*");
        }
        else {
           System.out.print("[");
           printStuff(level - 1);
           System.out.print(",");
           printStuff(level - 1);
           System.out.println("]");
        }
    }


Show the output that would be produced by the subroutine
callsprintStuff(0), printStuff(1), printStuff(2), andprintStuff(3).


Answer
^^^^^^

The outputs are:


.. code-block:: java

    printStuff(0) outputs:   *
    printStuff(1) outputs:   [*,*]
    printStuff(2) outputs:   [[*,*],[*,*]]
    printStuff(3) outputs:   [[[*,*],[*,*]],[[*,*],[*,*]]]


(Explanation: For printStuff(0), the value of the parameter is 0, so
the first clause of the if is executed, and the output is just *. For
printStuff(1), the else clause is executed. This else clause contains
two recursive calls to printStuff(level-1). Sincelevel is 1, level-1
is 0, so each call to printStuff outputs a *. The overall output from
printStuff(1) is [*,*]. In a similar way, printStuff(2) includes two
recursive calls toprintStuff(1). Each call to printStuff(1) outputs
[*,*]. AndprintStuff(2) just takes two copies of this and puts them
between [ and ] separated by a comma: [[*,*],[*,*]]. Finally, the
output fromprintStuff(3) outputs two copies of [[*,*],[*,*]] separated
by a comma and enclosed between brackets. Once you recognize the
pattern, you can doprintStuff(N) for any N without trying to follow
the execution of the subroutine in detail.)


Question3
~~~~~~~~~

Suppose that a linked list is formed from objects that belong to the
class


.. code-block:: java

    class ListNode {
       int item;       // An item in the list.
       ListNode next;  // Pointer to next item in the list.
    }


Write a subroutine that will count the number of zeros that occur in a
given linked list of ints. The subroutine should have a parameter of
type ListNode and should return a value of type int.


Answer
^^^^^^

I'll give both a non-recursive solution and a recursive solution. For
a linked list, the recursion is not really necessary, but it does
nicely reflect the recursive definition ofListNode


.. code-block:: java

    
    static int countZeros( ListNode head ) {
       int count;        // The number of zeros in the list.
       ListNode runner;  // For running along the list.
       count = 0;
       runner = head;    // Start at the beginning of the list.
       while (runner != null) {
          if ( runner.item == 0)
             count++;  // Count the zero found in the current node.
          runner = runner.next;  // Advance to the next node.
       }
       return count;
    }
    
    static int countZerosRecursively( ListNode head ) {
       if ( head == null) {
              // An empty list does not contain any zeros.
           return 0;
       }
       else {
           int count = countZerosRecursively( head.next );  // Count zeros in tail.
           if ( head.item == 0 )
               count++;  // Add 1 to account for the zero in the head node.
           return count;
       }
    }



Question4
~~~~~~~~~

What are the three operations on a stack?


Answer
^^^^^^

The three stack operations are push , pop, and isEmpty. The
definitions of these operations are:push(item) adds the specified item
to the top of the stack;pop() removes the top item of the stack and
returns it; andisEmpty() is a boolean-valued function that returns
true if there are no items on the stack.


Question5
~~~~~~~~~

What is the basic difference between a stack and a queue?


Answer
^^^^^^

In a stack, items are added to the stack and removed from the stack on
the same end (called the "top" of the stack). In a queue, items are
added at one end (the "back") and removed at the other end (the
"front"). Because of this difference, a queue is a FIFO structure
(items are removed in the same order in which they were added), and a
stack is a LIFO structure (the item that is popped from a stack is the
one that was added most recently).


Question6
~~~~~~~~~

What is an activation record ? What role does a stack of activation
records play in a computer?


Answer
^^^^^^

When a subroutine is called, an activation record is created to hold
the information that is needed for the execution of the subroutine,
such as the values of the parameters and local variables. This
activation record is stored on a stack of activation records. A stack
is used since one subroutine can call another, which can then call a
third, and so on. Because of this, many activation records can be in
use at the same time. The data structure is a stack because an
activation record has to continue to exist while all the subroutines
that are called by the subroutine are executed. While they are being
executed, the stack of activation records can grow and shrink as
subroutines are called and return.


Question7
~~~~~~~~~

Suppose that a binary tree of integers is formed from objects
belonging to the class


.. code-block:: java

    class TreeNode {
       int item;       // One item in the tree.
       TreeNode left;  // Pointer to the left subtree.
       TreeNode right; // Pointer to the right subtree.
    }


Write a recursive subroutine that will find the sum of all the nodes
in the tree. Your subroutine should have a parameter of type TreeNode,
and it should return a value of type int.


Answer
^^^^^^


.. code-block:: java

    static int treeSum( TreeNode root ) {
           // Find the sum of all the nodes in the tree to which root points.
        if ( root == null ) {
              // The sum of the nodes in an empty tree is zero.
           return 0;
        }
        else {
              // Add the item in the root to the sum of the
              // items in the left subtree and the sum of the
              // items in the right subtree.
           int total = root.item;
           total += treeSum( root.left );
           total += treeSum( root.right );
           return total;
        }
     }



Question8
~~~~~~~~~

What is a postorder traversal of a binary tree?


Answer
^^^^^^

In a traversal of a binary tree, all the nodes are processed in some
way. (For example, they might be printed.) In a postorder traversal,
the order of processing is defined by the rule: For each node, the
nodes in the left subtree of that node are processed first. Then the
nodes in the right subtree are processed. Finally, the node itself is
processed. This rule is applied at all levels of the tree.


Question9
~~~~~~~~~

Suppose that a <multilist> is defined by the BNF rule


.. code-block:: java

    <multilist>  ::=  <word>  |  "(" [ <multilist> ]... ")"


where a <word> can be any sequence of letters. Give five different
<multilist>'s that can be generated by this rule. (This rule, by the
way, is almost the entire syntax of the programming languageLISP! LISP
is known for its simple syntax and its elegant and powerful
semantics.)


Answer
^^^^^^

Here are five possibilities (out of an infinite number of
possibilities), with some explanation:


.. code-block:: java

    fred  --  A <multilist> can just be a word, such as "fred".
              
    ( )   --  The [ ]... around <multilist> means that there can be
              any number of nested <multilist>'s, including zero.  If
              there are zero, then all that's left is the empty
              parentheses.
              
    ( fred mary chicago ) -- A <multilist> consisting of three
                             <multilist>'s -- "fred", "mary", and
                             "chicago" -- inside parentheses
                             
    ( ( able ) ( baker charlie ) ) -- A <multilist> containing two
                                      <multilist>'s.
                                      
    ( ( a ( b ) ) ( c ( d e ) g ) )  -- Even more nesting.



Question10
~~~~~~~~~~

Explain what is meant by parsing a computer program.


Answer
^^^^^^

To parse a computer program means to determine its syntactic
structure, that is, to figure out how it can be constructed using the
rules of a grammar (such as a BNF grammar).



