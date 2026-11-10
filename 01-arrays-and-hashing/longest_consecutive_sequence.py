
"""
========================================================
PROBLEM: LONGEST CONSECUTIVE SEQUENCE
TOPIC: ARRAYS AND HASHING
APPROACH: HASH SET
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given an unsorted array of integers called nums:

Return the length of the longest consecutive
sequence of numbers.

In simple words:

Find the longest group of numbers that follow
each other without missing any number.

IMPORTANT:

The numbers do not need to be next to each other
in the original array.

The original array is unsorted.

We only return the LENGTH of the longest sequence,
not the sequence itself.

The algorithm must run in O(n) time.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
nums = [100, 4, 200, 1, 3, 2]

Output:
4

Explanation:

The longest consecutive sequence is:

[1, 2, 3, 4]

Its length is 4.

Other numbers:

100 and 200 do not make a longer sequence.

Therefore:
Output = 4


Example 2:

Input:
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

Output:
9

Explanation:

The longest consecutive sequence is:

[0, 1, 2, 3, 4, 5, 6, 7, 8]

Its length is 9.

Notice:

The number 0 appears twice.

But duplicates do not increase the sequence length.

Therefore:
Output = 9


Example 3:

Input:
nums = [1, 2, 0, 1]

Output:
3

Explanation:

The longest consecutive sequence is:

[0, 1, 2]

Its length is 3.

The repeated 1 does not increase the length.


3. MY APPROACH: HASH SET
--------------------------------------------------------

I use one Hash Set.

A Hash Set stores unique numbers.

It also allows us to check whether a number exists
in approximately O(1) average time.

My steps:

1. Check whether the input array is empty.

2. If it is empty, return 0.

3. Create an empty Hash Set called num_set.

4. Add every number from nums into num_set.

5. Create a variable called longest_sub.
   It stores the longest sequence length found so far.

6. Visit every unique number in num_set.

7. Check whether the previous number (num - 1)
   exists in the Hash Set.

8. If it exists, skip the current number.

   Why?

   Because the current number is not the beginning
   of a sequence.

9. If the previous number does not exist,
   the current number is the beginning of a sequence.

10. Create current_num to track the current number.

11. Create current_sub to count the sequence length.

12. Keep checking whether current_num + 1 exists.

13. If it exists:
    - Move to the next number.
    - Increase the sequence length.

14. Update longest_sub if the current sequence
    is longer.

15. After checking all unique numbers,
    return longest_sub.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def longestConsecutive(self, nums: list[int]) -> int:

        # If the input list is empty, return 0
        if len(nums) == 0:
            return 0

        # Create a Hash Set containing unique numbers
        num_set = set(nums)

        # Store the longest sequence length
        longest_sub = 1

        # Visit every unique number in the Hash Set
        for num in num_set:

            # Check whether the previous number exists
            if num - 1 in num_set:
                continue

            # Start counting a new sequence
            current_num = num
            current_sub = 1

            # Check whether the next consecutive number exists
            while current_num + 1 in num_set:

                # Move to the next number
                current_num += 1

                # Increase the sequence length
                current_sub += 1

            # Update the longest sequence length
            longest_sub = max(longest_sub, current_sub)

        # Return the longest sequence length
        return longest_sub


"""
5. ELS10 EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def longestConsecutive(self, nums: list[int]) -> int:

Creates a function that finds the longest
consecutive sequence.

self:
Refers to the current object of the class.

nums:
The input list of integers.

list[int]:
Means a list containing integers.

int:
Means the function returns one integer.


if len(nums) == 0:

Checks whether the input list is empty.

len(nums):
Counts how many elements are in the list.

Example:

nums = []

len(nums) = 0

Therefore, the condition is True.


return 0

If the list is empty, there is no sequence.

So the answer is 0.

We return immediately because there is
nothing else to check.


num_set = set(nums)

Creates a Hash Set from the input list.

A Hash Set:

- Stores unique values.
- Removes duplicates automatically.
- Allows fast membership checking.

Example:

nums = [1, 2, 2, 3, 3, 4]

num_set = {1, 2, 3, 4}

Notice:

The duplicate numbers disappear.

This is useful because duplicates do not
change the length of a consecutive sequence.


longest_sub = 1

Creates a variable to remember the longest
sequence length found so far.

Why 1?

Because we already know the list is not empty.

At least one unique number exists.

A single number can form a sequence of length 1.

Example:

nums = [100]

The longest sequence is:

[100]

Its length is 1.


for num in num_set:

Visits every unique number in the Hash Set.

Example:

