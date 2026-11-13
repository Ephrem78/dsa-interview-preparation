
"""
========================================================
PROBLEM: LONGEST REPEATING CHARACTER REPLACEMENT
TOPIC: SLIDING WINDOW
APPROACH: SLIDING WINDOW + FREQUENCY ARRAY
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given:
- A string s containing uppercase English letters.
- An integer k representing the maximum replacements.

Find the length of the longest substring that can
contain the same letter after at most k replacements.

In simple words:

Find the longest group of consecutive characters that
can become the same letter by changing no more than
k characters.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
s = "ABAB"
k = 2

Output:
4

Explanation:

We can change both A characters into B.

"ABAB" becomes "BBBB".

The longest length is 4.


Example 2:

Input:
s = "AABABBA"
k = 1

Output:
4

Explanation:

We can change one A into B.

"AABABBA" can contain the substring "BBBB"
after one replacement.

The longest length is 4.


3. MY APPROACH: SLIDING WINDOW + FREQUENCY ARRAY
--------------------------------------------------------

I use two main ideas:

1. SLIDING WINDOW

   left = beginning of the current window.
   right = end of the current window.

2. FREQUENCY ARRAY

   Stores how many times each uppercase letter appears
   inside the current window.

My steps:

1. Create an array with 26 zeros.

2. Create left and right pointers.

3. Create longest to store the best answer.

4. Create max_frequency to store the highest character
   frequency found in the current window.

5. Move right through the string.

6. Count the current character.

7. Update max_frequency.

8. Calculate how many replacements are needed.

9. If replacements needed are greater than k,
   remove the left character and move left forward.

10. Update the longest window length.

11. Return longest.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:

        frequency = [0] * 26

        left = 0
        longest = 0
        max_frequency = 0

        for right in range(len(s)):

            index = ord(s[right]) - ord("A")
            frequency[index] += 1

            max_frequency = max(max_frequency, frequency[index])

            if (right - left + 1) - max_frequency > k:
                left_index = ord(s[left]) - ord("A")
                frequency[left_index] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def characterReplacement(self, s: str, k: int) -> int:

Creates a function that finds the longest substring
we can make using the same character.

self:
Refers to the current object.

s:
The input string.

k:
The maximum number of replacements allowed.

-> int:
Means the function returns an integer.


frequency = [0] * 26

Creates a list containing 26 zeros.

Why 26?

The problem uses uppercase English letters:

A, B, C, D, E, F, G, H, I, J, K, L, M,
N, O, P, Q, R, S, T, U, V, W, X, Y, Z

We need one position for each letter.

Example:

frequency = [0, 0, 0, 0, ... , 0]

Each position stores the frequency of one letter.

Position 0 = A
Position 1 = B
Position 2 = C

And so on.


left = 0

Creates the left pointer.

It marks the beginning of our current window.


longest = 0

Stores the longest valid window length found so far.

We start at 0 because we have not processed anything.


max_frequency = 0

Stores the highest frequency of one character
inside the current window.

Example:

Window = "AABAB"

A appears 3 times.
B appears 2 times.

Therefore:

max_frequency = 3

We use this value to calculate how many replacements
we need.


for right in range(len(s)):

Moves right through every character in the string.

range(len(s)) gives the indexes:

0, 1, 2, 3, ...

right is the index of the character we are processing.


index = ord(s[right]) - ord("A")

Converts the current uppercase letter into a number
between 0 and 25.

ord() gives the numerical code of a character.

Example:

ord("A") = 65
ord("B") = 66
ord("C") = 67

If the current character is "C":

index = ord("C") - ord("A")
index = 67 - 65
index = 2

Therefore, C uses position 2 in our frequency array.


frequency[index] += 1

Increases the count of the current character by 1.

Example:

If the current character is A:

frequency[0] += 1

The number of A characters increases by one.


max_frequency = max(max_frequency, frequency[index])

Compares:

1. The previous maximum frequency.
2. The current character's frequency.

Keeps the bigger number.

Example:

Previous max_frequency = 2
Current A frequency = 3

Then:

max(2, 3) = 3

Therefore:

max_frequency = 3


if (right - left + 1) - max_frequency > k:

This is the most important line.

Let's understand it.

right - left + 1

Calculates the current window length.

max_frequency

Tells us how many times the most common character
appears in the window.

The remaining characters must be replaced.

Therefore:

Characters to replace = window length - max_frequency


Example:

Window = "AABAB"

Window length = 5

A appears 3 times.
B appears 2 times.

max_frequency = 3

Replacements needed:

5 - 3 = 2

We need to replace two characters to make the
whole window contain the same letter.

If k = 2:

The window is valid.

If k = 1:

The window needs too many replacements.

Therefore, we must shrink the window.


left_index = ord(s[left]) - ord("A")

Finds the frequency-array position of the character
at the left side of the window.

Example:

If s[left] = "A":

left_index = 0


frequency[left_index] -= 1

Removes one occurrence of the left character
from our frequency array.

We are removing that character from our window.

Therefore, its frequency must decrease.


left += 1

Moves the left pointer one position forward.

This makes our window smaller.


longest = max(longest, right - left + 1)

Calculates the current window length.

Compares it with the longest length found before.

Keeps the bigger value.

Example:

Previous longest = 3
Current window length = 4

Then:

max(3, 4) = 4

Therefore:

longest = 4


return longest

Returns the longest possible window length.


IMPORTANT: WHY DO WE USE IF INSTEAD OF WHILE?

In this solution, we use:

if replacements_needed > k:

We do not use:

while replacements_needed > k:

The reason is that max_frequency is allowed to stay
at its highest value even after the left character
is removed.

It may no longer be the exact highest frequency
inside the current window.

This is intentional.

The algorithm still finds the correct maximum length.

It keeps the window from growing beyond the best
valid length found so far.

Using while would also be a valid approach if we
recalculated the actual maximum frequency after
shrinking the window. But that would add extra work.

This is an important optimization.


6. DRY RUN: "AABABBA", k = 1
--------------------------------------------------------

Input:

s = "AABABBA"
k = 1

We start with:

left = 0
longest = 0
max_frequency = 0

frequency = 26 zeros


STEP 1:

right = 0
character = A

A frequency = 1

max_frequency = 1

Window = "A"

Replacements needed = 1 - 1 = 0

Valid.

longest = 1


STEP 2:

right = 1
character = A

A frequency = 2

max_frequency = 2

Window = "AA"

Replacements needed = 2 - 2 = 0

Valid.

longest = 2


STEP 3:

right = 2
character = B

A frequency = 2
B frequency = 1

max_frequency = 2

Window = "AAB"

Replacements needed = 3 - 2 = 1

Valid.

longest = 3


STEP 4:

right = 3
character = A

A frequency = 3
B frequency = 1

max_frequency = 3

Window = "AABA"

Replacements needed = 4 - 3 = 1

Valid.

longest = 4


STEP 5:

right = 4
character = B

A frequency = 3
B frequency = 2

max_frequency = 3

Window = "AABAB"

Replacements needed = 5 - 3 = 2

2 is greater than k = 1.

We must shrink the window.

Remove the leftmost A.

Move left forward.

Now:

left = 1

Current window = "ABAB"

longest remains 4.


STEP 6:

right = 5
character = B

B frequency = 3

max_frequency = 3

Window = "ABABB"

Replacements needed = 5 - 3 = 2

2 is greater than k = 1.

Remove the leftmost A.

Move left forward.

Now:

left = 2

Current window = "BABB"

longest remains 4.


STEP 7:

right = 6
character = A

A frequency increases.

The window length is 5.

max_frequency remains 3.

Replacements needed = 5 - 3 = 2

2 is greater than k = 1.

Remove the leftmost B.

Move left forward.

Now:

left = 3

Current window = "ABBA"

longest remains 4.


FINAL ANSWER:

4


7. TIME COMPLEXITY
--------------------------------------------------------

O(N)

Where:

N = Length of the input string.

WHY?

We visit every character once using the right pointer.

The left pointer also moves forward.

Neither pointer moves backwards.

Frequency array operations take O(1) time.

The frequency array always has exactly 26 positions.

Therefore:

TIME COMPLEXITY = O(N)


8. SPACE COMPLEXITY
--------------------------------------------------------

O(1)

WHY?

The frequency array always contains 26 numbers.

It does not grow when the input string becomes longer.

We also use a fixed number of variables:

left
longest
max_frequency
right
index

Therefore:

SPACE COMPLEXITY = O(1)

This is constant space because the problem only uses
26 uppercase English letters.


9. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
s = "ABAB"
k = 2

Expected:
4

Reason:
We can change two characters.


Test 2:

Input:
s = "AABABBA"
k = 1

Expected:
4

Reason:
One replacement is enough to make a substring
of length 4 contain the same letter.


Test 3:

Input:
s = "AAAA"
k = 0

Expected:
4

Reason:
All characters are already the same.


Test 4:

Input:
s = "ABCDE"
k = 1

Expected:
2

Reason:
We can change one character to match its neighbor.


Test 5:

Input:
s = "AAAA"
k = 2

Expected:
4

Reason:
No replacements are needed.


Test 6:

Input:
s = "ABBB"
k = 2

Expected:
4

Reason:
We can change A into B.


Test 7:

Input:
s = "A"
k = 0

Expected:
1

Reason:
Only one character exists.


Test 8:

Input:
s = "ABCD"
k = 3

Expected:
4

Reason:
We can change three characters into the same letter.


Test 9:

Input:
s = "BAAAB"
k = 2

Expected:
5

Reason:
We can change both B characters into A.


Test 10:

Input:
s = ""
k = 1

Expected:
0

Reason:
The string is empty.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what character replacement means.
[ ] I understand what k represents.
[ ] I understand what a sliding window is.
[ ] I understand why we use left and right pointers.
[ ] I understand what a frequency array is.
[ ] I understand why the frequency array has 26 positions.
[ ] I understand how ord() works.
[ ] I understand how we count each character.
[ ] I understand what max_frequency means.
[ ] I understand window length - max_frequency.
[ ] I understand how to calculate replacements needed.
[ ] I understand why we shrink the window.
[ ] I understand why the Java code uses if.
[ ] I understand why max_frequency can stay unchanged
    after removing a character.
[ ] I understand O(N) time complexity.
[ ] I understand O(1) space complexity.
[ ] I can write this solution without looking.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
    ("AAAA", 0, 4),
    ("ABCDE", 1, 2),
    ("AAAA", 2, 4),
    ("ABBB", 2, 4),
    ("A", 0, 1),
    ("ABCD", 3, 4),
    ("BAAAB", 2, 5),
    ("", 1, 0)
]

passed = 0

print("LONGEST REPEATING CHARACTER REPLACEMENT")
print("----------------------------------")

for s, k, expected in test_cases:

    result = solution.characterReplacement(s, k)

    print("String:", s)
    print("K:", k)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
