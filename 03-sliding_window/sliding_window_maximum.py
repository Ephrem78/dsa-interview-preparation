"""
========================================================
                 SLIDING WINDOW MAXIMUM
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

You are given:

nums = an array of integers
k = the size of the sliding window

A sliding window is a group of k consecutive numbers.

The window starts at the beginning of the array.

After checking the maximum number in the window,
the window moves one position to the right.

For every window, find the maximum number.

Return a list containing all maximum numbers.


IMPORTANT:

1. The window always contains k numbers.
2. The window moves one position to the right each time.
3. We find the largest number inside each window.
4. We return all maximum numbers in a list.


2. EXAMPLES
--------------------------------------------------------

Example 1:

Input:

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

Windows:

[1, 3, -1], -3, 5, 3, 6, 7

1, [3, -1, -3], 5, 3, 6, 7

1, 3, [-1, -3, 5], 3, 6, 7

1, 3, -1, [-3, 5, 3], 6, 7

1, 3, -1, -3, [5, 3, 6], 7

1, 3, -1, -3, 5, [3, 6, 7]


Maximum of each window:

[3, 3, 5, 5, 6, 7]

Expected:

[3, 3, 5, 5, 6, 7]


Example 2:

Input:

nums = [1]
k = 1

Window:

[1]

Expected:

[1]


Example 3:

Input:

nums = [1, -1]
k = 1

Windows:

[1], -1

1, [-1]

Expected:

[1, -1]


Example 4:

Input:

nums = [9, 11]
k = 2

Window:

[9, 11]

Expected:

[11]


Example 5:

Input:

nums = [4, -2]
k = 2

Window:

[4, -2]

Expected:

[4]


Example 6:

Input:

nums = [7, 2, 4]
k = 2

Windows:

[7, 2], 4

7, [2, 4]

Expected:

[7, 4]


3. APPROACH: SLIDING WINDOW + DEQUE
--------------------------------------------------------

We use:

- Sliding Window
- Deque
- Two Pointers / Indices
- Monotonic Decreasing Queue

WHAT IS A DEQUE?

Deque means Double-Ended Queue.

It is a data structure that allows us to:

1. Add an element at the beginning.
2. Add an element at the end.
3. Remove an element from the beginning.
4. Remove an element from the end.

In Python, we use:

from collections import deque


WHY DO WE USE A DEQUE?

We need to find the maximum number in every window.

A simple solution checks every number in every window.

But that can take O(N * K) time.

We can do better with a deque.

Our deque stores INDICES, not the actual numbers.

Example:

nums = [1, 3, -1]

The indices are:

Index:  0  1   2
Value:  1  3  -1

If our deque contains:

[1, 2]

It means we are storing the indices 1 and 2.

The actual values are:

nums[1] = 3
nums[2] = -1


IMPORTANT DEQUE RULE:

The values represented by indices in the deque
are kept in decreasing order.

Example:

Deque indices:

[1, 2, 3]

Corresponding values:

[3, 2, 1]

The largest value is always at the FRONT.

Therefore:

deque[0] gives us the index of the maximum number.

nums[deque[0]] gives us the maximum number itself.


WHY DO WE REMOVE SMALLER NUMBERS?

Example:

nums = [2, 5]

We are processing 5.

The previous number is 2.

Can 2 ever become the maximum in a future window
that also contains 5?

No.

Why?

Because 5 is bigger than 2 and appears after it.

Whenever both are inside a window, 5 is the maximum.

Therefore, we remove the index of 2.

This keeps our deque useful and efficient.


4. COMPLETE PYTHON SOLUTION
--------------------------------------------------------

The following Python code is a direct conversion
of your Java algorithm.

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

            # Step 7: Remove indices whose values are smaller
            # than the current number.
            while (deque_indices and
                   nums[deque_indices[-1]] < nums[i]):
                deque_indices.pop()

            # Step 8: Add the current index to the deque.
            deque_indices.append(i)

            # Step 9: Start saving answers when the first
            # complete window has been formed.
            if i >= k - 1:

                # Get the maximum number from the front index.
                result[i - k + 1] = nums[deque_indices[0]]

        # Step 10: Return all window maximums.
        return result


"""
5. COMPLETE ELS10 CODE EXPLANATION
--------------------------------------------------------


FIRST:

from collections import deque


What does this mean?

collections is a Python module.

A module is a collection of ready-made tools.

deque is one of those tools.

We import deque because we need a queue that can
add and remove elements from both ends.


NEXT:

class Solution:


What does this mean?

We create a class called Solution.

A class is like a container for related code.

Our solution method will be inside this class.


NEXT:

