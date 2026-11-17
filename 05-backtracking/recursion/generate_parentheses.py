
"""
========================================================
PROBLEM: GENERATE PARENTHESES
TOPIC: STACK / BACKTRACKING / RECURSION
APPROACH: BACKTRACKING + RECURSION
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given an integer n representing the number of pairs
of parentheses:

Generate all possible combinations of well-formed
parentheses.

In simple words:

We need to generate every possible combination of
opening "(" and closing ")" parentheses.

Every combination must follow two rules:

1. Every opening parenthesis must have a matching
   closing parenthesis.

2. A closing parenthesis cannot appear before its
   matching opening parenthesis.

For example:

Valid:
((()))
(()())
(())()
()(())
()()()

Invalid:
())(
(()))
)(()

The function must return all valid combinations.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
n = 3

Output:
["((()))", "(()())", "(())()", "()(())", "()()()"]

Explanation:

We have 3 pairs of parentheses.

We must generate all possible valid combinations.

There are 5 valid combinations.

Therefore:
Output = ["((()))", "(()())", "(())()", "()(())", "()()()"]


Example 2:

Input:
n = 1

Output:
["()"]

Explanation:

We have only one pair.

There is only one valid combination.

Therefore:
Output = ["()"]


Example 3:

Input:
n = 2

Output:
["(())", "()()"]

Explanation:

We have 2 opening parentheses and 2 closing parentheses.

There are only 2 valid combinations.

Therefore:
Output = ["(())", "()()"]


3. MY APPROACH: BACKTRACKING + RECURSION
--------------------------------------------------------

I use:

1. A LIST CALLED result
2. A LIST CALLED current
3. RECURSION
4. TWO COUNTERS

The two counters are:

open_count:
Counts how many opening parentheses "(" we have added.

close_count:
Counts how many closing parentheses ")" we have added.


MY STEPS:

1. Create an empty list called result.

2. Create an empty list called current.

3. Create a recursive function called backtrack().

4. Check whether the current combination contains
   exactly 2 * n characters.

5. If it does:
   - Convert current into a string.
   - Add that string to result.
   - Stop that recursive path.

6. If open_count < n:
   - Add "(" to current.
   - Call backtrack() again.
   - Increase open_count by 1.
   - Remove the last character using pop().

7. If close_count < open_count:
   - Add ")" to current.
   - Call backtrack() again.
   - Increase close_count by 1.
   - Remove the last character using pop().

8. Start recursion with:
   open_count = 0
   close_count = 0

9. Return result.


THE TWO DECISIVE CONDITIONS:

CONDITION 1:

open_count < n

We can add an opening parenthesis only when
we have not used all n opening parentheses.


CONDITION 2:

close_count < open_count

We can add a closing parenthesis only when
there is an unmatched opening parenthesis.

These two conditions prevent invalid combinations
before they are created.


4. PYTHON SOLUTION
--------------------------------------------------------
"""


class Solution:

    def generateParenthesis(self, n: int) -> list[str]:

        # Store all completed valid combinations
        result = []

        # Build the current combination
        current = []

        # Recursive backtracking function
        def backtrack(open_count: int, close_count: int):

            # Check whether the combination is complete
            if len(current) == 2 * n:

                # Convert the character list into a string
                result.append("".join(current))

                # Stop this recursive path
                return

            # Check whether we can add an opening parenthesis
            if open_count < n:

                # Make the choice
                current.append("(")

                # Explore this choice
                backtrack(open_count + 1, close_count)

                # Undo the choice
                current.pop()

            # Check whether we can add a closing parenthesis
            if close_count < open_count:

                # Make the choice
                current.append(")")

                # Explore this choice
                backtrack(open_count, close_count + 1)

                # Undo the choice
                current.pop()

        # Start with zero opening and zero closing parentheses
        backtrack(0, 0)

        # Return all valid combinations
        return result


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------


class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def generateParenthesis(self, n: int) -> list[str]:

Creates a function that generates valid parentheses.

self:
Refers to the current object of the class.

n:
The number of pairs of parentheses.

int:
Means n is expected to be an integer.

list[str]:
Means the function returns a list of strings.


result = []

Creates an empty list.