num_set = {100, 4, 200, 1, 3, 2}

The loop visits each unique number.

The order does not matter.

We are not depending on the order of the Hash Set.


if num - 1 in num_set:

Checks whether the previous number exists.

num - 1 means:

Current number minus 1.

Example:

If num = 4:

num - 1 = 3

Python checks:

Is 3 inside num_set?

If yes, 4 is not the beginning
of a consecutive sequence.

Example:

num_set = {1, 2, 3, 4}

For num = 4:

4 - 1 = 3

3 exists in the Hash Set.

Therefore, 4 is not the beginning.

The sequence started earlier at 1.


continue

Skips the current number.

Python moves to the next number in the for loop.

We skip because we do not want to count
the same sequence repeatedly.

IMPORTANT:

Only the first number of a sequence
starts the counting process.

For example:

Sequence = [1, 2, 3, 4]

We start counting at 1.

We skip 2, 3, and 4 because each one
has a previous number in the Hash Set.


current_num = num

Creates a variable to track the current number
while counting a sequence.

Example:

If the starting number is 1:

current_num = 1

We will increase it as we find consecutive numbers.


current_sub = 1

Creates a counter for the current sequence.

Why 1?

Because the starting number already counts
as the first element.

Example:

Sequence:

[1]

Current length = 1


while current_num + 1 in num_set:

Checks whether the next consecutive number exists.

current_num + 1 means:

Current number plus 1.

Example:

If:

current_num = 1

Python checks:

Is 2 inside num_set?

If yes, the sequence continues.

If no, the sequence stops.


current_num += 1

Increases current_num by 1.

This is the shorter version of:

current_num = current_num + 1

Example:

current_num = 1

After:

current_num += 1

current_num = 2

We move to the next consecutive number.


current_sub += 1

Increases the current sequence length by 1.

This is the shorter version of:

current_sub = current_sub + 1

Example:

Before:

current_sub = 1

After:

current_sub += 1

current_sub = 2

We found another number in the sequence.


longest_sub = max(longest_sub, current_sub)

Compares two numbers:

1. longest_sub:
   The longest sequence found before.

2. current_sub:
   The length of the sequence we just counted.

max() returns the bigger number.

Example:

longest_sub = 3
current_sub = 4

max(3, 4) = 4

Therefore:

longest_sub = 4

This keeps the longest sequence length updated.


return longest_sub

Returns the final longest sequence length.

After checking all unique numbers,
the answer is stored in longest_sub.


IMPORTANT: WHY DO WE CHECK num - 1?

This is the most important idea in this solution.

Example:

num_set = {1, 2, 3, 4}

If we start counting from 1:

1 - 1 = 0

0 does not exist.

Therefore, 1 is the beginning of the sequence.

We count:

1 -> 2 -> 3 -> 4

Length = 4

But if we start with 2:

2 - 1 = 1

1 exists.

So we skip 2.

We also skip 3 and 4.

This prevents us from counting the same sequence
again and again.


6. DRY RUN: STEP-BY-STEP EXECUTION
--------------------------------------------------------

Input:

nums = [100, 4, 200, 1, 3, 2]


STEP 1: CREATE HASH SET

num_set = {100, 4, 200, 1, 3, 2}

longest_sub = 1


STEP 2: CHECK THE NUMBERS

Consider num = 100:

100 - 1 = 99

99 does not exist.

100 is the beginning of a sequence.

current_num = 100
current_sub = 1

Check 101:

101 does not exist.

Sequence length = 1

longest_sub = 1


Consider num = 4:

4 - 1 = 3

3 exists.

Skip 4 using continue.


Consider num = 200:

200 - 1 = 199

199 does not exist.

200 is the beginning of a sequence.

current_num = 200
current_sub = 1

Check 201:

201 does not exist.

Sequence length = 1

longest_sub = 1


Consider num = 1:

1 - 1 = 0

0 does not exist.

1 is the beginning of a sequence.

current_num = 1
current_sub = 1


Check the next numbers:

Is 2 in num_set?

YES.

current_num = 2
current_sub = 2


Is 3 in num_set?

YES.

current_num = 3
current_sub = 3


Is 4 in num_set?

YES.

current_num = 4
current_sub = 4


Is 5 in num_set?

NO.

Stop counting.

The current sequence is:

[1, 2, 3, 4]

current_sub = 4

Update:

longest_sub = max(1, 4)

longest_sub = 4


Consider num = 3:

3 - 1 = 2

2 exists.

Skip 3.


Consider num = 2:

2 - 1 = 1

1 exists.

Skip 2.


FINAL ANSWER:

return 4


