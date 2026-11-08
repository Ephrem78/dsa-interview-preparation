
"""
========================================================
PROBLEM: PRODUCT OF ARRAY EXCEPT SELF
TOPIC: ARRAYS AND HASHING
APPROACH: PREFIX AND POSTFIX PRODUCTS
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given an integer array called nums:

Return an array called answer.

Each answer[i] must contain the product of every
number in nums EXCEPT nums[i].

In simple words:

For every position, multiply all the other numbers
without multiplying the number at that position.

RULES:

1. Do not use division.
2. The algorithm must run in O(n) time.
3. Prefix and suffix products fit in a 32-bit integer.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
nums = [1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Explanation:

For index 0:
2 * 3 * 4 = 24

For index 1:
1 * 3 * 4 = 12

For index 2:
1 * 2 * 4 = 8

For index 3:
1 * 2 * 3 = 6


Example 2:

Input:
nums = [-1, 1, 0, -3, 3]

Output:
[0, 0, 9, 0, 0]

Explanation:

For index 0:
1 * 0 * -3 * 3 = 0

For index 1:
-1 * 0 * -3 * 3 = 0

For index 2:
-1 * 1 * -3 * 3 = 9

For index 3:
-1 * 1 * 0 * 3 = 0

For index 4:
-1 * 1 * 0 * -3 = 0


3. MY APPROACH: PREFIX AND POSTFIX PRODUCTS
--------------------------------------------------------

I use two running variables:

1. PREFIX

   Stores the product of all numbers BEFORE
   the current index.

2. POSTFIX

   Stores the product of all numbers AFTER
   the current index.

My steps:

1. Create a result list filled with 1.

2. Set prefix = 1.

3. Set postfix = 1.

4. First pass: move from LEFT to RIGHT.

5. Store the prefix product at each position.

6. Update prefix by multiplying it by the
   current number.

7. Second pass: move from RIGHT to LEFT.

8. Multiply each result position by the
   postfix product.

9. Update postfix by multiplying it by the
   current number.

10. Return the result list.


IMPORTANT:

The first loop calculates products on the LEFT.

The second loop calculates products on the RIGHT.

We multiply both products to get the final answer.


4. PYTHON SOLUTION
--------------------------------------------------------
"""


class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # Create a result list filled with 1
        result = [1] * len(nums)

        # Store products from the left and right
        prefix = 1
        postfix = 1

        # First pass: calculate prefix products
        for i in range(len(nums)):

            # Store the product of numbers before index i
            result[i] = prefix

            # Include the current number in the prefix
            prefix *= nums[i]

        # Second pass: calculate postfix products
        for i in range(len(nums) - 1, -1, -1):

            # Multiply the prefix by the postfix
            result[i] *= postfix

            # Include the current number in the postfix
            postfix *= nums[i]

        # Return the final answer
        return result


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def productExceptSelf(self, nums: list[int]) -> list[int]:

Creates a function that calculates the product
of all numbers except the current number.

self:
Refers to the current object of the class.

nums:
The input list of integers.

list[int]:
Means the function returns a list of integers.


result = [1] * len(nums)

Creates a result list with the same length as nums.

Every position starts with 1.

Example:

nums = [1, 2, 3, 4]

result = [1, 1, 1, 1]

Why 1?

Because 1 does not change multiplication.

Example:

1 * 5 = 5

We will update this list during both loops.


prefix = 1

Creates a variable called prefix.

It stores the product of all numbers
BEFORE the current index.

We start with 1 because there are no numbers
before the first position.

Example:

nums = [1, 2, 3, 4]

At index 0:
prefix = 1

At index 1:
prefix = 1

At index 2:
prefix = 2

At index 3:
prefix = 6


postfix = 1

Creates a variable called postfix.

It stores the product of all numbers
AFTER the current index.

We start with 1 because there are no numbers
after the last position.


FIRST LOOP: PREFIX PRODUCTS
--------------------------------------------------------

for i in range(len(nums)):

Visits every index from LEFT to RIGHT.

Example:

nums = [1, 2, 3, 4]

The indexes are:

0
1
2
3


result[i] = prefix

Stores the product of all numbers
BEFORE the current index.

Example:

At index 0:
result[0] = 1

At index 1:
result[1] = 1

At index 2:
result[2] = 2

At index 3:
result[3] = 6

After the first loop:

result = [1, 1, 2, 6]


prefix *= nums[i]

This is a shorter way of writing:

prefix = prefix * nums[i]

It updates the prefix by multiplying it
by the current number.

Example:

Start:
prefix = 1

Index 0:
prefix = 1 * 1 = 1

Index 1:
prefix = 1 * 2 = 2

Index 2:
prefix = 2 * 3 = 6

Index 3:
prefix = 6 * 4 = 24

IMPORTANT:

We store prefix BEFORE updating it.

Why?

Because we must exclude the current number
from its own answer.


SECOND LOOP: POSTFIX PRODUCTS
--------------------------------------------------------

for i in range(len(nums) - 1, -1, -1):

Visits every index from RIGHT to LEFT.

The range() function has three parts:

range(start, stop, step)

start:
The first index.

stop:
The loop stops BEFORE this number.

step:
How much the index changes each time.

Example:

nums = [1, 2, 3, 4]

range(3, -1, -1)

Produces:

3
2
1
0

The step is -1 because we move backwards.


result[i] *= postfix

This is a shorter way of writing:

result[i] = result[i] * postfix

It multiplies the prefix product already stored
in result[i] by the postfix product.

Example:

Before the second loop:

result = [1, 1, 2, 6]

At index 3:
result[3] = 6 * 1 = 6

At index 2:
result[2] = 2 * 4 = 8

