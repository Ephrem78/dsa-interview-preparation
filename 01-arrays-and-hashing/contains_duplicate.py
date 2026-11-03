
"""
========================================================
PROBLEM: CONTAINS DUPLICATE
TOPIC: ARRAYS AND HASHING
APPROACH: HASH SET
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given a list of integers called nums:

Return True if any number appears two or more times.

Return False if every number is different.

In simple words:
We need to find out if the list contains a duplicate number.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
nums = [1, 4, 3, 5, 4]

Output:
True

Explanation:
The number 4 appears two times.
Therefore, the list contains a duplicate.


Example 2:

Input:
nums = [1, 2, 3, 4, 5]

Output:
False

Explanation:
Every number appears only once.
Therefore, there are no duplicates.


3. MY APPROACH: HASH SET
--------------------------------------------------------

I use a Python set to remember the numbers I have already
visited.

A set stores unique values.

My steps:

1. Create an empty set called seen.
2. Visit every number in the list.
3. Check whether the current number is already in seen.
4. If YES, return True because a duplicate exists.
5. If NO, add the number to seen.
6. If the loop finishes, return False.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def containsDuplicate(self, nums: list[int]) -> bool:

        # Create an empty set to remember visited numbers
        seen = set()

        # Visit every number using its index
        for i in range(len(nums)):

            # Check whether the current number is already in seen
            if nums[i] in seen:

                # A duplicate exists
                return True

            else:

                # Remember the current number
                seen.add(nums[i])

        # The loop finished without finding a duplicate
        return False


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:
Creates a class called Solution.
LeetCode commonly uses this class structure.

def containsDuplicate(self, nums: list[int]) -> bool:
Creates a function that checks for duplicate numbers.

self:
Refers to the current object of the class.

nums:
The list of numbers given to our function.

list[int]:
Means that nums is expected to be a list of integers.

-> bool:
Means that the function returns True or False.

seen = set():
Creates an empty set.
We use it to remember numbers we have already visited.

for i in range(len(nums)):
Visits every position in the list.

nums[i]:
Gets the number at position i.

if nums[i] in seen:
Checks whether the current number is already in the set.

return True:
Stops the function and reports that a duplicate exists.

seen.add(nums[i]):
Adds the current number to the set.

return False:
If the loop finishes, no duplicate was found.


6. TIME COMPLEXITY
--------------------------------------------------------

O(n)

n = number of elements in the list.

Why?

We visit each number at most once.

Checking whether a number exists in a set takes O(1)
average time.

Therefore:

n visits × O(1) average lookup = O(n)


7. SPACE COMPLEXITY
--------------------------------------------------------

O(n)

Why?

We use an additional set called seen.

In the worst case, every number is different.
The set may then store all n numbers.

Therefore, the extra space can grow with the input size.


8. MY OWN TEST CASES
--------------------------------------------------------

Test 1:
Input:  [1, 4, 3, 5, 4]
Expected: True
Reason: 4 appears twice.

Test 2:
Input:  [1, 2, 3, 4, 5]
Expected: False
Reason: Every number is different.

Test 3:
Input:  [7, 7]
Expected: True
Reason: 7 appears twice.

Test 4:
Input:  []
Expected: False
Reason: The list is empty.

Test 5:
Input:  [9]
Expected: False
Reason: There is only one number.

Test 6:
Input:  [-1, 0, -1]
Expected: True
Reason: -1 appears twice.

Test 7:
Input:  [0, 1, 2, 3]
Expected: False
Reason: Every number is different.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a Hash Set is.
[ ] I understand how the for loop works.
[ ] I understand how "in" checks membership.
[ ] I understand how set.add() works.
[ ] I can explain return True and return False.
[ ] I can write this solution without looking.
[ ] I understand O(n) time complexity.
[ ] I understand O(n) space complexity.

========================================================
"""

# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    ([1, 4, 3, 5, 4], True),
    ([1, 2, 3, 4, 5], False),
    ([7, 7], True),
    ([], False),
    ([9], False),
    ([-1, 0, -1], True),
    ([0, 1, 2, 3], False)
]

print("CONTAINS DUPLICATE - TEST RESULTS")
print("----------------------------------")

for nums, expected in test_cases:

    result = solution.containsDuplicate(nums)

    print("Input:", nums)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
    else:
        print("Status: FAIL")

    print("----------------------------------")
