
"""
========================================================
PROBLEM: 3SUM
TOPIC: ARRAYS AND HASHING
APPROACH: SORTING + TWO POINTERS
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given an integer array called nums:

Find all groups of THREE different elements
whose sum equals ZERO.

In simple words:

Find three numbers that add up to 0.

IMPORTANT RULES:

1. We must use three different positions.
2. The three numbers must add up to zero.
3. We cannot return duplicate triplets.
4. The order of the output does not matter.

Example:

nums = [-1, 0, 1, 2, -1, -4]

The valid triplets are:

[-1, -1, 2]
[-1, 0, 1]

Check:

-1 + -1 + 2 = 0

-1 + 0 + 1 = 0

Therefore:

Output = [[-1, -1, 2], [-1, 0, 1]]


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
nums = [-1, 0, 1, 2, -1, -4]

Output:
[[-1, -1, 2], [-1, 0, 1]]

Explanation:

The valid triplets are:

[-1, -1, 2]
-1 + -1 + 2 = 0

[-1, 0, 1]
-1 + 0 + 1 = 0

We return each distinct triplet only once.


Example 2:

Input:
nums = [0, 1, 1]

Output:
[]

Explanation:

There are not three numbers that add up to zero.

Therefore, return an empty list.


Example 3:

Input:
nums = [0, 0, 0]

Output:
[[0, 0, 0]]

Explanation:

0 + 0 + 0 = 0

There is one unique triplet.


3. MY APPROACH: SORTING + TWO POINTERS
--------------------------------------------------------

I use two main techniques.

1. SORTING

First, arrange the numbers from smallest to largest.

Example:

[-1, 0, 1, 2, -1, -4]

After sorting:

[-4, -1, -1, 0, 1, 2]

Sorting makes it easier to use two pointers.

2. TWO POINTERS

For every selected first number:

- LEFT starts immediately after the first number.
- RIGHT starts at the last number.

We calculate:

sum = first number + left number + right number

There are three possible situations:


CASE 1: SUM IS SMALLER THAN ZERO

If:

sum < 0

The sum is too small.

Move LEFT forward.

Why?

Because the array is sorted.

Moving left forward gives us a bigger number.

This can increase the sum.


CASE 2: SUM IS GREATER THAN ZERO

If:

sum > 0

The sum is too big.

Move RIGHT backward.

Why?

Because the array is sorted.

Moving right backward gives us a smaller number.

This can decrease the sum.


CASE 3: SUM EQUALS ZERO

If:

sum == 0

We found a valid triplet.

Add the three numbers to the result.

Then move both pointers toward the middle.

We also skip duplicate numbers.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # Sort the numbers from smallest to largest
        nums.sort()

        # Create an empty list to store valid triplets
        result = []

        # Choose the first number of each triplet
        for i in range(len(nums)):

            # If the first number is positive, stop
            if nums[i] > 0:
                break

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Find the other two numbers
            self.twoSum2(nums, i, result)

        # Return all unique triplets
        return result


    def twoSum2(self, nums: list[int], i: int, result: list[list[int]]) -> None:

        # Start left immediately after the first number
        left = i + 1

        # Start right at the last number
        right = len(nums) - 1

        # Continue while the pointers have not met
        while left < right:

            # Calculate the sum of all three numbers
            total = nums[i] + nums[left] + nums[right]

            # If the sum is too small, move left forward
            if total < 0:
                left += 1

            # If the sum is too big, move right backward
            elif total > 0:
                right -= 1

            # If the sum equals zero, we found a triplet
            else:

                # Add the three numbers to the result
                result.append([nums[i], nums[left], nums[right]])

                # Move both pointers toward the middle
                left += 1
                right -= 1

                # Skip duplicate numbers on the left
                while left < right and nums[left] == nums[left - 1]:
                    left += 1


"""
5. COMPLETE ELS10 EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------


class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def threeSum(self, nums: list[int]) -> list[list[int]]:

Creates a function called threeSum.

self:
Refers to the current object of the class.

nums:
The input list of integers.

list[int]:
Means nums is a list containing integers.

-> list[list[int]]:

Means the function returns a list containing other lists
of integers.

Example:

[
    [-1, -1, 2],
    [-1, 0, 1]
]

This is a list containing two triplets.


nums.sort()

Sorts the numbers from smallest to largest.

Example:

Before:

