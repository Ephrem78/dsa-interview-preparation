
"""
========================================================
SLIDING WINDOW MAXIMUM
========================================================

1. PROBLEM DESCRIPTION
--------------------------------------------------------

You are given:
- nums: a list of integers.
- k: the size of the sliding window.

A sliding window is a group of k consecutive numbers.
The window moves one position to the right each time.

Find the maximum number in every window and return
a list containing all the maximum numbers.

IMPORTANT:
1. Every window contains exactly k numbers.
2. The window moves one position to the right.
3. We find the largest number in each window.
4. We return all maximum numbers in a list.

2. EXAMPLES
--------------------------------------------------------

Example 1:
Input:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

Windows:
[1, 3, -1]
[3, -1, -3]
[-1, -3, 5]
[-3, 5, 3]
[5, 3, 6]
[3, 6, 7]

Expected:
[3, 3, 5, 5, 6, 7]

Example 2:
Input: nums = [1], k = 1
Expected: [1]

Example 3:
Input: nums = [1, -1], k = 1
Expected: [1, -1]

Example 4:
Input: nums = [9, 11], k = 2
Expected: [11]

Example 5:
Input: nums = [4, -2], k = 2
Expected: [4]

Example 6:
Input: nums = [7, 2, 4], k = 2
Expected: [7, 4]


3. APPROACH: SLIDING WINDOW + DEQUE
--------------------------------------------------------

We use:
- Sliding Window
- Deque
- Indices
- Monotonic Decreasing Queue

WHAT IS A DEQUE?

Deque means Double-Ended Queue.

It allows us to add and remove elements from both ends.

Python provides deque through:

    from collections import deque

WHY DO WE USE A DEQUE?

We need to find the maximum number in every window.

A simple solution checks every number in every window.
That can take O(N * K) time.

A deque helps us solve the problem in O(N) time.

IMPORTANT: OUR DEQUE STORES INDICES, NOT NUMBERS.

Example:

    nums = [1, 3, -1]

    Index:  0  1   2
    Value:  1  3  -1

If the deque contains:

    [1, 2]

It stores indices 1 and 2.

Their values are:

    nums[1] = 3
    nums[2] = -1

DEQUE RULE:

The values represented by the indices are kept
in decreasing order.

Example:

    Deque indices: [1, 2, 3]
    Values:        [5, 3, 1]

The largest value stays at the FRONT.

Therefore:

    deque_indices[0]          -> index of maximum
    nums[deque_indices[0]]    -> maximum number

WHY REMOVE SMALLER NUMBERS?

Example:

    nums = [2, 5]

We are processing 5.

The previous number is 2.

Can 2 become the maximum in a future window
that also contains 5?

No. The number 5 is bigger and appears after 2.

Whenever both are inside a window, 5 is the maximum.

Therefore, we remove the index of 2.


4. COMPLETE PYTHON SOLUTION
--------------------------------------------------------

This is the Python conversion of your Java algorithm.

Python uses collections.deque instead of Java's
Deque and LinkedList.
"""

from collections import deque


class Solution:

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        # Step 1: Check invalid inputs.
        if not nums or k <= 0 or k > len(nums):
            return []

        # Step 2: Get the length of the array.
        n = len(nums)

        # Step 3: Create the result list.
        result = [0] * (n - k + 1)

        # Step 4: Create an empty deque.
        deque_indices = deque()

        # Step 5: Visit every number in nums.
        for i in range(n):

            # Step 6: Remove indices outside the current window.
            while deque_indices and deque_indices[0] < i - k + 1:
                deque_indices.popleft()

            # Step 7: Remove smaller values from the back.
            while (deque_indices and
                   nums[deque_indices[-1]] < nums[i]):
                deque_indices.pop()

            # Step 8: Add the current index.
            deque_indices.append(i)

            # Step 9: Save the answer when a full window exists.
            if i >= k - 1:
                result[i - k + 1] = nums[deque_indices[0]]

        # Step 10: Return all window maximums.
        return result


