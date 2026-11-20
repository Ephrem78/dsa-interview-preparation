
"""
========================================================
PROBLEM: LARGEST RECTANGLE IN HISTOGRAM
TOPIC: STACK
APPROACH: MONOTONIC INCREASING STACK
========================================================
1. PROBLEM DESCRIPTION
--------------------------------------------------------
Given a list of integers called heights:
Each integer represents the height of one histogram bar.
The width of every bar is 1.
Return the largest rectangular area that can be formed inside the histogram.
In simple words:
Find the biggest rectangle that can fit inside the histogram.
IMPORTANT:
A rectangle can cover multiple neighboring bars.
The rectangle's height cannot be greater than the shortest bar it covers.
Formula:
AREA = HEIGHT * WIDTH
2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------
Example 1:
Input:
heights = [2, 1, 5, 6, 2, 3]
Output:
10
Explanation:
The bars with heights 5 and 6 can form a rectangle with:
Height = 5
Width = 2
Area = 5 * 2 = 10
Therefore:
Largest area = 10
Example 2:
Input:
heights = [2, 4]
Output:
4
Explanation:
Bar 1: Height = 2, Width = 1, Area = 2
Bar 2: Height = 4, Width = 1, Area = 4
Largest area = 4
Example 3:
Input:
heights = [2, 2, 2, 2]
Output:
8
Explanation:
All four bars have height 2.
We can create one rectangle using all four bars.
Height = 2
Width = 4
Area = 2 * 4 = 8
3. MY APPROACH: MONOTONIC INCREASING STACK
--------------------------------------------------------
I use one main data structure:
1. STACK
The stack stores the INDICES of histogram bars.
IMPORTANT:
We store indices, not heights.
Why?
Because we need to calculate the rectangle's width.
We need to know where a bar starts and ends.
MY STEPS:
1. Create maxArea and initialize it to zero.
2. Create an empty stack.
3. Find the number of bars.
4. Visit every bar, including one extra imaginary bar.
5. Use zero as the height of the extra bar.
6. Compare the current height with the height represented by the top index of the stack.
7. While the current height is smaller:
   a. Pop the previous index.
   b. Get the popped bar's height.
   c. Calculate the rectangle's width.
   d. Calculate its area.
   e. Update maxArea if the area is larger.
8. Push the current index onto the stack.
9. Continue until every bar and the extra imaginary bar have been processed.
10. Return maxArea.
WHY DO WE USE A MONOTONIC INCREASING STACK?
The stack stores indices whose corresponding heights are in increasing order.
Example:
heights = [2, 3, 5, 6]
stack = [0, 1, 2, 3]
The represented heights are:
[2, 3, 5, 6]
They are increasing.
When a shorter bar appears, we pop the previous bars because their rectangles cannot extend through the shorter bar.
4. PYTHON SOLUTION
--------------------------------------------------------
"""
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Store the largest rectangle area found so far
        maxArea = 0
        # Create a stack to store bar indices
        stack = []
        # Find the number of histogram bars
        n = len(heights)
        # Visit every bar and one extra imaginary bar
        for i in range(n + 1):
            # Use zero as the height of the extra bar
            currentHeight = 0 if i == n else heights[i]
            # Pop bars while the current bar is shorter
            while stack and currentHeight < heights[stack[-1]]:
                # Remove the previous bar's index
                height = heights[stack.pop()]
                # Calculate the rectangle's width
                width = i if not stack else i - stack[-1] - 1
                # Calculate the rectangle's area
                area = height * width
                # Keep the largest area
                maxArea = max(maxArea, area)
            # Push the current index onto the stack
            stack.append(i)
        # Return the largest rectangle area
        return maxArea