nums = [-1, 0, 1, 2, -1, -4]

After:

nums = [-4, -1, -1, 0, 1, 2]

IMPORTANT:

sort() changes the original list.

It does not create a separate sorted list.

Why do we sort?

Because sorting helps us understand how moving
left and right changes the sum.


result = []

Creates an empty list.

We will store every valid triplet inside it.

Example:

result = [
    [-1, -1, 2],
    [-1, 0, 1]
]


for i in range(len(nums)):

Visits each index in nums.

Example:

nums = [-4, -1, -1, 0, 1, 2]

Positions:

Number: -4  -1  -1   0   1   2
Index:   0   1   2   3   4   5

The loop visits:

i = 0
i = 1
i = 2
i = 3
i = 4
i = 5

Each position can become the first number
of a possible triplet.


if nums[i] > 0:

Checks whether the selected first number
is greater than zero.

Example:

nums[i] = 2

2 > 0 is True.

Why do we stop?

Because the array is sorted.

If the first number is already positive,
all numbers after it are also positive.

Three positive numbers cannot add up to zero.

Therefore, we do not need to continue.


break

Stops the entire for loop immediately.

It does not just skip one number.

It ends the loop.


if i > 0 and nums[i] == nums[i - 1]:

Checks whether the current first number
is the same as the previous first number.

Let's break it down.

i > 0

Checks that we are not at the first position.

Why?

Because there is no previous position
before index 0.

nums[i]

Gets the current number.

nums[i - 1]

Gets the previous number.

Example:

nums = [-4, -1, -1, 0, 1, 2]

At i = 2:

nums[i] = -1
nums[i - 1] = -1

They are equal.

This means we already tried -1 as the first number.

We do not need to repeat the same search.


continue

Skips the current loop iteration.

In simple words:

Do not process this duplicate number.

Move to the next iteration of the for loop.

IMPORTANT:

continue skips only the current iteration.

It does not stop the entire loop.

This prevents duplicate triplets
starting with the same first number.


self.twoSum2(nums, i, result)

Calls another function named twoSum2.

We use this function to find the other two numbers.

It receives three things:

nums:
The sorted input list.

i:
The position of the first number.

result:
The list where we store valid triplets.

self:

Means we are calling a function belonging
to the same Solution object.


def twoSum2(self, nums, i, result) -> None:

Creates a helper function.

A helper function is a function that another
function uses to complete part of its work.

threeSum chooses the first number.

twoSum2 finds the other two numbers.

-> None means this helper does not return
a value to the caller.

Instead, it adds valid triplets directly
to the result list.


left = i + 1

Creates the left pointer.

It starts immediately after the first number.

Why?

Because we need three different positions.

We cannot use the same element twice.

Example:

i = 1

Then:

left = 1 + 1

left = 2

The left pointer starts at index 2.


right = len(nums) - 1

Creates the right pointer.

It starts at the last position of the list.

Example:

nums = [-4, -1, -1, 0, 1, 2]

len(nums) = 6

right = 6 - 1

right = 5

The right pointer starts at number 2.


while left < right:

Continues while the left pointer is smaller
than the right pointer.

Why?

Because we need two different positions.

When the pointers meet or cross,
there are no more pairs to check.


total = nums[i] + nums[left] + nums[right]

Adds the three selected numbers.

Example:

nums = [-4, -1, -1, 0, 1, 2]

i = 1
left = 2
right = 5

The numbers are:

nums[i] = -1
nums[left] = -1
nums[right] = 2

Therefore:

total = -1 + -1 + 2

total = 0


if total < 0:

Checks whether the sum is smaller than zero.

Example:

total = -5

-5 < 0 is True.

The sum is too small.


left += 1

Means:

left = left + 1

Move the left pointer one position forward.

Because the list is sorted, the next number
is equal or bigger.

This can increase the total sum.

Example:

Before:

left points to -1.

After:

left points to 0.


elif total > 0:

Checks whether the sum is greater than zero.

Example:

total = 4

4 > 0 is True.

The sum is too big.


right -= 1

Means:

right = right - 1

Move the right pointer one position backward.

Because the list is sorted, the previous number
is equal or smaller.

This can decrease the total sum.

Example:

Before:

right points to 2.

After:

right points to 1.


else:

Runs when the sum is neither smaller nor greater
than zero.

Therefore:

total == 0

We found a valid triplet.