def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:


What does this mean?

We create a method called maxSlidingWindow.

It receives:

nums:
The list of numbers.

k:
The size of the sliding window.

It returns:

A list containing the maximum number from every window.


STEP 1:

if not nums or k <= 0 or k > len(nums):
    return []


Let's understand every part.


if:

Checks whether a condition is true.


not nums:

Checks whether nums is empty.

Example:

nums = []

This condition is True.


k <= 0:

Checks whether k is zero or negative.

A window cannot have zero or negative size.


k > len(nums):

Checks whether the window is bigger than the array.

Example:

nums = [1, 2, 3]
k = 5

We cannot create a window of five numbers
from an array containing only three numbers.


or:

Means at least one condition must be True.


return []:

Returns an empty list.

We stop because the input is invalid.


STEP 2:

n = len(nums)


What does this do?

len(nums) counts how many numbers are inside nums.

Example:

nums = [1, 3, -1, -3, 5, 3, 6, 7]

len(nums) = 8

Therefore:

n = 8


Why do we need n?

We use it to control the loop.

We also use it to calculate the result size.


STEP 3:

result = [0] * (n - k + 1)


What does this do?

Creates a list with enough spaces for all answers.

Let's understand it.


n = 8
k = 3


Calculation:

n - k + 1

8 - 3 + 1 = 6


Therefore:

result = [0, 0, 0, 0, 0, 0]


Why six?

Because an array of eight numbers has six
possible windows of size three.

Example:

[1, 3, -1]
[3, -1, -3]
[-1, -3, 5]
[-3, 5, 3]
[5, 3, 6]
[3, 6, 7]

There are six windows.

Therefore, we need six answer spaces.


STEP 4:

deque_indices = deque()


What does this do?

Creates an empty deque.

IMPORTANT:

We store INDICES inside this deque.

We do not store the actual numbers.

Example:

nums = [1, 3, -1]

Index:

0  1   2

Value:

1  3  -1


If:

deque_indices = [1, 2]

It means:

We are storing index 1 and index 2.

Their values are:

nums[1] = 3
nums[2] = -1


Why store indices?

Because we need to know:

1. The value of each number.
2. Where each number is located.
3. Whether an index is outside the current window.


STEP 5:

for i in range(n):


What does this mean?

We visit every index in nums.

range(n) produces:

0, 1, 2, 3, 4, 5, 6, 7

If n = 8.

i represents the current index.

Example:

When i = 0:

nums[i] = nums[0] = 1

When i = 1:

nums[i] = nums[1] = 3

When i = 2:

nums[i] = nums[2] = -1


STEP 6:

while deque_indices and deque_indices[0] < i - k + 1:


This is one of the most important lines.


First part:

deque_indices


Checks whether the deque contains anything.

An empty deque is treated as False.

A deque with elements is treated as True.

We cannot remove an element from an empty deque.


Second part:

deque_indices[0]


Gets the first element of the deque.

Remember:

The deque stores indices.

Therefore, deque_indices[0] is the oldest index
currently stored at the front.


Third part:

i - k + 1


Calculates the beginning index of the current window.

Example:

i = 4
k = 3

Calculation:

4 - 3 + 1 = 2

The current window starts at index 2.


Therefore:

deque_indices[0] < i - k + 1


Checks whether the first stored index is outside
the current window.

If it is outside, we must remove it.


deque_indices.popleft()


What does this do?

Removes the first element from the deque.

Example:

Before:

[0, 2, 3]

After popleft():

[2, 3]


Why?

Because index 0 is no longer inside the current window.


STEP 7:

while (deque_indices and
       nums[deque_indices[-1]] < nums[i]):


This is another very important part.


First:

deque_indices


Checks whether the deque is empty.


Second:

deque_indices[-1]


Gets the last index in the deque.

IMPORTANT:

- deque_indices[0] means the first index.
- deque_indices[-1] means the last index.


Third:

nums[deque_indices[-1]]


Gets the actual number at the last stored index.


Example:

nums = [2, 5]

deque_indices = [0]

Then:

deque_indices[-1] = 0

nums[deque_indices[-1]] = nums[0] = 2


Fourth:

nums[i]


Gets the current number we are processing.

Example:

i = 1

nums[i] = nums[1] = 5


The comparison:

nums[deque_indices[-1]] < nums[i]


Means:

Is the last stored number smaller than the
current number?


Example:

2 < 5

True.


Why do we remove the smaller number?

Because the new number is bigger.

The new number is also further to the right.

So the smaller old number cannot be the maximum
in any future window that contains the new number.

We do not need to keep it.


deque_indices.pop()