We use result to store all completed valid combinations.

Example:

[
    "((()))",
    "(()())",
    "(())()"
]

Every time we find a complete valid combination,
we save it inside result.


current = []

Creates an empty list.

We use current to build one combination at a time.

Example:

current = ["(", "(", ")"]

This represents:

"(()"

IMPORTANT:

result stores completed answers.

current stores the combination we are currently building.

We use a list because Python lists can be changed.

We can add characters using append()
and remove characters using pop().


def backtrack(open_count: int, close_count: int):

Creates a recursive function.

This function builds the parentheses combination
one character at a time.

It receives two counters.


open_count:

Counts how many opening parentheses "("
we have added so far.

Example:

current = ["(", "("]

open_count = 2


close_count:

Counts how many closing parentheses ")"
we have added so far.

Example:

current = ["(", "(", ")"]

close_count = 1


THE BASE CASE:

if len(current) == 2 * n:

Checks whether we have built a complete combination.

Why 2 * n?

Because every valid combination must contain:

n opening parentheses
+
n closing parentheses

Total characters = 2 * n

Example:

n = 3

Total characters = 6

A complete combination must contain 6 characters.


result.append("".join(current))

First:

"".join(current)

Combines all characters inside current
into one string.

Example:

current = ["(", "(", ")", ")"]

"".join(current) produces:

"(())"

Then:

result.append("(())")

Adds the completed combination to result.


return

Stops the current recursive call.

Why?

Because we have already created one complete answer.

We do not need to add more characters to it.


THE OPENING PARENTHESIS CONDITION:

if open_count < n:

Checks whether we have used fewer than n
opening parentheses.

Example:

n = 3

open_count = 0

0 < 3 is True.

We can add "(".


If:

open_count = 3

3 < 3 is False.

We cannot add another opening parenthesis.

Why?

Because we already used all 3 opening parentheses.


current.append("(")

Adds an opening parenthesis to current.

Example:

Before:

current = ["("]

After:

current = ["(", "("]

This is called making a choice.


backtrack(open_count + 1, close_count)

Calls the same function again.

This is recursion.

We added one opening parenthesis.

Therefore:

open_count increases by 1.

Example:

Before:

open_count = 1
close_count = 0

Next call:

backtrack(2, 0)

We now have two opening parentheses
and zero closing parentheses.


current.pop()

Removes the last character from current.

Example:

Before:

current = ["(", "("]

After:

current = ["("]

Why do we remove it?

Because we have finished exploring the path
where we added that opening parenthesis.

Now we return to the previous state.

We can then explore another possible choice.

This is called BACKTRACKING.

IMPORTANT:

append() makes a choice.

backtrack() explores the choice.

pop() undoes the choice.


THE CLOSING PARENTHESIS CONDITION:

if close_count < open_count:

This is the most important condition
for keeping the combinations valid.

It checks whether we have more opening parentheses
than closing parentheses.

Why?

Every closing parenthesis must have
an unmatched opening parenthesis before it.

Example:

current = ["(", "("]

open_count = 2
close_count = 0

Check:

0 < 2

True.

We can safely add ")".


Another example:

current = ["(", ")"]

open_count = 1
close_count = 1

Check:

1 < 1

False.

We cannot add another closing parenthesis.

Why?

There is no unmatched opening parenthesis.

Adding ")" would produce:

"())"

This is invalid.


current.append(")")

Adds a closing parenthesis to current.

Example:

Before:

current = ["(", "("]

After:

current = ["(", "(", ")"]


backtrack(open_count, close_count + 1)

Calls the recursive function again.

We added one closing parenthesis.

Therefore:

close_count increases by 1.

Example:

Before:

open_count = 2
close_count = 0

Next call:

backtrack(2, 1)


current.pop()

Removes the last closing parenthesis.

This restores the previous state.

Now the algorithm can explore another path.


START THE RECURSION:

backtrack(0, 0)

Starts the process.

At the beginning:

open_count = 0
close_count = 0
current = []

We have not added any parentheses yet.


return result

Returns all completed valid combinations.


6. THE DECISIVE LOGIC BEHIND THIS PROBLEM
--------------------------------------------------------

There are two important conditions.


