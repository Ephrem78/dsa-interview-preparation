
"""
========================================================
PROBLEM: MIN STACK
TOPIC: STACK
APPROACH: LINKED LIST + MINIMUM STORED IN EACH NODE
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Design a stack that supports four operations:

1. push(val):
   Adds a number to the top of the stack.

2. pop():
   Removes the top number from the stack.

3. top():
   Returns the top number without removing it.

4. getMin():
   Returns the smallest number in the stack.

IMPORTANT:

Every operation must have O(1) time complexity.

This means every operation must take constant time,
regardless of how many elements are in the stack.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Operations:
push(-2)
push(0)
push(-3)
getMin()
pop()
top()
getMin()

Output:
[None, None, None, -3, None, 0, -2]

Explanation:

After push(-2):
Stack = [-2]
Minimum = -2

After push(0):
Stack = [-2, 0]
Minimum = -2

After push(-3):
Stack = [-2, 0, -3]
Minimum = -3

getMin():
Returns -3.

pop():
Removes -3.

top():
Returns 0.

getMin():
Returns -2.


Example 2:

Operations:
push(5)
push(3)
push(7)
getMin()
pop()
getMin()

Output:
[None, None, None, 3, None, 3]

Explanation:

5 is the first element.
3 becomes the new minimum.
7 does not change the minimum.

After removing 7, the minimum is still 3.


Example 3:

Operations:
push(4)
push(4)
push(2)
getMin()
pop()
getMin()

Output:
[None, None, None, 2, None, 4]

Explanation:

We push 4 twice.

Then we push 2.

The minimum becomes 2.

After removing 2, the minimum becomes 4.

The duplicate 4 is handled correctly.


3. MY APPROACH: LINKED LIST + MINIMUM IN EACH NODE
--------------------------------------------------------

I use a Linked List.

Each node stores three things:

1. val:
   The actual number stored in the node.

2. min:
   The smallest number from this node down
   to the bottom of the stack.

3. next:
   A reference to the next node below it.

I also use a variable called head.

head:
Points to the top node of the stack.

IMPORTANT IDEA:

Every node remembers the minimum value
from its position down to the bottom.

This means the top node always contains
the current minimum of the entire stack.

We do not need to search through the stack.

MY STEPS:

1. Create a MinStack class.

2. Create a Node class inside MinStack.

3. Store val, min, and next inside each node.

4. Initialize head as None.

5. When push() is called:
   - If the stack is empty, the new value is the minimum.
   - Otherwise, compare the new value with the previous minimum.
   - Store the smaller value in the new node.
   - Connect the new node to the previous head.
   - Move head to the new node.

6. When pop() is called:
   - Move head to head.next.
   - The previous node is removed from the stack.

7. When top() is called:
   - Return head.val.

8. When getMin() is called:
   - Return head.min.

Because the minimum is already stored,
all four operations take O(1) time.


4. COMPLETE PYTHON SOLUTION
--------------------------------------------------------
"""

from __future__ import annotations


class MinStack:

    # Node class: stores one element of the stack
    class Node:

        def __init__(self, val: int, min_val: int,
                     next_node: Node | None):

            self.val = val
            self.min = min_val
            self.next = next_node

    # Initialize an empty stack
    def __init__(self):

        self.head = None

    # Add a number to the top of the stack
    def push(self, val: int) -> None:

        if self.head is None:

            self.head = self.Node(val, val, None)

        else:

            self.head = self.Node(
                val,
                min(val, self.head.min),
                self.head
            )

    # Remove the top number
    def pop(self) -> None:

        if self.head is None:
            raise IndexError("Cannot pop from an empty stack")

        self.head = self.head.next

    # Return the top number
    def top(self) -> int:

        if self.head is None:
            raise IndexError("Stack is empty")

        return self.head.val

    # Return the smallest number
    def getMin(self) -> int:

        if self.head is None:
            raise IndexError("Stack is empty")

        return self.head.min