result.append([nums[i], nums[left], nums[right]])

Adds the three numbers to the result list.

append() adds an item to the end of a list.

Example:

result = []

After:

result.append([-1, -1, 2])

The result becomes:

[[-1, -1, 2]]


left += 1

Moves the left pointer forward.

We already used its current number
in a valid triplet.

We move to another position to search
for another possible triplet.


right -= 1

Moves the right pointer backward.

We already used its current number
in the valid triplet.

We move toward the middle to search
for another possible triplet.


while left < right and nums[left] == nums[left - 1]:

This is the duplicate-skipping loop.

It checks two things:

1. left < right

The pointers have not met or crossed.

2. nums[left] == nums[left - 1]

The current left number is the same
as the previous left number.

If both conditions are True,
we have found a duplicate number.

We skip it.


left += 1

Moves past the duplicate number.

Why?

Because using the same left number again
could create the same triplet.

We want each triplet only once.


return result

Returns all the unique triplets.

Example:

[
    [-1, -1, 2],
    [-1, 0, 1]
]


6. WHY DO WE NEED TWO DIFFERENT DUPLICATE CHECKS?
--------------------------------------------------------

This is very important.

We have two duplicate checks.

FIRST CHECK:

if i > 0 and nums[i] == nums[i - 1]:
    continue

This prevents duplicate FIRST numbers.

Example:

nums = [-4, -1, -1, 0, 1, 2]

We already tried -1 at index 1.

We skip -1 at index 2 as another first number.


SECOND CHECK:

while left < right and nums[left] == nums[left - 1]:
    left += 1

This prevents duplicate SECOND numbers
after we find a valid triplet.

Example:

nums = [-2, 0, 0, 0, 2, 2]

We might find:

[-2, 0, 2]

We do not want to add the same triplet again.

Therefore, we skip repeated left values.


IMPORTANT:

The first duplicate check controls the for loop.

The second duplicate check controls the left pointer.

Both help prevent duplicate triplets.


7. STEP-BY-STEP EXECUTION
--------------------------------------------------------

Let's use:

nums = [-1, 0, 1, 2, -1, -4]

FIRST:

Sort the list.

nums = [-4, -1, -1, 0, 1, 2]


FIRST OUTER LOOP:

i = 0

nums[i] = -4

left = 1
right = 5

Numbers:

-4, -1, 2

Calculate:

-4 + -1 + 2 = -3

-3 < 0

The sum is too small.

Move left forward.


Next:

-4 + -1 + 2 = -3

Still too small.

Move left forward.


Next:

-4 + 0 + 2 = -2

Still too small.

Move left forward.


Next:

-4 + 1 + 2 = -1

Still too small.

Move left forward.

The pointers meet.

No triplet was found for -4.


SECOND OUTER LOOP:

i = 1

nums[i] = -1

left = 2
right = 5

Numbers:

-1, -1, 2

Calculate:

-1 + -1 + 2 = 0

We found a triplet!

Add:

[-1, -1, 2]

Move both pointers:

left = 3
right = 4


Next:

Numbers:

-1, 0, 1

Calculate:

-1 + 0 + 1 = 0

We found another triplet!

Add:

[-1, 0, 1]

Move both pointers.

Now left = 4 and right = 3.

The loop stops.


NEXT OUTER LOOP:

i = 2

nums[i] = -1

Previous number:

nums[i - 1] = -1

They are equal.

The duplicate check runs.

continue skips this number.

We do not repeat the same search.


FINAL RESULT:

[
    [-1, -1, 2],
    [-1, 0, 1]
]


8. WHY DO WE STOP WHEN nums[i] > 0?
--------------------------------------------------------

Remember:

The list is sorted.

Example:

[-4, -1, 0, 1, 2, 5]

Imagine the first selected number is 1.

The next two numbers must be greater than
or equal to 1.

Therefore:

1 + 2 + 5 = 8

Three positive numbers cannot add up to zero.

So when nums[i] > 0, we can stop.

We do not need to check the remaining numbers.


9. TIME COMPLEXITY
--------------------------------------------------------

O(N²)

Where:

N = Number of elements in nums.

There are two main operations.


1. SORTING

nums.sort()

Sorting takes:

O(N log N)


2. FINDING TRIPLETS

The outer for loop can visit N elements.

For each selected first number,
the two pointers move through the remaining list.

