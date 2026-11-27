"""
========================================================
PROBLEM: MEDIAN OF TWO SORTED ARRAYS
TOPIC: BINARY SEARCH
APPROACH: BINARY SEARCH ON PARTITIONS
========================================================
1. PROBLEM DESCRIPTION
--------------------------------------------------------
Given two sorted integer arrays:
nums1
nums2
Find the median of the two arrays combined.
IMPORTANT:
Both input arrays are already sorted.
We must find the median without necessarily combining
the two arrays into one new array.
What is the median?
The median is the middle value of a sorted collection.
There are two situations.
SITUATION 1: ODD NUMBER OF ELEMENTS
Example:
[1, 2, 3]
There are three elements.
The middle value is:
2
Therefore:
Median = 2
SITUATION 2: EVEN NUMBER OF ELEMENTS
Example:
[1, 2, 3, 4]
There are four elements.
There are two middle values:
2 and 3
The median is their average:
Median = (2 + 3) / 2
Median = 2.5
IMPORTANT:
The combined arrays do not need to be stored in a new list.
Our goal is to find the median using:
O(log(min(m, n))) time complexity.
Where:
m = length of nums1
n = length of nums2
========================================================
2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------
Example 1:
Input:
nums1 = [1, 3]
nums2 = [2]
Output:
2.0
Explanation:
The combined sorted array would be:
[1, 2, 3]
There are three elements.
The middle value is:
2
Therefore:
Median = 2.0
Example 2:
Input:
nums1 = [1, 2]
nums2 = [3, 4]
Output:
2.5
Explanation:
The combined sorted array would be:
[1, 2, 3, 4]
There are four elements.
The two middle values are:
2 and 3
Median:
(2 + 3) / 2 = 2.5
Example 3:
Input:
nums1 = []
nums2 = [1]
Output:
1.0
Explanation:
The first array is empty.
The second array contains one element.
The only element is the median.
Therefore:
Median = 1.0
Example 4:
Input:
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
Output:
3.5
Explanation:
The combined sorted array would be:
[1, 2, 3, 4, 5, 6]
The two middle values are:
3 and 4
Median:
(3 + 4) / 2 = 3.5
========================================================
3. MY APPROACH: BINARY SEARCH ON PARTITIONS
--------------------------------------------------------
I use one main algorithm:
1. BINARY SEARCH
The important idea is to divide both sorted arrays
into two parts.
We create:
LEFT PART | RIGHT PART
We want the left part to contain the same number
of elements as the right part.
If the total number of elements is odd,
the left part contains one extra element.
IMPORTANT:
We do not actually combine the arrays.
Instead, we find the correct partition positions.
OUR MAIN GOAL:
Every element in the left part must be less than
or equal to every element in the right part.
In particular, we check:
xLeft <= yRight
AND
yLeft <= xRight
Where:
xLeft  = Last element on the left side of nums1.
xRight = First element on the right side of nums1.
yLeft  = Last element on the left side of nums2.
yRight = First element on the right side of nums2.
WHY DO WE USE BINARY SEARCH?
Because both arrays are already sorted.
We can change the partition position in nums1
without checking every possible combination.
We always search the smaller array.
MY STEPS:
1. Check which array is larger.
2. If nums1 is larger, swap the arrays.
3. Find the lengths of both arrays.
4. Initialize the binary search boundaries.
5. Calculate the partition position in nums1.
6. Calculate the matching partition position in nums2.
7. Find the four boundary values.
8. Check whether the partition is correct.
9. If the partition is correct:
   a. Check whether the total length is even.
   b. If even, calculate the average of the two middle values.
   c. If odd, return the largest value on the left.
10. If nums1's left value is too large:
    Move the binary search to the left.
11. Otherwise:
    Move the binary search to the right.
12. Continue until the correct partition is found.
IMPORTANT:
We use binary search on the smaller array.
This gives us:
O(log(min(m, n))) time complexity.
========================================================
4. PYTHON SOLUTION
--------------------------------------------------------
"""
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        x, y = len(nums1), len(nums2)
        start, end = 0, x
        while start <= end:
            partX = (start + end) // 2
            partY = (x + y + 1) // 2 - partX
            xLeft = float("-inf") if partX == 0 else nums1[partX - 1]
            xRight = float("inf") if partX == x else nums1[partX]
            yLeft = float("-inf") if partY == 0 else nums2[partY - 1]
            yRight = float("inf") if partY == y else nums2[partY]
            if xLeft <= yRight and yLeft <= xRight:
                if (x + y) % 2 == 0:
                    return (max(xLeft, yLeft) + min(xRight, yRight)) / 2
                return max(xLeft, yLeft)
            elif xLeft > yRight:
                end = partX - 1
            else:
                start = partX + 1
        return 0.0