What does this do?

Removes the last element from the deque.

Example:

Before:

[0]

After pop():

[]


IMPORTANT DIFFERENCE:

popleft() removes from the FRONT.

pop() removes from the BACK.


STEP 8:

deque_indices.append(i)


What does this do?

Adds the current index to the end of the deque.

Example:

i = 3

Before:

[1, 2]

After:

[1, 2, 3]


Why add the index?

Because the current number may become the maximum
in this window or a future window.


STEP 9:

if i >= k - 1:


What does this mean?

We only save an answer after the first complete
window has been formed.


Example:

k = 3

The first window needs three numbers.

Their indices are:

0, 1, 2


When i = 0:

We have one number.

Not enough.


When i = 1:

We have two numbers.

Not enough.


When i = 2:

We have three numbers.

The first complete window is ready.


Therefore:

i >= k - 1

When:

i >= 2

We can start saving answers.


STEP 10:

result[i - k + 1] = nums[deque_indices[0]]


This line saves the maximum number.


Let's understand it.


deque_indices[0]

Gets the index at the FRONT of the deque.

Why?

Because the deque keeps its values in decreasing order.

The biggest value is always at the front.


nums[deque_indices[0]]

Uses that index to get the actual maximum number.


Example:

nums = [1, 3, -1]

deque_indices = [1, 2]

The front index is:

deque_indices[0] = 1

The actual number is:

nums[1] = 3

Therefore, the maximum is 3.


Now:

i - k + 1


Calculates where to save the answer.

Example:

i = 2
k = 3

2 - 3 + 1 = 0

Therefore:

result[0] = 3


For the next window:

i = 3
k = 3

3 - 3 + 1 = 1

Therefore:

result[1] = maximum of the second window.


STEP 11:

return result


What does this do?

Returns the completed list of maximum numbers.

Example:

[3, 3, 5, 5, 6, 7]


6. COMPLETE DRY RUN
--------------------------------------------------------

Let's follow the algorithm step by step.

INPUT:

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3


Initial values:

n = 8

result = [0, 0, 0, 0, 0, 0]

deque_indices = []


IMPORTANT:

The deque stores indices.

We will show both the indices and their values.


--------------------------------------------------------
ITERATION 1
--------------------------------------------------------

i = 0

Current number:

nums[0] = 1


STEP A:

Remove indices outside the window.

No indices exist.

Nothing happens.


STEP B:

Remove smaller numbers from the back.

The deque is empty.

Nothing happens.


STEP C:

Add current index.

deque_indices = [0]

Values:

[1]


STEP D:

Check:

i >= k - 1

0 >= 2

False.

We do not save an answer yet.


--------------------------------------------------------
ITERATION 2
--------------------------------------------------------

i = 1

Current number:

nums[1] = 3


STEP A:

Remove expired indices.

Nothing happens.


STEP B:

Compare the last value with current value.

Last value = 1

Current value = 3

1 < 3

True.

Remove index 0.


Deque:

[]


STEP C:

Add current index 1.

Deque indices:

[1]

Values:

[3]


STEP D:

Check:

1 >= 2

False.

No answer yet.


--------------------------------------------------------
ITERATION 3
--------------------------------------------------------

i = 2

Current number:

nums[2] = -1


STEP A:

Remove expired indices.

Current window starts at:

i - k + 1

2 - 3 + 1 = 0

Index 1 is still inside the window.

Nothing is removed.


STEP B:

Compare last value with current value.

3 < -1

False.

Keep index 1.


STEP C:

Add current index 2.

Deque indices:

[1, 2]

Values:

[3, -1]


STEP D:

Check:

2 >= 2

True.

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

Current number:

nums[3] = -3


STEP A:

Current window starts at:

3 - 3 + 1 = 1

Deque indices:

[1, 2]

Index 1 is still valid.

Nothing is removed.


STEP B:

Compare last value with current value.

Last value = -1

Current value = -3

-1 < -3

False.

Keep index 2.


STEP C:

Add index 3.

Deque indices:

[1, 2, 3]

Values:

[3, -1, -3]


STEP D:

The window is complete.

Maximum:

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

Current number:

nums[4] = 5


STEP A:

Current window starts at:

4 - 3 + 1 = 2

Index 1 is outside the window.

Remove index 1.


Deque:

[2, 3]


STEP B:

Compare the last value with 5.

Last value = -3

-3 < 5

True.

Remove index 3.


Deque:

[2]


Compare again:

Last value = -1

-1 < 5

True.

Remove index 2.


Deque:

[]


STEP C:

Add index 4.

Deque:

[4]

Values:

[5]


