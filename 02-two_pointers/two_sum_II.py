
"""
========================================================
PROBLEM: TWO SUM II - INPUT ARRAY IS SORTED
TOPIC: TWO POINTERS
APPROACH: TWO POINTERS (LEFT AND RIGHT)
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given a sorted array of integers called numbers
and an integer called target:

Find two different numbers whose sum equals target.

Return their positions as a list of two integers.

IMPORTANT RULES:

1. The array is already sorted in non-decreasing order.
2. We cannot use the same element twice.
3. There is exactly one valid solution.
4. We must return 1-based indices, not 0-based indices.
5. We must use O(1) extra space.

What does 1-based index mean?

Python normally starts counting positions from 0.

Example:

numbers = [2, 7, 11, 15]

Python positions:

Number:  2   7   11   15
Index:   0   1    2    3

But this problem wants:

Index:   1   2    3    4

Therefore, we add 1 to both Python indices.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
numbers = [2, 7, 11, 15]
target = 9

Output:
[1, 2]

Explanation:

2 + 7 = 9

Python indices:
0 and 1

Required 1-based indices:
1 and 2

Therefore:
Output = [1, 2]


Example 2:

Input:
numbers = [2, 3, 4]
target = 6

Output:
[1, 3]

Explanation:

2 + 4 = 6

Python indices:
0 and 2

Required 1-based indices:
1 and 3

Therefore:
Output = [1, 3]


Example 3:

Input:
numbers = [-1, 0]
target = -1

Output:
[1, 2]

Explanation:

-1 + 0 = -1

Therefore:
Output = [1, 2]


3. MY APPROACH: TWO POINTERS
--------------------------------------------------------

I use two pointers:

1. LEFT POINTER
   Starts at the first element.

2. RIGHT POINTER
   Starts at the last element.

My steps:

1. Set left = 0.
2. Set right = len(numbers) - 1.
3. Add the numbers at both pointer positions.
4. Compare their sum with the target.

There are three possible situations:

CASE 1: SUM IS GREATER THAN TARGET

If:

numbers[left] + numbers[right] > target

The sum is too big.

Because the array is sorted, move the right pointer
one position to the left.

This gives us a smaller number.

CASE 2: SUM IS SMALLER THAN TARGET

If:

numbers[left] + numbers[right] < target

The sum is too small.

Because the array is sorted, move the left pointer
one position to the right.

This gives us a bigger number.

CASE 3: SUM EQUALS TARGET

If:

numbers[left] + numbers[right] == target

We found the answer.

Return:

[left + 1, right + 1]

We add 1 because the problem requires
1-based indices.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        # Start the left pointer at the first element
        left = 0

        # Start the right pointer at the last element
        right = len(numbers) - 1

        # Continue while the pointers have not met
        while left < right:

            # Calculate the sum of the two numbers
            total = numbers[left] + numbers[right]

            # If the sum is too big, move right backward
            if total > target:
                right -= 1

            # If the sum is too small, move left forward
            elif total < target:
                left += 1

            # If the sum equals the target, return the indices
            else:
                return [left + 1, right + 1]

        # The problem guarantees one solution
        return []


"""
5. COMPLETE ELS10 EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------


class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def twoSum(self, numbers: list[int], target: int) -> list[int]:

Creates a function called twoSum.

self:
Refers to the current object of the class.

numbers:
The input list of integers.

list[int]:
Means numbers is a list containing integers.

target:
The number we want the two elements to add up to.

int:
Means target is an integer.

-> list[int]:

Means the function returns a list of integers.

Example:

[1, 2]


left = 0

Creates the left pointer.

The left pointer starts at position 0.

Example:

numbers = [2, 7, 11, 15]

Positions:

Number:  2   7   11   15
Index:   0   1    2    3

Therefore:

left = 0

The left pointer starts at number 2.


right = len(numbers) - 1

Creates the right pointer.

len(numbers) counts how many elements are in the list.

Example:

numbers = [2, 7, 11, 15]

len(numbers) = 4

But the last Python index is 3.

Why?

Python starts counting from 0.

Therefore:

right = 4 - 1

right = 3

The right pointer starts at number 15.


while left < right:

This loop continues while left is smaller than right.

In simple words:

Continue checking while the pointers
have not met or crossed.

Why do we need this condition?

Because we cannot use the same element twice.

If both pointers meet, they point to the same element.

We must stop before that happens.


total = numbers[left] + numbers[right]

Gets the two numbers and adds them together.

Example:

numbers = [2, 7, 11, 15]

left = 0
right = 3

numbers[left] = 2
numbers[right] = 15

Therefore:

total = 2 + 15

total = 17

The variable total stores the result.


if total > target:

Checks whether the sum is greater than the target.

Example:

total = 17
target = 9

17 > 9 is True.

This means the sum is too big.

We need a smaller sum.


right -= 1

Means:

right = right - 1

Move the right pointer one position backward.

Example:

right = 3

After:

right -= 1

right = 2

Before:

numbers[right] = 15

After:

numbers[right] = 11

We moved from 15 to 11.

Why?

Because the array is sorted.

Moving right backward gives us a smaller number.

This can make the total smaller.


elif total < target:

elif means "otherwise, if".

This checks another condition if the first condition
was not True.

Example:

total = 6
target = 9

6 < 9 is True.

The sum is too small.

We need a bigger sum.


left += 1

Means:

left = left + 1

Move the left pointer one position forward.

Example:

left = 0

After:

left += 1

left = 1

Before:

numbers[left] = 2

After:

numbers[left] = 7

We moved from 2 to 7.

Why?