"""
========================================================
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------
class Solution:
Creates a class called Solution.
LeetCode commonly uses this class structure.
def findMedianSortedArrays(self, nums1, nums2):
Creates a function called findMedianSortedArrays.
self:
Refers to the current object of the class.
nums1:
The first sorted input array.
nums2:
The second sorted input array.
list[int]:
Means that the input is a list of integers.
-> float:
Means that the function returns a floating-point number.
WHY FLOAT?
Because the median can contain a decimal value.
Example:
[1, 2, 3, 4]
Median = 2.5
A. MAKE SURE NUMS1 IS THE SMALLER ARRAY
--------------------------------------------------------
if len(nums1) > len(nums2):
    return self.findMedianSortedArrays(nums2, nums1)
This checks whether nums1 is larger than nums2.
PART 1:
len(nums1)
Returns the number of elements in the first array.
PART 2:
len(nums2)
Returns the number of elements in the second array.
PART 3:
len(nums1) > len(nums2)
Checks whether the first array contains more elements.
If TRUE:
We call the same function again, but reverse the arrays.
Example:
nums1 = [1, 2, 3, 4]
nums2 = [5, 6]
The first array is larger.
Therefore, we call:
self.findMedianSortedArrays(nums2, nums1)
Now:
nums1 = [5, 6]
nums2 = [1, 2, 3, 4]
The smaller array is now nums1.
IMPORTANT:
We do this because binary search should operate
on the smaller array.
WHY?
The number of possible partition positions depends
on the length of the array we search.
Searching the smaller array gives us:
O(log(min(m, n)))
This recursive call only swaps the arrays once.
It does not repeatedly search the arrays recursively.
B. FIND THE LENGTHS OF BOTH ARRAYS
--------------------------------------------------------
x, y = len(nums1), len(nums2)
This creates two variables.
x:
Length of nums1.
y:
Length of nums2.
Example:
nums1 = [1, 3]
nums2 = [2, 4, 5]
Then:
x = 2
y = 3
Total number of elements:
x + y = 5
C. INITIALIZE THE BINARY SEARCH BOUNDARIES
--------------------------------------------------------
start, end = 0, x
This creates two variables.
start:
The smallest possible partition position.
end:
The largest possible partition position.
Why start = 0?
Because we may put zero elements from nums1
on the left side.
Why end = x?
Because we may put every element from nums1
on the left side.
Example:
nums1 = [1, 3, 5]
Possible partition positions:
0, 1, 2, 3
The binary search can examine these positions.
IMPORTANT:
A partition position is not the same as an array index.
A partition position tells us how many elements
we take from the array for the left side.
D. START THE BINARY SEARCH
--------------------------------------------------------
while start <= end:
This loop continues while there are still
possible partition positions to examine.
Why <= instead of <?
Because start and end can point to the same
valid partition position.
Example:
start = 2
end = 2
There is still one possible position to check.
Therefore, we use:
start <= end
E. CALCULATE THE PARTITION IN NUMS1
--------------------------------------------------------
partX = (start + end) // 2
This calculates the middle position between
the binary search boundaries.
The // operator performs floor division.
Example:
start = 0
end = 4
partX = (0 + 4) // 2
partX = 2
This means:
We place two elements from nums1
on the left side.
Example:
nums1 = [1, 3, 5, 7]
partX = 2
Partition:
[1, 3] | [5, 7]
IMPORTANT:
partX represents the number of elements
taken from nums1 for the left side.
It does not represent the index of the last
element on the left.
F. CALCULATE THE PARTITION IN NUMS2
--------------------------------------------------------
partY = (x + y + 1) // 2 - partX
THIS IS ONE OF THE MOST IMPORTANT LINES
IN THE ALGORITHM.
We want the left side to contain half
of the total elements.
If the total number is odd,
the left side must contain one extra element.
The expression:
(x + y + 1) // 2
Calculates the number of elements needed
on the left side.
Then:
partY = total_left_elements - partX
This calculates how many elements we need
from nums2.
Example:
nums1 = [1, 3]
nums2 = [2, 4, 5]
x = 2
y = 3
Total:
x + y = 5
Required left-side elements:
(2 + 3 + 1) // 2
= 6 // 2
= 3
Suppose:
partX = 1
Then:
partY = 3 - 1
partY = 2
Our partition becomes:
nums1:
[1] | [3]
nums2:
[2, 4] | [5]
Left side:
[1, 2, 4]
Right side:
[3, 5]
There are three elements on the left
and two elements on the right.
The left side has one extra element.
That is exactly what we want for an odd total.
WHY DO WE ADD 1?
Because we want the left side to contain
one extra element when the total is odd.
For an odd total:
5 elements:
Left = 3
Right = 2
For an even total:
6 elements:
Left = 3
Right = 3
The formula handles both situations.
G. FIND THE FOUR BOUNDARY VALUES
--------------------------------------------------------
We need four values to check whether
our partition is correct.
They are:
xLeft
xRight
yLeft
yRight
IMPORTANT:
We do not need to examine every element.
We only need the values around the two partitions.
PART 1: FIND XLEFT
--------------------------------------------------------
xLeft = float("-inf") if partX == 0 else nums1[partX - 1]
This is a Python conditional expression.
It has two possible results.
SITUATION 1:
partX == 0
This means we take zero elements from nums1
for the left side.
There is no actual element on the left side
of nums1's partition.
Therefore:
xLeft = float("-inf")
Negative infinity is smaller than every
ordinary number.
Why use negative infinity?
Because there is no real left boundary.
We need a value that will not incorrectly
block a valid partition.
SITUATION 2:
partX != 0
We have at least one element on the left.
Therefore:
xLeft = nums1[partX - 1]
Example:
nums1 = [1, 3, 5, 7]
partX = 2
Then:
xLeft = nums1[1]
xLeft = 3
The left side of nums1 is:
[1, 3]
The last value is 3.
PART 2: FIND XRIGHT
--------------------------------------------------------
xRight = float("inf") if partX == x else nums1[partX]
This finds the first value on the right side
of nums1's partition.
SITUATION 1:
partX == x
This means every element from nums1
is on the left side.
There is no real element on the right side.
Therefore:
xRight = float("inf")
Positive infinity is larger than every
ordinary number.
SITUATION 2:
partX != x
There is at least one element on the right.
Therefore:
xRight = nums1[partX]
Example:
nums1 = [1, 3, 5, 7]
partX = 2
Then:
xRight = nums1[2]
xRight = 5
The right side of nums1 is:
[5, 7]
The first value is 5.
PART 3: FIND YLEFT
--------------------------------------------------------
yLeft = float("-inf") if partY == 0 else nums2[partY - 1]
This works exactly like xLeft.
If partY is zero:
There are no elements from nums2
on the left side.
We use negative infinity.
Otherwise:
We take the element immediately before
the partition position.
Example:
nums2 = [2, 4, 6]
partY = 2
Then:
yLeft = nums2[1]
yLeft = 4
PART 4: FIND YRIGHT
--------------------------------------------------------
yRight = float("inf") if partY == y else nums2[partY]
This works exactly like xRight.
If partY equals the length of nums2:
There are no elements from nums2
on the right side.
We use positive infinity.
Otherwise:
We take the element at the partition position.
Example:
nums2 = [2, 4, 6]
partY = 2
Then:
yRight = nums2[2]
yRight = 6
WHY DO WE USE INFINITY?
Sometimes a partition is at the beginning
or end of an array.
There may be no real value on one side.
We use:
float("-inf")
For a missing left boundary.
We use:
float("inf")
For a missing right boundary.
This allows us to use the same comparison
logic for every partition.
We do not need separate complicated conditions
for empty sides.
H. CHECK WHETHER THE PARTITION IS CORRECT
--------------------------------------------------------
if xLeft <= yRight and yLeft <= xRight:
THIS IS THE MOST IMPORTANT CONDITION
IN THE ALGORITHM.
It checks whether the elements are correctly
divided between the left and right sides.
PART 1:
xLeft <= yRight
The last value on the left side of nums1
must be less than or equal to the first
value on the right side of nums2.
PART 2:
yLeft <= xRight
The last value on the left side of nums2
must be less than or equal to the first
value on the right side of nums1.
Both conditions must be TRUE.
WHY?
Because both input arrays are already sorted.
If these two boundary conditions are satisfied,
every element on the left side is less than
or equal to every element on the right side.
Example:
nums1 = [1, 3]
nums2 = [2, 4, 5]
Suppose:
partX = 1
partY = 2
The partition is:
nums1:
[1] | [3]
nums2:
[2, 4] | [5]
Boundary values:
xLeft = 1
xRight = 3
yLeft = 4
yRight = 5
Check:
xLeft <= yRight
1 <= 5
TRUE.
Check:
yLeft <= xRight
4 <= 3
FALSE.
Therefore:
The partition is incorrect.
We must move the partition in nums1
to the right or left depending on
the comparison.
I. CHECK WHETHER THE TOTAL LENGTH IS EVEN
--------------------------------------------------------
if (x + y) % 2 == 0:
The % operator calculates the remainder.
If the remainder after dividing by 2 is zero,
the total number of elements is even.
Example:
6 % 2 = 0
Therefore, 6 is even.
If:
(x + y) % 2 == 0
We have an even number of elements.
We need the two middle values.
The largest value on the left is:
max(xLeft, yLeft)
The smallest value on the right is:
min(xRight, yRight)
These are the two middle values
of the combined sorted arrays.
J. CALCULATE THE MEDIAN FOR AN EVEN TOTAL
--------------------------------------------------------
return (max(xLeft, yLeft) + min(xRight, yRight)) / 2
This calculates the average of the two middle values.
Example:
xLeft = 2
yLeft = 3
xRight = 4
yRight = 5
Largest value on the left:
max(2, 3) = 3
Smallest value on the right:
min(4, 5) = 4
Median:
(3 + 4) / 2
= 3.5
IMPORTANT:
We do not need to combine the arrays.
We only use the four boundary values.
K. CALCULATE THE MEDIAN FOR AN ODD TOTAL
--------------------------------------------------------
return max(xLeft, yLeft)
If the total number of elements is odd,
the left side contains one extra element.
Therefore, the median is the largest value
on the left side.
Example:
nums1 = [1, 3]
nums2 = [2]
Correct partition:
nums1:
[1] | [3]
nums2:
[2] | []
The left side is:
[1, 2]
The right side is:
[3]
The largest value on the left is:
max(1, 2) = 2
Therefore:
Median = 2
L. MOVE THE BINARY SEARCH TO THE LEFT
--------------------------------------------------------
elif xLeft > yRight:
end = partX - 1
This condition means:
The last value on the left side of nums1
is larger than the first value on the right
side of nums2.
Therefore, we have taken too many elements
from nums1 for the left side.
We must move the partition in nums1 to the left.
Example:
nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6]
Suppose:
xLeft = 5
yRight = 4
Check:
5 > 4
TRUE.
This means the partition in nums1 is too far right.
We update:
end = partX - 1
Now binary search examines smaller partition positions.
M. MOVE THE BINARY SEARCH TO THE RIGHT
--------------------------------------------------------
else:
start = partX + 1
If the correct partition was not found
and xLeft is not greater than yRight,
the other boundary condition must be incorrect.
That means:
yLeft > xRight
We have taken too few elements from nums1
for the left side.
Therefore, we move the partition in nums1
to the right.
We update:
start = partX + 1
Example:
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
Suppose:
yLeft = 6
xRight = 3
Check:
6 > 3
TRUE.
We need more elements from nums1
on the left side.
Therefore:
start = partX + 1
N. FINAL FALLBACK
--------------------------------------------------------
return 0.0
This line is reached only if the binary search
finishes without finding a valid partition.
For valid sorted input arrays where at least
one array is non-empty, a valid partition exists.
Therefore, this line is a fallback.
It is not the normal result of the algorithm.
========================================================
6. COMPLETE DRY RUN
--------------------------------------------------------
Input:
nums1 = [1, 3]
nums2 = [2]
INITIAL STATE:
x = 2
y = 1
Total:
x + y = 3
start = 0
end = 2
The first array is already smaller.
No swapping is needed.
ITERATION 1:
--------------------------------------------------------
start = 0
end = 2
Calculate partX:
partX = (0 + 2) // 2
partX = 1
Calculate partY:
partY = (2 + 1 + 1) // 2 - 1
partY = 4 // 2 - 1
partY = 1
FIND THE FOUR BOUNDARY VALUES:
nums1 = [1, 3]
nums2 = [2]
partX = 1
partY = 1
xLeft:
nums1[0] = 1
xLeft = 1
xRight:
nums1[1] = 3
xRight = 3
yLeft:
nums2[0] = 2
yLeft = 2
yRight:
partY == y
1 == 1
TRUE.
Therefore:
yRight = float("inf")
BOUNDARY VALUES:
xLeft = 1
xRight = 3
yLeft = 2
yRight = infinity
CHECK THE PARTITION:
xLeft <= yRight
1 <= infinity
TRUE.
yLeft <= xRight
2 <= 3
TRUE.
Both conditions are TRUE.
Therefore:
THE PARTITION IS CORRECT.
CHECK THE TOTAL LENGTH:
x + y = 3
3 % 2 = 1
The total is odd.
Therefore, the median is:
max(xLeft, yLeft)
max(1, 2) = 2
FINAL RESULT:
Median = 2.0
The function returns 2.
========================================================
7. SECOND DRY RUN: EVEN NUMBER OF ELEMENTS
--------------------------------------------------------
Input:
nums1 = [1, 2]
nums2 = [3, 4]
INITIAL STATE:
x = 2
y = 2
Total:
x + y = 4
start = 0
end = 2
ITERATION 1:
--------------------------------------------------------
partX = (0 + 2) // 2
partX = 1
partY = (2 + 2 + 1) // 2 - 1
partY = 5 // 2 - 1
partY = 1
BOUNDARY VALUES:
xLeft = nums1[0] = 1
xRight = nums1[1] = 2
yLeft = nums2[0] = 3
yRight = nums2[1] = 4
CHECK THE PARTITION:
xLeft <= yRight
1 <= 4
TRUE.
yLeft <= xRight
3 <= 2
FALSE.
The partition is incorrect.
MOVE THE BINARY SEARCH TO THE RIGHT:
Because:
yLeft > xRight
We execute:
start = partX + 1
start = 1 + 1
start = 2
Now:
start = 2
end = 2
ITERATION 2:
--------------------------------------------------------
partX = (2 + 2) // 2
partX = 2
partY = (2 + 2 + 1) // 2 - 2
partY = 5 // 2 - 2
partY = 0
BOUNDARY VALUES:
xLeft:
nums1[1] = 2
xLeft = 2
xRight:
partX == x
2 == 2
TRUE.
xRight = infinity
yLeft:
partY == 0
TRUE.
yLeft = negative infinity
yRight:
nums2[0] = 3
yRight = 3
CHECK THE PARTITION:
xLeft <= yRight
2 <= 3
TRUE.
yLeft <= xRight
negative infinity <= infinity
TRUE.
The partition is correct.
CHECK THE TOTAL LENGTH:
x + y = 4
4 % 2 = 0
The total is even.
Therefore, we need two middle values.
Largest value on the left:
max(2, negative infinity) = 2
Smallest value on the right:
min(infinity, 3) = 3
Calculate the median:
(2 + 3) / 2
= 2.5
FINAL RESULT:
Median = 2.5
========================================================
8. WHY THIS IS BINARY SEARCH ON PARTITIONS
--------------------------------------------------------
Binary search normally searches for a value
inside a sorted array.
Here, we search for a correct partition position.
We do not search directly for the median.
We search for the position that divides
the two arrays into correctly ordered halves.
THE CORRECT PARTITION MUST SATISFY:
xLeft <= yRight
AND
yLeft <= xRight
WHY DOES THIS WORK?
Both arrays are already sorted.
Inside nums1:
Every element on its left side is less than
or equal to every element on its right side.
Inside nums2:
Every element on its left side is less than
or equal to every element on its right side.
We only need to check the two boundaries
between the arrays.
If both boundary conditions are correct,
the entire left side is correctly ordered
before the entire right side.
Then we can identify the middle value
or the two middle values.
WHY DO WE SEARCH ONLY THE SMALLER ARRAY?
Suppose:
nums1 contains 5 elements.
nums2 contains 1,000 elements.
We search the array with 5 elements.
This reduces the number of possible partition
positions we need to examine.
The time complexity becomes:
O(log(min(m, n)))
IMPORTANT:
We do not sort the arrays again.
We do not merge them.
We do not create a combined array.
We use binary search and four boundary values.
========================================================
9. TIME COMPLEXITY
--------------------------------------------------------
O(log(min(m, n)))
Where:
m = Length of nums1.
n = Length of nums2.
There are several important operations.
1. CHECK WHICH ARRAY IS SMALLER
--------------------------------------------------------
if len(nums1) > len(nums2):
This takes constant time.
Time complexity:
O(1)
2. BINARY SEARCH
--------------------------------------------------------
while start <= end:
We perform binary search on the smaller array.
If the smaller array contains k elements,
there are k + 1 possible partition positions.
Binary search reduces the search area
by approximately half in every iteration.
Therefore:
Time complexity:
O(log(k))
Where:
k = min(m, n)
3. CALCULATE THE PARTITIONS
--------------------------------------------------------
partX = (start + end) // 2
partY = (x + y + 1) // 2 - partX
These are arithmetic operations.
They take constant time.
Time complexity:
O(1)
4. CHECK THE FOUR BOUNDARY VALUES
--------------------------------------------------------
We calculate:
xLeft
xRight
yLeft
yRight
Each operation takes constant time.
Time complexity:
O(1)
5. CALCULATE THE MEDIAN
--------------------------------------------------------
max(xLeft, yLeft)
min(xRight, yRight)
These operations compare only two values.
They take constant time.
Time complexity:
O(1)
FINAL TIME COMPLEXITY:
O(log(min(m, n)))
IMPORTANT:
We do not visit every element.
We only examine partition positions
using binary search.
That is why this solution is faster
than combining the arrays and sorting them.
========================================================
10. SPACE COMPLEXITY
--------------------------------------------------------
O(1)
The algorithm uses a fixed number of variables.
We use:
x
y
start
end
partX
partY
xLeft
xRight
yLeft
yRight
We do not create:
1. A new combined array.
2. A sorting list.
3. Another data structure that grows with input size.
The recursive call used to swap the arrays
happens at most once.
Therefore, the additional space is constant.
FINAL SPACE COMPLEXITY:
O(1)
========================================================
11. EDGE CASES
--------------------------------------------------------
EDGE CASE 1: ONE ARRAY IS EMPTY
Input:
nums1 = []
nums2 = [1]
Expected:
1.0
Reason:
The only element is the median.
EDGE CASE 2: BOTH ARRAYS CONTAIN ONE ELEMENT
Input:
nums1 = [1]
nums2 = [2]
Expected:
1.5
Reason:
The two middle values are 1 and 2.
Median:
(1 + 2) / 2 = 1.5
EDGE CASE 3: BOTH ARRAYS HAVE EQUAL LENGTH
Input:
nums1 = [1, 2]
nums2 = [3, 4]
Expected:
2.5
Reason:
The two middle values are 2 and 3.
EDGE CASE 4: ARRAYS CONTAIN DUPLICATE VALUES
Input:
nums1 = [0, 0]
nums2 = [0, 0]
Expected:
0.0
Reason:
Every element is zero.
The median is zero.
EDGE CASE 5: NEGATIVE NUMBERS
Input:
nums1 = [-5, -3]
nums2 = [-2, -1]
Expected:
-2.5
Reason:
The two middle values are -3 and -2.
Median:
(-3 + -2) / 2 = -2.5
EDGE CASE 6: FIRST ARRAY IS MUCH LARGER
Input:
nums1 = [1, 2, 3, 4, 5, 6, 7]
nums2 = [100]
Expected:
4.0
Reason:
The algorithm swaps the arrays.
It performs binary search on the smaller array.
EDGE CASE 7: SECOND ARRAY IS MUCH LARGER
Input:
nums1 = [100]
nums2 = [1, 2, 3, 4, 5, 6, 7]
Expected:
4.0
Reason:
The smaller array is already nums1.
The algorithm searches it directly.
EDGE CASE 8: DIFFERENT ARRAY LENGTHS
Input:
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [7, 8, 9, 10]
Expected:
5.5
Reason:
The combined sorted order is:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
The two middle values are 5 and 6.
Median:
5.5
EDGE CASE 9: LARGE VALUE IN THE FIRST ARRAY
Input:
nums1 = [1, 2, 100]
nums2 = [3, 4, 5, 6, 7, 8, 9]
Expected:
5.5
Reason:
The combined sorted order is:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
The two middle values are 5 and 6.
Median:
5.5
EDGE CASE 10: ALL VALUES ARE EQUAL
Input:
nums1 = [1, 1]
nums2 = [1, 1]
Expected:
1.0
Reason:
Every element has the same value.
The median is 1.0.
========================================================
12. MY OWN TEST CASES
--------------------------------------------------------
Test 1:
Input:
nums1 = [1, 3]
nums2 = [2]
Expected:
2.0
Test 2:
Input:
nums1 = [1, 2]
nums2 = [3, 4]
Expected:
2.5
Test 3:
Input:
nums1 = []
nums2 = [1]
Expected:
1.0
Test 4:
Input:
nums1 = [2]
nums2 = []
Expected:
2.0
Test 5:
Input:
nums1 = [1]
nums2 = [2]
Expected:
1.5
Test 6:
Input:
nums1 = [0, 0]
nums2 = [0, 0]
Expected:
0.0
Test 7:
Input:
nums1 = [-5, -3]
nums2 = [-2, -1]
Expected:
-2.5
Test 8:
Input:
nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8]
Expected:
4.5
Test 9:
Input:
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9]
Expected:
5.0
Test 10:
Input:
nums1 = [100]
nums2 = [1, 2, 3, 4, 5, 6, 7]
Expected:
4.0
Test 11:
Input:
nums1 = [1, 2, 3, 4, 5, 6, 7]
nums2 = [100]
Expected:
4.0
Test 12:
Input:
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [7, 8, 9, 10]
Expected:
5.5
Test 13:
Input:
nums1 = [1, 2, 100]
nums2 = [3, 4, 5, 6, 7, 8, 9]
Expected:
5.5
Test 14:
Input:
nums1 = [1, 1]
nums2 = [1, 1]
Expected:
1.0
Test 15:
Input:
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
Expected:
3.5
========================================================
MY LEARNING CHECKLIST
========================================================
[ ] I understand the Median problem.
[ ] I understand what a median is.
[ ] I understand the difference between odd and even totals.
[ ] I understand why both arrays must be sorted.
[ ] I understand why we do not need to merge the arrays.
[ ] I understand what binary search does.
[ ] I understand why we search the smaller array.
[ ] I understand what a partition is.
[ ] I understand the difference between an array index
    and a partition position.
[ ] I understand what x and y represent.
[ ] I understand why start begins at zero.
[ ] I understand why end begins at x.
[ ] I understand how partX is calculated.
[ ] I understand how partY is calculated.
[ ] I understand why we add 1 in the partY formula.
[ ] I understand what xLeft represents.
[ ] I understand what xRight represents.
[ ] I understand what yLeft represents.
[ ] I understand what yRight represents.
[ ] I understand why we use negative infinity.
[ ] I understand why we use positive infinity.
[ ] I understand the correct partition condition.
[ ] I understand why both boundary conditions
    must be TRUE.
[ ] I understand how to calculate the median
    when the total is even.
[ ] I understand how to calculate the median
    when the total is odd.
[ ] I understand why max(xLeft, yLeft)
    gives the middle value for an odd total.
[ ] I understand why min(xRight, yRight)
    gives the other middle value for an even total.
[ ] I understand why xLeft > yRight means
    we move the binary search to the left.
[ ] I understand why we move the binary search
    to the right in the other case.
[ ] I understand the complete dry run.
[ ] I understand why the time complexity is
    O(log(min(m, n))).
[ ] I understand why the space complexity is O(1).
[ ] I can write this solution without looking.
========================================================
"""
"""
------------------------------------------------------
TESTING THE SOLUTION
------------------------------------------------------
"""
solution = Solution()
test_cases = [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([], [1], 1.0),
    ([2], [], 2.0),
    ([1], [2], 1.5),
    ([0, 0], [0, 0], 0.0),
    ([-5, -3], [-2, -1], -2.5),
    ([1, 3, 5, 7], [2, 4, 6, 8], 4.5),
    ([1, 2, 3, 4, 5], [6, 7, 8, 9], 5.0),
    ([100], [1, 2, 3, 4, 5, 6, 7], 4.0),
    ([1, 2, 3, 4, 5, 6, 7], [100], 4.0),
    ([1, 2, 3, 4, 5, 6], [7, 8, 9, 10], 5.5),
    ([1, 2, 100], [3, 4, 5, 6, 7, 8, 9], 5.5),
    ([1, 1], [1, 1], 1.0),
    ([1, 2, 3], [4, 5, 6], 3.5)
]
passed = 0
print("MEDIAN OF TWO SORTED ARRAYS - TEST RESULTS")
print("----------------------------------------------")
for nums1, nums2, expected in test_cases:
    result = solution.findMedianSortedArrays(nums1, nums2)
    print("Nums1:", nums1)
    print("Nums2:", nums2)
    print("Expected:", expected)
    print("Actual:", result)
    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")
    print("----------------------------------------------")
print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")