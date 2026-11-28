"""
========================================================
PROBLEM: REVERSE LINKED LIST
TOPIC: LINKED LIST
APPROACH: ITERATIVE POINTER REVERSAL
========================================================
1. PROBLEM DESCRIPTION
--------------------------------------------------------
Given the head of a singly linked list, reverse the list and return the new head.
A singly linked list is made of nodes. Each node stores:
1. A value.
2. A pointer called next, which points to the next node.
Example:
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
IMPORTANT:
We do not reverse the values inside the nodes.
We change the direction of the next pointers.
The old first node becomes the last node.
The old last node becomes the new head.
2. MY APPROACH: ITERATIVE POINTER REVERSAL
--------------------------------------------------------
We use three pointers:
1. prev: the previous node. It starts as None.
2. curr: the node we are currently processing. It starts at head.
3. temp: temporarily saves the next node before we change curr.next.
MAIN IDEA:
For each node:
1. Save the next node in temp.
2. Point the current node backwards to prev.
3. Move prev to the current node.
4. Move curr to the saved next node.
Repeat until curr becomes None.
At the end, prev points to the new head.
3. PYTHON SOLUTION
--------------------------------------------------------
"""


class ListNode:
    """A single node in a singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


"""
4. COMPLETE ELS10 EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------
A. THE NODE CLASS
class ListNode:
Creates a blueprint for one linked-list node.
def __init__(self, val=0, next=None):
Runs when we create a new node.
self.val = val
Stores the node's value.
self.next = next
Stores the reference to the next node.
None means that there is no next node.
NOTE:
LeetCode already provides ListNode. The class above is included so this file can run independently.
B. THE SOLUTION FUNCTION
def reverseList(self, head: ListNode | None) -> ListNode | None:
Defines a method named reverseList.
head is the first node of the original linked list.
ListNode | None means head can be a node or None.
The return type means the result can also be a node or None.
C. INITIALIZE prev
prev = None
Creates a pointer named prev.
It represents the part of the list that has already been reversed.
At the beginning, no node has been reversed.
Therefore, prev is None.
Why None?
The old first node must become the last node.
The last node must point to None.
D. INITIALIZE curr
curr = head
Makes curr point to the first node.
curr is the node we are currently processing.
We use curr to walk through the original list.
E. THE WHILE LOOP
while curr is not None:
Continue while curr points to a real node.
When curr becomes None, we have passed the original last node.
At that point, every node has been processed.
F. SAVE THE NEXT NODE
temp = curr.next
Saves the node after curr.
Why must we do this before changing curr.next?
Because we are about to reverse curr.next.
If we change the pointer first, we could lose access to the rest of the original list.
Example:
curr is node 2.
Before:
2 -> 3
temp saves node 3.
G. REVERSE THE CURRENT POINTER
curr.next = prev
Makes the current node point to the previous node.
This is the actual reversal.
Example:
Before:
1 -> 2 -> 3
Suppose curr is node 2 and prev is node 1.
After this line:
2 -> 1
Node 2 no longer points to node 3.
That is why temp had to save node 3 first.
H. MOVE prev FORWARD
prev = curr
The current node is now the first node in the reversed part.
So prev moves to curr.
Example:
prev now points to node 2.
The reversed part is:
2 -> 1 -> None
I. MOVE curr FORWARD
curr = temp
Moves curr to the next node in the original list.
We use temp because curr.next has already been changed.
Example:
temp points to node 3.
After this line, curr points to node 3.
The next loop iteration processes node 3.
J. RETURN THE NEW HEAD
return prev
When the loop finishes, curr is None.
prev points to the last node of the original list.
That node is now the first node of the reversed list.
Therefore, prev is the new head.
5. COMPLETE DRY RUN
--------------------------------------------------------
Input:
1 -> 2 -> 3 -> None
INITIAL STATE:
prev = None
curr = node 1
temp = not assigned yet
ITERATION 1:
curr = node 1
Step 1: temp = curr.next
temp points to node 2.
Step 2: curr.next = prev
node 1 -> None
Step 3: prev = curr
prev points to node 1.
Step 4: curr = temp
curr points to node 2.
State:
Reversed part: 1 -> None
Remaining part: 2 -> 3 -> None
ITERATION 2:
curr = node 2
Step 1: temp = curr.next
temp points to node 3.
Step 2: curr.next = prev
node 2 -> node 1
Step 3: prev = curr
prev points to node 2.
Step 4: curr = temp
curr points to node 3.
State:
Reversed part: 2 -> 1 -> None
Remaining part: 3 -> None
ITERATION 3:
curr = node 3
Step 1: temp = curr.next
temp is None.
Step 2: curr.next = prev
node 3 -> node 2
Step 3: prev = curr
prev points to node 3.
Step 4: curr = temp
curr becomes None.
State:
Reversed part: 3 -> 2 -> 1 -> None
Remaining part: None
STOP:
curr is None, so the while loop ends.
RETURN:
prev points to node 3.
Final output:
3 -> 2 -> 1 -> None
6. WHY THE ORDER OF THE FOUR LINES MATTERS
--------------------------------------------------------
These four lines must stay in this order:
temp = curr.next
curr.next = prev
prev = curr
curr = temp
First, save the next node so it is not lost.
Second, reverse the current pointer.
Third, move the previous pointer forward.
Fourth, move to the saved next node.
If you change curr.next before saving it, you can lose the remaining list.
7. TIME COMPLEXITY
--------------------------------------------------------
O(N)
N = number of nodes in the linked list.
The while loop visits each node exactly once.
For every node, we do a fixed number of pointer operations:
1. Read curr.next.
2. Change curr.next.
3. Move prev.
4. Move curr.
Each operation takes constant time, O(1).
For N nodes, the total work grows in proportion to N.
Therefore:
TIME COMPLEXITY = O(N)
8. SPACE COMPLEXITY
--------------------------------------------------------
O(1) AUXILIARY SPACE
We use only three pointer variables:
prev, curr, and temp.
We do not create another linked list.
We do not use a stack, recursion, or another data structure that grows with N.
The existing nodes are changed in place.
Therefore:
AUXILIARY SPACE COMPLEXITY = O(1)
IMPORTANT:
The input linked list itself is not counted as extra space.
9. EDGE CASES
--------------------------------------------------------
EDGE CASE 1: EMPTY LIST
Input: None
Expected: None
Reason:
curr starts as None.
The while loop does not run.
prev is returned as None.
EDGE CASE 2: ONE NODE
Input: 7 -> None
Expected: 7 -> None
Reason:
The node's next pointer is already None.
The loop processes it once and returns that same node.
EDGE CASE 3: TWO NODES
Input: 1 -> 2 -> None
Expected: 2 -> 1 -> None
Reason:
The pointer between the two nodes is reversed.
EDGE CASE 4: FIVE NODES
Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
Expected: 5 -> 4 -> 3 -> 2 -> 1 -> None
Reason:
Every next pointer is reversed.
EDGE CASE 5: DUPLICATE VALUES
Input: 1 -> 2 -> 2 -> 3 -> None
Expected: 3 -> 2 -> 2 -> 1 -> None
Reason:
Nodes are reversed by their links. Equal values do not cause a problem.
EDGE CASE 6: NEGATIVE VALUES
Input: -1 -> -2 -> 3 -> None
Expected: 3 -> -2 -> -1 -> None
Reason:
The algorithm changes pointers, not values.
10. COMMON MISTAKES
--------------------------------------------------------
1. Changing curr.next before saving curr.next in temp.
   This can disconnect the remaining nodes.
