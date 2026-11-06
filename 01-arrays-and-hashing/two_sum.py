
"""
========================================================
PROBLEM: TWO SUM
TOPIC: ARRAYS AND HASHING
APPROACH: HASH MAP
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given a list of integers called nums and an integer
called target:

Return the indices of the two numbers whose sum equals
the target.

Important rules:

1. We must return the indices, not the numbers.
2. We cannot use the same element twice.
3. There is exactly one valid answer.

In simple words:

Find two different numbers that add up to the target.
Then return their original positions (indices).


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Explanation:

nums[0] = 2
nums[1] = 7

2 + 7 = 9

Therefore, we return their indices: [0, 1].


Example 2:

Input:
nums = [3, 2, 4]
target = 6

Output:
[1, 2]

Explanation:

nums[1] = 2
nums[2] = 4

2 + 4 = 6

Therefore, we return [1, 2].


Example 3:

Input:
nums = [3, 3]
target = 6

Output:
[0, 1]

Explanation:

3 + 3 = 6

The two numbers are at different indices.


3. MY APPROACH: HASH MAP
--------------------------------------------------------

I use a Python dictionary to remember numbers I have
already visited and their original indices.

My dictionary is called seen.

The dictionary stores:

KEY   = number
VALUE = index of that number

My steps:

1. Create an empty dictionary called seen.
2. Visit every number using its index.
3. Calculate the number we need:

   complement = target - current number

4. Check whether the complement already exists in seen.
5. If YES, return the stored index and the current index.
6. If NO, store the current number and its index.
7. If the loop finishes, return an empty list.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # Create an empty dictionary
        seen = {}

        # Visit every number using its index
        for i in range(len(nums)):

            # Calculate the number we need
            complement = target - nums[i]

            # Check whether the needed number exists
            if complement in seen:

                # Return both original indices
                return [seen[complement], i]

            # Store the current number and its index
            seen[nums[i]] = i

        # Return an empty list if no answer is found
        return []


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def twoSum(self, nums: list[int], target: int) -> list[int]:

Creates a function called twoSum.

self:
Refers to the current object of the class.

nums:
The list of numbers given to our function.

list[int]:
Means nums is expected to contain integers.

target:
The number that the two selected numbers must add up to.

-> list[int]:
Means the function returns a list of integers.
In this problem, those integers are the two indices.


seen = {}

Creates an empty dictionary.

We use it to remember numbers we have already visited
and their original indices.

Example:

seen = {
    2: 0,
    7: 1
}

Here:
2 is stored at index 0.
7 is stored at index 1.


for i in range(len(nums)):

Visits every index in the list.

If nums = [2, 7, 11, 15]:

i = 0
i = 1
i = 2
i = 3


complement = target - nums[i]

Calculates the number we need to reach the target.

Example:

target = 9
nums[i] = 2

complement = 9 - 2

complement = 7

This means we need the number 7.


if complement in seen:

Checks whether the number we need is already stored
in our dictionary.

If the complement exists, we have found two numbers
whose sum equals the target.


return [seen[complement], i]

Returns the two original indices.

seen[complement]:
Gets the index of the previously visited number.

i:
Is the index of the current number.

Example:

seen = {2: 0}
i = 1
complement = 2

return [seen[2], 1]

Result:

[0, 1]


seen[nums[i]] = i

Stores the current number and its index.

Example:

nums[i] = 2
i = 0

seen[2] = 0

The dictionary now contains:

{2: 0}


return []

If the loop finishes without finding a solution,
the function returns an empty list.

Under the standard Two Sum problem conditions,
a valid answer is guaranteed, so this line is a
fallback.


6. WHY DO WE CHECK BEFORE STORING?
--------------------------------------------------------

This is very important.

We check:

if complement in seen:

BEFORE storing:

seen[nums[i]] = i

Why?

Because we cannot use the same element twice.

Example:

nums = [3]
target = 6

If we store 3 first, the dictionary contains:

{3: 0}

Then we calculate:

complement = 6 - 3
complement = 3

The dictionary already contains 3.

We might incorrectly use the same element twice.

By checking first, we avoid this problem.

We only find a match with a number from an earlier index.


7. DRY RUN: STEP-BY-STEP EXAMPLE
--------------------------------------------------------

Input:

nums = [2, 7, 11, 15]
target = 9

Initially:

seen = {}


STEP 1:

i = 0
nums[i] = 2

complement = 9 - 2
complement = 7

Is 7 in seen?

NO.

Store:

seen[2] = 0

Dictionary:

{2: 0}


STEP 2:

i = 1
nums[i] = 7

complement = 9 - 7
complement = 2

Is 2 in seen?

YES!

seen[2] = 0

Current index = 1

Return:

[0, 1]

We found the answer!


8. TIME COMPLEXITY
--------------------------------------------------------

O(n) AVERAGE TIME

n = number of elements in the list.

Why?

1. We visit each number at most once.
2. For each number, we calculate its complement.
3. Checking whether a key exists in a dictionary
   takes O(1) average time.
4. Storing a number and its index also takes O(1)
   average time.

Therefore:

n visits × O(1) average work = O(n)


Comparison:

Brute Force approach:

O(n²)

Hash Map approach:

O(n) average

The Hash Map approach is faster for large lists
because it avoids checking every possible pair.


9. SPACE COMPLEXITY
--------------------------------------------------------

O(n) WORST-CASE SPACE

Why?

We create an additional dictionary called seen.

In the worst case, we may visit almost every number
without finding a matching pair.

The dictionary can then store almost all n numbers
and their indices.

Therefore:

The extra space can grow with the input size.

Space Complexity = O(n)


10. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
nums = [15, 7, 2, 11]
target = 9

Expected:
[1, 2]

Reason:
7 + 2 = 9.


Test 2:

Input:
nums = [2, 7, 11, 15]
target = 9

Expected:
[0, 1]

Reason:
2 + 7 = 9.


Test 3:

Input:
nums = [3, 2, 4]
target = 6

Expected:
[1, 2]

Reason:
2 + 4 = 6.


Test 4:

Input:
nums = [3, 3]
target = 6

Expected:
[0, 1]

Reason:
3 + 3 = 6.


Test 5:

Input:
nums = [-1, -2, -3, -4, -5]
target = -8

Expected:
[2, 4]

Reason:
-3 + -5 = -8.


Test 6:

Input:
nums = [0, 4, 3, 0]
target = 0

Expected:
[0, 3]

Reason:
0 + 0 = 0.


Test 7:

Input:
nums = [1, 5, 3, 7]
target = 10

Expected:
[2, 3]

Reason:
3 + 7 = 10.


Test 8:

Input:
nums = [10, 1, 5, 3]
target = 6

Expected:
[1, 2]

Reason:
1 + 5 = 6.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a Hash Map is.
[ ] I understand dictionary keys and values.
[ ] I understand how the for loop works.
[ ] I understand how to calculate the complement.
[ ] I understand how "in" checks dictionary keys.
[ ] I understand how seen[complement] gets an index.
[ ] I understand seen[nums[i]] = i.
[ ] I understand why we check before storing.
[ ] I can explain return [seen[complement], i].
[ ] I can write this solution without looking.
[ ] I understand O(n) average time complexity.
[ ] I understand O(n) space complexity.

========================================================
"""

# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    ([15, 7, 2, 11], 9, [1, 2]),
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ([0, 4, 3, 0], 0, [0, 3]),
    ([1, 5, 3, 7], 10, [2, 3]),
    ([10, 1, 5, 3], 6, [1, 2])
]

print("TWO SUM - TEST RESULTS")
print("----------------------------------")

passed = 0

for nums, target, expected in test_cases:

    result = solution.twoSum(nums, target)

    print("Input:", nums)
    print("Target:", target)
    print("Expected:", expected)
    print("Actual:", result)

    # Compare indices without depending on their order
    if sorted(result) == sorted(expected):
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