At index 1:
result[1] = 1 * 12 = 12

At index 0:
result[0] = 1 * 24 = 24

Final result:

[24, 12, 8, 6]


postfix *= nums[i]

This is a shorter way of writing:

postfix = postfix * nums[i]

It updates the postfix product by multiplying
it by the current number.

We move from RIGHT to LEFT.

Example:

nums = [1, 2, 3, 4]

Start:
postfix = 1

Index 3:
postfix = 1 * 4 = 4

Index 2:
postfix = 4 * 3 = 12

Index 1:
postfix = 12 * 2 = 24

Index 0:
postfix = 24 * 1 = 24

IMPORTANT:

We multiply result[i] BEFORE updating postfix.

Why?

Because we must exclude the current number
from its own answer.


return result

Returns the final result list.

Example:

nums = [1, 2, 3, 4]

result = [24, 12, 8, 6]


6. COMPLETE DRY RUN
--------------------------------------------------------

Input:

nums = [1, 2, 3, 4]

STARTING VALUES:

result = [1, 1, 1, 1]
prefix = 1
postfix = 1


FIRST LOOP: LEFT TO RIGHT

Index 0:

result[0] = 1
prefix = 1 * 1 = 1

result = [1, 1, 1, 1]


Index 1:

result[1] = 1
prefix = 1 * 2 = 2

result = [1, 1, 1, 1]


Index 2:

result[2] = 2
prefix = 2 * 3 = 6

result = [1, 1, 2, 1]


Index 3:

result[3] = 6
prefix = 6 * 4 = 24

result = [1, 1, 2, 6]


SECOND LOOP: RIGHT TO LEFT

Index 3:

result[3] = 6 * 1 = 6
postfix = 1 * 4 = 4

result = [1, 1, 2, 6]


Index 2:

result[2] = 2 * 4 = 8
postfix = 4 * 3 = 12

result = [1, 1, 8, 6]


Index 1:

result[1] = 1 * 12 = 12
postfix = 12 * 2 = 24

result = [1, 12, 8, 6]


Index 0:

result[0] = 1 * 24 = 24
postfix = 24 * 1 = 24

result = [24, 12, 8, 6]


FINAL ANSWER:

[24, 12, 8, 6]


7. TIME COMPLEXITY
--------------------------------------------------------

O(n)

Where:

n = Number of elements in nums.

Why?

There are two loops.


1. FIRST LOOP

Visits every element once.

Time complexity = O(n)


2. SECOND LOOP

Also visits every element once.

Time complexity = O(n)


TOTAL TIME COMPLEXITY:

O(n) + O(n) = O(2n)

We remove the constant factor.

Therefore:

TIME COMPLEXITY = O(n)


8. SPACE COMPLEXITY
--------------------------------------------------------

O(1) AUXILIARY SPACE

Why?

We only use two extra variables:

prefix
postfix

These variables do not grow when the input list
becomes larger.

Therefore:

Auxiliary space = O(1)


OUTPUT SPACE:

The result list has the same length as nums.

If nums contains n elements:

Output space = O(n)


IMPORTANT:

Total space including the required output:

O(n)

Auxiliary space excluding the output:

O(1)


9. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
nums = [1, 2, 3, 4]

Expected:
[24, 12, 8, 6]

Reason:
Every position contains the product of the
other three numbers.


Test 2:

Input:
nums = [-1, 1, 0, -3, 3]

Expected:
[0, 0, 9, 0, 0]

Reason:
There is one zero.
Only the answer at the zero's position
can have a non-zero product.


Test 3:

Input:
nums = [1, 2]

Expected:
[2, 1]

Reason:
Each position contains the other number.


Test 4:

Input:
nums = [0, 0]

Expected:
[0, 0]

Reason:
Both positions have another zero.


Test 5:

Input:
nums = [2, 3, 4, 5]

Expected:
[60, 40, 30, 24]

Reason:
Each position contains the product
of the other three numbers.


Test 6:

Input:
nums = [-2, 3, 4]

Expected:
[12, -8, -6]

Reason:
Negative numbers affect the sign of the product.


Test 7:

Input:
nums = [1, 0, 3]

Expected:
[0, 3, 0]

Reason:
The middle position excludes zero.
The other positions still include zero.


Test 8:

Input:
nums = [5]

Expected:
[1]

Reason:
There are no other numbers to multiply.

The empty product is 1.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a prefix product means.
[ ] I understand what a postfix product means.
[ ] I understand why result starts with 1.
[ ] I understand why prefix starts with 1.
[ ] I understand why postfix starts with 1.
[ ] I understand how range() works.
[ ] I understand range(len(nums)).
[ ] I understand range(len(nums) - 1, -1, -1).
[ ] I understand why the first loop moves LEFT to RIGHT.
[ ] I understand why the second loop moves RIGHT to LEFT.
[ ] I understand why we store prefix before updating it.
[ ] I understand why we multiply by postfix before updating it.
[ ] I understand how the algorithm handles zero.
[ ] I can write this solution without looking.
[ ] I understand O(n) time complexity.
[ ] I understand O(1) auxiliary space complexity.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([1, 2], [2, 1]),
    ([0, 0], [0, 0]),
    ([2, 3, 4, 5], [60, 40, 30, 24]),
    ([-2, 3, 4], [12, -8, -6]),
    ([1, 0, 3], [0, 3, 0]),
    ([5], [1])
]

passed = 0

print("PRODUCT OF ARRAY EXCEPT SELF - TEST RESULTS")
print("--------------------------------------------")

for nums, expected in test_cases:

    result = solution.productExceptSelf(nums)

    print("Numbers:", nums)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("--------------------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
