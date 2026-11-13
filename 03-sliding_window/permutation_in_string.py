
"""
========================================================
PROBLEM: PERMUTATION IN STRING
TOPIC: SLIDING WINDOW
APPROACH: FIXED-SIZE SLIDING WINDOW + FREQUENCY ARRAYS
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given two strings:

s1 = the string whose permutation we are looking for.
s2 = the string where we search.

Return True if s2 contains a substring that is a
permutation of s1.

Otherwise, return False.

In simple words:

Check whether s2 contains the same characters as s1,
with the same frequency, but possibly in a different
order.

IMPORTANT:

A permutation must contain exactly the same characters
and the same number of each character.

The characters must be next to each other in s2.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
s1 = "ab"
s2 = "eidbaooo"

Output:
True

Explanation:

The substring "ba" exists inside s2.

"ba" is a permutation of "ab".


Example 2:

Input:
s1 = "ab"
s2 = "eidboaoo"

Output:
False

Explanation:

No substring of length 2 contains exactly one "a"
and one "b".


3. MY APPROACH: FIXED-SIZE SLIDING WINDOW
   + FREQUENCY ARRAYS
--------------------------------------------------------

I use two frequency arrays:

1. s1_count:
   Stores the frequency of each character in s1.

2. window_count:
   Stores the frequency of each character in the
   current window of s2.

Both arrays have 26 positions because we use
lowercase English letters.

My steps:

1. Check whether s1 is longer than s2.
   If yes, return False.

2. Create two frequency arrays.

3. Count the characters in s1.

4. Count the characters in the first window of s2.

5. Compare both frequency arrays.

6. If they match, return True.

7. Slide the window one position forward.

8. Add the new character entering the window.

9. Remove the old character leaving the window.

10. Compare the frequency arrays again.

11. If a matching window is found, return True.

12. If no matching window exists, return False.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(s1)):
            s1_index = ord(s1[i]) - ord("a")
            window_index = ord(s2[i]) - ord("a")

            s1_count[s1_index] += 1
            window_count[window_index] += 1

        if s1_count == window_count:
            return True

        for right in range(len(s1), len(s2)):

            new_index = ord(s2[right]) - ord("a")
            old_index = ord(s2[right - len(s1)]) - ord("a")

            window_count[new_index] += 1
            window_count[old_index] -= 1

            if s1_count == window_count:
                return True

        return False


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def checkInclusion(self, s1: str, s2: str) -> bool:

Creates a function that checks whether s2 contains
a permutation of s1.

self:
Refers to the current object.

s1:
The string whose permutation we are searching for.

s2:
The string where we search.

-> bool:
Means the function returns True or False.


if len(s1) > len(s2):

Checks whether s1 is longer than s2.

Example:

s1 = "abcd"
s2 = "abc"

s1 has 4 characters.
s2 has 3 characters.

A 4-character permutation cannot fit inside
a 3-character string.

Therefore, we return False.


s1_count = [0] * 26

Creates an array with 26 zeros.

Each position represents one lowercase English letter.

Position 0 = a
Position 1 = b
Position 2 = c

And so on.


window_count = [0] * 26

Creates another frequency array.

This array counts the characters inside the
current window of s2.

Why two arrays?

We need to compare the character frequencies
of s1 with the current window in s2.


for i in range(len(s1)):

Visits every character in s1.

We also use this loop to count the first window
of s2.

Why?

The first window must have the same length as s1.


s1_index = ord(s1[i]) - ord("a")

Converts the current character in s1 into an
array position between 0 and 25.

Example:

ord("a") = 97
ord("b") = 98
ord("c") = 99

If the character is "c":

99 - 97 = 2

Therefore, c uses position 2.


window_index = ord(s2[i]) - ord("a")

Finds the array position of the corresponding
character in the first window of s2.

Example:

s2[i] = "b"

window_index = 1


s1_count[s1_index] += 1

Increases the frequency of the current character
in s1 by one.


window_count[window_index] += 1

Increases the frequency of the current character
in the first window of s2 by one.


if s1_count == window_count:

Compares the two frequency arrays.

Python can compare lists directly.

It checks whether every position has the same value.

Example:

s1_count = [1, 1, 0, 0, ...]
window_count = [1, 1, 0, 0, ...]

They are equal.

Therefore, the current window is a permutation
of s1.

Return True.


for right in range(len(s1), len(s2)):

Moves the window through the remaining characters
of s2.

We start at len(s1) because the first window
has already been counted.

Example:

s1 = "ab"
s2 = "eidbaooo"

len(s1) = 2

The first window is:

"ei"

The next new character is at index 2.

Therefore, right starts at 2.


new_index = ord(s2[right]) - ord("a")

Finds the frequency-array position of the new
character entering the window.

Example:

Current new character = "d"

Its array position is 3.


old_index = ord(s2[right - len(s1)]) - ord("a")

Finds the frequency-array position of the old
character leaving the window.

Why subtract len(s1)?

Because the window has a fixed size.

For a window of length 2:

When a new character enters, the character
two positions behind leaves.


window_count[new_index] += 1

Adds the new character to the window frequency.

The new character has entered the window.

Therefore, its frequency increases by one.


window_count[old_index] -= 1

Removes the old character from the window frequency.

The old character has left the window.

Therefore, its frequency decreases by one.


if s1_count == window_count:

Compares the frequency arrays again.

If they match, the current window is a permutation
of s1.

Return True.


return False

If we finish checking every window without finding
a match, return False.


6. DRY RUN: s1 = "ab", s2 = "eidbaooo"
--------------------------------------------------------

First:

s1 = "ab"
s2 = "eidbaooo"

len(s1) = 2

len(s2) = 8

We need to check windows of size 2.


STEP 1: CREATE FREQUENCY ARRAYS

s1 = "ab"

a appears 1 time.
b appears 1 time.

s1_count:

a = 1
b = 1

First window of s2 = "ei"

e appears 1 time.
i appears 1 time.

window_count:

e = 1
i = 1

The arrays do not match.

Move the window.


STEP 2: WINDOW = "id"

Remove "e".
Add "d".

The window contains:

i = 1
d = 1

The arrays do not match.

Move the window.


STEP 3: WINDOW = "db"

Remove "i".
Add "b".

The window contains:

d = 1
b = 1

The arrays do not match.

Move the window.


STEP 4: WINDOW = "ba"

Remove "d".
Add "a".

The window contains:

b = 1
a = 1

Compare with s1:

s1 = "ab"
window = "ba"

Both contain:

a = 1
b = 1

The arrays match.

Return True.


FINAL ANSWER:

True


7. TIME COMPLEXITY
--------------------------------------------------------

O(N + K)

Where:

N = Length of s2.
K = Length of s1.

WHY?

STEP 1: BUILD FREQUENCY ARRAYS

We visit every character in s1.

We also visit the first window of s2.

This takes O(K).


STEP 2: SLIDE THE WINDOW

We visit the remaining characters of s2.

Each movement adds one character and removes
one character.

This takes O(N - K).


STEP 3: COMPARE FREQUENCY ARRAYS

We compare 26 positions.

This takes O(26) = O(1).

We do this for each window.

There are at most N - K + 1 windows.

Therefore, comparisons take O(N) because 26
is a fixed number.

TOTAL:

O(K) + O(N - K) + O(26 * (N - K + 1))

Therefore:

TIME COMPLEXITY = O(N)

The simpler answer is O(N), because the alphabet
has a fixed size of 26.


8. SPACE COMPLEXITY
--------------------------------------------------------

O(1)

WHY?

We create two frequency arrays.

s1_count = 26 positions.
window_count = 26 positions.

Their sizes never grow.

We only use a fixed number of additional variables.

Therefore:

SPACE COMPLEXITY = O(1)


9. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

s1 = "ab"
s2 = "eidbaooo"

Expected:
True

Reason:
"ba" is a permutation of "ab".


Test 2:

s1 = "ab"
s2 = "eidboaoo"

Expected:
False

Reason:
No window contains one a and one b.


Test 3:

s1 = "a"
s2 = "a"

Expected:
True

Reason:
The strings contain the same character.


Test 4:

s1 = "ab"
s2 = "a"

Expected:
False

Reason:
s2 is shorter than s1.


Test 5:

s1 = "abc"
s2 = "ccccbbbbaaaa"

Expected:
False

Reason:
No window contains exactly a, b, and c.


Test 6:

s1 = "abc"
s2 = "bbbca"

Expected:
True

Reason:
The substring "bca" is a permutation of "abc".


Test 7:

s1 = "aabc"
s2 = "caaebaa"

Expected:
False

Reason:
No window contains two a characters, one b,
and one c.


Test 8:

s1 = "adc"
s2 = "dcda"

Expected:
True

Reason:
The substring "cda" is a permutation of "adc".


Test 9:

s1 = "hello"
s2 = "ooolleoooleh"

Expected:
False

Reason:
No window has the same character frequencies
as "hello".


Test 10:

s1 = "abc"
s2 = "abc"

Expected:
True

Reason:
The entire s2 string is a permutation of s1.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a permutation means.
[ ] I understand why character order does not matter.
[ ] I understand why the substring must be consecutive.
[ ] I understand what a fixed-size sliding window is.
[ ] I understand why the window size equals len(s1).
[ ] I understand what a frequency array is.
[ ] I understand why we use two frequency arrays.
[ ] I understand why each array has 26 positions.
[ ] I understand how ord() works.
[ ] I understand how we count characters.
[ ] I understand how Python compares two lists.
[ ] I understand how a new character enters the window.
[ ] I understand how an old character leaves the window.
[ ] I understand why we add one and subtract one.
[ ] I understand why we check the final window.
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
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False),
    ("a", "a", True),
    ("ab", "a", False),
    ("abc", "ccccbbbbaaaa", False),
    ("abc", "bbbca", True),
    ("aabc", "caaebaa", False),
    ("adc", "dcda", True),
    ("hello", "ooolleoooleh", False),
    ("abc", "abc", True)
]

passed = 0

print("PERMUTATION IN STRING - TEST RESULTS")
print("----------------------------------")

for s1, s2, expected in test_cases:

    result = solution.checkInclusion(s1, s2)

    print("S1:", s1)
    print("S2:", s2)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
