
"""
========================================================
PROBLEM: DAILY TEMPERATURES
TOPIC: STACK
APPROACH: MONOTONIC DECREASING STACK
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given an integer array called temperatures:

Return an array called answer.

For every day i:

answer[i] represents the number of days we must wait
after day i to find a warmer temperature.

If there is no future day with a warmer temperature,
answer[i] must be 0.

In simple words:

For every temperature, find the next warmer temperature
that appears somewhere after it.

Then calculate how many days separate those two days.

IMPORTANT:

A warmer temperature must be STRICTLY GREATER.

An equal temperature does not count as warmer.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

Output:
[1, 1, 4, 2, 1, 1, 0, 0]

Explanation:

Day 0:
Temperature = 73.
The next warmer temperature is 74 on day 1.
Wait = 1 day.

Day 1:
Temperature = 74.
The next warmer temperature is 75 on day 2.
Wait = 1 day.

Day 2:
Temperature = 75.
The next warmer temperature is 76 on day 6.
Wait = 4 days.

Day 3:
Temperature = 71.
The next warmer temperature is 72 on day 5.
Wait = 2 days.

Day 4:
Temperature = 69.
The next warmer temperature is 72 on day 5.
Wait = 1 day.

Day 5:
Temperature = 72.
The next warmer temperature is 76 on day 6.
Wait = 1 day.

Day 6:
Temperature = 76.
There is no warmer future temperature.
Answer = 0.

Day 7:
Temperature = 73.
There is no future day.
Answer = 0.


Example 2:

Input:
temperatures = [30, 40, 50, 60]

Output:
[1, 1, 1, 0]

Explanation:

30 waits 1 day for 40.
40 waits 1 day for 50.
50 waits 1 day for 60.
60 has no warmer future day.


Example 3:

Input:
temperatures = [30, 60, 90]

Output:
[1, 1, 0]

Explanation:

30 waits 1 day for 60.
60 waits 1 day for 90.
90 has no warmer future day.


Example 4:

Input:
temperatures = [90, 80, 70, 60]

Output:
[0, 0, 0, 0]

Explanation:

Every future temperature is colder.

No day has a warmer future temperature.


3. MY APPROACH: MONOTONIC STACK
--------------------------------------------------------

I use one main data structure:

1. STACK

A stack stores the indices of days that are still
waiting for a warmer temperature.

IMPORTANT:

We store INDICES, not temperatures.

Why?

Because we need to know:

1. The temperature of each waiting day.
2. The position of that day in the input list.

We can get the temperature using:

temperatures[index]

We can calculate the waiting days using:

current_index - previous_index


MY STEPS:

1. Find the length of the temperatures list.

2. Create an answer list filled with zeros.

3. Create an empty stack.

4. Visit every day using a for loop.

5. Check whether the stack is not empty.

6. Compare today's temperature with the temperature
   belonging to the index at the top of the stack.

7. If today's temperature is warmer:

   a. Remove the previous index from the stack.
   b. Calculate the number of waiting days.
   c. Store that number in the answer list.

8. Continue checking the stack using while.

9. When no more waiting days can be solved,
   push today's index onto the stack.

10. Continue until every day has been processed.

11. Return the answer list.


WHY DO WE USE A MONOTONIC STACK?

A monotonic stack keeps its stored values in a
consistent order.

In this problem, the stack stores indices whose
temperatures are in decreasing order from the
bottom of the stack to the top.

Example:

temperatures = [75, 71, 69]

stack = [0, 1, 2]

The temperatures represented by those indices are:

[75, 71, 69]

They are decreasing.

When a warmer temperature arrives, we remove the
previous days that are colder than today's temperature.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        # Find the total number of days
        n = len(temperatures)

        # Create an answer list filled with zeros
        answer = [0] * n

        # Create an empty stack to store day indices
        stack = []

        # Visit every day in the temperatures list
        for i in range(n):

            # Check whether today's temperature is warmer
            # than the temperature at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:

                # Remove the previous day index from the stack
                index = stack.pop()

                # Calculate how many days we waited
                answer[index] = i - index

            # Add today's index to the stack
            stack.append(i)

        # Return the completed answer list
        return answer


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------


class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.

We put our solution function inside this class.


def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

Creates a function called dailyTemperatures.

self:
Refers to the current object of the class.

temperatures:
The input list containing daily temperatures.

list[int]:
Means that temperatures is a list of integers.

-> list[int]:
Means that the function returns a list of integers.

Example:

temperatures = [73, 74, 75, 71]


--------------------------------------------------------
A. FIND THE NUMBER OF DAYS
--------------------------------------------------------

n = len(temperatures)

len() is a Python function that counts the number
of elements inside a list.

Example:

temperatures = [73, 74, 75, 71]

len(temperatures) = 4

Therefore:

n = 4

Why do we need n?

We need to know how many days we must process.

The indices are:

0, 1, 2, 3


--------------------------------------------------------
B. CREATE THE ANSWER LIST
--------------------------------------------------------

answer = [0] * n

Creates a list containing n zeros.

Example:

n = 4

answer = [0] * 4

Result:

answer = [0, 0, 0, 0]

Why do we start with zeros?

Because the problem says:

If there is no warmer future temperature,
the answer must be zero.

We only change a zero when we find a warmer day.

IMPORTANT:

Each position in answer belongs to the same day
as the corresponding position in temperatures.

For example:

temperatures[2] belongs to day 2.

answer[2] stores the waiting days for day 2.


--------------------------------------------------------
C. CREATE THE STACK
--------------------------------------------------------

stack = []

Creates an empty Python list.

We use this list as a stack.

A stack follows the LIFO principle.

LIFO means:

LAST IN, FIRST OUT.

Think about a pile of plates:

The last plate you put on top is the first plate
you remove.

Python lists provide stack operations:

append() = Push an element onto the stack.

pop() = Remove the last element from the stack.

IMPORTANT:

We store day INDICES inside the stack.

We do not directly store temperatures.

Example:

temperatures = [75, 71, 69]

stack = [0, 1, 2]

This means:

Index 0 represents temperature 75.
Index 1 represents temperature 71.
Index 2 represents temperature 69.

Why store indices?

Because we need to calculate the number of days
between the previous day and the current day.

We also need the index to access its temperature.


--------------------------------------------------------
D. VISIT EVERY DAY
--------------------------------------------------------

for i in range(n):

A for loop repeats code for every index.

range(n) generates numbers from 0 up to n - 1.

Example:

n = 4

range(4) gives:

0, 1, 2, 3

Therefore, the loop visits:

i = 0
i = 1
i = 2
i = 3

Here:

i represents the current day.

We use i to access today's temperature:

temperatures[i]


--------------------------------------------------------
E. CHECK WHETHER TODAY IS WARMER
--------------------------------------------------------

while stack and temperatures[i] > temperatures[stack[-1]]:

THIS IS THE MOST IMPORTANT LINE IN THE ALGORITHM.

Let's divide it into three parts.


PART 1: stack

stack

Checks whether the stack is not empty.

In Python:

An empty list is False.

A non-empty list is True.

Example:

stack = []

bool(stack) = False

stack = [0, 1]

bool(stack) = True

Why check this?

Because we cannot access the top element of an
empty stack.

The condition prevents us from trying to access
an element that does not exist.


PART 2: stack[-1]

stack[-1]

Gets the last element of the stack.

In Python, index -1 means the last element.

Example:

stack = [0, 1, 2]

stack[-1] = 2

The top of our stack is index 2.

Remember:

The stack stores indices, not temperatures.


PART 3: temperatures[stack[-1]]

temperatures[stack[-1]]

Uses the index at the top of the stack to get
the temperature belonging to that day.

Example:

temperatures = [75, 71, 69]

stack = [0, 1, 2]

stack[-1] = 2

temperatures[stack[-1]] = temperatures[2]

Result:

69


PART 4: temperatures[i]

temperatures[i]

Gets today's temperature.

Example:

temperatures = [75, 71, 69, 80]

When i = 3:

temperatures[i] = 80


PART 5: COMPARE THE TWO TEMPERATURES

temperatures[i] > temperatures[stack[-1]]

Asks:

Is today's temperature strictly greater than
the temperature at the top of the stack?

Example:

Today's temperature = 80.

Top stack temperature = 69.

Comparison:

80 > 69

Result:

True.

We found a warmer future day for that previous day.


WHY DO WE USE WHILE INSTEAD OF IF?

This is very important.

One current temperature can be warmer than
several previous temperatures.

Example:

temperatures = [70, 65, 60, 80]

Before reaching 80:

stack = [0, 1, 2]

The current temperature is 80.

80 is warmer than:

60
65
70

Therefore, we must solve all three previous days.

A single if statement would only solve one day.

A while loop continues checking until no more
previous days can be solved.


WHY DO WE USE > INSTEAD OF >=?

The problem requires a STRICTLY warmer temperature.

Example:

temperatures = [70, 70]

The second temperature is equal to the first.

It is not warmer.

Therefore:

70 > 70 is False.

Both answer positions remain zero.

Using >= would incorrectly treat equal temperatures
as warmer.


--------------------------------------------------------
F. REMOVE THE PREVIOUS DAY FROM THE STACK
--------------------------------------------------------

index = stack.pop()

pop() removes the last element from the stack.

It also returns the removed element.

We save that returned index inside a variable
called index.

Example:

stack = [0, 1, 2]

index = stack.pop()

After this operation:

index = 2

stack = [0, 1]

Why remove it?

Because we have found a warmer future temperature
for that previous day.

That day no longer needs to wait.

We can now calculate its answer.


--------------------------------------------------------
G. CALCULATE THE WAITING DAYS
--------------------------------------------------------

answer[index] = i - index

This calculates how many days separate:

i:
The current warmer day.

index:
The previous day waiting for warmer weather.

Example:

index = 2
i = 6

Calculation:

answer[2] = 6 - 2

answer[2] = 4

This means:

The person on day 2 must wait 4 days to get
a warmer temperature.

Why subtract the indices?

Because every index represents one day.

The difference between two day indices gives
the number of days between them.

Another example:

index = 3
i = 5

answer[3] = 5 - 3

answer[3] = 2

The waiting time is 2 days.


--------------------------------------------------------
H. ADD TODAY'S INDEX TO THE STACK
--------------------------------------------------------

stack.append(i)

append() adds an element to the end of a list.

Here, we add today's index to the stack.

Example:

i = 4

stack.append(i)

If the stack was:

stack = [1, 2]

It becomes:

stack = [1, 2, 4]

Why do we add today's index?

Because today's temperature may need to wait
for a warmer temperature in the future.

We keep it in the stack until:

1. A warmer temperature appears and solves it.

OR

2. The algorithm finishes without finding
   a warmer future temperature.


--------------------------------------------------------
I. RETURN THE ANSWER
--------------------------------------------------------

return answer

Returns the completed answer list.

Every day that found a warmer future day has
its waiting time stored in answer.

Every day that did not find a warmer future day
still has zero.

Why?

Because we initialized every answer position
with zero.

If an index remains in the stack after the loop,
its answer stays zero.

That is exactly what the problem requires.


6. COMPLETE DRY RUN
--------------------------------------------------------

Let's use this input:

temperatures = [73, 74, 75, 71, 72]

There are 5 days.

INITIAL STATE:

n = 5

answer = [0, 0, 0, 0, 0]

stack = []


ITERATION 1:

i = 0

Today's temperature:

temperatures[0] = 73

The stack is empty.

There is no previous day to compare.

Push index 0:

stack = [0]

answer = [0, 0, 0, 0, 0]


ITERATION 2:

i = 1

Today's temperature:

temperatures[1] = 74

Stack:

stack = [0]

Top index:

stack[-1] = 0

Previous temperature:

temperatures[0] = 73

Compare:

74 > 73

True.

A warmer day is found.

Pop index 0:

index = 0

stack = []

Calculate:

answer[0] = 1 - 0

answer[0] = 1

Push today's index:

stack = [1]

answer = [1, 0, 0, 0, 0]


ITERATION 3:

i = 2

Today's temperature:

temperatures[2] = 75

Stack:

stack = [1]

Top index:

stack[-1] = 1

Previous temperature:

temperatures[1] = 74

Compare:

75 > 74

True.

Pop index 1:

index = 1

Calculate:

answer[1] = 2 - 1

answer[1] = 1

Push today's index:

stack = [2]

answer = [1, 1, 0, 0, 0]


ITERATION 4:

i = 3

Today's temperature:

temperatures[3] = 71

Stack:

stack = [2]

Top index:

stack[-1] = 2

Previous temperature:

temperatures[2] = 75

Compare:

71 > 75

False.

There is no warmer temperature for day 2 yet.

Push today's index:

stack = [2, 3]

answer = [1, 1, 0, 0, 0]


ITERATION 5:

i = 4

Today's temperature:

temperatures[4] = 72

Stack:

stack = [2, 3]

Top index:

stack[-1] = 3

Previous temperature:

temperatures[3] = 71

Compare:

72 > 71

True.

Pop index 3:

index = 3

Calculate:

answer[3] = 4 - 3

answer[3] = 1

Stack:

stack = [2]

Now check the while condition again.

Top index:

stack[-1] = 2

Previous temperature:

temperatures[2] = 75

Compare:

72 > 75

False.

Stop the while loop.

Push today's index:

stack = [2, 4]

Final answer:

answer = [1, 1, 0, 1, 0]


FINAL RESULT:

[1, 1, 0, 1, 0]

IMPORTANT:

Indices 2 and 4 remain in the stack.

They have no warmer future temperature.

Their answers remain zero.


7. WHY THIS IS A MONOTONIC DECREASING STACK
--------------------------------------------------------

A monotonic stack keeps its stored values in
a particular order.

In Daily Temperatures, we store indices.

The temperatures represented by those indices
remain in decreasing order from bottom to top.

Example:

temperatures = [75, 71, 69]

stack = [0, 1, 2]

The actual temperatures are:

temperatures[0] = 75
temperatures[1] = 71
temperatures[2] = 69

Therefore:

[75, 71, 69]

This is decreasing order.

Now suppose the next temperature is 80.

80 is greater than 69.

We pop index 2.

80 is greater than 71.

We pop index 1.

80 is greater than 75.

We pop index 0.

The stack becomes empty.

Then we push the current index.

WHY IS THIS USEFUL?

Without a stack, we might repeatedly search the
future days for every temperature.

That can require O(N²) time.

With a monotonic stack, every index is pushed
once and popped at most once.

This gives us O(N) time.


8. TIME COMPLEXITY
--------------------------------------------------------

O(N)

Where:

N = Total number of elements in temperatures.

Why?

There are two main operations involving the stack.


1. FOR LOOP

for i in range(n):

The loop visits every day exactly once.

If there are N temperatures:

The loop runs N times.

Time complexity = O(N)


2. STACK OPERATIONS

stack.append(i)

Every index is pushed onto the stack exactly once.

Therefore:

Total pushes = N


stack.pop()

Every index can be removed from the stack
at most once.

Therefore:

Total pops <= N


IMPORTANT:

The while loop is inside the for loop.

At first, this may look like O(N²).

But it is NOT O(N²).

Why?

Because every index can only be pushed once
and popped once.

The while loop does not repeatedly remove
the same index.

Across the entire algorithm:

Maximum pushes = N
Maximum pops = N

Total stack operations are proportional to N.

Therefore:

TIME COMPLEXITY = O(N)


9. SPACE COMPLEXITY
--------------------------------------------------------

O(N)

Where:

N = Total number of elements in temperatures.


1. ANSWER LIST

answer = [0] * n

The answer list contains N elements.

Therefore:

Answer space = O(N)


2. STACK

stack = []

In the worst case, temperatures can always decrease.

Example:

temperatures = [90, 80, 70, 60, 50]

No previous index is removed.

The stack becomes:

[0, 1, 2, 3, 4]

Therefore:

Stack space = O(N)


TOTAL SPACE COMPLEXITY:

Answer list = O(N)

Stack = O(N)

Total = O(N) + O(N)

Therefore:

SPACE COMPLEXITY = O(N)


IMPORTANT:

This includes the returned answer list.

If we exclude the output list,
the auxiliary working space is still O(N)
because of the stack.


10. EDGE CASES
--------------------------------------------------------

EDGE CASE 1: ONLY ONE DAY

Input:
temperatures = [70]

Expected:
[0]

Reason:

There is no future day.


EDGE CASE 2: TEMPERATURES ALWAYS INCREASE

Input:
temperatures = [30, 40, 50, 60]

Expected:
[1, 1, 1, 0]

Reason:

Every day except the last finds a warmer
temperature the next day.


EDGE CASE 3: TEMPERATURES ALWAYS DECREASE

Input:
temperatures = [90, 80, 70, 60]

Expected:
[0, 0, 0, 0]

Reason:

No future temperature is warmer.


EDGE CASE 4: ALL TEMPERATURES ARE EQUAL

Input:
temperatures = [70, 70, 70]

Expected:
[0, 0, 0]

Reason:

Equal temperatures are not warmer.


EDGE CASE 5: ONE WARMER DAY SOLVES MANY DAYS

Input:
temperatures = [70, 65, 60, 80]

Expected:
[3, 2, 1, 0]

Reason:

80 is warmer than 70, 65, and 60.


EDGE CASE 6: WARMER TEMPERATURE AFTER SEVERAL DAYS

Input:
temperatures = [70, 60, 65, 80]

Expected:
[3, 2, 1, 0]

Reason:

70 waits 3 days for 80.
60 waits 2 days for 65.
65 waits 1 day for 80.


11. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

Expected:
[1, 1, 4, 2, 1, 1, 0, 0]


Test 2:

Input:
temperatures = [30, 40, 50, 60]

Expected:
[1, 1, 1, 0]


Test 3:

Input:
temperatures = [30, 60, 90]

Expected:
[1, 1, 0]


Test 4:

Input:
temperatures = [90, 80, 70, 60]

Expected:
[0, 0, 0, 0]


Test 5:

Input:
temperatures = [70, 70, 70]

Expected:
[0, 0, 0]


Test 6:

Input:
temperatures = [70]

Expected:
[0]


Test 7:

Input:
temperatures = [70, 65, 60, 80]

Expected:
[3, 2, 1, 0]


Test 8:

Input:
temperatures = [70, 60, 65, 80]

Expected:
[3, 2, 1, 0]


Test 9:

Input:
temperatures = [80, 75, 70, 85, 90]

Expected:
[3, 2, 1, 1, 0]


Test 10:

Input:
temperatures = [50, 55, 53, 60, 52, 70]

Expected:
[1, 2, 1, 2, 1, 0]


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand the Daily Temperatures problem.
[ ] I understand what a stack is.
[ ] I understand LIFO: Last In, First Out.
[ ] I understand why we store indices, not temperatures.
[ ] I understand how len() works.
[ ] I understand how [0] * n creates the answer list.
[ ] I understand how range(n) works.
[ ] I understand how a for loop visits every day.
[ ] I understand how an empty list behaves in a condition.
[ ] I understand what stack[-1] means.
[ ] I understand how temperatures[stack[-1]] works.
[ ] I understand how the while condition works.
[ ] I understand why we use while instead of if.
[ ] I understand why we use > instead of >=.
[ ] I understand what pop() does.
[ ] I understand what append() does.
[ ] I understand why we calculate i - index.
[ ] I understand why we return answer.
[ ] I understand what a Monotonic Stack is.
[ ] I understand why this stack is decreasing.
[ ] I understand why every index is pushed once.
[ ] I understand why every index is popped at most once.
[ ] I understand why time complexity is O(N).
[ ] I understand why space complexity is O(N).
[ ] I can write this solution without looking.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [

    (
        [73, 74, 75, 71, 69, 72, 76, 73],
        [1, 1, 4, 2, 1, 1, 0, 0]
    ),

    (
        [30, 40, 50, 60],
        [1, 1, 1, 0]
    ),

    (
        [30, 60, 90],
        [1, 1, 0]
    ),

    (
        [90, 80, 70, 60],
        [0, 0, 0, 0]
    ),

    (
        [70, 70, 70],
        [0, 0, 0]
    ),

    (
        [70],
        [0]
    ),

    (
        [70, 65, 60, 80],
        [3, 2, 1, 0]
    ),

    (
        [70, 60, 65, 80],
        [3, 2, 1, 0]
    ),

    (
        [80, 75, 70, 85, 90],
        [3, 2, 1, 1, 0]
    ),

    (
        [50, 55, 53, 60, 52, 70],
        [1, 2, 1, 2, 1, 0]
    )

]

passed = 0

print("DAILY TEMPERATURES - TEST RESULTS")
print("----------------------------------")

for temperatures, expected in test_cases:

    result = solution.dailyTemperatures(temperatures)

    print("Temperatures:", temperatures)
    print("Expected:    ", expected)
    print("Actual:      ", result)

    if result == expected:

        print("Status: PASS")
        passed += 1

    else:

        print("Status: FAIL")

    print("----------------------------------")


print(
    "FINAL RESULT:",
    passed,
    "/",
    len(test_cases),
    "TESTS PASSED"
)