The left pointer only moves forward.

The right pointer only moves backward.

Together, their movements take O(N)
for each outer-loop iteration.

Therefore:

N × O(N) = O(N²)


TOTAL TIME COMPLEXITY:

O(N log N) + O(N²)

The larger term is O(N²).

Therefore:

TIME COMPLEXITY = O(N²)


10. SPACE COMPLEXITY
--------------------------------------------------------

There are two things to consider.


1. ALGORITHM AUXILIARY SPACE

We use:

i
left
right
total

Only a constant number of variables.

Therefore:

O(1) auxiliary space for the pointer algorithm.


2. SORTING SPACE

Python's list.sort() sorts the original list.

It does not create a second full list.

However, Python's sorting algorithm can use
temporary memory, up to O(N) in the worst case.


3. OUTPUT SPACE

The result list stores all valid triplets.

The amount of output memory depends on
how many triplets we find.

In the worst case, it can be O(N²).


IMPORTANT:

For the two-pointer algorithm itself,
auxiliary space is O(1).

For the complete Python implementation,
the sorting operation can use O(N) temporary space.

The output list is separate from auxiliary space.


11. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
nums = [-1, 0, 1, 2, -1, -4]

Expected:
[[-1, -1, 2], [-1, 0, 1]]


Test 2:

Input:
nums = [0, 1, 1]

Expected:
[]


Test 3:

Input:
nums = [0, 0, 0]

Expected:
[[0, 0, 0]]


Test 4:

Input:
nums = []

Expected:
[]


Test 5:

Input:
nums = [-2, 0, 1, 1, 2]

Expected:
[[-2, 0, 2], [-2, 1, 1]]


Test 6:

Input:
nums = [-1, -1, -1, 2, 2]

Expected:
[[-1, -1, 2]]


Test 7:

Input:
nums = [-4, -2, -1, 0, 1, 2, 3]

Expected:
[[-4, 1, 3], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]


Test 8:

Input:
nums = [1, 2, 3, 4]

Expected:
[]


Test 9:

Input:
nums = [-2, -2, 0, 0, 2, 2]

Expected:
[[-2, 0, 2]]


Test 10:

Input:
nums = [-3, 0, 1, 2, -1, 1, -2]

Expected:
[[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a triplet means.
[ ] I understand why the three positions must be different.
[ ] I understand why we sort the array.
[ ] I understand what nums.sort() does.
[ ] I understand what the outer for loop does.
[ ] I understand why i selects the first number.
[ ] I understand why left starts at i + 1.
[ ] I understand why right starts at len(nums) - 1.
[ ] I understand how the three numbers are added.
[ ] I understand why left moves when sum < 0.
[ ] I understand why right moves when sum > 0.
[ ] I understand what happens when sum == 0.
[ ] I understand what append() does.
[ ] I understand why we move both pointers after a match.
[ ] I understand why we skip duplicate first numbers.
[ ] I understand why we skip duplicate left numbers.
[ ] I understand why we stop when nums[i] > 0.
[ ] I understand why the time complexity is O(N²).
[ ] I understand Python sorting space complexity.
[ ] I can write this solution without looking.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    (
        [-1, 0, 1, 2, -1, -4],
        [[-1, -1, 2], [-1, 0, 1]]
    ),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
    ([], []),
    (
        [-2, 0, 1, 1, 2],
        [[-2, 0, 2], [-2, 1, 1]]
    ),
    (
        [-1, -1, -1, 2, 2],
        [[-1, -1, 2]]
    ),
    (
        [-4, -2, -1, 0, 1, 2, 3],
        [[-4, 1, 3], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    ),
    ([1, 2, 3, 4], []),
    (
        [-2, -2, 0, 0, 2, 2],
        [[-2, 0, 2]]
    ),
    (
        [-3, 0, 1, 2, -1, 1, -2],
        [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    )
]

passed = 0

print("3SUM - TEST RESULTS")
print("----------------------------------")

for nums, expected in test_cases:

    result = solution.threeSum(nums)

    # Sort each triplet and the complete result.
    # This makes the comparison independent of output order.
    actual_sorted = sorted(tuple(triplet) for triplet in result)
    expected_sorted = sorted(tuple(triplet) for triplet in expected)

    print("Input:", nums)
    print("Expected:", expected)
    print("Actual:", result)

    if actual_sorted == expected_sorted:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