CONDITION 1:

open_count < n

PURPOSE:

Prevents us from adding too many opening parentheses.

Example:

n = 3

We can add "(" when:

open_count = 0
open_count = 1
open_count = 2

We cannot add another when:

open_count = 3


CONDITION 2:

close_count < open_count

PURPOSE:

Prevents us from adding a closing parenthesis
without an unmatched opening parenthesis.

Example:

Current:

"(("

open_count = 2
close_count = 0

We can add ")".

But:

Current:

"()"

open_count = 1
close_count = 1

We cannot add another ")".


WHY ARE THESE CONDITIONS ENOUGH?

Condition 1 guarantees that we never use
more than n opening parentheses.

Condition 2 guarantees that we never have
more closing parentheses than opening parentheses
at any point.

When the combination reaches 2 * n characters:

- We have used n opening parentheses.
- We have used n closing parentheses.
- Every closing parenthesis has a matching opening one.

Therefore, the combination is valid.

IMPORTANT:

We do not generate invalid combinations
and then check them.

We prevent invalid choices before making them.

This is the decisive idea behind this solution.


7. DRY RUN: n = 2
--------------------------------------------------------

Input:

n = 2

We need:

2 opening parentheses
2 closing parentheses

Total characters = 4


INITIAL STATE:

current = []

open_count = 0
close_count = 0


STEP 1:

Check:

open_count < n

0 < 2 = True

Add "(".

current = ["("]

open_count = 1
close_count = 0


STEP 2:

Check:

open_count < n

1 < 2 = True

Add another "(".

current = ["(", "("]

open_count = 2
close_count = 0


STEP 3:

Check opening condition:

2 < 2 = False

We cannot add another "(".

Check closing condition:

0 < 2 = True

We can add ")".

current = ["(", "(", ")"]

open_count = 2
close_count = 1


STEP 4:

Check closing condition:

1 < 2 = True

Add another ")".

current = ["(", "(", ")", ")"]

open_count = 2
close_count = 2


STEP 5:

Check the base case:

len(current) == 2 * n

4 == 4 = True

Convert current into a string:

"(())"

Add it to result.

result = ["(())"]


STEP 6: BACKTRACK

The algorithm returns to the previous state.

It removes the last ")" using pop().

Then it continues returning through earlier calls
until it reaches:

current = ["("]

Now it explores another possible choice.


STEP 7:

Add ")".

current = ["(", ")"]

open_count = 1
close_count = 1

Now we can add "(" because:

1 < 2 = True


STEP 8:

Add "(".

current = ["(", ")", "("]

open_count = 2
close_count = 1

Now we can add ")" because:

1 < 2 = True


STEP 9:

Add ")".

current = ["(", ")", "(", ")"]

open_count = 2
close_count = 2

The combination is complete.

Save:

"()()"


FINAL RESULT:

result = ["(())", "()()"]


8. WHY DO WE USE APPEND() AND POP()?
--------------------------------------------------------

This is the main backtracking pattern.

Example:

current.append("(")

backtrack(open_count + 1, close_count)

current.pop()


The three operations have different purposes:


append():

Makes a choice.

Adds a character to the current combination.


backtrack():

Explores the choice.

Calls the recursive function to continue
building the combination.


pop():

Undoes the choice.

Removes the last character and restores
the previous combination.


WHY IS THIS IMPORTANT?

We use one shared current list.

We do not need to create a completely new list
for every possible combination.

We make a choice, explore it, and undo it.

This saves working memory.


9. EDGE CASES
--------------------------------------------------------

Test 1:

Input:
n = 1

Expected:
["()"]

Reason:

Only one pair exists.


Test 2:

Input:
n = 2

Expected:
["(())", "()()"]

Reason:

There are two valid combinations.


Test 3:

Input:
n = 3

Expected:
[
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]

Reason:

There are five valid combinations.


Test 4:

Input:
n = 4

Expected:
14 valid combinations.

Reason:

Every additional pair creates more possible
valid combinations.


10. TIME COMPLEXITY
--------------------------------------------------------

O(n * C(n))

Where:

n = Number of pairs of parentheses.

C(n) = Number of valid combinations.

