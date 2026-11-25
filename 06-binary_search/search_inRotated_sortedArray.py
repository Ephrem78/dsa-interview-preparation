
"""
========================================================
PROBLEM: SEARCH IN ROTATED SORTED ARRAY
TOPIC: BINARY SEARCH
APPROACH: BINARY SEARCH + IDENTIFY SORTED HALF
========================================================
1. PROBLEM DESCRIPTION
Given an ascending sorted array with distinct values, the array may be rotated.
Find the index of target. If target does not exist, return -1.
Example:
Original: [0, 1, 2, 4, 5, 6, 7]
Rotated:  [4, 5, 6, 7, 0, 1, 2]
Target: 0
Output: 4
IMPORTANT:
The array contains two sorted sections.
At every iteration, at least one half is sorted.
We use that sorted half to decide where target may exist.
The algorithm must run in O(log N) time.
2. EXAMPLES
Example 1:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Example 2:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1
Example 4:
Input: nums = [1], target = 1
Output: 0
3. MY APPROACH: BINARY SEARCH
We use three variables:
left  = first possible index
right = last possible index
mid   = middle index
MY STEPS:
1. Set left = 0.
2. Set right = len(nums) - 1.
3. Continue while left <= right.
4. Calculate mid.
5. If nums[mid] == target, return mid.
6. Identify which half is sorted.
7. Check whether target belongs inside that sorted half.
8. Keep the half that may contain target.
9. If target is not found, return -1.
KEY RULE 1: LEFT HALF IS SORTED
If nums[left] <= nums[mid]:
The left half is sorted.
Check whether target is inside it:
nums[left] <= target <= nums[mid]
If true:
Search left: right = mid - 1
Otherwise:
Search right: left = mid + 1
KEY RULE 2: RIGHT HALF IS SORTED
Otherwise:
The right half is sorted.
Check whether target is inside it:
nums[mid] <= target <= nums[right]
If true:
Search right: left = mid + 1
Otherwise:
Search left: right = mid - 1
WHY DOES THIS WORK?
One half is always sorted.
In a sorted half, we can check whether target belongs
between its smallest and largest values.
If target is outside that range, it cannot be there.
We safely remove that half.
4. PYTHON SOLUTION
========================================================
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


"""
5. EXPLANATION OF IMPORTANT LINES
========================================================
class Solution:
Creates a class called Solution.
LeetCode uses this class structure.
def search(self, nums: list[int], target: int) -> int:
Creates a function called search.
self:
Refers to the current object.
nums:
The input list.
list[int]:
Means nums contains integers.
target:
The value we are searching for.
-> int:
The function returns an integer index or -1.
A. INITIALIZE SEARCH BOUNDARIES
--------------------------------------------------------
left, right = 0, len(nums) - 1
left = 0:
Starts at the first index.
right = len(nums) - 1:
Starts at the last index.
We subtract 1 because indices start at zero.
Example:
nums = [4, 5, 6, 7, 0, 1, 2]
len(nums) = 7
right = 6
Valid indices:
0, 1, 2, 3, 4, 5, 6
B. SEARCH WHILE THE RANGE IS VALID
--------------------------------------------------------
while left <= right:
Continues while at least one possible index remains.
Why <= instead of <?
Because left and right can point to the same index.
That last index must still be checked.
Example:
left = 3
right = 3
There is one candidate.
We must check it.
If left > right:
The search range is empty.
The target was not found.
C. CALCULATE THE MIDDLE INDEX
--------------------------------------------------------
mid = left + (right - left) // 2
Finds the middle index.
 // means integer division.
Example:
left = 2
right = 6
mid = 2 + (6 - 2) // 2
mid = 2 + 4 // 2
mid = 4
Why use this formula?
It calculates the middle of the search range.
D. CHECK IF TARGET IS FOUND
--------------------------------------------------------
if nums[mid] == target:
    return mid
