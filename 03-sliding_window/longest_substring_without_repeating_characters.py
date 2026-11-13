
"""
========================================================
PROBLEM: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
TOPIC: SLIDING WINDOW
APPROACH: SLIDING WINDOW + HASH SET
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given a string s:

Find the length of the longest substring that contains
no repeating characters.

In simple words:

Find the longest group of characters next to each other
where every character is different.

IMPORTANT:

A substring must contain consecutive characters.

A subsequence does not need to contain consecutive
characters.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
s = "abcabcbb"

Output:
3

Explanation:
The longest substring is "abc".

It contains 3 different characters.


Example 2:

Input:
s = "bbbbb"

Output:
1

Explanation:
Every character is the same.

The longest valid substring is "b".


Example 3:

Input:
s = "pwwkew"

Output:
3

Explanation:
The longest substring is "wke".

It contains 3 different characters.


3. MY APPROACH: SLIDING WINDOW + HASH SET
--------------------------------------------------------

I use two main ideas:

1. SLIDING WINDOW

   Uses two pointers:

   left = start of the current window.
   right = end of the current window.

2. HASH SET

   Stores the characters inside the current window.

   A set does not allow duplicate characters.

My steps:

1. Create left and right pointers.

2. Create a variable called longest.

3. Create an empty set called seen.

4. Move right through the string.

5. Get the current character.

6. Check whether the character already exists
   inside the set.

7. If it exists, remove characters from the left
   until the duplicate is gone.

8. Add the current character to the set.

9. Calculate the current window length.

10. Update the longest length if the current window
    is bigger.

11. Move right to the next character.

12. Return the longest length.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        longest = 0

        seen = set()

        while right < len(s):

            char = s[right]

            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)

            longest = max(longest, right - left + 1)

            right += 1

        return longest


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def lengthOfLongestSubstring(self, s: str) -> int:

Creates a function that finds the longest substring
without repeating characters.

self:
Refers to the current object of the class.

s:
The input string.

str:
Means the input should be a string.

-> int:
Means the function returns an integer.


left = 0

Creates the left pointer.

It marks the beginning of our current window.

Example:

s = "abcabcbb"

left = 0

The window starts at the first character.


right = 0

Creates the right pointer.

It moves through the string and finds the next
character to process.

The left and right pointers work together to create
a sliding window.


longest = 0

Stores the length of the longest valid substring
we have found so far.

At the beginning, we have not found any substring.

Therefore, longest starts at 0.


seen = set()

Creates an empty Hash Set.

A set stores unique values.

Example:

seen = set()

seen.add("a")
seen.add("b")
seen.add("a")

The set contains:

{"a", "b"}

The second "a" is not added again.

WHY DO WE NEED IT?

We need to know whether a character already exists
inside our current window.


while right < len(s):

Keeps running while right is inside the string.

len(s) gives the total number of characters.

Example:

s = "abcabcbb"

len(s) = 8

The valid indexes are:

0, 1, 2, 3, 4, 5, 6, 7

When right becomes 8, the loop stops.


char = s[right]

Gets the character at the current right position.

Example:

s = "abc"

If:

right = 0

Then:

char = "a"

If:

right = 1

Then:

char = "b"


while char in seen:

Checks whether the current character already exists
inside the set.

Example:

seen = {"a", "b", "c"}

char = "a"

The condition is True because "a" already exists.

WHY DO WE USE WHILE INSTEAD OF IF?

Because we may need to remove more than one character
from the left side before the duplicate disappears.

We keep removing characters until the duplicate
is gone.


seen.remove(s[left])

Removes the character at the left side of the window.

Example:

s = "abcabcbb"

left = 0

s[left] = "a"

Therefore:

seen.remove("a")

The character "a" is removed from the set.


left += 1

Moves the left pointer one position forward.

Example:

Before:

left = 0

After:

left = 1

We have removed the first character from our window.


seen.add(char)

Adds the current character to the set.

We do this after removing any duplicate.

Now our current window contains only unique characters.


longest = max(longest, right - left + 1)

This line calculates the current window length
and updates the longest answer.

Let's understand it.

right - left + 1

Calculates the number of characters inside the window.

Example:

left = 0
right = 2

Calculation:

2 - 0 + 1 = 3

The current window is:

"abc"

Its length is 3.


max(longest, right - left + 1)

Compares two numbers:

1. The longest length found before.
2. The current window length.

It keeps the bigger number.

Example:

longest = 2
current window length = 3

Then:

max(2, 3) = 3

Therefore:

longest = 3


right += 1

Moves the right pointer one position forward.

It allows us to process the next character.


return longest

Returns the length of the longest valid substring.

We do not return the substring itself.

We return only its length.


6. DRY RUN: "abcabcbb"
--------------------------------------------------------

Input:

s = "abcabcbb"

We start with:

left = 0
right = 0
longest = 0
seen = {}


STEP 1:

Current character = "a"

"a" is not inside seen.

Add "a".

Window = "a"

seen = {"a"}

Current length = 1

longest = 1


STEP 2:

Current character = "b"

"b" is not inside seen.

Add "b".

Window = "ab"

seen = {"a", "b"}

Current length = 2

longest = 2


STEP 3:

Current character = "c"

"c" is not inside seen.

Add "c".

Window = "abc"

seen = {"a", "b", "c"}

Current length = 3

longest = 3


STEP 4:

Current character = "a"

"a" already exists inside seen.

We have a duplicate.

Remove the old "a".

Move left forward.

Now:

Window = "bc"

Add the new "a".

Window = "bca"

Current length = 3

longest = 3


STEP 5:

Current character = "b"

"b" already exists.

Remove the old "b".

Move left forward.

Add the new "b".

Window = "cab"

Current length = 3

longest = 3


STEP 6:

Current character = "c"

"c" already exists.

Remove the old "c".

Move left forward.

Add the new "c".

Window = "abc"

Current length = 3

longest = 3


STEP 7:

Current character = "b"

"b" already exists.

Remove characters from the left:

First remove "a".

Then remove the old "b".

Now add the new "b".

Window = "cb"

Current length = 2

longest = 3


STEP 8:

Current character = "b"

"b" already exists.

Remove the old "b".

Move left forward.

Add the new "b".

Window = "b"

Current length = 1

longest = 3


FINAL ANSWER:

3

The longest substring is "abc".


7. TIME COMPLEXITY
--------------------------------------------------------

O(N)

Where:

N = Length of the input string.

WHY?

The right pointer visits every character once.

The left pointer also moves forward.

Important:

Neither pointer moves backward.

Although we have a while loop inside another while
loop, this does not make the time complexity O(N²).

Each character can be added to the set once and
removed from the set once.

Set operations take O(1) time on average.

Therefore:

TIME COMPLEXITY = O(N)


8. SPACE COMPLEXITY
--------------------------------------------------------

O(min(N, K))

Where:

N = Length of the input string.

K = Number of possible distinct characters.

WHY?

The set stores characters from the current window.

It cannot contain more than:

- N characters, because the string has N characters.
- K different characters, because only K different
  characters are possible.

Therefore:

SPACE COMPLEXITY = O(min(N, K))

For a general string with no fixed character limit,
the upper bound is O(N).


9. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
s = "abcabcbb"

Expected:
3

Reason:
The longest substring is "abc".


Test 2:

Input:
s = "bbbbb"

Expected:
1

Reason:
Only one different character exists.


Test 3:

Input:
s = "pwwkew"

Expected:
3

Reason:
The longest substring is "wke".


Test 4:

Input:
s = ""

Expected:
0

Reason:
The string is empty.


Test 5:

Input:
s = "a"

Expected:
1

Reason:
Only one character exists.


Test 6:

Input:
s = "abcdef"

Expected:
6

Reason:
Every character is different.


Test 7:

Input:
s = "abba"

Expected:
2

Reason:
The longest valid substring is "ab" or "ba".


Test 8:

Input:
s = "dvdf"

Expected:
3

Reason:
The longest substring is "vdf".


Test 9:

Input:
s = "tmmzuxt"

Expected:
5

Reason:
The longest substring is "mzuxt".


Test 10:

Input:
s = "anviaj"

Expected:
5

Reason:
The longest substring is "nviaj".


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a substring means.
[ ] I understand the difference between substring
    and subsequence.
[ ] I understand what a sliding window is.
[ ] I understand why we use left and right pointers.
[ ] I understand what a Hash Set is.
[ ] I understand how set() works in Python.
[ ] I understand how to check if a character exists
    inside a set.
[ ] I understand how seen.remove() works.
[ ] I understand why we use while instead of if.
[ ] I understand why left moves forward.
[ ] I understand why right moves forward.
[ ] I understand right - left + 1.
[ ] I understand how max() updates longest.
[ ] I can write this solution without looking.
[ ] I understand O(N) time complexity.
[ ] I understand O(min(N, K)) space complexity.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    ("a", 1),
    ("abcdef", 6),
    ("abba", 2),
    ("dvdf", 3),
    ("tmmzuxt", 5),
    ("anviaj", 5)
]

passed = 0

print("LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS")
print("----------------------------------")

for s, expected in test_cases:

    result = solution.lengthOfLongestSubstring(s)

    print("String:", s)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