Because the array is sorted.

Moving left forward gives us a bigger number.

This can make the total bigger.


else:

The else block runs when neither condition above
is True.

That means:

total is not greater than target.
total is not smaller than target.

Therefore:

total == target

The two numbers add up to the target.


return [left + 1, right + 1]

Returns the positions of the two numbers.

IMPORTANT:

Python uses 0-based indices.

But this problem requires 1-based indices.

Therefore, we add 1 to each pointer.

Example:

left = 0
right = 1

Return:

[0 + 1, 1 + 1]

Result:

[1, 2]


return []

If the loop finishes without finding a solution,
return an empty list.

The problem guarantees exactly one solution.

Therefore, this line should not be reached
for valid problem inputs.

We use [] as a safe Python return value.


6. STEP-BY-STEP EXECUTION
--------------------------------------------------------

Let's use:

numbers = [2, 7, 11, 15]
target = 9

INITIAL POSITIONS:

Number:  2    7    11    15
Index:   0    1     2     3
         L                 R

left = 0
right = 3


FIRST LOOP:

numbers[left] = 2
numbers[right] = 15

total = 2 + 15

total = 17

Compare:

17 > 9

The sum is too big.

Move right backward:

right = 2


SECOND LOOP:

Number:  2    7    11    15
Index:   0    1     2     3
         L          R

numbers[left] = 2
numbers[right] = 11

total = 2 + 11

total = 13

Compare:

13 > 9

The sum is still too big.

Move right backward:

right = 1


THIRD LOOP:

Number:  2    7    11    15
Index:   0    1     2     3
         L    R

numbers[left] = 2
numbers[right] = 7

total = 2 + 7

total = 9

Compare:

9 == 9

We found the answer!


RETURN:

left = 0
right = 1

Return:

[left + 1, right + 1]

[0 + 1, 1 + 1]

FINAL OUTPUT:

[1, 2]


7. WHY DOES THE TWO POINTER APPROACH WORK?
--------------------------------------------------------

This is the most important idea.

The array is sorted.

Example:

numbers = [2, 7, 11, 15]

The numbers increase from left to right.

When the sum is too big:

numbers[left] + numbers[right] > target

We move right to the left.

Why?

Because the numbers become smaller.

When the sum is too small:

numbers[left] + numbers[right] < target

We move left to the right.

Why?

Because the numbers become bigger.

We do not need to check every possible pair.

The sorted order helps us eliminate possibilities
without using extra memory.

IMPORTANT:

This approach works because the array is sorted.

For an unsorted array, this pointer movement
does not guarantee the correct answer.


8. TIME COMPLEXITY
--------------------------------------------------------

O(N)

Where:

N = Number of elements in numbers.

WHY?

The left pointer only moves forward.

The right pointer only moves backward.

Each pointer moves at most N positions.

Neither pointer moves backward and forward
repeatedly through the same elements.

Therefore, the total number of pointer movements
is proportional to N.

TIME COMPLEXITY = O(N)


9. SPACE COMPLEXITY
--------------------------------------------------------

O(1)

WHY?

We only create a few variables:

left
right
total

We do not create:

- Another list.
- A Hash Map.
- A Hash Set.
- A Heap.

The amount of extra memory stays constant,
even when the input array becomes larger.

Therefore:

SPACE COMPLEXITY = O(1)

IMPORTANT:

The returned list contains two indices.

That is the required output.

The algorithm uses O(1) auxiliary space
excluding the output list.

This satisfies the problem's constant extra space rule.


10. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
numbers = [2, 7, 11, 15]
target = 9

Expected:
[1, 2]


Test 2:

Input:
numbers = [2, 3, 4]
target = 6

Expected:
[1, 3]


Test 3:

Input:
numbers = [-1, 0]
target = -1

Expected:
[1, 2]


Test 4:

Input:
numbers = [1, 2, 3, 4, 5]
target = 6

Expected:
[1, 5]


Test 5:

Input:
numbers = [1, 3, 4, 5, 7, 10, 11]
target = 9

Expected:
[3, 4]


Test 6:

Input:
numbers = [1, 2, 3, 4, 4, 9, 56, 90]
target = 8

Expected:
[4, 5]


Test 7:

Input:
numbers = [-5, -3, 0, 2, 4, 8]
target = 5

Expected:
[2, 6]


Test 8:

Input:
numbers = [2, 2, 11, 15]
target = 4

Expected:
[1, 2]


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a sorted array means.
[ ] I understand what Two Pointers means.
[ ] I understand why left starts at 0.
[ ] I understand why right starts at len(numbers) - 1.
[ ] I understand what while left < right means.
[ ] I understand how total calculates the sum.
[ ] I understand why we move right when the sum is too big.
[ ] I understand why we move left when the sum is too small.
[ ] I understand how if, elif, and else work.
[ ] I understand why we return left + 1 and right + 1.
[ ] I understand why the array must be sorted.
[ ] I can write this solution without looking.
[ ] I understand O(N) time complexity.
[ ] I understand O(1) auxiliary space complexity.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),
    ([1, 2, 3, 4, 5], 6, [1, 5]),
    ([1, 3, 4, 5, 7, 10, 11], 9, [3, 4]),
    ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
    ([-5, -3, 0, 2, 4, 8], 5, [2, 6]),
    ([2, 2, 11, 15], 4, [1, 2])
]

passed = 0

print("TWO SUM II - TEST RESULTS")
print("----------------------------------")

for numbers, target, expected in test_cases:

    result = solution.twoSum(numbers, target)

    print("Numbers:", numbers)
    print("Target:", target)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