"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------
class Solution:
Creates a class called Solution.
LeetCode commonly uses this class structure.
def largestRectangleArea(self, heights: list[int]) -> int:
Creates a function called largestRectangleArea.
self:
Refers to the current object of the class.
heights:
The input list containing histogram bar heights.
list[int]:
Means that heights is a list of integers.
-> int:
Means that the function returns one integer.
A. INITIALIZE THE MAXIMUM AREA
--------------------------------------------------------
maxArea = 0
Creates a variable called maxArea.
It stores the largest rectangle area found so far.
Why start with zero?
Because we have not calculated any rectangle yet.
Example:
maxArea = 0
Later, if we find an area of 10:
maxArea = 10
If we find an area of 12:
maxArea = 12
We always keep the largest area.
B. CREATE THE STACK
--------------------------------------------------------
stack = []
Creates an empty Python list.
We use this list as a stack.
A stack follows LIFO:
LAST IN, FIRST OUT.
Python provides two important stack operations:
append() = Push an element onto the stack.
pop() = Remove the last element from the stack.
IMPORTANT:
We store INDICES inside the stack.
We do not directly store heights.
Example:
heights = [2, 3, 5]
stack = [0, 1, 2]
This means:
Index 0 represents height 2.
Index 1 represents height 3.
Index 2 represents height 5.
Why store indices?
Because we need to calculate the rectangle's width.
The width depends on the positions of the bars.
C. FIND THE NUMBER OF BARS
--------------------------------------------------------
n = len(heights)
len() counts the number of elements in a list.
Example:
heights = [2, 1, 5, 6, 2, 3]
n = 6
The valid indices are:
0, 1, 2, 3, 4, 5
D. VISIT EVERY BAR AND ONE EXTRA BAR
--------------------------------------------------------
for i in range(n + 1):
This loop visits every real bar and one extra imaginary bar.
Why n + 1 instead of n?
Normally:
range(n)
visits:
0, 1, 2, ..., n - 1
But:
range(n + 1)
visits:
0, 1, 2, ..., n
The final index n does not represent a real bar.
We use it to process the bars still waiting inside the stack.
Example:
n = 6
range(7) gives:
0, 1, 2, 3, 4, 5, 6
Index 6 is the extra imaginary bar.
E. CREATE THE IMAGINARY ZERO HEIGHT
--------------------------------------------------------
currentHeight = 0 if i == n else heights[i]
This is a Python conditional expression.
It has two possible results.
PART 1:
i == n
Checks whether we have reached the extra index.
If true:
currentHeight = 0
PART 2:
else heights[i]
If i is not equal to n:
currentHeight = heights[i]
That means we use the actual height of the current bar.
Example:
heights = [2, 1, 5]
When i = 0:
currentHeight = 2
When i = 1:
currentHeight = 1
When i = 2:
currentHeight = 5
When i = 3:
currentHeight = 0
Why do we use zero?
The extra zero-height bar is smaller than every positive histogram bar.
It forces the remaining bars to be popped from the stack.
Without it, some bars might never be processed after the loop finishes.
IMPORTANT:
The zero is imaginary.
We do not add it to the original heights list.
F. CHECK THE STACK AND COMPARE HEIGHTS
--------------------------------------------------------
while stack and currentHeight < heights[stack[-1]]:
THIS IS THE MOST IMPORTANT LINE IN THE ALGORITHM.
Let's understand each part.
PART 1: stack
Checks whether the stack is not empty.
An empty list is False in Python.
A non-empty list is True.
Why?
Because we cannot access the top element if the stack is empty.
PART 2: stack[-1]
Gets the last element of the stack.
This is the top of our stack.
Example:
stack = [0, 2, 4]
stack[-1] = 4
Remember:
The stack stores indices.
PART 3: heights[stack[-1]]
Uses the top index to get the corresponding height.
Example:
heights = [2, 1, 5, 6, 2]
stack = [0, 2, 3]
stack[-1] = 3
heights[stack[-1]] = heights[3]
Result:
6
PART 4: currentHeight
Represents the height of the current bar.
Example:
heights = [2, 1, 5, 6, 2]
When i = 4:
currentHeight = 2
PART 5: COMPARE THE HEIGHTS
currentHeight < heights[stack[-1]]
Asks:
Is the current bar shorter than the bar at the top of the stack?
Example:
Current height = 2.
Top stack height = 6.
Comparison:
2 < 6
Result:
True.
We have found a shorter bar.
This means the bar with height 6 cannot extend its rectangle any further to the right.
We can now calculate its maximum possible area.
WHY DO WE USE WHILE INSTEAD OF IF?
One shorter bar can make several previous bars finish their possible rectangles.
Example:
heights = [2, 3, 5, 6, 1]
Before processing the final 1:
stack = [0, 1, 2, 3]
Current height = 1.
The current bar is shorter than:
6, 5, 3, and 2.
We need to pop several indices.
A single if statement would only pop one index.
The while loop continues until the stack is empty or the top bar is no longer taller than the current bar.
WHY DO WE USE < INSTEAD OF <=?
The algorithm uses:
currentHeight < heights[stack[-1]]
Equal heights are allowed to remain in the stack.
Example:
heights = [2, 2, 2]
The equal heights stay in the stack.
When the imaginary zero arrives, they are popped.
The width calculation still allows the rectangle to cover all three bars.
Therefore, the algorithm handles equal heights correctly without using <=.
G. POP THE PREVIOUS INDEX AND GET ITS HEIGHT
--------------------------------------------------------
height = heights[stack.pop()]
This line performs two operations.
PART 1:
stack.pop()
Removes and returns the last index from the stack.
Example:
stack = [0, 1, 2]
stack.pop() returns 2.
After popping:
stack = [0, 1]
PART 2:
heights[stack.pop()]
Uses the removed index to get its height.
Example:
heights = [2, 3, 5]
The popped index is 2.
Therefore:
height = heights[2]
height = 5
IMPORTANT:
We remove the index, but save the actual height in the variable called height.
WHY CAN WE CALCULATE THE AREA NOW?
Because the current bar is shorter.
The popped bar cannot extend its rectangle any further to the right.
We have found its first shorter bar on the right.
The stack also helps us identify the boundary on the left.
H. CALCULATE THE RECTANGLE WIDTH
--------------------------------------------------------
width = i if not stack else i - stack[-1] - 1
THIS IS THE SECOND MOST IMPORTANT LINE.
It calculates how many neighboring bars the popped bar can cover.
Let's understand both situations.
SITUATION 1: THE STACK IS EMPTY
if not stack
Means there are no remaining indices in the stack.
The popped bar has no shorter bar on its left inside the histogram.
Therefore, its rectangle can extend from index 0 up to index i - 1.
The width is:
width = i
Example:
heights = [2, 3, 5, 6, 1]
Suppose we pop all previous bars when we reach 1.
After popping the last remaining index:
stack = []
Current index:
i = 4
Width:
width = 4
The rectangle covers indices:
0, 1, 2, 3
There are four bars.
Therefore:
width = 4
SITUATION 2: THE STACK IS NOT EMPTY
If the stack still contains indices:
stack[-1]
is the index of the nearest remaining bar to the left.
That bar is shorter than or equal to the popped bar.
The rectangle cannot include that remaining bar as a bar of greater height.
Therefore, the rectangle starts one position after that index.
The current bar is also excluded because it is shorter.
Formula:
width = i - stack[-1] - 1
Example:
heights = [2, 1, 5, 6, 2, 3]
Suppose:
i = 4
The current height is 2.
We pop the index representing height 6.
After popping:
stack = [0, 1, 2]
The top index is:
stack[-1] = 2
The popped bar's height was 6.
Width:
width = 4 - 2 - 1
width = 1
The rectangle covers only index 3.
Now suppose we pop the bar with height 5.
After popping:
stack = [0, 1]
The top index is:
stack[-1] = 1
Width:
width = 4 - 1 - 1
width = 2
The rectangle covers indices:
2 and 3.
This is why we subtract 1:
We exclude the left boundary and the current shorter bar.
I. CALCULATE THE RECTANGLE AREA
--------------------------------------------------------
area = height * width
The rectangle area is:
HEIGHT * WIDTH
Example:
height = 5
width = 2
area = 5 * 2
area = 10
J. UPDATE THE LARGEST AREA
--------------------------------------------------------
maxArea = max(maxArea, area)
Python's max() function returns the larger of two values.
Example:
maxArea = 8
area = 10
maxArea = max(8, 10)
Result:
maxArea = 10
Another example:
maxArea = 10
area = 6
maxArea = max(10, 6)
Result:
maxArea = 10
We never replace the largest area with a smaller one.
K. PUSH THE CURRENT INDEX
--------------------------------------------------------
stack.append(i)
Adds the current index to the top of the stack.
Why?
Because the current bar might form a larger rectangle with future bars.
We keep its index until a shorter bar appears.
Example:
stack = [0, 1]
i = 2
After:
stack.append(i)
stack = [0, 1, 2]
IMPORTANT:
We push the index, not currentHeight.
This allows us to access both the position and the height later.
L. RETURN THE MAXIMUM AREA
--------------------------------------------------------
return maxArea
Returns the largest rectangle area found during the entire algorithm.
Every bar is eventually processed.
The extra zero-height bar ensures that the remaining bars are also processed.
6. COMPLETE DRY RUN
--------------------------------------------------------
Input:
heights = [2, 1, 5, 6, 2, 3]
INITIAL STATE:
maxArea = 0
stack = []
n = 6
ITERATION 1:
i = 0
currentHeight = 2
Stack is empty.
Nothing to pop.
Push index 0.
stack = [0]
maxArea = 0
ITERATION 2:
i = 1
currentHeight = 1
Stack:
[0]
Top index:
0
Top height:
heights[0] = 2
Compare:
1 < 2
TRUE.
Pop index 0.
height = 2
Stack is now empty.
Width:
width = i
width = 1
Area:
area = 2 * 1
area = 2
Update:
maxArea = max(0, 2)
maxArea = 2
Push index 1.
stack = [1]
ITERATION 3:
i = 2
currentHeight = 5
Stack:
[1]
Top height:
heights[1] = 1
Compare:
5 < 1
FALSE.
Push index 2.
stack = [1, 2]
maxArea = 2
ITERATION 4:
i = 3
currentHeight = 6
Stack:
[1, 2]
Top height:
heights[2] = 5
Compare:
6 < 5
FALSE.
Push index 3.
stack = [1, 2, 3]
maxArea = 2
ITERATION 5:
i = 4
currentHeight = 2
Stack:
[1, 2, 3]
Top height:
heights[3] = 6
Compare:
2 < 6
TRUE.
POP INDEX 3:
height = 6
Stack:
[1, 2]
Width:
width = 4 - 2 - 1
width = 1
Area:
area = 6 * 1
area = 6
Update:
maxArea = max(2, 6)
maxArea = 6
CHECK THE WHILE LOOP AGAIN.
Top index:
2
Top height:
heights[2] = 5
Compare:
2 < 5
TRUE.
POP INDEX 2:
height = 5
Stack:
[1]
Width:
width = 4 - 1 - 1
width = 2
Area:
area = 5 * 2
area = 10
Update:
maxArea = max(6, 10)
maxArea = 10
CHECK THE WHILE LOOP AGAIN.
Top index:
1
Top height:
heights[1] = 1
Compare:
2 < 1
FALSE.
Stop the while loop.
Push index 4.
stack = [1, 4]
maxArea = 10
ITERATION 6:
i = 5
currentHeight = 3
Stack:
[1, 4]
Top height:
heights[4] = 2
Compare:
3 < 2
FALSE.
Push index 5.
stack = [1, 4, 5]
maxArea = 10
ITERATION 7: EXTRA IMAGINARY BAR
i = 6
Because i == n:
currentHeight = 0
This is our imaginary bar.
Stack:
[1, 4, 5]
Top index:
5
Top height:
heights[5] = 3
Compare:
0 < 3
TRUE.
POP INDEX 5:
height = 3
Stack:
[1, 4]
Width:
width = 6 - 4 - 1
width = 1
Area:
area = 3 * 1
area = 3
maxArea remains 10.
CHECK THE WHILE LOOP AGAIN.
Top index:
4
Top height:
heights[4] = 2
Compare:
0 < 2
TRUE.
POP INDEX 4:
height = 2
Stack:
[1]
Width:
width = 6 - 1 - 1
width = 4
Area:
area = 2 * 4
area = 8
maxArea remains 10.
CHECK THE WHILE LOOP AGAIN.
Top index:
1
Top height:
heights[1] = 1
Compare:
0 < 1
TRUE.
POP INDEX 1:
height = 1
Stack:
[]
Width:
width = 6
Area:
area = 1 * 6
area = 6
maxArea remains 10.
The stack is empty.
Push the imaginary index 6.
stack = [6]
The loop finishes.
FINAL RESULT:
maxArea = 10
Largest rectangle area = 10
7. WHY THIS IS A MONOTONIC INCREASING STACK
--------------------------------------------------------
A monotonic stack keeps its stored values in a consistent order.
In this problem, the stack stores indices.
The heights represented by those indices remain in increasing order from bottom to top.
Example:
heights = [2, 3, 5, 6]
stack = [0, 1, 2, 3]
Represented heights:
[2, 3, 5, 6]
This is increasing order.
Now suppose the next height is 1.
1 is smaller than 6.
We pop index 3.
1 is smaller than 5.
We pop index 2.
1 is smaller than 3.
We pop index 1.
1 is smaller than 2.
We pop index 0.
The stack becomes empty.
Then we push the current index.
WHY IS THIS USEFUL?
When we pop a bar:
1. We know its first shorter bar on the right.
2. We can use the remaining stack to find its left boundary.
3. We can calculate its maximum possible width.
4. We can calculate its maximum possible area.
We avoid checking every possible rectangle.
8. TIME COMPLEXITY
--------------------------------------------------------
O(N)
Where:
N = Number of histogram bars.
There are two important operations.
1. FOR LOOP
for i in range(n + 1):
The loop visits N real bars and one extra bar.
Therefore, it runs N + 1 times.
We ignore the constant 1 in Big O notation.
Time complexity = O(N)
2. STACK OPERATIONS
stack.append(i)
Every index is pushed onto the stack at most once.
Total pushes = N + 1
stack.pop()
Every real bar index is popped at most once.
Total pops <= N
IMPORTANT:
The while loop is inside the for loop.
It may look like O(N²).
But it is NOT O(N²).
Why?
Every real index can only be:
1. Pushed once.
2. Popped once.
Even though the while loop can pop many elements during one iteration, those elements cannot be popped again.
Across the entire algorithm:
Total pushes = N + 1
Total pops <= N
Therefore:
TIME COMPLEXITY = O(N)
9. SPACE COMPLEXITY
--------------------------------------------------------
O(N)
Where:
N = Number of histogram bars.
1. STACK
In the worst case, heights are increasing.
Example:
heights = [1, 2, 3, 4, 5]
Every new height is greater than the previous one.
No real index is popped.
The stack can contain all N indices.
Therefore:
Stack space = O(N)
2. OTHER VARIABLES
We use:
maxArea
currentHeight
height
width
area
i
n
These are individual variables.
They use constant extra space.
Therefore:
Other space = O(1)
TOTAL SPACE COMPLEXITY:
Stack = O(N)
Other variables = O(1)
Therefore:
SPACE COMPLEXITY = O(N)
IMPORTANT:
The algorithm does not create another list whose size depends on N.
The stack is the main additional memory.
10. EDGE CASES
--------------------------------------------------------
EDGE CASE 1: ONE BAR
Input:
heights = [5]
Expected:
5
Reason:
Height = 5
Width = 1
Area = 5
EDGE CASE 2: INCREASING HEIGHTS
Input:
heights = [1, 2, 3, 4, 5]
Expected:
9
Reason:
The last two bars can form:
Height = 4
Width = 2
Area = 8
But the last three bars can form:
Height = 3
Width = 3
Area = 9
Largest area = 9
EDGE CASE 3: DECREASING HEIGHTS
Input:
heights = [5, 4, 3, 2, 1]
Expected:
9
Reason:
The first three bars can form:
Height = 3
Width = 3
Area = 9
EDGE CASE 4: ALL HEIGHTS ARE EQUAL
Input:
heights = [2, 2, 2, 2]
Expected:
8
Reason:
Height = 2
Width = 4
Area = 8
EDGE CASE 5: TWO BARS
Input:
heights = [2, 4]
Expected:
4
Reason:
The second bar alone gives area 4.
EDGE CASE 6: ZERO HEIGHT
Input:
heights = [0, 2, 0]
Expected:
2
Reason:
The middle bar gives:
Height = 2
Width = 1
Area = 2
EDGE CASE 7: LARGE RECTANGLE IN THE MIDDLE
Input:
heights = [2, 1, 5, 6, 2, 3]
Expected:
10
Reason:
Height = 5
Width = 2
Area = 10
EDGE CASE 8: ONE SHORT BAR SPLITS THE HISTOGRAM
Input:
heights = [4, 4, 1, 4, 4]
Expected:
8
Reason:
The first two bars create area 8.
The last two bars also create area 8.
11. MY OWN TEST CASES
--------------------------------------------------------
Test 1:
Input:
heights = [2, 1, 5, 6, 2, 3]
Expected:
10
Test 2:
Input:
heights = [2, 4]
Expected:
4
Test 3:
Input:
heights = [2, 2, 2, 2]
Expected:
8
Test 4:
Input:
heights = [1, 2, 3, 4, 5]
Expected:
9
Test 5:
Input:
heights = [5, 4, 3, 2, 1]
Expected:
9
Test 6:
Input:
heights = [5]
Expected:
5
Test 7:
Input:
heights = [0, 2, 0]
Expected:
2
Test 8:
Input:
heights = [4, 4, 1, 4, 4]
Expected:
8
Test 9:
Input:
heights = [2, 1, 2]
Expected:
3
Test 10:
Input:
heights = [6, 2, 5, 4, 5, 1, 6]
Expected:
12
========================================================
MY LEARNING CHECKLIST
========================================================
[ ] I understand the Largest Rectangle problem.
[ ] I understand how rectangle area is calculated.
[ ] I understand why the shortest bar limits rectangle height.
[ ] I understand what a stack is.
[ ] I understand LIFO: Last In, First Out.
[ ] I understand why we store indices instead of heights.
[ ] I understand what maxArea stores.
[ ] I understand how len() works.
[ ] I understand why we use range(n + 1).
[ ] I understand the imaginary zero-height bar.
[ ] I understand the Python conditional expression.
[ ] I understand how stack[-1] works.
[ ] I understand how heights[stack[-1]] works.
[ ] I understand why we use while instead of if.
[ ] I understand why we use < instead of <=.
[ ] I understand what stack.pop() returns.
[ ] I understand how the popped index gives us a height.
[ ] I understand why the width formula has two cases.
[ ] I understand why we subtract 1 from the width.
[ ] I understand how to calculate height * width.
[ ] I understand how max() updates the largest area.
[ ] I understand why we push the current index.
[ ] I understand what a Monotonic Increasing Stack is.
[ ] I understand why the stack stores increasing heights.
[ ] I understand why every index is pushed at most once.
[ ] I understand why every real index is popped at most once.
[ ] I understand why time complexity is O(N).
[ ] I understand why space complexity is O(N).
[ ] I can write this solution without looking.
========================================================
"""
# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------
solution = Solution()
test_cases = [
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4),
    ([2, 2, 2, 2], 8),
    ([1, 2, 3, 4, 5], 9),
    ([5, 4, 3, 2, 1], 9),
    ([5], 5),
    ([0, 2, 0], 2),
    ([4, 4, 1, 4, 4], 8),
    ([2, 1, 2], 3),
    ([6, 2, 5, 4, 5, 1, 6], 12)
]
passed = 0
print("LARGEST RECTANGLE IN HISTOGRAM - TEST RESULTS")
print("----------------------------------------------")
for heights, expected in test_cases:
    result = solution.largestRectangleArea(heights)
    print("Heights:", heights)
    print("Expected:", expected)
    print("Actual:", result)
    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")
    print("----------------------------------------------")
print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