C(n) is the nth Catalan number.

Formula:

C(n) = (1 / (n + 1)) * (2n choose n)


WHY?


1. GENERATING THE COMBINATIONS

The algorithm explores possible choices
using backtracking.

It produces exactly C(n) valid combinations.

2. BUILDING EACH FINAL STRING

Every completed combination contains 2 * n characters.

Converting current into a string using:

"".join(current)

takes O(n) time.

3. SAVING THE ANSWERS

We save C(n) strings.

Each string contains 2 * n characters.

Therefore:

C(n) * O(n)

= O(n * C(n))


TOTAL TIME COMPLEXITY:

O(n * C(n))


IMPORTANT:

We cannot avoid generating all valid combinations.

The problem asks us to return every valid combination.

The number of answers grows quickly as n increases.


11. SPACE COMPLEXITY
--------------------------------------------------------

There are two types of space to understand.


1. AUXILIARY SPACE: O(n)

This is the extra working memory used
while generating the combinations.

CURRENT LIST:

The current list contains at most 2 * n characters.

Therefore:

O(n)


RECURSION STACK:

Each recursive call adds one character.

The maximum recursion depth is 2 * n.

Therefore:

O(n)


Total auxiliary space:

O(n)


2. OUTPUT SPACE: O(n * C(n))

The result list stores all valid combinations.

There are C(n) combinations.

Each combination contains 2 * n characters.

Therefore:

Output space = O(n * C(n))


TOTAL SPACE COMPLEXITY:

Including the returned output:

O(n * C(n))


Excluding the returned output:

O(n)


IMPORTANT:

When discussing space complexity,
always explain whether the output is included.


12. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
n = 1

Expected:
["()"]

Reason:
Only one pair exists.


Test 2:

Input:
n = 2

Expected:
["(())", "()()"]

Reason:
There are two valid combinations.


Test 3:

Input:
n = 3

Expected:
[
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]

Reason:
There are five valid combinations.


Test 4:

Input:
n = 4

Expected:
14 valid combinations.

Reason:
There are fourteen valid combinations.


Test 5:

Input:
n = 5

Expected:
42 valid combinations.

Reason:
There are forty-two valid combinations.


Test 6:

Input:
n = 0

Expected:
[""]

Reason:
There are no parentheses to add.

The empty combination is the only possible result.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what backtracking means.
[ ] I understand what recursion means.
[ ] I understand why we use result.
[ ] I understand why we use current.
[ ] I understand what open_count represents.
[ ] I understand what close_count represents.
[ ] I understand why we use open_count < n.
[ ] I understand why we use close_count < open_count.
[ ] I understand the base case.
[ ] I understand why we use 2 * n.
[ ] I understand what append() does.
[ ] I understand what pop() does.
[ ] I understand why we use "".join(current).
[ ] I understand how recursion explores different paths.
[ ] I understand why we undo choices.
[ ] I can explain the decisive logic in an interview.
[ ] I understand O(n * C(n)) time complexity.
[ ] I understand O(n) auxiliary space.
[ ] I understand O(n * C(n)) output space.
[ ] I can write this solution without looking.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    (1, ["()"]),

    (2, ["(())", "()()"]),

    (3, [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]),

    (4, [
        "(((())))",
        "((()()))",
        "((())())",
        "((()))()",
        "(()(()))",
        "(()()())",
        "(()())()",
        "(())(())",
        "(())()()",
        "()((()))",
        "()(())()",
        "()()(())",
        "()()()()",
        "()(()())"
    ]),

    (5, None),

    (0, [""])
]

passed = 0

print("GENERATE PARENTHESES - TEST RESULTS")
print("-----------------------------------")

for n, expected in test_cases:

    result = solution.generateParenthesis(n)

    # Sort both lists because output order does not matter
    actual_sorted = sorted(result)

    if expected is None:
        # For n = 5, check the number of valid combinations
        test_passed = len(result) == 42
    else:
        expected_sorted = sorted(expected)
        test_passed = actual_sorted == expected_sorted

    print("Input:", n)
    print("Expected:", expected if expected is not None else "42 combinations")
    print("Actual:", result)

    if test_passed:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("-----------------------------------")


print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
