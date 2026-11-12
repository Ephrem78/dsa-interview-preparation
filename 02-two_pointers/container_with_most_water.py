
"""
========================================================
PROBLEM: CONTAINER WITH MOST WATER
TOPIC: TWO POINTERS
APPROACH: TWO POINTERS
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

You are given a list of integers called height.

Each number represents the height of a vertical line.

The position of each number represents where its
vertical line is located.

You must choose two lines.

Together with the x-axis, these two lines form
a container.

Your task is to find the container that can hold
the maximum amount of water.

In simple words:

Find two lines that can hold the most water
between them.

IMPORTANT:

The container cannot be tilted.

The water level is limited by the shorter line.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Output:
49

Explanation:

The best container uses:

Left line = 8
Right line = 7

Width = 8 - 1 = 7

Height = min(8, 7) = 7

Area = 7 * 7 = 49

Therefore:
Maximum area = 49


Example 2:

Input:
height = [1, 1]

Output:
1

Explanation:

Left line = 1
Right line = 1

Width = 1

Height = 1

Area = 1 * 1 = 1


Example 3:

Input:
height = [4, 3, 2, 1, 4]

Output:
16

Explanation:

Left line = 4
Right line = 4

Width = 4

Height = 4

Area = 4 * 4 = 16


3. MY APPROACH: TWO POINTERS
--------------------------------------------------------

I use two pointers:

1. LEFT POINTER

   Starts at the beginning of the list.

2. RIGHT POINTER

   Starts at the end of the list.

My steps:

1. Create a variable called max_area and set it to 0.

2. Create left and set it to 0.

3. Create right and set it to the last index.

4. Calculate the height of the container.

   We use the shorter line because water cannot
   rise above the shorter line.

5. Calculate the width.

   Width = right - left.

6. Calculate the area.

   Area = height * width.

7. Update max_area if the new area is larger.

8. Compare the two lines.

   If the left line is shorter, move left forward.

   Otherwise, move right backward.

9. Repeat until left and right meet.

10. Return max_area.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def maxArea(self, height: list[int]) -> int:

        # Store the maximum area found so far
        max_area = 0

        # Start the left pointer at the first index
        left = 0

        # Start the right pointer at the last index
        right = len(height) - 1

        # Continue while the pointers have not met
        while left < right:

            # Find the shorter line
            width_height = min(height[left], height[right])

            # Calculate the distance between the two lines
            width = right - left

            # Calculate the current container area
            area = width_height * width

            # Update the maximum area if needed
            max_area = max(max_area, area)

            # Move the pointer at the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # Return the largest area found
        return max_area


"""
5. COMPLETE ELS10 LINE-BY-LINE EXPLANATION
--------------------------------------------------------


class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.

We put our solution method inside this class.


def maxArea(self, height: list[int]) -> int:

Creates a method called maxArea.

self:
Refers to the current object of the class.

height:
The input list containing the heights of the lines.

list[int]:
Means height is a list of integers.

-> int:
Means the method returns an integer.

Example:

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


max_area = 0

Creates a variable called max_area.

It stores the largest container area found so far.

We start at 0 because we have not calculated
any container yet.

Example:

max_area = 0


left = 0

Creates the left pointer.

It starts at index 0.

Python lists start counting indexes from 0.

Example:

height = [1, 8, 6, 2, 5]

Indexes:

          0  1  2  3  4
height = [1, 8, 6, 2, 5]

Therefore:

left = 0

height[left] = 1


right = len(height) - 1

Creates the right pointer.

len(height) tells us how many elements
are inside the list.

Example:

height = [1, 8, 6, 2, 5]

len(height) = 5

The last index is:

5 - 1 = 4

Therefore:

right = 4

height[right] = 5

IMPORTANT:

We subtract 1 because Python indexes
start from 0.


while left < right:

Creates a loop.

The loop continues while left is smaller than right.

Why?

Because we need two different lines to create
a container.

When both pointers meet, there is no width left.

Example:

left = 0
right = 4

0 < 4

TRUE.

The loop continues.


width_height = min(height[left], height[right])

Finds the shorter line.

min() returns the smaller value.

Why do we need the shorter line?

Because water cannot rise above the shorter line.

Example:

height[left] = 8
height[right] = 7

min(8, 7) = 7

Therefore:

width_height = 7

The container can only hold water up to height 7.

IMPORTANT:

The taller line does not decide the water height.

The shorter line decides the water height.


width = right - left

Calculates the distance between the two lines.

This distance is the container width.

Example:

left = 1
right = 8

width = 8 - 1

width = 7

IMPORTANT:

We subtract the indexes, not the line heights.

The indexes tell us the horizontal distance.


area = width_height * width

Calculates how much water the container can hold.

Formula:

Area = Container Height * Container Width

Example:

width_height = 7
width = 7

area = 7 * 7

area = 49


max_area = max(max_area, area)

Compares the current area with the largest
area we have already found.

max() returns the larger value.

Example 1:

max_area = 20
area = 49

max(20, 49) = 49

Therefore:

max_area = 49


Example 2:

max_area = 49
area = 30

max(49, 30) = 49

The maximum area stays 49.

IMPORTANT:

We never want to lose the best answer
we have already found.


if height[left] < height[right]:

Compares the heights of the two lines.

We need to decide which pointer to move.

If the left line is shorter than the right line,
we move the left pointer.


left += 1

Moves the left pointer one position forward.

It is the same as:

left = left + 1

Example:

left = 1

After:

left += 1

left = 2

Why move the shorter line?

Because the shorter line limits the water height.

If we move the taller line instead:

- The width becomes smaller.
- The shorter line stays the same.
- The maximum possible area cannot increase.

So we move the shorter line to search
for a taller line.