"""
5. COMPLETE ELS10 CODE EXPLANATION
--------------------------------------------------------

IMPORT:

    from collections import deque

collections is a Python module.
A module is a collection of ready-made tools.

deque is one of those tools.

We import deque because we need a data structure
that can add and remove elements from both ends.

--------------------------------------------------------

CLASS:

    class Solution:

A class is a container for related code.

We create a class called Solution because
this is the format expected by LeetCode.

--------------------------------------------------------

FUNCTION:

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

def creates a function.

maxSlidingWindow is the function name.

It receives:
- self: refers to the current Solution object.
- nums: the list of numbers.
- k: the size of the window.

-> list[int] tells us that the function returns
a list of integers.

--------------------------------------------------------

STEP 1: CHECK INVALID INPUTS

    if not nums or k <= 0 or k > len(nums):
        return []

if checks whether a condition is True.

not nums checks whether the list is empty.

Example:
    nums = []

The condition not nums is True.

k <= 0 checks whether k is zero or negative.
A window cannot have zero or negative size.

k > len(nums) checks whether the window is bigger
than the entire array.

Example:
    nums = [1, 2, 3]
    k = 5

We cannot create a window of five numbers
from an array containing only three numbers.

or means at least one condition must be True.

return [] sends an empty list back and stops
the function.

--------------------------------------------------------

STEP 2: GET THE ARRAY LENGTH

    n = len(nums)

len() counts the number of elements in a list.

Example:
    nums = [1, 3, -1, -3, 5, 3, 6, 7]

    len(nums) = 8

Therefore:
    n = 8

We use n to control the loop and calculate
the size of the result list.

--------------------------------------------------------

STEP 3: CREATE THE RESULT LIST

    result = [0] * (n - k + 1)

This creates a list with enough spaces
for all the answers.

Example:
    n = 8
    k = 3

Calculation:
    n - k + 1
    8 - 3 + 1 = 6

Therefore:
    result = [0, 0, 0, 0, 0, 0]

WHY SIX?

An array of eight numbers has six possible
windows of size three.

We need six answer spaces.

--------------------------------------------------------

STEP 4: CREATE THE DEQUE

    deque_indices = deque()

This creates an empty deque.

IMPORTANT: We store INDICES, not actual numbers.

Example:
    nums = [1, 3, -1]

    Index:  0  1   2
    Value:  1  3  -1

If:
    deque_indices = [1, 2]

It means we store index 1 and index 2.

Their values are:
    nums[1] = 3
    nums[2] = -1

WHY STORE INDICES?

We need to know:
1. The value of each number.
2. Where each number is located.
3. Whether an index is outside the current window.

--------------------------------------------------------

STEP 5: VISIT EVERY INDEX

    for i in range(n):

range(n) produces the indices from 0 to n - 1.

If n = 8:

    0, 1, 2, 3, 4, 5, 6, 7

i represents the current index.

Example:
    i = 0 -> nums[i] = 1
    i = 1 -> nums[i] = 3
    i = 2 -> nums[i] = -1

The loop visits every number once.

--------------------------------------------------------

STEP 6: REMOVE EXPIRED INDICES

    while deque_indices and deque_indices[0] < i - k + 1:
        deque_indices.popleft()

This removes indices that are outside
the current sliding window.

Let's understand each part.

deque_indices checks whether the deque contains elements.
An empty deque behaves like False.

We must not remove an element from an empty deque.

deque_indices[0] gets the first index in the deque.

i - k + 1 calculates the beginning index
of the current window.

Example:
    i = 4
    k = 3

Calculation:
    4 - 3 + 1 = 2

The current window starts at index 2.

Now imagine:
    deque_indices = [0, 2, 3]

The first index is 0.

Check:
    0 < 2

This is True.

Index 0 is outside the current window.

popleft() removes the first element.

Before:
    [0, 2, 3]

After:
    [2, 3]

WHY DO WE REMOVE IT?

Because index 0 is no longer inside the current window.
It cannot be the answer for this window.

--------------------------------------------------------

STEP 7: REMOVE SMALLER VALUES FROM THE BACK

    while (deque_indices and
           nums[deque_indices[-1]] < nums[i]):
        deque_indices.pop()

This keeps the deque values in decreasing order.

deque_indices checks whether the deque is empty.

deque_indices[-1] gets the last index.

Remember:
    deque_indices[0]  -> first index
    deque_indices[-1] -> last index

nums[deque_indices[-1]] gets the actual value
at the last stored index.

Example:
    nums = [2, 5]
    deque_indices = [0]
    i = 1

Then:
    deque_indices[-1] = 0
    nums[0] = 2
    nums[i] = 5

The comparison becomes:
    2 < 5

This is True.

WHY REMOVE 2?

Because 5 is bigger and comes after 2.

If a future window contains both numbers,
5 will always be bigger.

So 2 is no longer useful.

pop() removes the last element from the deque.

IMPORTANT DIFFERENCE:

    popleft() -> removes from the FRONT.
    pop()     -> removes from the BACK.

--------------------------------------------------------

STEP 8: ADD THE CURRENT INDEX

    deque_indices.append(i)

append() adds an element to the end of a list
or deque.

Example:
    deque_indices = [1, 2]
    i = 3

After:
    deque_indices = [1, 2, 3]

We add the current index because its number
may become the maximum in this or a future window.

--------------------------------------------------------

STEP 9: CHECK WHETHER A COMPLETE WINDOW EXISTS

    if i >= k - 1:

We save an answer only after the first complete
window has been formed.

Example:
    k = 3

The first window contains indices:
    0, 1, 2

When i = 0:
    One number. Not enough.

When i = 1:
    Two numbers. Not enough.

When i = 2:
    Three numbers. The first window is complete.

Therefore:
    i >= k - 1

When i is at least 2, we can save answers.

--------------------------------------------------------

STEP 10: SAVE THE MAXIMUM

    result[i - k + 1] = nums[deque_indices[0]]

deque_indices[0] gets the first index in the deque.

Why the first index?

Because the deque keeps its values in decreasing order.
The largest value stays at the front.

nums[deque_indices[0]] uses that index
to get the actual maximum number.

Example:
    nums = [1, 3, -1]
    deque_indices = [1, 2]

The front index is:
    deque_indices[0] = 1

The actual number is:
    nums[1] = 3

Therefore, the maximum is 3.

Now calculate where to save the answer:

    i - k + 1

If:
    i = 2
    k = 3

Then:
    2 - 3 + 1 = 0

Therefore:
    result[0] = 3

For the next window:
    i = 3
    k = 3

Then:
    result[1] = maximum of the second window.

--------------------------------------------------------

STEP 11: RETURN THE RESULT

    return result

This sends the completed list back.

Example:
    [3, 3, 5, 5, 6, 7]


6. COMPLETE DRY RUN
--------------------------------------------------------

INPUT:

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

INITIAL VALUES:

    n = 8
    result = [0, 0, 0, 0, 0, 0]
    deque_indices = []

IMPORTANT:
The deque stores indices.
We will show both indices and their values.

--------------------------------------------------------
ITERATION 1
--------------------------------------------------------

i = 0
Current number = nums[0] = 1

A. Remove expired indices.
The deque is empty. Nothing happens.

B. Remove smaller values.
The deque is empty. Nothing happens.

C. Add current index:
    deque_indices = [0]
    Values = [1]

D. Check:
    i >= k - 1
    0 >= 2 -> False

No answer is saved yet.

--------------------------------------------------------
ITERATION 2
--------------------------------------------------------

i = 1
Current number = nums[1] = 3

A. Remove expired indices.
Nothing happens.

B. Compare the last value with 3:
    1 < 3 -> True

Remove index 0.

    deque_indices = []

C. Add index 1:
    deque_indices = [1]
    Values = [3]

D. Check:
    1 >= 2 -> False

No answer is saved yet.

--------------------------------------------------------
ITERATION 3
--------------------------------------------------------

i = 2
Current number = nums[2] = -1

A. Calculate the window start:
    i - k + 1
    2 - 3 + 1 = 0

Index 1 is still inside the window.
Nothing is removed.

B. Compare:
    3 < -1 -> False

Keep index 1.

C. Add index 2:
    deque_indices = [1, 2]
    Values = [3, -1]

D. Check:
    2 >= 2 -> True

The first complete window is ready.

Maximum:
    nums[deque_indices[0]]
    nums[1] = 3

Save:
    result[0] = 3

Result:
    [3, 0, 0, 0, 0, 0]

Current window:
    [1, 3, -1]

--------------------------------------------------------
ITERATION 4
--------------------------------------------------------

i = 3
Current number = nums[3] = -3

A. Window start:
    3 - 3 + 1 = 1

Index 1 is still valid.

B. Compare:
    -1 < -3 -> False

Keep index 2.

C. Add index 3:
    deque_indices = [1, 2, 3]
    Values = [3, -1, -3]

D. Maximum:
    nums[1] = 3

Save:
    result[1] = 3

Result:
    [3, 3, 0, 0, 0, 0]

Current window:
    [3, -1, -3]

--------------------------------------------------------
ITERATION 5
--------------------------------------------------------

i = 4
Current number = nums[4] = 5

A. Window start:
    4 - 3 + 1 = 2

Index 1 is outside the window.

Remove index 1:
    deque_indices = [2, 3]

B. Compare the last value with 5:

    -3 < 5 -> True

Remove index 3:
    deque_indices = [2]

Compare again:

    -1 < 5 -> True

Remove index 2:
    deque_indices = []

C. Add index 4:
    deque_indices = [4]
    Values = [5]

D. Maximum:
    nums[4] = 5

Save:
    result[2] = 5

Result:
    [3, 3, 5, 0, 0, 0]

Current window:
    [-1, -3, 5]

--------------------------------------------------------
ITERATION 6
--------------------------------------------------------

i = 5
Current number = nums[5] = 3

A. Window start:
    5 - 3 + 1 = 3

Index 4 is valid.

B. Compare:
    5 < 3 -> False

Keep index 4.

C. Add index 5:
    deque_indices = [4, 5]
    Values = [5, 3]

D. Maximum:
    nums[4] = 5

Save:
    result[3] = 5

Result:
    [3, 3, 5, 5, 0, 0]

Current window:
    [-3, 5, 3]

--------------------------------------------------------
ITERATION 7
--------------------------------------------------------

i = 6
Current number = nums[6] = 6

A. Window start:
    6 - 3 + 1 = 4

Index 4 is valid.

B. Compare the last value with 6:

    3 < 6 -> True

Remove index 5:
    deque_indices = [4]

Compare again:

    5 < 6 -> True

Remove index 4:
    deque_indices = []

C. Add index 6:
    deque_indices = [6]
    Values = [6]

D. Maximum:
    nums[6] = 6

Save:
    result[4] = 6

Result:
    [3, 3, 5, 5, 6, 0]

Current window:
    [5, 3, 6]

--------------------------------------------------------
ITERATION 8
--------------------------------------------------------

i = 7
Current number = nums[7] = 7

A. Window start:
    7 - 3 + 1 = 5

Index 6 is valid.

B. Compare:
    6 < 7 -> True

Remove index 6:
    deque_indices = []

C. Add index 7:
    deque_indices = [7]
    Values = [7]

D. Maximum:
    nums[7] = 7

Save:
    result[5] = 7

FINAL RESULT:
    [3, 3, 5, 5, 6, 7]


7. TIME COMPLEXITY
--------------------------------------------------------

TIME COMPLEXITY: O(N)

N means the number of elements in nums.

WHY O(N)?

We visit every number once:

    for i in range(n):

But what about the two while loops?

Do they make the algorithm O(N * K)?

No.

IMPORTANT:

Every index is:
1. Added to the deque once.
2. Removed from the deque at most once.

An index can be removed from the front or the back.
It cannot be removed twice.

Therefore, the total number of deque operations
across the whole algorithm is O(N).

FINAL TIME COMPLEXITY:

    O(N)

COMPARE WITH BRUTE FORCE:

Brute force checks every number inside every window.

Time complexity:
    O(N * K)

Deque solution processes every index at most
a constant number of times.

Time complexity:
    O(N)

This is why the deque solution is faster.


8. SPACE COMPLEXITY
--------------------------------------------------------

A deque can store at most K indices.

Deque space:
    O(K)

The result contains N - K + 1 numbers.

Output space:
    O(N - K + 1)

Total space:
    O(K + N - K + 1)

Simplified:
    O(N)

IMPORTANT:

If we do not count the output list,
the extra working space is O(K).

This is because the deque stores at most K indices.


9. MY LEARNING CHECKLIST
--------------------------------------------------------

[ ] I understand what a sliding window is.
[ ] I understand what the maximum means.
[ ] I understand why the window moves right.
[ ] I understand what a deque is.
[ ] I understand why we use collections.deque.
[ ] I understand why the deque stores indices.
[ ] I understand deque_indices[0].
[ ] I understand deque_indices[-1].
[ ] I understand append().
[ ] I understand popleft().
[ ] I understand pop().
[ ] I understand why we remove expired indices.
[ ] I understand why we remove smaller values.
[ ] I understand why the largest value stays at the front.
[ ] I understand the expression i - k + 1.
[ ] I understand why we use i >= k - 1.
[ ] I understand how the result list is created.
[ ] I understand how the maximum is saved.
[ ] I can explain the complete dry run.
[ ] I understand why time complexity is O(N).
[ ] I understand why deque space is O(K).
[ ] I can write this solution without looking.


10. TESTING THE SOLUTION
--------------------------------------------------------
"""

solution = Solution()

test_cases = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ([1], 1, [1]),
    ([1, -1], 1, [1, -1]),
    ([9, 11], 2, [11]),
    ([4, -2], 2, [4]),
    ([7, 2, 4], 2, [7, 4]),
    ([5, 5, 5, 5], 2, [5, 5, 5]),
    ([9, 8, 7, 6, 5], 3, [9, 8, 7]),
    ([-7, -8, -6, -5, -9], 2, [-7, -6, -5, -5]),
    ([1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]),
    ([], 1, []),
    ([1, 2, 3], 0, []),
    ([1, 2, 3], 4, []),
    ([3, 3, 3], 1, [3, 3, 3]),
    ([10, 9, 8, 7], 4, [10])
]

passed = 0

print("SLIDING WINDOW MAXIMUM - TEST RESULTS")
print("--------------------------------------")

for nums, k, expected in test_cases:

    result = solution.maxSlidingWindow(nums, k)

    print("Input:", nums)
    print("Window size:", k)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("--------------------------------------")

print(
    "FINAL RESULT:",
    passed,
    "/",
    len(test_cases),
    "TESTS PASSED"
)