"""
5. DETAILED EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------


A. IMPORT FUTURE ANNOTATIONS
--------------------------------------------------------

from __future__ import annotations

What does this do?

Allows Python to handle type hints that refer
to classes before those classes are fully defined.

Example:

next_node: Node | None

This means:

next_node can contain a Node object
or None.

None means there is no next node.

This import makes the forward reference to Node
work correctly.


B. CREATE THE MIN STACK CLASS
--------------------------------------------------------

class MinStack:

What does this do?

Creates a class called MinStack.

A class is a blueprint for creating objects.

We will create an object like this:

min_stack = MinStack()

That object will contain its own stack.

The stack will have its own head pointer.


C. CREATE THE NODE CLASS
--------------------------------------------------------

class Node:

What is a Node?

A node is one element of a linked list.

Our Node stores three things:

1. val
2. min
3. next

Example:

A node can look like this:

val = 5
min = 3
next = another Node

The actual number is 5.

The smallest number from this node down
to the bottom of the stack is 3.

The next reference connects this node
to the node below it.


D. NODE CONSTRUCTOR
--------------------------------------------------------

def __init__(self, val: int, min_val: int,
             next_node: Node | None):

What does __init__ mean?

It is a constructor.

Python automatically calls it when we create
a new Node object.

Example:

Node(5, 3, None)

The constructor receives:

val = 5
min_val = 3
next_node = None

self means the current Node object.


self.val = val

Stores the actual number inside the node.

Example:

self.val = 5

The node now remembers that its value is 5.


self.min = min_val

Stores the minimum number for this node.

IMPORTANT:

This is not necessarily the same as val.

Example:

val = 10
min_val = 3

The node stores:

val = 10
min = 3

Why?

Because 3 is the smallest number from this node
down to the bottom of the stack.


self.next = next_node

Connects this node to the next node.

In our stack, next points to the node below it.

If there is no node below it:

self.next = None


E. INITIALIZE THE STACK
--------------------------------------------------------

def __init__(self):

What does this do?

Runs automatically when we create a MinStack object.

Example:

min_stack = MinStack()

Python calls this constructor.


self.head = None

What is head?

head is a reference to the top node of our stack.

Initially, the stack is empty.

Therefore:

head = None

None means that head does not point to any node.

IMPORTANT:

We use head to access the top of the stack
without searching through the linked list.


F. PUSH OPERATION
--------------------------------------------------------

def push(self, val: int) -> None:

What does this function do?

Adds a new number to the top of the stack.

val:
The number we want to add.

-> None:
Means the function does not return a value.


if self.head is None:

What does this check?

Checks whether the stack is empty.

If head is None:

There is no node in the stack.

We must create the first node.


self.head = self.Node(val, val, None)

What does this do?

Creates a new Node.

It receives three arguments:

1. val
2. val
3. None

Why do we use val twice?

Because the first number is automatically
the smallest number in the stack.

Example:

push(10)

The new node stores:

val = 10
min = 10
next = None

Now head points to this node.

The stack contains:

10


else:

What does this mean?

The stack is not empty.

There is already a node at the top.

We need to create a new node
and calculate its minimum.


self.head = self.Node(
    val,
    min(val, self.head.min),
    self.head
)

This is the most important part of push().

Let's understand each argument.


FIRST ARGUMENT:

val

The new number we want to add.

Example:

push(5)

The new node's actual value is 5.


SECOND ARGUMENT:

min(val, self.head.min)

What does min() do?

Returns the smaller of two numbers.

We compare:

1. The new number.
2. The previous minimum.

Example 1:

Previous minimum = 10
New number = 5

min(5, 10)

Result:

5

The new minimum becomes 5.


Example 2:

Previous minimum = 5
New number = 20

min(20, 5)

Result:

5

The minimum stays 5.


Example 3:

Previous minimum = -3
New number = -10

min(-10, -3)

Result:

-10

The new minimum becomes -10.

IMPORTANT:

We do not search through the stack.

We only compare two numbers:

The new value and the previous minimum.


THIRD ARGUMENT:

self.head

What does this mean?

Connects the new node to the previous top node.

Before pushing:

HEAD → 10 → None

We push 5.

The new node becomes:

5 → 10 → None

Finally:

self.head = new_node

Moves head to the new node.

Now:

HEAD → 5 → 10 → None

The new node is the top of the stack.


G. POP OPERATION
--------------------------------------------------------

def pop(self) -> None:

What does this function do?

Removes the top node from the stack.

-> None means it does not return a value.


if self.head is None:

Checks whether the stack is empty.

If it is empty, there is nothing to remove.


raise IndexError("Cannot pop from an empty stack")

What does raise mean?

It creates an error and stops the operation.

We use it because popping an empty stack
is not a valid operation.

The coding problem normally guarantees
that pop() is called on a non-empty stack.


self.head = self.head.next

This is the most important line in pop().

It moves head to the next node.

Example:

BEFORE POP:

HEAD → 5 → 10 → 20 → None

The top value is 5.

After pop():

HEAD → 10 → 20 → None

The node containing 5 is no longer part
of the stack.

IMPORTANT:

We do not calculate the minimum again.

Why?

Because the new top node already stores
the correct minimum for the remaining stack.

This is why our approach is efficient.


H. TOP OPERATION
--------------------------------------------------------

def top(self) -> int:

What does this function do?

Returns the top number of the stack.

It does not remove the number.


if self.head is None:

Checks whether the stack is empty.

If it is empty, there is no top element.


raise IndexError("Stack is empty")

Raises an error because we cannot read
the top of an empty stack.


return self.head.val

What does this do?

Returns the actual value stored in the top node.

Example:

HEAD → 5 → 10 → 20 → None

self.head.val = 5

Therefore:

top() returns 5.

IMPORTANT:

The node stays in the stack.

top() only reads the value.


I. GET MIN OPERATION
--------------------------------------------------------

def getMin(self) -> int:

What does this function do?

Returns the smallest number in the stack.


if self.head is None:

Checks whether the stack is empty.

If it is empty, there is no minimum.


raise IndexError("Stack is empty")

Raises an error because an empty stack
does not have a minimum value.


return self.head.min

This is the most important line of the problem.

What does it do?

Returns the minimum value stored
inside the top node.

Example:

HEAD → (val=5, min=3)
       (val=10, min=10)
       (val=20, min=20)

self.head.min = 3

Therefore:

getMin() returns 3.

Why is this O(1)?

Because the minimum is already stored.

We do not need a loop.

We do not need to search through the stack.

We simply read one value.


6. COMPLETE DRY RUN
--------------------------------------------------------

Let's use this sequence:

push(-2)
push(0)
push(-3)
getMin()
pop()
top()
getMin()


INITIAL STATE:

head = None

The stack is empty.


OPERATION 1: push(-2)
--------------------------------------------------------

We call:

push(-2)

The stack is empty.

Therefore, we execute:

self.head = self.Node(-2, -2, None)

The new node stores:

val = -2
min = -2
next = None

STACK:

HEAD → (-2, -2, None)

Current minimum:

-2


OPERATION 2: push(0)
--------------------------------------------------------

We call:

push(0)

The stack is not empty.

Previous minimum:

self.head.min = -2

New value:

val = 0

We calculate:

min(0, -2)

Result:

-2

The new node stores:

val = 0
min = -2
next = previous head

STACK:

HEAD → (0, -2)
       (-2, -2)

Current minimum:

-2


OPERATION 3: push(-3)
--------------------------------------------------------

We call:

push(-3)

Previous minimum:

-2

New value:

-3

We calculate:

min(-3, -2)

Result:

-3

The new node stores:

val = -3
min = -3
next = previous head

STACK:

HEAD → (-3, -3)
       (0, -2)
       (-2, -2)

Current minimum:

-3


OPERATION 4: getMin()
--------------------------------------------------------

We call:

getMin()

The function executes:

return self.head.min

The top node stores:

min = -3

Output:

-3

The stack does not change.


OPERATION 5: pop()
--------------------------------------------------------

We call:

pop()

The function executes:

self.head = self.head.next

The top node containing -3 is removed.

The new head points to the node containing 0.

STACK:

HEAD → (0, -2)
       (-2, -2)

Current minimum:

-2

IMPORTANT:

We did not search for the new minimum.

The new head already stores -2.


OPERATION 6: top()
--------------------------------------------------------

We call:

top()

The function executes:

return self.head.val

The top node contains:

val = 0

Output:

0

The stack does not change.


OPERATION 7: getMin()
--------------------------------------------------------

We call:

getMin()

The function executes:

return self.head.min

The top node contains:

min = -2

Output:

-2


FINAL RESULTS:

getMin() = -3
top() = 0
getMin() = -2


7. TIME COMPLEXITY
--------------------------------------------------------

O(1) FOR EVERY OPERATION.

Where:

O(1) = Constant Time.

This means the operation does not become slower
when the stack gets bigger.


1. PUSH()

Time complexity = O(1)

Why?

We:

- Create one new node.
- Compare two numbers.
- Connect the new node.
- Update head.

We never search through the stack.

Therefore:

push() = O(1)


2. POP()

Time complexity = O(1)

Why?

We only execute:

self.head = self.head.next

We move one pointer.

We do not search for the next node.

Therefore:

pop() = O(1)


3. TOP()

Time complexity = O(1)

Why?

We only read:

self.head.val

No loop is needed.

Therefore:

top() = O(1)


4. GET MIN()

Time complexity = O(1)

Why?

We only read:

self.head.min

The minimum was calculated and stored
when the node was created.

No searching is needed.

Therefore:

getMin() = O(1)


FINAL TIME COMPLEXITY:

push()   = O(1)
pop()    = O(1)
top()    = O(1)
getMin() = O(1)


8. SPACE COMPLEXITY
--------------------------------------------------------

O(N)

Where:

N = Number of elements in the stack.

Why?

Every push() creates one new node.

Each node stores:

1. val
2. min
3. next

If we push 5 numbers:

We create 5 nodes.

If we push 100 numbers:

We create 100 nodes.

Therefore, memory grows with the number
of elements in the stack.

FINAL SPACE COMPLEXITY:

O(N)


IMPORTANT:

The stack stores two integer values
and one reference in every node.

The extra minimum value does not change
the overall space complexity.

It remains O(N).


9. MY OWN TEST CASES
--------------------------------------------------------

TEST 1: STANDARD EXAMPLE

Operations:

push(-2)
push(0)
push(-3)
getMin()
pop()
top()
getMin()

Expected outputs:

None
None
None
-3
None
0
-2


TEST 2: INCREASING NUMBERS

Operations:

push(1)
push(2)
push(3)
getMin()
top()

Expected outputs:

None
None
None
1
3

Reason:

The minimum stays 1.


TEST 3: DECREASING NUMBERS

Operations:

push(5)
push(4)
push(3)
getMin()
top()

Expected outputs:

None
None
None
3
3

Reason:

Every new number becomes the minimum.


TEST 4: DUPLICATE MINIMUMS

Operations:

push(4)
push(4)
push(2)
getMin()
pop()
getMin()

Expected outputs:

None
None
None
2
None
4

Reason:

After removing 2, the previous minimum is 4.


TEST 5: NEGATIVE NUMBERS

Operations:

push(-5)
push(-10)
push(-3)
getMin()
pop()
getMin()

Expected outputs:

None
None
None
-10
None
-5

Reason:

-10 is the smallest number.

After removing -3, -10 is still in the stack.

Correction to understand:
The pop removes -3, not -10, because -3 is on top.


TEST 6: ONE ELEMENT

Operations:

push(100)
top()
getMin()
pop()

Expected outputs:

None
100
100
None


TEST 7: POP THE CURRENT MINIMUM

Operations:

push(10)
push(5)
push(2)
pop()
getMin()
pop()
getMin()

Expected outputs:

None
None
None
None
5
None
10

Reason:

First, 2 is the minimum.

After removing 2, the minimum becomes 5.

After removing 5, the minimum becomes 10.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a Stack is.
[ ] I understand LIFO.
[ ] I understand what a Linked List is.
[ ] I understand what a Node is.
[ ] I understand the purpose of val.
[ ] I understand the purpose of min.
[ ] I understand the purpose of next.
[ ] I understand what head means.
[ ] I understand why head starts as None.
[ ] I understand how the Node constructor works.
[ ] I understand how push() creates a new node.
[ ] I understand why push() compares two minimum values.
[ ] I understand how min() works.
[ ] I understand how the new node connects to the old head.
[ ] I understand how pop() moves the head pointer.
[ ] I understand why pop() does not recalculate the minimum.
[ ] I understand why top() only reads the value.
[ ] I understand why getMin() reads head.min.
[ ] I understand why duplicate minimums work.
[ ] I understand how negative numbers work.
[ ] I understand why every operation is O(1).
[ ] I understand why space complexity is O(N).
[ ] I can write the complete solution without looking.

========================================================
10. TESTING THE SOLUTION
========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

test_cases = [

    # Test 1: Standard example
    (
        [
            ("push", -2),
            ("push", 0),
            ("push", -3),
            ("getMin", None),
            ("pop", None),
            ("top", None),
            ("getMin", None)
        ],
        [None, None, None, -3, None, 0, -2]
    ),

    # Test 2: Increasing numbers
    (
        [
            ("push", 1),
            ("push", 2),
            ("push", 3),
            ("getMin", None),
            ("top", None)
        ],
        [None, None, None, 1, 3]
    ),

    # Test 3: Decreasing numbers
    (
        [
            ("push", 5),
            ("push", 4),
            ("push", 3),
            ("getMin", None),
            ("top", None)
        ],
        [None, None, None, 3, 3]
    ),

    # Test 4: Duplicate minimums
    (
        [
            ("push", 4),
            ("push", 4),
            ("push", 2),
            ("getMin", None),
            ("pop", None),
            ("getMin", None)
        ],
        [None, None, None, 2, None, 4]
    ),

    # Test 5: Negative numbers
    (
        [
            ("push", -5),
            ("push", -10),
            ("push", -3),
            ("getMin", None),
            ("pop", None),
            ("getMin", None)
        ],
        [None, None, None, -10, None, -10]
    ),

    # Test 6: One element
    (
        [
            ("push", 100),
            ("top", None),
            ("getMin", None),
            ("pop", None)
        ],
        [None, 100, 100, None]
    ),

    # Test 7: Remove the current minimum
    (
        [
            ("push", 10),
            ("push", 5),
            ("push", 2),
            ("pop", None),
            ("getMin", None),
            ("pop", None),
            ("getMin", None)
        ],
        [None, None, None, None, 5, None, 10]
    )
]


passed = 0

print("MIN STACK - TEST RESULTS")
print("------------------------")

for test_number, (operations, expected) in enumerate(test_cases, start=1):

    min_stack = MinStack()
    actual = []

    for operation, value in operations:

        if operation == "push":
            result = min_stack.push(value)

        elif operation == "pop":
            result = min_stack.pop()

        elif operation == "top":
            result = min_stack.top()

        elif operation == "getMin":
            result = min_stack.getMin()

        actual.append(result)

    print("TEST:", test_number)
    print("Expected:", expected)
    print("Actual:  ", actual)

    if actual == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