7. TIME COMPLEXITY
--------------------------------------------------------

O(n)

Where:

n = Number of elements in nums.


WHY?

There are three main operations:


1. EMPTY LIST CHECK

if len(nums) == 0:

This takes O(1) time.


2. CREATE HASH SET

num_set = set(nums)

We visit the input numbers and insert them
into the Hash Set.

Average time = O(n)


3. FIND CONSECUTIVE SEQUENCES

We visit every unique number.

The important idea:

We only start counting when the previous
number does not exist.

Therefore, we only count from the beginning
of each consecutive sequence.

The while loops do not repeatedly count
the same sequence from every number.

Across all sequences, each number is advanced
through at most once.

Average time = O(n)


TOTAL TIME COMPLEXITY:

O(1) + O(n) + O(n)

Therefore:

TIME COMPLEXITY = O(n)


IMPORTANT:

Hash Set membership checking takes O(1)
average time.

This is why the solution can achieve O(n).

A sorting solution would take O(n log n),
which does not meet the required O(n) time.


8. SPACE COMPLEXITY
--------------------------------------------------------

O(n)

Where:

n = Number of elements in nums.


WHY?

num_set = set(nums)

The Hash Set stores the unique numbers.

In the worst case, every number is different.

Example:

nums = [1, 2, 3, 4, 5]

The Hash Set stores all 5 numbers.

Therefore:

Hash Set space = O(n)


Other variables:

longest_sub
current_num
current_sub

These variables use O(1) extra space.


TOTAL SPACE COMPLEXITY:

O(n) + O(1)

Therefore:

SPACE COMPLEXITY = O(n)


IMPORTANT:

The Hash Set is the main source of extra memory.


9. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
nums = [100, 4, 200, 1, 3, 2]

Expected:
4

Reason:
The longest sequence is [1, 2, 3, 4].


Test 2:

Input:
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

Expected:
9

Reason:
The longest sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8].


Test 3:

Input:
nums = []

Expected:
0

Reason:
There are no elements.


Test 4:

Input:
nums = [1]

Expected:
1

Reason:
One number creates a sequence of length 1.


Test 5:

Input:
nums = [1, 2, 0, 1]

Expected:
3

Reason:
The longest sequence is [0, 1, 2].
The duplicate 1 does not increase the length.


Test 6:

Input:
nums = [9, 8, 7, 6, 5, 4]

Expected:
6

Reason:
The longest sequence is [4, 5, 6, 7, 8, 9].


Test 7:

Input:
nums = [10, 30, 20, 50]

Expected:
1

Reason:
There are no consecutive numbers.


Test 8:

Input:
nums = [-2, -1, 0, 1, 2, 10]

Expected:
5

Reason:
The longest sequence is [-2, -1, 0, 1, 2].


Test 9:

Input:
nums = [1, 2, 3, 4, 5, 6]

Expected:
6

Reason:
Every number belongs to one consecutive sequence.


Test 10:

Input:
nums = [100, 4, 200, 1, 3, 2, 2, 3, 4]

Expected:
4

Reason:
The longest sequence is [1, 2, 3, 4].
Duplicates do not increase the length.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a consecutive sequence is.
[ ] I understand why the original order does not matter.
[ ] I understand what a Hash Set is.
[ ] I understand why set(nums) removes duplicates.
[ ] I understand why we check for an empty list.
[ ] I understand what num_set contains.
[ ] I understand what num - 1 means.
[ ] I understand why we skip numbers with a predecessor.
[ ] I understand what continue does.
[ ] I understand why we start counting only at sequence beginnings.
[ ] I understand current_num.
[ ] I understand current_sub.
[ ] I understand how the while loop works.
[ ] I understand current_num += 1.
[ ] I understand current_sub += 1.
[ ] I understand how max() works.
[ ] I understand why the algorithm runs in O(n) average time.
[ ] I understand why the Hash Set uses O(n) space.
[ ] I can write this solution without looking.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([], 0),
    ([1], 1),
    ([1, 2, 0, 1], 3),
    ([9, 8, 7, 6, 5, 4], 6),
    ([10, 30, 20, 50], 1),
    ([-2, -1, 0, 1, 2, 10], 5),
    ([1, 2, 3, 4, 5, 6], 6),
    ([100, 4, 200, 1, 3, 2, 2, 3, 4], 4)
]

passed = 0

print("LONGEST CONSECUTIVE SEQUENCE - TEST RESULTS")
print("----------------------------------")

for nums, expected in test_cases:

    result = solution.longestConsecutive(nums)

    print("Numbers:", nums)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