2. Moving curr to curr.next after reversing the pointer.
   curr.next now points backwards. Move curr to temp instead.
3. Returning head.
   head is the old first node, which is now the last node.
   Return prev because prev is the new head.
4. Forgetting prev = None.
   The old first node must point to None after reversal.
5. Using a new list unnecessarily.
   This solution reverses the existing links in place.
11. MY LEARNING CHECKLIST
--------------------------------------------------------
[ ] I understand what a singly linked list is.
[ ] I understand what head points to.
[ ] I understand what a node's next pointer stores.
[ ] I understand what None means.
[ ] I understand why prev starts as None.
[ ] I understand why curr starts at head.
[ ] I understand why we need temp.
[ ] I understand why temp must save curr.next first.
[ ] I understand how curr.next = prev reverses a link.
[ ] I understand why prev = curr moves the reversed-list head.
[ ] I understand why curr = temp moves through the original list.
[ ] I understand why the loop stops when curr is None.
[ ] I understand why we return prev, not head.
[ ] I can dry-run the algorithm with three nodes.
[ ] I understand why the solution changes links, not node values.
[ ] I understand why time complexity is O(N).
[ ] I understand why auxiliary space complexity is O(1).
[ ] I can write the solution without looking.
========================================================
"""


def build_linked_list(values):
    """Build a linked list from a Python list and return its head."""
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def linked_list_to_list(head):
    """Convert a linked list to a Python list for testing."""
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([], []),
        ([7], [7]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [3, 2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2, 2, 3], [3, 2, 2, 1]),
        ([-1, -2, 3], [3, -2, -1]),
        ([0, 0, 0], [0, 0, 0]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([100], [100]),
    ]
    passed = 0
    print("REVERSE LINKED LIST - TEST RESULTS")
    print("----------------------------------------------")
    for input_values, expected in test_cases:
        head = build_linked_list(input_values)
        result_head = solution.reverseList(head)
        actual = linked_list_to_list(result_head)
        print("Input:", input_values)
        print("Expected:", expected)
        print("Actual:", actual)
        if actual == expected:
            print("Status: PASS")
            passed += 1
        else:
            print("Status: FAIL")
        print("----------------------------------------------")
    print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")