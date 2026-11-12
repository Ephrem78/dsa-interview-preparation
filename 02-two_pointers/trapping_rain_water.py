
"""
========================================================
PROBLEM: TRAPPING RAIN WATER
TOPIC: TWO POINTERS
APPROACH: TWO POINTERS + LEFT MAX + RIGHT MAX
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given an integer array called height:

Each number represents the height of a vertical bar.

Each bar has a width of 1.

After raining, water can collect between the bars.

Calculate how much water can be trapped.

In simple words:

Find the empty spaces between the bars
where rainwater can collect.

Return the total amount of trapped water.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

Output:
6

Explanation:

The bars create empty spaces where water can collect.

The total trapped water is 6 units.


Example 2:

Input:
height = [4, 2, 0, 3, 2, 5]

Output:
9

Explanation:

The total amount of water trapped
between the bars is 9 units.


Example 3:

Input:
height = [3, 0, 2, 0, 4]

Output:
7

Explanation:

The empty spaces between the bars
can hold 7 units of water.


3. MY APPROACH: TWO POINTERS
--------------------------------------------------------

I use two pointers and two variables
to remember the highest bars.

My important variables:

1. LEFT POINTER

   Starts at the beginning of the list.

2. RIGHT POINTER

   Starts at the end of the list.

3. LEFT MAX

   Stores the highest bar found from the left.

4. RIGHT MAX

   Stores the highest bar found from the right.

5. TOTAL

   Stores the total amount of trapped water.


My steps:

1. Create a left pointer at index 0.

2. Create a right pointer at the last index.

3. Create total = 0.

4. Store the first bar in leftMax.

5. Store the last bar in rightMax.

6. Continue while left is smaller than right.

7. Compare the current left and right bar heights.

8. If the left bar is smaller:

   - Update leftMax.
   - Calculate water using leftMax.
   - Add the water to total.
   - Move the left pointer one position right.

9. Otherwise:

   - Update rightMax.
   - Calculate water using rightMax.
   - Add the water to total.
   - Move the right pointer one position left.

10. When the pointers meet, return total.


IMPORTANT:

We process the side with the smaller
current bar height.

Why?

Because the smaller side limits the amount
of water that can be trapped at that position.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def trap(self, height: list[int]) -> int:

        # Handle an empty input list
        if not height:
            return 0

        # Create the left and right pointers
        left = 0
        right = len(height) - 1

        # Store the total trapped water
        total = 0

        # Store the highest bars found on each side
        leftMax = height[0]
        rightMax = height[right]

        # Continue while the pointers have not met
        while left < right:

            # Process the left side if its bar is smaller
            if height[left] < height[right]:

                # Update the highest bar on the left
                leftMax = max(leftMax, height[left])

                # Calculate and add the trapped water
                if leftMax - height[left] > 0:
                    total = total + leftMax - height[left]

                # Move the left pointer to the right
                left += 1

            else:

                # Update the highest bar on the right
                rightMax = max(rightMax, height[right])

                # Calculate and add the trapped water
                if rightMax - height[right] > 0:
                    total = total + rightMax - height[right]

                # Move the right pointer to the left
                right -= 1

        # Return the total trapped water
        return total


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def trap(self, height: list[int]) -> int:

Creates a method called trap.

self:
Refers to the current object of the class.

height:
The input list containing the heights of the bars.

list[int]:
Means the input is a list of integers.

-> int:
Means the method returns an integer.


if not height:

Checks whether the input list is empty.

An empty list means there are no bars.

Therefore, no water can be trapped.


return 0

Returns zero if the input list is empty.

This also prevents errors when trying to access
height[0] or height[right].


left = 0

Creates the left pointer.

It starts at index 0.

Index 0 is the first element in the list.


right = len(height) - 1

Creates the right pointer.

len(height) gives the total number of elements.

Python indexes start from zero.

Example:

height = [0, 1, 0, 2, 1]

len(height) = 5

right = 5 - 1

right = 4

The last element is at index 4.


total = 0

Creates a variable to store the total
amount of trapped water.

At the beginning, no water has been collected.


leftMax = height[0]

Stores the height of the first bar.

This is our starting maximum height from the left.

Example:

height[0] = 0

Therefore:

leftMax = 0


rightMax = height[right]

Stores the height of the last bar.

This is our starting maximum height from the right.

Example:

right = 4

height[4] = 1

Therefore:

rightMax = 1


while left < right:

Starts a loop.

The loop continues while the left pointer
is smaller than the right pointer.

Why?

Because we need to process the positions
between the two pointers.

When both pointers meet, the loop stops.


if height[left] < height[right]:

Compares the current height of the left bar
with the current height of the right bar.

Example:

height[left] = 0
height[right] = 1

Python checks:

0 < 1

This is True.

Therefore, we process the left side.

IMPORTANT:

We process the side with the smaller bar
because that side limits the water level
at the current position.


leftMax = max(leftMax, height[left])

max() returns the larger of two values.

It compares:

1. The highest bar we previously found on the left.
2. The current left bar.

Example:

leftMax = 1
height[left] = 2

Python checks:

max(1, 2)

Result:

leftMax = 2

This keeps track of the highest bar
we have found from the left.


if leftMax - height[left] > 0:

Checks whether water can be trapped
at the current left position.

The formula is:

Water = leftMax - current bar height

Example:

leftMax = 3
height[left] = 1

Calculate:

3 - 1 = 2

This position can hold 2 units of water.

But if:

leftMax = 3
height[left] = 3

Calculate:

3 - 3 = 0

No water is trapped at this position.

That is why we check whether the result
is greater than zero.


total = total + leftMax - height[left]

Adds the trapped water to the total.

Example:

total = 2
leftMax = 3
height[left] = 1

Calculate:

total = 2 + 3 - 1

New total:

total = 4

We have collected 4 units of water so far.


left += 1

Moves the left pointer one position
to the right.

It is the same as:

left = left + 1

We have finished processing the current
left position.

Now we move to the next position.


else:

Runs when the left bar is not smaller
than the right bar.

This means:

height[left] >= height[right]

Now we process the right side.


rightMax = max(rightMax, height[right])

Compares:

1. The highest bar found from the right.
2. The current right bar.

Example:

rightMax = 1
height[right] = 3

Python checks:

max(1, 3)

Result:

rightMax = 3

This keeps track of the highest bar
we have found from the right.


if rightMax - height[right] > 0:

Checks whether water can be trapped
at the current right position.

The formula is:

Water = rightMax - current bar height

Example:

rightMax = 4
height[right] = 1

Calculate:

4 - 1 = 3

This position can hold 3 units of water.


total = total + rightMax - height[right]

Adds the trapped water on the right
to the total.

Example:

total = 4
rightMax = 4
height[right] = 1

Calculate:

total = 4 + 4 - 1

New total:

total = 7


right -= 1

Moves the right pointer one position
to the left.

It is the same as:

right = right - 1

We have finished processing the current
right position.


return total

Returns the total amount of trapped water.

When the two pointers meet,
the while loop stops.

For Example 1:

The answer is:

6

Therefore:

return 6


IMPORTANT:

The left pointer only moves to the right.

The right pointer only moves to the left.

Every position is processed once.

We do not need another list to store
the maximum heights.


6. HOW THE ALGORITHM WORKS
--------------------------------------------------------

Example:

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

Starting values:

left = 0
right = 11

leftMax = 0
rightMax = 1

total = 0


MAIN RULE:

If the left bar is smaller:

1. Update leftMax.
2. Calculate leftMax - height[left].
3. Add the water to total.
4. Move left forward.


If the right bar is smaller or equal:

1. Update rightMax.
2. Calculate rightMax - height[right].
3. Add the water to total.
4. Move right backward.


The algorithm continues until:

left == right


Final answer:

total = 6


7. TIME COMPLEXITY
--------------------------------------------------------

O(N)

Where:

N = Number of elements in height.

Why?

There is one main while loop:

while left < right:

Inside the loop, one pointer moves
one position toward the other pointer.

The left pointer never moves backward.

The right pointer never moves forward.

Together, the pointers process the list
in one pass.

Example:

If the input contains 12 elements,
the algorithm performs at most approximately
12 processing steps.

Therefore:

TIME COMPLEXITY = O(N)


8. SPACE COMPLEXITY
--------------------------------------------------------

O(1)

Why?

We only use a fixed number of variables:

left
right
total
leftMax
rightMax

These variables do not grow when
the input list becomes larger.

We do not create:

- Another list.
- A dictionary.
- A heap.
- An additional array.

Therefore:

SPACE COMPLEXITY = O(1)

IMPORTANT:

O(1) means constant extra space.

Even if the input contains 1,000,000 elements,
the algorithm still uses the same fixed number
of extra variables.


9. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

Expected:
6

Reason:
The bars create spaces that hold 6 units of water.


Test 2:

Input:
height = [4, 2, 0, 3, 2, 5]

Expected:
9

Reason:
The total trapped water is 9 units.


Test 3:

Input:
height = [3, 0, 2, 0, 4]

Expected:
7

Reason:
The empty spaces hold 7 units of water.


Test 4:

Input:
height = [3, 2, 1, 0]

Expected:
0

Reason:
The bars decrease from left to right.
There is no right boundary to trap water.


Test 5:

Input:
height = [0, 1, 2, 3]

Expected:
0

Reason:
The bars increase from left to right.
There is no left boundary to trap water.


Test 6:

Input:
height = [3, 3, 3, 3]

Expected:
0

Reason:
All bars have the same height.
There are no empty spaces between them.


Test 7:

Input:
height = [5]

Expected:
0

Reason:
One bar cannot trap water.


Test 8:

Input:
height = [2, 0, 2]

Expected:
2

Reason:
The middle position can hold 2 units of water.


Test 9:

Input:
height = [4, 2, 3]

Expected:
1

Reason:
The middle position can hold 1 unit of water.


Test 10:

Input:
height = [5, 4, 1, 2]

Expected:
1

Reason:
The last position has a boundary of height 2.
One unit of water is trapped at the third position.


Test 11:

Input:
height = []

Expected:
0

Reason:
There are no bars.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what the elevation map represents.
[ ] I understand what trapped rainwater means.
[ ] I understand how Two Pointers work.
[ ] I understand why left starts at index 0.
[ ] I understand why right starts at len(height) - 1.
[ ] I understand what leftMax stores.
[ ] I understand what rightMax stores.
[ ] I understand how max() works.
[ ] I understand why we compare height[left] and height[right].
[ ] I understand why we process the smaller side.
[ ] I understand the water calculation formula.
[ ] I understand how total stores the water.
[ ] I understand why left moves forward.
[ ] I understand why right moves backward.
[ ] I understand why the loop stops when the pointers meet.
[ ] I can write this solution without looking.
[ ] I understand O(N) time complexity.
[ ] I understand O(1) space complexity.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([3, 0, 2, 0, 4], 7),
    ([3, 2, 1, 0], 0),
    ([0, 1, 2, 3], 0),
    ([3, 3, 3, 3], 0),
    ([5], 0),
    ([2, 0, 2], 2),
    ([4, 2, 3], 1),
    ([5, 4, 1, 2], 1),
    ([], 0)
]

passed = 0

print("TRAPPING RAIN WATER - TEST RESULTS")
print("----------------------------------")

for height, expected in test_cases:

    result = solution.trap(height)

    print("Height:", height)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