Checks whether the middle value is the target.
If equal:
We found it.
Return its index immediately.
Example:
nums[mid] = 0
target = 0
Return mid.
E. IDENTIFY THE SORTED LEFT HALF
--------------------------------------------------------
if nums[left] <= nums[mid]:
Checks whether the left half is sorted.
Why <=?
The left and middle indices may be the same.
A single element is also sorted.
Example:
nums = [4, 5, 6, 7, 0, 1, 2]
left = 0
mid = 3
nums[left] = 4
nums[mid] = 7
4 <= 7
TRUE.
The left half [4, 5, 6, 7] is sorted.
F. CHECK IF TARGET IS INSIDE THE SORTED LEFT HALF
--------------------------------------------------------
if nums[left] <= target <= nums[mid]:
Python chained comparison.
This means:
nums[left] <= target AND target <= nums[mid]
Example:
nums[left] = 4
target = 6
nums[mid] = 7
4 <= 6 <= 7
TRUE.
Target is inside the sorted left half.
G. SEARCH THE LEFT HALF
--------------------------------------------------------
right = mid - 1
Removes mid and everything to its right.
Why?
We already checked nums[mid].
Target is inside the left sorted section.
Therefore, search the remaining left section.
H. SEARCH THE RIGHT HALF
--------------------------------------------------------
left = mid + 1
Used when target is NOT inside the sorted left half.
The target must be in the other half, if it exists.
We remove mid and everything before it.
I. IDENTIFY THE SORTED RIGHT HALF
--------------------------------------------------------
else:
Runs when the left half is not sorted.
The right half must be sorted.
Example:
nums = [6, 7, 0, 1, 2, 3, 4]
left = 0
mid = 3
nums[left] = 6
nums[mid] = 1
6 <= 1 is FALSE.
The left half crosses the rotation.
The right half [1, 2, 3, 4] is sorted.
J. CHECK IF TARGET IS INSIDE THE SORTED RIGHT HALF
--------------------------------------------------------
if nums[mid] <= target <= nums[right]:
Checks whether target is inside the sorted right half.
Example:
nums[mid] = 1
target = 3
nums[right] = 4
1 <= 3 <= 4
TRUE.
Target belongs to the right half.
K. SEARCH THE RIGHT HALF
--------------------------------------------------------
left = mid + 1
Removes the left half.
Target may exist in the right sorted half.
L. SEARCH THE LEFT HALF
--------------------------------------------------------
right = mid - 1
Used when target is NOT inside the sorted right half.
Target must be in the other half, if it exists.
We remove mid and everything to its right.
M. TARGET NOT FOUND
--------------------------------------------------------
return -1
The while loop finishes when:
left > right
There are no remaining indices to search.
The target does not exist.
Return -1.
6. COMPLETE DRY RUN: TARGET = 0
========================================================
Input:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
INITIAL:
left = 0
right = 6
ITERATION 1:
left = 0
right = 6
mid = 0 + (6 - 0) // 2
mid = 3
nums[mid] = 7
Is 7 == 0?
FALSE.
CHECK LEFT HALF:
nums[left] = 4
nums[mid] = 7
4 <= 7
TRUE.
Left half [4, 5, 6, 7] is sorted.
CHECK TARGET RANGE:
4 <= 0 <= 7
FALSE.
Target is not inside the left half.
SEARCH RIGHT:
left = mid + 1
left = 4
New range:
Indices 4 to 6
Values [0, 1, 2]
ITERATION 2:
left = 4
right = 6
mid = 4 + (6 - 4) // 2
mid = 5
nums[mid] = 1
Is 1 == 0?
FALSE.
CHECK LEFT HALF:
nums[left] = 0
nums[mid] = 1
0 <= 1
TRUE.
Left half [0, 1] is sorted.
CHECK TARGET RANGE:
0 <= 0 <= 1
TRUE.
Target belongs to the left half.
SEARCH LEFT:
right = mid - 1
right = 4
New range:
Index 4 only
Value [0]
ITERATION 3:
left = 4
right = 4
mid = 4 + (4 - 4) // 2
mid = 4
nums[mid] = 0
Is 0 == target?
TRUE.
RETURN:
4
FINAL ANSWER: 4
7. DRY RUN: TARGET = 3 (NOT FOUND)
========================================================
Input:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
ITERATION 1:
left = 0, right = 6
mid = 3
nums[mid] = 7
Target is not 7.
Left half is sorted:
4 <= 7
Check target:
4 <= 3 <= 7
FALSE.
Search right:
left = 4
ITERATION 2:
left = 4, right = 6
mid = 5
nums[mid] = 1
Target is not 1.
Left half is sorted:
0 <= 1
Check target:
0 <= 3 <= 1
FALSE.
Search right:
left = 6
ITERATION 3:
left = 6, right = 6
mid = 6
nums[mid] = 2
Target is not 2.
Left half is sorted:
2 <= 2
Check target:
2 <= 3 <= 2
FALSE.
Search right:
left = 7
right = 6
STOP:
left > right
Search range is empty.
RETURN: -1
FINAL ANSWER: -1
8. WHY BINARY SEARCH WORKS
========================================================
The array has two sorted sections after rotation.
Example:
[6, 7, 0, 1, 2, 3, 4]
At each step:
1. We calculate mid.
2. One half is sorted.
3. We check whether target is inside that sorted half.
4. If it is, we search that half.
5. If not, we search the other half.
We remove about half of the search range each iteration.
We never need to check every element.
Therefore, the algorithm is Binary Search.
9. TIME COMPLEXITY
========================================================
O(LOG N)
N = number of elements.
Every iteration removes about half of the search range.
Example:
8 -> 4 -> 2 -> 1
For 8 elements, it takes about 3 search steps.
For 1,000,000 elements, it takes about 20 steps.
Each iteration performs a fixed number of operations:
1. Calculate mid.
2. Compare values.
3. Update left or right.
Each operation takes O(1).
Therefore:
TIME COMPLEXITY = O(LOG N)
10. SPACE COMPLEXITY
========================================================
O(1)
We use only a few variables:
left
right
mid
No new list, set, dictionary, or stack is created.
Memory does not grow with the input size.
Therefore:
SPACE COMPLEXITY = O(1)
11. EDGE CASES
========================================================
EDGE CASE 1: ONE ELEMENT, TARGET FOUND
Input: nums = [5], target = 5
Expected: 0
The only element is the target.
EDGE CASE 2: ONE ELEMENT, TARGET MISSING
Input: nums = [5], target = 3
Expected: -1
The only element is not the target.
EDGE CASE 3: TWO ELEMENTS, ROTATED
Input: nums = [3, 1], target = 1
Expected: 1
EDGE CASE 4: TWO ELEMENTS, NOT ROTATED
Input: nums = [1, 3], target = 3
Expected: 1
EDGE CASE 5: TARGET AT FIRST INDEX
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 4
Expected: 0
EDGE CASE 6: TARGET AT LAST INDEX
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 2
Expected: 6
EDGE CASE 7: TARGET AT ROTATION POINT
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Expected: 4
EDGE CASE 8: TARGET DOES NOT EXIST
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Expected: -1
EDGE CASE 9: ARRAY NOT ROTATED
Input: nums = [1, 2, 3, 4, 5, 6], target = 5
Expected: 4
EDGE CASE 10: ROTATED BY ONE
Input: nums = [5, 1, 2, 3, 4], target = 5
Expected: 0
IMPORTANT:
The problem guarantees distinct values.
Duplicates would make identifying the sorted half more difficult.
12. LEARNING CHECKLIST
========================================================
[ ] I understand what a rotated sorted array is.
[ ] I understand why the array has two sorted sections.
[ ] I understand why left starts at 0.
[ ] I understand why right starts at len(nums) - 1.
[ ] I understand why we use while left <= right.
[ ] I understand how mid is calculated.
[ ] I understand why we check nums[mid] == target first.
[ ] I understand nums[left] <= nums[mid].
[ ] I understand how to identify the sorted left half.
[ ] I understand how to check the target range.
[ ] I understand why right = mid - 1 is used.
[ ] I understand why left = mid + 1 is used.
[ ] I understand how to identify the sorted right half.
[ ] I understand nums[mid] <= target <= nums[right].
[ ] I understand why one half can always be sorted.
[ ] I understand why we can remove half the range.
[ ] I understand why we return -1.
[ ] I understand the complete dry run.
[ ] I understand time complexity O(log N).
[ ] I understand space complexity O(1).
[ ] I can write the solution without looking at the notes.
========================================================
"""
# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([3, 1], 1, 1),
        ([1, 3], 3, 1),
        ([4, 5, 6, 7, 0, 1, 2], 4, 0),
        ([4, 5, 6, 7, 0, 1, 2], 2, 6),
        ([1, 2, 3, 4, 5, 6], 5, 4),
        ([5, 1, 2, 3, 4], 5, 0),
        ([6, 7, 0, 1, 2, 3, 4, 5], 3, 5),
        ([6, 7, 0, 1, 2, 3, 4, 5], 6, 0),
    ]

    passed = 0

    print("SEARCH IN ROTATED SORTED ARRAY - TEST RESULTS")
    print("--------------------------------------------")

    for nums, target, expected in test_cases:
        result = solution.search(nums, target)
        status = "PASS" if result == expected else "FAIL"

        print(f"Nums: {nums} | Target: {target}")
        print(f"Expected: {expected} | Actual: {result} | {status}")

        passed += result == expected
        print("--------------------------------------------")

    print(f"FINAL RESULT: {passed}/{len(test_cases)} TESTS PASSED")
