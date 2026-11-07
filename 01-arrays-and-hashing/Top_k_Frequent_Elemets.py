"""
========================================================
PROBLEM: TOP K FREQUENT ELEMENTS
TOPIC: ARRAYS AND HASHING
APPROACH: HASH MAP + MIN HEAP (PRIORITY QUEUE)
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given an integer array called nums and an integer k:

Return the k most frequent elements.

In simple words:

Find the numbers that appear most frequently
in the input array.

Return only the k numbers with the highest frequencies.

The order of the answer does not matter.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
nums = [1, 1, 1, 2, 2, 3]
k = 2

Output:
[1, 2]

Explanation:

Number 1 appears 3 times.
Number 2 appears 2 times.
Number 3 appears 1 time.

We need the 2 most frequent numbers.

Therefore:
Output = [1, 2]


Example 2:

Input:
nums = [1]
k = 1

Output:
[1]

Explanation:

Number 1 appears once.

We need the 1 most frequent number.

Therefore:
Output = [1]


Example 3:

Input:
nums = [4, 4, 4, 6, 6, 7, 7, 7]
k = 2

Output:
[4, 7]

Explanation:

Number 4 appears 3 times.
Number 6 appears 2 times.
Number 7 appears 3 times.

We need the 2 most frequent numbers.

Therefore:
Output = [4, 7]

NOTE:
When two numbers have the same frequency,
either can be returned if they both satisfy the
required frequency ranking.


3. MY APPROACH: HASH MAP + MIN HEAP
--------------------------------------------------------

I use two data structures:

1. HASH MAP (DICTIONARY)

   Counts how many times each number appears.

2. MIN HEAP (PRIORITY QUEUE)

   Keeps the k most frequent numbers.

My steps:

1. Create an empty dictionary called count.

2. Visit every number in nums.

3. Count how many times each number appears.

4. Create an empty Min Heap called heap.

5. Visit every unique number in the dictionary.

6. Insert each number into the heap together
   with its frequency.

7. If the heap contains more than k elements,
   remove the element with the smallest frequency.

8. After processing all unique numbers,
   the heap contains the k most frequent numbers.

9. Extract the numbers from the heap.

10. Return the answer.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

import heapq


class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # Create an empty dictionary to count frequencies
        count = {}

        # Count how many times each number appears
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Create an empty Min Heap
        heap = []

        # Visit every unique number in the dictionary
        for num, frequency in count.items():

            # Add (frequency, number) to the Min Heap
            heapq.heappush(heap, (frequency, num))

            # Keep the heap size at k or smaller
            if len(heap) > k:

                # Remove the number with the smallest frequency
                heapq.heappop(heap)

        # Extract the numbers from the heap
        result = []

        while heap:
            frequency, num = heapq.heappop(heap)
            result.append(num)

        # Return the k most frequent numbers
        return result


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

import heapq

Imports Python's built-in heapq library.

heapq provides functions for working with Min Heaps.

A Min Heap is a data structure where the smallest
element is always at the top.

We use it to remove the number with the smallest
frequency.


class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def topKFrequent(self, nums: list[int], k: int) -> list[int]:

Creates a function that finds the k most frequent numbers.

self:
Refers to the current object of the class.

nums:
The input list of integers.

k:
The number of frequent elements we need to return.

list[int]:
Means that the function returns a list of integers.


count = {}

Creates an empty dictionary.

We use this dictionary to count how many times
each number appears.

Dictionary structure:

{
    number: frequency
}


for num in nums:

Visits every number in the input list.

Example:

nums = [1, 1, 1, 2, 2, 3]

The loop visits:

1
1
1
2
2
3


count[num] = count.get(num, 0) + 1

Counts the frequency of each number.

get() checks whether the number already exists.

If the number does not exist:
Its starting frequency is 0.

If the number already exists:
We get its current frequency.

Then we add 1.

Example:

First 1:
count = {1: 1}

Second 1:
count = {1: 2}

Third 1:
count = {1: 3}

First 2:
count = {1: 3, 2: 1}

Second 2:
count = {1: 3, 2: 2}

Number 3:
count = {1: 3, 2: 2, 3: 1}


heap = []

Creates an empty Min Heap.

We will store pairs inside the heap.

Each pair contains:

(frequency, number)

Example:

(3, 1)

Means:

Number 1 appears 3 times.


for num, frequency in count.items():

Visits every number and its frequency
in the dictionary.

Example:

count = {
    1: 3,
    2: 2,
    3: 1
}

First:
num = 1
frequency = 3

Second:
num = 2
frequency = 2

Third:
num = 3
frequency = 1


heapq.heappush(heap, (frequency, num))

Adds a pair to the Min Heap.

The heap uses the frequency as its first priority.

The smallest frequency stays at the top.

Example:

After adding:

(3, 1)
(2, 2)
(1, 3)

The smallest frequency is 1.

Therefore, the pair (1, 3) is at the top.


if len(heap) > k:

Checks whether the heap contains more than k elements.

Why?

Because we only need k most frequent numbers.

We do not need to keep every unique number
inside the heap.


heapq.heappop(heap)

Removes and returns the smallest element
from the Min Heap.

Since frequency is the first value in each pair,
the number with the smallest frequency is removed.

Example:

heap = [(1, 3), (2, 2), (3, 1)]

If we remove the smallest pair:

(1, 3)

Number 3 is removed because it has the smallest frequency.


while heap:

Continues running while the heap contains elements.

A non-empty list is treated as True in Python.

An empty list is treated as False.


frequency, num = heapq.heappop(heap)

Removes the smallest pair from the heap.

The pair contains:

frequency = number of occurrences
num = actual number


result.append(num)

Adds the number to the result list.

We only append the number, not its frequency.


return result

Returns the k most frequent numbers.


IMPORTANT:

The Min Heap does not need to store all unique numbers.

Whenever its size becomes greater than k,
we remove the least frequent number.

Therefore, after processing all unique numbers,
the heap contains only the k most frequent numbers.


6. TIME COMPLEXITY
--------------------------------------------------------

O(N + M log K)

Where:

N = Total number of elements in nums.

M = Number of unique elements in nums.

K = Number of elements we want to return.

Why?

There are two main operations:


1. HASH MAP FREQUENCY COUNTING

We visit every number in nums once.

If nums contains N elements:

Time complexity = O(N)


2. MIN HEAP OPERATIONS

We visit every unique number.

There are M unique numbers.

For every unique number:

- Insert it into the heap.
- Check whether heap size is greater than k.
- If necessary, remove the smallest element.

Heap insertion takes O(log K) when the heap
contains at most K elements.

Heap removal also takes O(log K).

Therefore:

M unique elements × O(log K)

= O(M log K)


TOTAL TIME COMPLEXITY:

O(N) + O(M log K)

Therefore:

TIME COMPLEXITY = O(N + M log K)


Since M cannot be greater than N,
we can also express the upper bound as:

O(N log K)

But O(N + M log K) describes the two stages
more precisely.


7. SPACE COMPLEXITY
--------------------------------------------------------

O(M + K)

Where:

M = Number of unique elements.
K = Number of elements we want to return.

Why?

HASH MAP:

The dictionary stores one entry for each
unique number.

Therefore:

Dictionary space = O(M)


MIN HEAP:

The heap never contains more than k elements.

Therefore:

Heap space = O(K)


RESULT:

The result contains k numbers.

Therefore:

Result space = O(K)


TOTAL SPACE COMPLEXITY:

O(M + K)

The heap and result are both O(K).

The dictionary uses O(M).

Therefore:

TOTAL SPACE COMPLEXITY = O(M + K)


IMPORTANT:

The space complexity includes the output list.

If we exclude the output list,
the additional auxiliary space is:

O(M + K)


8. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
nums = [1, 1, 1, 2, 2, 3]
k = 2

Expected:
[1, 2]

Reason:
1 appears 3 times.
2 appears 2 times.
3 appears 1 time.


Test 2:

Input:
nums = [1]
k = 1

Expected:
[1]

Reason:
There is only one number.


Test 3:

Input:
nums = [4, 4, 4, 6, 6, 7, 7, 7]
k = 2

Expected:
[4, 7]

Reason:
4 and 7 both appear 3 times.


Test 4:

Input:
nums = [1, 2, 3, 4, 5]
k = 3

Expected:
Any 3 different numbers.

Reason:
Every number appears once.
All numbers have the same frequency.


Test 5:

Input:
nums = [-1, -1, -1, 2, 2, 3]
k = 2

Expected:
[-1, 2]

Reason:
-1 appears 3 times.
2 appears 2 times.
3 appears once.


Test 6:

Input:
nums = [5, 5, 5, 5, 2, 2, 3, 3]
k = 1

Expected:
[5]

Reason:
5 appears 4 times.
It is the most frequent number.


Test 7:

Input:
nums = [1, 1, 2, 2, 3, 3]
k = 2

Expected:
Any 2 different numbers.

Reason:
All three numbers appear twice.
Any two satisfy the requirement.


Test 8:

Input:
nums = [10, 10, 10, 20, 20, 30, 40, 40]
k = 3

Expected:
[10, 20, 40]

Reason:
10 appears 3 times.
20 appears 2 times.
40 appears 2 times.
30 appears once.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what frequency means.
[ ] I understand how a Hash Map counts frequencies.
[ ] I understand how dictionary get() works.
[ ] I understand what a Min Heap is.
[ ] I understand what a Priority Queue is.
[ ] I understand how heapq works in Python.
[ ] I understand what heappush() does.
[ ] I understand what heappop() does.
[ ] I understand why we store (frequency, number).
[ ] I understand why we remove the smallest frequency.
[ ] I understand why the heap size must not exceed k.
[ ] I can write this solution without looking.
[ ] I understand O(N + M log K) time complexity.
[ ] I understand O(M + K) space complexity.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([4, 4, 4, 6, 6, 7, 7, 7], 2, [4, 7]),
    ([1, 2, 3, 4, 5], 3, [1, 2, 3]),
    ([-1, -1, -1, 2, 2, 3], 2, [-1, 2]),
    ([5, 5, 5, 5, 2, 2, 3, 3], 1, [5]),
    ([1, 1, 2, 2, 3, 3], 2, [1, 2]),
    ([10, 10, 10, 20, 20, 30, 40, 40], 3, [10, 20, 40])
]

passed = 0

print("TOP K FREQUENT ELEMENTS - TEST RESULTS")
print("----------------------------------")

for nums, k, expected in test_cases:

    result = solution.topKFrequent(nums, k)

    # Sort the results because output order does not matter
    actual_sorted = sorted(result)
    expected_sorted = sorted(expected)

    print("Numbers:", nums)
    print("K:", k)
    print("Expected:", expected)
    print("Actual:", result)

    if actual_sorted == expected_sorted:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
