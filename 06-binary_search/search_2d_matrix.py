"""
========================================================
PROBLEM: SEARCH A 2D MATRIX
TOPIC: BINARY SEARCH
APPROACH: BINARY SEARCH ON A VIRTUAL 1D ARRAY
========================================================
1. PROBLEM DESCRIPTION
--------------------------------------------------------
You are given an m x n integer matrix.
The matrix has two important properties:
1. Every row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.
Given an integer called target, return True if target exists in the matrix.
Otherwise, return False.
IMPORTANT:
The matrix can be treated as one sorted 1D array.
We do not need to create a new 1D array.
We can use the original matrix directly.
OUR GOAL:
Find the target using:
TIME COMPLEXITY = O(log(m * n))
2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------
Example 1:
Input:
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
Output:
True
Explanation:
The value 3 exists in the first row.
Therefore, return True.
Example 2:
Input:
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 13
Output:
False
Explanation:
The value 13 does not exist in the matrix.
Therefore, return False.
Example 3:
Input:
matrix = [
    [1, 3, 5],
    [7, 9, 11]
]
target = 11
Output:
True
Explanation:
The value 11 exists in the second row.
Therefore, return True.
3. MY APPROACH: BINARY SEARCH
--------------------------------------------------------
I use one main algorithm:
1. BINARY SEARCH
IMPORTANT:
We do not search every row separately.
We treat the entire matrix as one sorted 1D array.
Example:
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
Virtual 1D array:
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
The array has:
m = 3 rows
n = 4 columns
Total elements = m * n = 12
MY STEPS:
1. Find the number of rows: m.
2. Find the number of columns: n.
3. Set left = 0.
4. Set right = m * n - 1.
5. Continue while left <= right.
6. Calculate the middle index.
7. Convert the middle index into a matrix row and column.
8. Get the value at that matrix position.
9. If the value equals target, return True.
10. If the value is smaller than target, search the right half.
11. If the value is greater than target, search the left half.
12. If the loop finishes without finding target, return False.
WHY DOES THIS WORK?
The matrix is globally sorted when read from left to right and top to bottom.
Therefore, binary search can eliminate half of the remaining elements each time.
4. PYTHON SOLUTION
--------------------------------------------------------
"""
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Handle an empty matrix or an empty first row
        if not matrix or not matrix[0]:
            return False
        # Find the number of rows and columns
        m = len(matrix)
        n = len(matrix[0])
        # Set the search boundaries
        left = 0
        right = m * n - 1
        # Continue while there are elements to search
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2
            # Convert the 1D index into a matrix position
            midValue = matrix[mid // n][mid % n]
            # Check whether the middle value is the target
            if midValue == target:
                return True
            # Search the right half
            elif midValue < target:
                left = mid + 1
            # Search the left half
            else:
                right = mid - 1
        # Target was not found
        return False
"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------
class Solution:
Creates a class called Solution.
LeetCode commonly uses this class structure.
def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
Creates a function called searchMatrix.
self:
Refers to the current object of the class.
matrix:
The input 2D list containing integers.
list[list[int]]:
Means a list containing other lists of integers.
target:
The integer we want to find.
-> bool:
Means the function returns a Boolean value:
True or False.
A. HANDLE AN EMPTY MATRIX
--------------------------------------------------------
if not matrix or not matrix[0]:
This checks whether the matrix is empty or its first row is empty.
PART 1:
not matrix
Checks whether the entire matrix is empty.
Example:
matrix = []
Result:
True
PART 2:
not matrix[0]
Checks whether the first row is empty.
Example:
matrix = [[]]
Result:
True
WHY DO WE CHECK THIS?
Because we need at least one row and one column to perform binary search.
If the matrix is empty, there is no target to find.
Therefore:
return False
IMPORTANT:
This solution assumes the matrix is rectangular, meaning every row has the same number of columns, as in the problem.
B. FIND THE NUMBER OF ROWS
--------------------------------------------------------
m = len(matrix)
len() counts the number of elements in a list.
Example:
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
There are three rows.
Therefore:
m = 3
C. FIND THE NUMBER OF COLUMNS
--------------------------------------------------------
n = len(matrix[0])
matrix[0] means the first row.
len(matrix[0]) counts the number of elements in the first row.
Example:
matrix[0] = [1, 3, 5, 7]
Therefore:
n = 4
IMPORTANT:
The problem guarantees that every row has the same number of columns.
D. INITIALIZE THE LEFT BOUNDARY
--------------------------------------------------------
left = 0
Creates the starting position of our virtual 1D array.
The first element has index 0.
Example:
Virtual array:
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
left = 0
E. INITIALIZE THE RIGHT BOUNDARY
--------------------------------------------------------
right = m * n - 1
This calculates the last index of the virtual 1D array.
m = number of rows.
n = number of columns.
m * n = total number of elements.
Example:
m = 3
n = 4
Total elements:
3 * 4 = 12
The indices are:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
The last index is:
11
Therefore:
right = 3 * 4 - 1
right = 11
WHY DO WE SUBTRACT 1?
Because Python indices start at zero.
An array containing 12 elements has a final index of 11.
F. START THE BINARY SEARCH LOOP
--------------------------------------------------------
while left <= right:
This loop continues while there are still elements to search.
Example:
left = 0
right = 11
0 <= 11
Result:
True
The loop starts.
WHY <= INSTEAD OF <?
Because left and right can point to the same remaining element.
Example:
left = 5
right = 5
There is still one element to check.
If we used left < right, we would skip that final element.
Therefore, we use:
left <= right
G. CALCULATE THE MIDDLE INDEX
--------------------------------------------------------
mid = left + (right - left) // 2
Calculates the middle position of the current search range.
PART 1:
right - left
Calculates the distance between the boundaries.
PART 2:
(right - left) // 2
Finds half of that distance.
PART 3:
left + ...
Adds half the distance to the left boundary.
Example:
left = 0
right = 11
mid = 0 + (11 - 0) // 2
mid = 0 + 11 // 2
mid = 5
IMPORTANT:
We use // instead of /.
In Python:
11 / 2 = 5.5
11 // 2 = 5
We need an integer index.
WHY NOT SIMPLY USE (left + right) // 2?
Both formulas work in Python.
However:
left + (right - left) // 2
also avoids potential integer overflow in languages with fixed-size integers.
H. CONVERT THE MIDDLE INDEX INTO A MATRIX POSITION
--------------------------------------------------------
midValue = matrix[mid // n][mid % n]
THIS IS THE MOST IMPORTANT LINE IN THIS SOLUTION.
Remember:
We are performing binary search as if the matrix were one 1D array.
But the actual data is still stored in a 2D matrix.
We need to convert the virtual 1D index into:
1. A row number.
2. A column number.
We use two operations:
PART 1: mid // n
Calculates the row number.
PART 2: mid % n
Calculates the column number.
Let's understand them.
WHAT DOES // MEAN?
// is integer division.
It divides two numbers and removes the decimal part.
Example:
5 // 4 = 1
WHAT DOES % MEAN?
% is the modulo operator.
It gives us the remainder after division.
Example:
5 % 4 = 1
EXAMPLE:
m = 3
n = 4
mid = 5
Row:
mid // n
5 // 4 = 1
Column:
mid % n
5 % 4 = 1
Therefore:
matrix[1][1]
The value is:
11
So:
midValue = 11
WHY DOES THIS CONVERSION WORK?
Each row contains exactly n elements.
Row 0 contains indices 0 to 3.
Row 1 contains indices 4 to 7.
Row 2 contains indices 8 to 11.
Integer division tells us which group of n elements contains the index.
The remainder tells us the position inside that group.
IMPORTANT:
We do not create a new 1D list.
We only calculate the correct position inside the original matrix.
I. CHECK WHETHER THE MIDDLE VALUE IS THE TARGET
--------------------------------------------------------
if midValue == target:
    return True
This compares the middle value with the target.
Example:
midValue = 11
target = 11
Comparison:
11 == 11
Result:
True
We found the target.
Therefore:
return True
The function stops immediately.
J. SEARCH THE RIGHT HALF
--------------------------------------------------------
elif midValue < target:
    left = mid + 1
This condition checks whether the middle value is smaller than the target.
Example:
midValue = 5
target = 11
Comparison:
5 < 11
Result:
True
The target must be on the right side because the matrix is sorted.
Therefore:
left = mid + 1
Example:
mid = 5
left = 5 + 1
left = 6
WHY mid + 1?
We already checked the middle element.
It is not the target.
We do not need to check it again.
We move one position after mid.
K. SEARCH THE LEFT HALF
--------------------------------------------------------
else:
    right = mid - 1
This happens when the middle value is greater than the target.
Example:
midValue = 16
target = 11
Comparison:
16 > 11
The target must be on the left side because the matrix is sorted.
Therefore:
right = mid - 1
Example:
mid = 6
right = 6 - 1
right = 5
WHY mid - 1?
We already checked the middle element.
It is not the target.
We move one position before mid.
L. RETURN FALSE
--------------------------------------------------------
return False
This line runs when the while loop finishes without finding the target.
Example:
target = 13
If every possible position has been eliminated, the target does not exist.
Therefore:
return False
6. COMPLETE DRY RUN
--------------------------------------------------------
Input:
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
INITIAL STATE:
m = 3
n = 4
left = 0
right = 3 * 4 - 1
right = 11
Virtual 1D array:
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
ITERATION 1:
left = 0
right = 11
Calculate mid:
mid = 0 + (11 - 0) // 2
mid = 5
Convert the index:
row = 5 // 4 = 1
column = 5 % 4 = 1
Get the value:
matrix[1][1] = 11
Compare:
11 == 3
FALSE.
11 < 3
FALSE.
Therefore, search the left half.
Update:
right = mid - 1
right = 5 - 1
right = 4
CURRENT SEARCH RANGE:
left = 0
right = 4
ITERATION 2:
left = 0
right = 4
Calculate mid:
mid = 0 + (4 - 0) // 2
mid = 2
Convert the index:
row = 2 // 4 = 0
column = 2 % 4 = 2
Get the value:
matrix[0][2] = 5
Compare:
5 == 3
FALSE.
5 < 3
FALSE.
Therefore, search the left half.
Update:
right = mid - 1
right = 2 - 1
right = 1
CURRENT SEARCH RANGE:
left = 0
right = 1
ITERATION 3:
left = 0
right = 1
Calculate mid:
mid = 0 + (1 - 0) // 2
mid = 0
Convert the index:
row = 0 // 4 = 0
column = 0 % 4 = 0
Get the value:
matrix[0][0] = 1
Compare:
1 == 3
FALSE.
1 < 3
TRUE.
Therefore, search the right half.
Update:
left = mid + 1
left = 0 + 1
left = 1
CURRENT SEARCH RANGE:
left = 1
right = 1
ITERATION 4:
left = 1
right = 1
Calculate mid:
mid = 1 + (1 - 1) // 2
mid = 1
Convert the index:
row = 1 // 4 = 0
column = 1 % 4 = 1
Get the value:
matrix[0][1] = 3
Compare:
3 == 3
TRUE.
We found the target.
RETURN:
True
FINAL RESULT:
True
7. HOW THE MATRIX INDEX CONVERSION WORKS
--------------------------------------------------------
Consider:
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
There are four columns in each row.
The virtual 1D positions are:
Index 0  -> matrix[0][0] -> 1
Index 1  -> matrix[0][1] -> 3
Index 2  -> matrix[0][2] -> 5
Index 3  -> matrix[0][3] -> 7
Index 4  -> matrix[1][0] -> 10
Index 5  -> matrix[1][1] -> 11
Index 6  -> matrix[1][2] -> 16
Index 7  -> matrix[1][3] -> 20
Index 8  -> matrix[2][0] -> 23
Index 9  -> matrix[2][1] -> 30
Index 10 -> matrix[2][2] -> 34
Index 11 -> matrix[2][3] -> 60
GENERAL FORMULAS:
Row = mid // n
Column = mid % n
Example:
mid = 10
n = 4
Row = 10 // 4 = 2
Column = 10 % 4 = 2
Therefore:
matrix[2][2] = 34
8. WHY THIS IS BINARY SEARCH
--------------------------------------------------------
Binary Search works because the matrix is globally sorted.
When the middle value is too small:
We eliminate the middle and everything before it.
When the middle value is too large:
We eliminate the middle and everything after it.
Each iteration removes about half of the remaining search area.
Example:
12 elements
After one iteration:
About 6 elements remain.
After two iterations:
About 3 elements remain.
After three iterations:
About 1 or 2 elements remain.
We do not need to inspect every element.
IMPORTANT:
The second matrix property makes this possible:
The first integer of each row is greater than the last integer of the previous row.
Without this property, treating the entire matrix as one sorted array would not be valid.
9. TIME COMPLEXITY
--------------------------------------------------------
O(log(m * n))
Where:
m = Number of rows.
n = Number of columns.
m * n = Total number of elements.
WHY?
1. CALCULATING MATRIX DIMENSIONS
m = len(matrix)
n = len(matrix[0])
These operations take constant time.
2. INITIALIZING THE BOUNDARIES
left = 0
right = m * n - 1
These operations take constant time.
3. THE BINARY SEARCH LOOP
while left <= right:
Each iteration removes approximately half of the remaining search range.
Example:
If there are 16 elements:
16 -> 8 -> 4 -> 2 -> 1
The number of iterations grows logarithmically.
Therefore:
TIME COMPLEXITY = O(log(m * n))
IMPORTANT:
We do not create or visit all m * n elements.
We only inspect the middle element during each iteration.
10. SPACE COMPLEXITY
--------------------------------------------------------
O(1)
WHY?
We use a fixed number of variables:
m
n
left
right
mid
midValue
These variables do not grow when the matrix becomes larger.
IMPORTANT:
We do not create another 1D array.
We do not create another matrix.
We do not use recursion.
The original matrix is used directly.
Therefore:
SPACE COMPLEXITY = O(1)
11. EDGE CASES
--------------------------------------------------------
EDGE CASE 1: ONE ELEMENT, TARGET FOUND
Input:
matrix = [[5]]
target = 5
Expected:
True
Reason:
The only element equals the target.
EDGE CASE 2: ONE ELEMENT, TARGET NOT FOUND
Input:
matrix = [[5]]
target = 3
Expected:
False
Reason:
The only element is not the target.
EDGE CASE 3: EMPTY MATRIX
Input:
matrix = []
target = 5
Expected:
False
Reason:
There are no elements to search.
EDGE CASE 4: EMPTY FIRST ROW
Input:
matrix = [[]]
target = 5
Expected:
False
Reason:
There are no columns to search.
EDGE CASE 5: TARGET AT THE FIRST POSITION
Input:
matrix = [[1, 3], [5, 7]]
target = 1
Expected:
True
EDGE CASE 6: TARGET AT THE LAST POSITION
Input:
matrix = [[1, 3], [5, 7]]
target = 7
Expected:
True
EDGE CASE 7: TARGET SMALLER THAN ALL ELEMENTS
Input:
matrix = [[10, 20], [30, 40]]
target = 5
Expected:
False
EDGE CASE 8: TARGET GREATER THAN ALL ELEMENTS
Input:
matrix = [[10, 20], [30, 40]]
target = 50
Expected:
False
EDGE CASE 9: ONE ROW
Input:
matrix = [[1, 3, 5, 7, 9]]
target = 5
Expected:
True
EDGE CASE 10: ONE COLUMN
Input:
matrix = [[1], [3], [5], [7]]
target = 5
Expected:
True
EDGE CASE 11: TARGET BETWEEN TWO VALUES
Input:
matrix = [[1, 3], [5, 7]]
target = 4
Expected:
False
EDGE CASE 12: DUPLICATE VALUES INSIDE A ROW
Input:
matrix = [[1, 1, 2], [3, 3, 4]]
target = 3
Expected:
True
Reason:
Rows are sorted in non-decreasing order, so duplicates inside a row are allowed.
12. MY OWN TEST CASES
--------------------------------------------------------
Test 1:
Input:
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
Expected:
True
Test 2:
Input:
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
Expected:
False
Test 3:
Input:
matrix = [[5]]
target = 5
Expected:
True
Test 4:
Input:
matrix = [[5]]
target = 3
Expected:
False
Test 5:
Input:
matrix = []
target = 5
Expected:
False
Test 6:
Input:
matrix = [[]]
target = 5
Expected:
False
Test 7:
Input:
matrix = [[1, 3], [5, 7]]
target = 1
Expected:
True
Test 8:
Input:
matrix = [[1, 3], [5, 7]]
target = 7
Expected:
True
Test 9:
Input:
matrix = [[10, 20], [30, 40]]
target = 5
Expected:
False
Test 10:
Input:
matrix = [[10, 20], [30, 40]]
target = 50
Expected:
False
Test 11:
Input:
matrix = [[1, 3, 5, 7, 9]]
target = 5
Expected:
True
Test 12:
Input:
matrix = [[1], [3], [5], [7]]
target = 5
Expected:
True
Test 13:
Input:
matrix = [[1, 3], [5, 7]]
target = 4
Expected:
False
Test 14:
Input:
matrix = [[1, 1, 2], [3, 3, 4]]
target = 3
Expected:
True
========================================================
MY LEARNING CHECKLIST
========================================================
[ ] I understand the Search a 2D Matrix problem.
[ ] I understand the two matrix sorting properties.
[ ] I understand why the entire matrix can be treated as one sorted array.
[ ] I understand what binary search does.
[ ] I understand why we do not need to create a new 1D array.
[ ] I understand what m represents.
[ ] I understand what n represents.
[ ] I understand how len() works.
[ ] I understand why right = m * n - 1.
[ ] I understand why we use while left <= right.
[ ] I understand why we calculate mid.
[ ] I understand the difference between / and //.
[ ] I understand what the modulo operator % does.
[ ] I understand why row = mid // n.
[ ] I understand why column = mid % n.
[ ] I understand how matrix[row][column] works.
[ ] I understand how midValue is obtained.
[ ] I understand why we return True when midValue == target.
[ ] I understand why left becomes mid + 1.
[ ] I understand why right becomes mid - 1.
[ ] I understand why we return False after the loop.
[ ] I understand the complete dry run.
[ ] I understand why binary search eliminates half the search range.
[ ] I understand why time complexity is O(log(m * n)).
[ ] I understand why space complexity is O(1).
[ ] I understand how the algorithm handles an empty matrix.
[ ] I can convert a 1D index into a 2D matrix position.
[ ] I can write this solution without looking.
========================================================
"""
# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------
solution = Solution()
test_cases = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ([[5]], 5, True),
    ([[5]], 3, False),
    ([], 5, False),
    ([[]], 5, False),
    ([[1, 3], [5, 7]], 1, True),
    ([[1, 3], [5, 7]], 7, True),
    ([[10, 20], [30, 40]], 5, False),
    ([[10, 20], [30, 40]], 50, False),
    ([[1, 3, 5, 7, 9]], 5, True),
    ([[1], [3], [5], [7]], 5, True),
    ([[1, 3], [5, 7]], 4, False),
    ([[1, 1, 2], [3, 3, 4]], 3, True)
]
passed = 0
print("SEARCH A 2D MATRIX - TEST RESULTS")
print("----------------------------------------------")
for matrix, target, expected in test_cases:
    result = solution.searchMatrix(matrix, target)
    print("Matrix:", matrix)
    print("Target:", target)
    print("Expected:", expected)
    print("Actual:", result)
    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")
    print("----------------------------------------------")
print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")