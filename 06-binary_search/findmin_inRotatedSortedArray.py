
"""
========================================================
PROBLEM: FIND MINIMUM IN ROTATED SORTED ARRAY
TOPIC: BINARY SEARCH
APPROACH: BINARY SEARCH ON THE ROTATION POINT
========================================================

1. PROBLEM DESCRIPTION
--------------------------------------------------------
Given a list nums that was sorted in ascending order and then rotated, return its smallest value.

All values are unique. The solution must run in O(log N) time.

A rotation moves the last element to the front.

Example:
Original: [1, 2, 3, 4, 5]
Rotated:  [3, 4, 5, 1, 2]
Minimum: 1

IMPORTANT:
The rotated array contains two sorted parts.
The minimum is where the second part begins.

2. EXAMPLES
--------------------------------------------------------
Example 1:
Input:  [3, 4, 5, 1, 2]
Output: 1

Example 2:
Input:  [4, 5, 6, 7, 0, 1, 2]
Output: 0

Example 3:
Input:  [11, 13, 15, 17]
Output: 11

Example 4:
Input:  [2, 1]
Output: 1

3. MY APPROACH: BINARY SEARCH
--------------------------------------------------------
We use two pointers:

left = first index that may contain the minimum.
right = last index that may contain the minimum.

At each step, calculate the middle index and compare
nums[mid] with nums[right].

KEY RULE:

1. If nums[mid] > nums[right]:
   The minimum must be to the RIGHT of mid.
   Set left = mid + 1.

2. Otherwise, nums[mid] <= nums[right]:
   The minimum is at mid or to its LEFT.
   Set right = mid.

WHY COMPARE WITH nums[right]?
The right value helps us identify which part contains
the minimum.

WHY right = mid, NOT mid - 1?
Because mid itself might be the minimum.
We must keep it in the search range.

WHY left = mid + 1?
Because when nums[mid] > nums[right], mid cannot be
the minimum. We can safely remove it.

MY STEPS:
1. Set left to 0.
2. Set right to the last index.
3. Continue while left < right.
4. Calculate mid.
5. Compare nums[mid] with nums[right].
6. Update left or right.
7. Return nums[left].

4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Start with the full search range
        left = 0
        right = len(nums) - 1

        # Continue while more than one candidate remains
        while left < right:
            # Find the middle index
            mid = left + (right - left) // 2

            # Minimum is strictly to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            # Mid may be the minimum, so keep it
            else:
                right = mid

        # Left and right meet at the minimum element
        return nums[left]


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:
Creates a class called Solution.
LeetCode expects this class structure.

def findMin(self, nums: list[int]) -> int:
Defines the method that finds the minimum.

self:
Refers to the current object of the class.

nums:
The input list containing integers.

list[int]:
Means nums is a list of integers.

-> int:
Means the method returns one integer.

left = 0
Starts the search at the first index.

right = len(nums) - 1
len(nums) counts the elements.
We subtract 1 because list indices start at zero.

Example:
nums = [3, 4, 5, 1, 2]
len(nums) = 5
right = 4

while left < right:
Continues while at least two possible positions remain.
When left == right, only one candidate remains.

mid = left + (right - left) // 2
Finds the middle index.

 // means integer division.
It removes the decimal part.

Example:
7 // 2 = 3

if nums[mid] > nums[right]:
Checks whether the middle value is greater than
the rightmost value.

If TRUE:
The minimum must be after mid.

left = mid + 1
Removes mid and everything before it.
Searches the right part.

else:
Runs when nums[mid] <= nums[right].

The minimum could be at mid or before it.

right = mid
Keeps mid as a possible answer.
We do not use mid - 1 because mid might be the minimum.

return nums[left]
When the loop finishes, left == right.
That index points to the minimum value.

6. COMPLETE DRY RUN
--------------------------------------------------------

Input:
nums = [3, 4, 5, 1, 2]

Start:
left = 0
right = 4

Index:  0  1  2  3  4
Value:  3  4  5  1  2

ITERATION 1:

left = 0
right = 4

mid = 0 + (4 - 0) // 2
mid = 2

nums[mid] = 5
nums[right] = 2

Compare:
5 > 2

TRUE.

The minimum must be to the right of index 2.

left = mid + 1
left = 3

New range:
Indices 3 to 4
Values [1, 2]

ITERATION 2:

left = 3
right = 4

mid = 3 + (4 - 3) // 2
mid = 3

nums[mid] = 1
nums[right] = 2

Compare:
1 > 2

FALSE.

The minimum may be at index 3.
We must keep mid.

right = mid
right = 3

New range:
Index 3 only
Value [1]

STOP:

left = 3
right = 3

left < right is FALSE.

Return:
nums[3] = 1

FINAL ANSWER: 1

7. WHY BINARY SEARCH WORKS
--------------------------------------------------------
The rotation creates two ascending sections.

Example:
[4, 5, 6, 7, 0, 1, 2]

The minimum is 0.
It is where the second sorted section begins.

We compare nums[mid] with nums[right].

If nums[mid] > nums[right]:
The minimum is after mid.

If nums[mid] <= nums[right]:
The minimum is at mid or before mid.

We remove the half that cannot contain the minimum.

Every iteration reduces the search range by about half.
That is why binary search works.

8. TIME COMPLEXITY
--------------------------------------------------------

O(LOG N)

Where:
N = number of elements in nums.

The search range becomes smaller each iteration:

N -> N/2 -> N/4 -> N/8 -> ... -> 1

The number of times we divide N by 2 is about
log2(N).

Each iteration performs only a fixed number of
operations:

1. Calculate mid.
2. Compare two values.
3. Update left or right.

Each operation takes O(1) time.

Therefore:

TIME COMPLEXITY = O(LOG N)

9. SPACE COMPLEXITY
--------------------------------------------------------

O(1)

We use only three extra variables:

left
right
mid

We do not create another list, set, or stack.

The amount of extra memory stays the same even when
the input list becomes larger.

Therefore:

SPACE COMPLEXITY = O(1)

10. EDGE CASES
--------------------------------------------------------

EDGE CASE 1: ONE ELEMENT

Input:
[5]

Expected:
5

Reason:
There is only one element.
The loop does not run.
We return nums[0].

EDGE CASE 2: TWO ELEMENTS

Input:
[2, 1]

Expected:
1

Reason:
The minimum is the second element.

EDGE CASE 3: ALREADY SORTED

Input:
[1, 2, 3, 4]

Expected:
1

Reason:
The first element is already the minimum.

EDGE CASE 4: MINIMUM AT THE END

Input:
[2, 3, 4, 1]

Expected:
1

Reason:
The minimum is the final element.

EDGE CASE 5: MINIMUM AT THE START

Input:
[1, 2, 3, 4, 5]

Expected:
1

Reason:
The minimum is at index 0.

EDGE CASE 6: LARGER INPUT

Input:
[7, 8, 9, 1, 2, 3, 4, 5, 6]

Expected:
1

Reason:
Binary search still removes about half the range
in each iteration.

IMPORTANT:
This problem guarantees unique values.
With duplicates, the comparison can become ambiguous.

11. LEARNING CHECKLIST
--------------------------------------------------------

[ ] I understand what a rotated sorted array is.
[ ] I understand what the minimum element means.
[ ] I understand why left starts at 0.
[ ] I understand why right is len(nums) - 1.
[ ] I understand what while left < right means.
[ ] I understand how mid is calculated.
[ ] I understand what integer division // does.
[ ] I understand why we compare nums[mid] and nums[right].
[ ] I understand why left = mid + 1 is used.
[ ] I understand why right = mid is used.
[ ] I understand why we do not use right = mid - 1.
[ ] I understand why the loop stops when left == right.
[ ] I understand why we return nums[left].
[ ] I understand why time complexity is O(log N).
[ ] I understand why space complexity is O(1).
[ ] I can explain the dry run without looking at the notes.

12. TEST RUNNER
--------------------------------------------------------
"""

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([2, 1], 1),
        ([5], 5),
        ([1, 2], 1),
        ([2, 3, 4, 1], 1),
        ([1, 2, 3, 4, 5], 1),
        ([7, 8, 9, 1, 2, 3, 4, 5, 6], 1),
        ([3, 1, 2], 1),
        ([6, 7, 1, 2, 3, 4, 5], 1),
        ([2, 3, 1], 1)
    ]

    passed = 0

    print("FIND MINIMUM IN ROTATED SORTED ARRAY")
    print("------------------------------------")

    for nums, expected in test_cases:
        result = solution.findMin(nums)

        print("Input:", nums)
        print("Expected:", expected)
        print("Actual:", result)

        if result == expected:
            print("Status: PASS")
            passed += 1
        else:
            print("Status: FAIL")

        print("------------------------------------")

    print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
