
"""
========================================================
PROBLEM: BINARY SEARCH
TOPIC: BINARY SEARCH
APPROACH: ITERATIVE BINARY SEARCH
========================================================
1. PROBLEM DESCRIPTION
--------------------------------------------------------
Given a list of integers called nums, sorted in ascending order, and an integer called target:
Find the index of target in nums.
If target exists:
Return its index.
If target does not exist:
Return -1.
IMPORTANT:
The array is already sorted in ascending order.
Example:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
Output:
4
Why?
The value 9 is at index 4.
We must achieve:
TIME COMPLEXITY = O(LOG N)
2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------
Example 1:
Input:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
Output:
4
Explanation:
The value 9 is at index 4.
Example 2:
Input:
nums = [-1, 0, 3, 5, 9, 12]
target = 2
Output:
-1
Explanation:
The value 2 does not exist in the array.
Example 3:
Input:
nums = [5]
target = 5
Output:
0
Explanation:
The only element is at index 0.
3. MY APPROACH: BINARY SEARCH
--------------------------------------------------------
I use three main variables:
1. left
2. right
3. mid
IMPORTANT:
Binary Search works because the array is sorted.
MY STEPS:
1. Set left to the first index: 0.
2. Set right to the last index: len(nums) - 1.
3. Check whether left is less than or equal to right.
4. Calculate the middle index.
5. Compare the middle value with target.
6. If they are equal, return mid.
7. If the middle value is smaller than target:
   Move left to mid + 1.
8. Otherwise:
   Move right to mid - 1.
9. Repeat until target is found or the search area is empty.
10. If the loop finishes, return -1.
WHY DO WE USE BINARY SEARCH?
Instead of checking every element, we remove approximately half of the remaining search area after every comparison.
Example:
nums = [1, 3, 5, 7, 9, 11, 13]
target = 11
First middle value = 7.
11 is greater than 7.
Ignore the left half.
Remaining:
[9, 11, 13]
Next middle value = 11.
Target found!
4. PYTHON SOLUTION
--------------------------------------------------------
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Set the first and last search indices
        left = 0
        right = len(nums) - 1
        # Continue while the search area is not empty
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2
            # Check whether the middle value is the target
            if nums[mid] == target:
                return mid
            # If the middle value is smaller, search right
            elif nums[mid] < target:
                left = mid + 1
            # Otherwise, search left
            else:
                right = mid - 1
        # Target does not exist in the array
        return -1
"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------
class Solution:
Creates a class called Solution.
LeetCode commonly uses this class structure.
def search(self, nums: list[int], target: int) -> int:
Creates a function called search.
self:
Refers to the current object of the class.
nums:
The input list containing sorted integers.
list[int]:
Means nums is a list of integers.
target:
The integer we want to find.
-> int:
Means the function returns an integer.
The returned integer is:
- The target's index, if found.
-1, if the target is not found.
A. INITIALIZE LEFT
--------------------------------------------------------
left = 0
Creates a variable called left.
It represents the first index of the current search area.
Python list indices start at zero.
Example:
nums = [2, 4, 6, 8, 10]
Indices:
          0  1  2  3   4
Therefore:
left = 0
B. INITIALIZE RIGHT
--------------------------------------------------------
right = len(nums) - 1
len(nums):
Counts the number of elements in the list.
Example:
nums = [2, 4, 6, 8, 10]
len(nums) = 5
But the last index is 4, not 5.
Why?
Because Python indices start at zero.
Therefore:
right = 5 - 1
right = 4
IMPORTANT:
left and right represent the boundaries of the current search area.
C. CHECK WHETHER THE SEARCH AREA EXISTS
--------------------------------------------------------
while left <= right:
This loop continues while left is less than or equal to right.
What does this mean?
left <= right
Means there is still at least one index inside the search area.
Example 1:
left = 2
right = 4
2 <= 4
TRUE.
Continue searching.
Example 2:
left = 3
right = 2
3 <= 2
FALSE.
The search area is empty.
Stop searching.
WHY DO WE USE <= INSTEAD OF <?
Because the middle element might be the only remaining element.
Example:
left = 2
right = 2
There is one element at index 2.
If we used:
left < right
The loop would stop.
We would miss that final element.
Therefore:
left <= right
is necessary for this implementation.
D. CALCULATE THE MIDDLE INDEX
--------------------------------------------------------
mid = left + (right - left) // 2
This calculates the middle index of the current search area.
Let's understand each part.
PART 1:
right - left
Calculates the distance between the boundaries.
Example:
left = 2
right = 6
right - left = 4
PART 2:
(right - left) // 2
Divides the distance by 2 and rounds down to a whole number.
Example:
4 // 2 = 2
PART 3:
left + (right - left) // 2
Adds the half-distance to the left boundary.
Example:
left = 2
right = 6
mid = 2 + (6 - 2) // 2
mid = 2 + 4 // 2
mid = 2 + 2
mid = 4
Therefore:
mid = 4
WHY DO WE USE // INSTEAD OF /?
/ performs normal division.
Example:
5 / 2 = 2.5
// performs floor division.
Example:
5 // 2 = 2
List indices must be integers.
Therefore:
We use //.
WHY NOT USE (left + right) // 2?
We could use it in Python:
mid = (left + right) // 2
It works because Python integers can grow beyond fixed machine integer limits.
However, the original Java formula:
left + (right - left) / 2
avoids possible integer overflow when using fixed-size integer types.
Our Python version preserves that formula.
E. CHECK WHETHER THE TARGET IS FOUND
--------------------------------------------------------
if nums[mid] == target:
This compares the middle value with target.
nums[mid]:
Gets the value stored at index mid.
Example:
nums = [2, 4, 6, 8, 10]
mid = 2
nums[mid] = nums[2]
nums[mid] = 6
Suppose:
target = 6
Comparison:
nums[mid] == target
6 == 6
TRUE.
The target has been found.
F. RETURN THE MIDDLE INDEX
--------------------------------------------------------
return mid
Returns the index where the target was found.
Example:
mid = 2
return 2
IMPORTANT:
We return the index, not the value.
G. SEARCH THE RIGHT HALF
--------------------------------------------------------
elif nums[mid] < target:
Checks whether the middle value is smaller than the target.
Example:
nums = [1, 3, 5, 7, 9, 11, 13]
mid = 3
nums[mid] = 7
target = 11
Comparison:
7 < 11
TRUE.
What does this tell us?
The array is sorted in ascending order.
Therefore, every value to the left of 7 is also smaller than 11.
We do not need to search that part.
We can ignore the left half.
H. MOVE THE LEFT BOUNDARY
--------------------------------------------------------
left = mid + 1
Moves the beginning of the search area to the position immediately after mid.
Example:
mid = 3
left = 3 + 1
left = 4
The new search area starts at index 4.
WHY +1?
Because we already checked nums[mid].
We know it is not the target.
Therefore, we do not need to check it again.
I. SEARCH THE LEFT HALF
--------------------------------------------------------
else:
This runs when both previous conditions are false.
We already know:
nums[mid] != target
And:
nums[mid] is NOT smaller than target.
Therefore:
nums[mid] > target
Example:
nums = [1, 3, 5, 7, 9, 11, 13]
mid = 3
nums[mid] = 7
target = 5
7 > 5
The target must be on the left side.
WHY?
Because the array is sorted in ascending order.
All values to the right of 7 are greater than or equal to 7.
They cannot contain 5.
We can ignore the right half.
J. MOVE THE RIGHT BOUNDARY
--------------------------------------------------------
right = mid - 1
Moves the end of the search area to the position immediately before mid.
Example:
mid = 3
right = 3 - 1
right = 2
The new search area ends at index 2.
WHY -1?
Because we already checked nums[mid].
We know it is not the target.
Therefore, we do not need to check it again.
K. RETURN -1
--------------------------------------------------------
return -1
This line runs when the while loop finishes.
It means:
The search area is empty.
The target was not found.
Example:
nums = [1, 3, 5, 7]
target = 4
No element equals 4.
Eventually:
left > right
The loop stops.
The function returns:
-1
IMPORTANT:
Index -1 is used here as a special result meaning "target not found."
6. COMPLETE DRY RUN
--------------------------------------------------------
Input:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
INITIAL STATE:
left = 0
right = 5
Indices:
       0  1  2  3  4   5
nums = [-1, 0, 3, 5, 9, 12]
ITERATION 1:
left = 0
right = 5
Calculate mid:
mid = 0 + (5 - 0) // 2
mid = 0 + 5 // 2
mid = 2
Check:
nums[2] = 3
Compare:
3 == 9
FALSE.
Check:
3 < 9
TRUE.
The target must be on the right side.
Move left:
left = mid + 1
left = 2 + 1
left = 3
New search area:
Indices 3, 4, 5
ITERATION 2:
left = 3
right = 5
Calculate mid:
mid = 3 + (5 - 3) // 2
mid = 3 + 2 // 2
mid = 4
Check:
nums[4] = 9
Compare:
9 == 9
TRUE.
TARGET FOUND!
Return:
4
FINAL RESULT:
Index of target = 4
7. SECOND DRY RUN: TARGET NOT FOUND
--------------------------------------------------------
Input:
nums = [1, 3, 5, 7, 9]
target = 4
INITIAL STATE:
left = 0
right = 4
ITERATION 1:
left = 0
right = 4
mid = 0 + (4 - 0) // 2
mid = 2
nums[2] = 5
Compare:
5 == 4
FALSE.
Compare:
5 < 4
FALSE.
Therefore:
5 > 4
Search the left half.
right = mid - 1
right = 1
ITERATION 2:
left = 0
right = 1
mid = 0 + (1 - 0) // 2
mid = 0
nums[0] = 1
Compare:
1 == 4
FALSE.
Compare:
1 < 4
TRUE.
Search the right half.
left = mid + 1
left = 1
ITERATION 3:
left = 1
right = 1
mid = 1 + (1 - 1) // 2
mid = 1
nums[1] = 3
Compare:
3 == 4
FALSE.
Compare:
3 < 4
TRUE.
Move left:
left = mid + 1
left = 2
NOW CHECK THE WHILE CONDITION:
left = 2
right = 1
2 <= 1
FALSE.
The loop stops.
FINAL RESULT:
return -1
The target does not exist.
8. WHY THIS IS BINARY SEARCH
--------------------------------------------------------
Binary Search repeatedly divides the search area into smaller parts.
Example:
nums = [1, 2, 3, 4, 5, 6, 7, 8]
Imagine we want to find 7.
FIRST SEARCH:
Check the middle.
SECOND SEARCH:
Ignore half of the array.
THIRD SEARCH:
Check the middle of the remaining part.
Each comparison removes approximately half of the remaining search area.
IMPORTANT:
We do not move through every element one by one.
We use the sorted order to decide which half can be ignored.
WHY MUST THE ARRAY BE SORTED?
Because the comparison tells us where to search.
If nums[mid] < target:
The target can only be on the right.
If nums[mid] > target:
The target can only be on the left.
Without sorted data, these decisions would not be reliable.
9. TIME COMPLEXITY
--------------------------------------------------------
O(LOG N)
Where:
N = Number of elements in nums.
WHY?
Every iteration removes approximately half of the remaining search area.
Example:
Start with 16 elements.
After each comparison:
16 -> 8 -> 4 -> 2 -> 1
We need only about 5 comparisons.
The number of comparisons grows logarithmically.
Mathematically:
After k iterations, the remaining search area is approximately:
N / 2^k
We stop when approximately one element remains.
Therefore:
N / 2^k = 1
This gives:
k = log2(N)
So:
TIME COMPLEXITY = O(LOG N)
IMPORTANT:
The while loop does not visit every element.
It repeatedly removes half of the search area.
That is why Binary Search is faster than a linear search for large sorted arrays.
COMPARISON:
Linear Search:
O(N)
Binary Search:
O(LOG N)
10. SPACE COMPLEXITY
--------------------------------------------------------
O(1)
WHY?
We only create a fixed number of variables:
left
right
mid
We do not create another list or stack.
We do not use recursion.
The algorithm works directly on the input list.
The number of extra variables stays the same even if the input list becomes very large.
Therefore:
SPACE COMPLEXITY = O(1)
IMPORTANT:
This is an iterative Binary Search.
An iterative solution uses a loop.
A recursive Binary Search would use function calls and require O(LOG N) call-stack space.
OUR SOLUTION:
TIME = O(LOG N)
SPACE = O(1)
11. EDGE CASES
--------------------------------------------------------
EDGE CASE 1: ONE ELEMENT, TARGET FOUND
Input:
nums = [5]
target = 5
Expected:
0
EDGE CASE 2: ONE ELEMENT, TARGET NOT FOUND
Input:
nums = [5]
target = 3
Expected:
-1
EDGE CASE 3: EMPTY ARRAY
Input:
nums = []
target = 5
Expected:
-1
Reason:
right = len(nums) - 1
right = 0 - 1
right = -1
The while condition is false immediately.
EDGE CASE 4: TARGET AT THE BEGINNING
Input:
nums = [1, 3, 5, 7, 9]
target = 1
Expected:
0
EDGE CASE 5: TARGET AT THE END
Input:
nums = [1, 3, 5, 7, 9]
target = 9
Expected:
4
EDGE CASE 6: TARGET IN THE MIDDLE
Input:
nums = [1, 3, 5, 7, 9]
target = 5
Expected:
2
EDGE CASE 7: TARGET SMALLER THAN ALL VALUES
Input:
nums = [2, 4, 6, 8]
target = 1
Expected:
-1
EDGE CASE 8: TARGET GREATER THAN ALL VALUES
Input:
nums = [2, 4, 6, 8]
target = 10
Expected:
-1
EDGE CASE 9: NEGATIVE NUMBERS
Input:
nums = [-10, -5, -2, 0, 3]
target = -5
Expected:
1
EDGE CASE 10: TWO ELEMENTS
Input:
nums = [2, 4]
target = 4
Expected:
1
IMPORTANT:
The problem states that nums is sorted.
The solution assumes the input follows that rule.
12. MY OWN TEST CASES
--------------------------------------------------------
Test 1:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
Expected: 4
Test 2:
nums = [-1, 0, 3, 5, 9, 12]
target = 2
Expected: -1
Test 3:
nums = [5]
target = 5
Expected: 0
Test 4:
nums = [5]
target = 3
Expected: -1
Test 5:
nums = []
target = 5
Expected: -1
Test 6:
nums = [1, 3, 5, 7, 9]
target = 1
Expected: 0
Test 7:
nums = [1, 3, 5, 7, 9]
target = 9
Expected: 4
Test 8:
nums = [2, 4, 6, 8]
target = 10
Expected: -1
Test 9:
nums = [-10, -5, -2, 0, 3]
target = -5
Expected: 1
Test 10:
nums = [2, 4]
target = 4
Expected: 1
========================================================
MY LEARNING CHECKLIST
========================================================
[ ] I understand the Binary Search problem.
[ ] I understand why the input must be sorted.
[ ] I understand what an index is.
[ ] I understand why Python indices start at zero.
[ ] I understand what left represents.
[ ] I understand what right represents.
[ ] I understand why right = len(nums) - 1.
[ ] I understand what the while loop checks.
[ ] I understand why we use <= instead of <.
[ ] I understand what mid represents.
[ ] I understand how the middle index is calculated.
[ ] I understand why we use // instead of /.
[ ] I understand how nums[mid] works.
[ ] I understand how == compares two values.
[ ] I understand why we return mid when found.
[ ] I understand why nums[mid] < target means search right.
[ ] I understand why we use left = mid + 1.
[ ] I understand why nums[mid] > target means search left.
[ ] I understand why we use right = mid - 1.
[ ] I understand why we do not check mid again.
[ ] I understand when the while loop stops.
[ ] I understand why we return -1.
[ ] I understand how Binary Search removes half the search area.
[ ] I understand why time complexity is O(LOG N).
[ ] I understand why space complexity is O(1).
[ ] I can write Binary Search without looking.
========================================================
"""
# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------
solution = Solution()
test_cases = [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([5], 5, 0),
    ([5], 3, -1),
    ([], 5, -1),
    ([1, 3, 5, 7, 9], 1, 0),
    ([1, 3, 5, 7, 9], 9, 4),
    ([2, 4, 6, 8], 10, -1),
    ([-10, -5, -2, 0, 3], -5, 1),
    ([2, 4], 4, 1)
]
passed = 0
print("BINARY SEARCH - TEST RESULTS")
print("----------------------------------------------")
for nums, target, expected in test_cases:
    result = solution.search(nums, target)
    print("Numbers:", nums)
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