else:

Runs when the left line is not shorter
than the right line.

This means:

height[left] >= height[right]

We move the right pointer.


right -= 1

Moves the right pointer one position backward.

It is the same as:

right = right - 1

Example:

right = 8

After:

right -= 1

right = 7


return max_area

Returns the largest container area found.

The loop has finished because the two pointers
have met.

We now return the best answer.


6. STEP-BY-STEP EXAMPLE
--------------------------------------------------------

Input:

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Initial values:

left = 0
right = 8
max_area = 0


STEP 1:

Left height = 1
Right height = 7

Width = 8 - 0 = 8

Container height = min(1, 7) = 1

Area = 1 * 8 = 8

max_area = 8

Left is shorter.

Move left forward.

left = 1


STEP 2:

Left height = 8
Right height = 7

Width = 8 - 1 = 7

Container height = min(8, 7) = 7

Area = 7 * 7 = 49

max_area = 49

Right is shorter.

Move right backward.

right = 7


STEP 3:

Left height = 8
Right height = 3

Width = 7 - 1 = 6

Container height = min(8, 3) = 3

Area = 3 * 6 = 18

max_area = 49

Right is shorter.

Move right backward.

right = 6


STEP 4:

Left height = 8
Right height = 8

Width = 6 - 1 = 5

Container height = min(8, 8) = 8

Area = 8 * 5 = 40

max_area = 49

Both heights are equal.

The else branch runs.

Move right backward.

right = 5


STEP 5:

Left height = 8
Right height = 4

Width = 5 - 1 = 4

Container height = 4

Area = 4 * 4 = 16

max_area = 49

Move right backward.

right = 4


STEP 6:

Left height = 8
Right height = 5

Width = 4 - 1 = 3

Container height = 5

Area = 5 * 3 = 15

max_area = 49

Move right backward.

right = 3


STEP 7:

Left height = 8
Right height = 2

Width = 3 - 1 = 2

Container height = 2

Area = 2 * 2 = 4

max_area = 49

Move right backward.

right = 2


STEP 8:

Left height = 8
Right height = 6

Width = 2 - 1 = 1

Container height = 6

Area = 6 * 1 = 6

max_area = 49

Move right backward.

right = 1


Now:

left = 1
right = 1

left < right is FALSE.

The loop stops.

Return:

49


7. WHY DO WE MOVE THE SHORTER LINE?
--------------------------------------------------------

This is the most important idea in this problem.

Imagine:

Left height = 4
Right height = 9
Width = 10

Area = 4 * 10 = 40

The shorter line is 4.

The water height cannot be more than 4.

Now imagine moving the taller line.

The new width becomes smaller.

But the shorter line is still 4.

Therefore:

The new area cannot be larger than 40.

So moving the taller line cannot help.

Instead, we move the shorter line.

Why?

Because we want to find another line
that might be taller.

A taller shorter-side line may allow
a larger container area, even with less width.

IMPORTANT RULE:

Always move the pointer at the shorter line.

If both heights are equal, moving either pointer
is valid. This code moves the right pointer.


8. TIME COMPLEXITY
--------------------------------------------------------

O(N)

Where:

N = Number of elements in height.


WHY?

We start with:

left = 0
right = len(height) - 1

In every loop:

- We calculate the area.
- We move either left or right by one position.

The pointers never move backward.

Each pointer can move across the list only once.

Therefore, the total number of loop iterations
cannot exceed N - 1.

Each loop operation takes O(1) time.

TOTAL TIME COMPLEXITY:

O(N)


WHY NOT O(N²)?

A brute force solution checks every possible pair
of lines.

That requires O(N²) time.

Our Two Pointers solution avoids checking
every possible pair.

It completes the search in O(N) time.


9. SPACE COMPLEXITY
--------------------------------------------------------

O(1)

WHY?

We only create a few variables:

max_area
left
right
width_height
width
area

We do not create another list, dictionary,
heap, or set.

The number of extra variables stays the same
regardless of the input size.

Therefore:

AUXILIARY SPACE COMPLEXITY = O(1)


10. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Expected:
49


Test 2:

Input:
height = [1, 1]

Expected:
1


Test 3:

Input:
height = [4, 3, 2, 1, 4]

Expected:
16


Test 4:

Input:
height = [1, 2, 1]

Expected:
2


Test 5:

Input:
height = [2, 3, 4, 5, 18, 17, 6]

Expected:
17


Test 6:

Input:
height = [5, 5, 5, 5]

Expected:
15


Test 7:

Input:
height = [1, 2, 3, 4, 5]

Expected:
6


Test 8:

Input:
height = [5, 1, 1, 1, 5]

Expected:
20


Test 9:

Input:
height = [2, 2, 2]

Expected:
4


Test 10:

Input:
height = [100, 1, 100]

Expected:
200


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what the height list represents.
[ ] I understand what a container is.
[ ] I understand what the left pointer does.
[ ] I understand what the right pointer does.
[ ] I understand why right = len(height) - 1.
[ ] I understand why we use min() for the height.
[ ] I understand why width = right - left.
[ ] I understand the area formula.
[ ] I understand how max() updates max_area.
[ ] I understand why we move the shorter line.
[ ] I understand why the loop stops when left meets right.
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
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 1], 2),
    ([2, 3, 4, 5, 18, 17, 6], 17),
    ([5, 5, 5, 5], 15),
    ([1, 2, 3, 4, 5], 6),
    ([5, 1, 1, 1, 5], 20),
    ([2, 2, 2], 4),
    ([100, 1, 100], 200)
]

passed = 0

print("CONTAINER WITH MOST WATER - TEST RESULTS")
print("----------------------------------")

for height, expected in test_cases:

    result = solution.maxArea(height)

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