STEP D:

Maximum:

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

Current number:

nums[5] = 3


STEP A:

Current window starts at:

5 - 3 + 1 = 3

Index 4 is valid.

Nothing is removed.


STEP B:

Compare:

5 < 3

False.

Keep index 4.


STEP C:

Add index 5.

Deque:

[4, 5]

Values:

[5, 3]


STEP D:

Maximum:

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

Current number:

nums[6] = 6


STEP A:

Current window starts at:

6 - 3 + 1 = 4

Index 4 is still valid.

Nothing is removed.


STEP B:

Compare the last value with 6.

3 < 6

True.

Remove index 5.


Deque:

[4]


Compare again:

5 < 6

True.

Remove index 4.


Deque:

[]


STEP C:

Add index 6.

Deque:

[6]

Values:

[6]


STEP D:

Maximum:

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

Current number:

nums[7] = 7


STEP A:

Current window starts at:

7 - 3 + 1 = 5

Index 6 is valid.

Nothing is removed.


STEP B:

Compare:

6 < 7

True.

Remove index 6.


Deque:

[]


STEP C:

Add index 7.

Deque:

[7]

Values:

[7]


STEP D:

Maximum:

nums[7] = 7


Save:

result[5] = 7


Final result:

[3, 3, 5, 5, 6, 7]


7. TIME COMPLEXITY
--------------------------------------------------------

O(N)

Where:

N = len(nums)


Why O(N)?

We visit every number once using:

for i in range(n)


But what about the two while loops?

Do they make the algorithm O(N * K)?

No.


IMPORTANT:

Every index is:

1. Added to the deque once.
2. Removed from the deque at most once.

An index can leave the deque from the front
or from the back.

It cannot be removed twice.


Therefore:

The total number of deque operations across
the entire algorithm is O(N).


Final time complexity:

O(N)


COMPARE WITH THE BRUTE FORCE APPROACH:

Brute force:

Check every number inside every window.

Time complexity:

O(N * K)


Deque solution:

Each index is added once and removed at most once.

Time complexity:

O(N)


This is why the deque solution is faster.


8. SPACE COMPLEXITY
--------------------------------------------------------

O(N) including the output list.

Let's separate the memory.


Deque:

The deque can store at most K indices.

Space:

O(K)


Result:

The result contains:

N - K + 1 numbers.

Space:

O(N - K + 1)


Total space:

O(K + N - K + 1)

Simplified:

O(N)


IMPORTANT:

If we do not count the output list,
the extra working space is O(K).

This is because the deque stores at most K indices.


9. TEST CASES
--------------------------------------------------------

Test 1:

Input:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

Expected:
[3, 3, 5, 5, 6, 7]


Test 2:

Input:
nums = [1]
k = 1

Expected:
[1]


Test 3:

Input:
nums = [1, -1]
k = 1

Expected:
[1, -1]


Test 4:

Input:
nums = [9, 11]
k = 2

Expected:
[11]


Test 5:

Input:
nums = [4, -2]
k = 2

Expected:
[4]


Test 6:

Input:
nums = [7, 2, 4]
k = 2

Expected:
[7, 4]


Test 7:

Input:
nums = [5, 5, 5, 5]
k = 2

Expected:
[5, 5, 5]


Test 8:

Input:
nums = [9, 8, 7, 6, 5]
k = 3

Expected:
[9, 8, 7]


Test 9:

Input:
nums = [-7, -8, -6, -5, -9]
k = 2

Expected:
[-7, -6, -5, -5]


Test 10:

Input:
nums = [1, 3, 1, 2, 0, 5]
k = 3

Expected:
[3, 3, 2, 5]


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a sliding window is.

[ ] I understand what the maximum means.

[ ] I understand why the window moves one position
    to the right.

[ ] I understand what a deque is.

[ ] I understand why we use collections.deque.

[ ] I understand why the deque stores indices,
    not actual numbers.

[ ] I understand deque[0].

[ ] I understand deque[-1].

[ ] I understand append().

[ ] I understand popleft().

[ ] I understand pop().

[ ] I understand why we remove expired indices.

[ ] I understand why we remove smaller values.

[ ] I understand why the largest value stays
    at the front.

[ ] I understand the expression i - k + 1.

[ ] I understand why we use i >= k - 1.

[ ] I understand how result is created.

[ ] I understand how the maximum is saved.

[ ] I understand the complete dry run.

[ ] I understand why the time complexity is O(N).

[ ] I understand why the deque uses O(K) space.

[ ] I can write this solution without looking.


========================================================
10. TESTING THE SOLUTION
========================================================
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

    # Additional edge cases
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