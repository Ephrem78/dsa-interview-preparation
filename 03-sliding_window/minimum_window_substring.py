"""
========================================================
                MINIMUM WINDOW SUBSTRING
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

You are given two strings:

s = the main string
t = the string containing the characters we need.

Find the smallest substring of s that contains every
character in t.

IMPORTANT:

1. Every character in t must exist in the window.
2. Duplicate characters matter.
3. The characters can appear in any order.
4. The answer must be the shortest valid substring.
5. If no valid substring exists, return "".


2. EXAMPLES
--------------------------------------------------------

Example 1:

Input:
s = "ADOBECODEBANC"
t = "ABC"

Expected:
"BANC"

Reason:

"BANC" contains:
B = 1
A = 1
C = 1

It is the shortest valid window.


Example 2:

Input:
s = "a"
t = "a"

Expected:
"a"


Example 3:

Input:
s = "a"
t = "aa"

Expected:
""

Reason:

We need two "a" characters, but s contains only one.


Example 4:

Input:
s = "aa"
t = "aa"

Expected:
"aa"

Reason:

We need two "a" characters.
The window must contain both.


Example 5:

Input:
s = "ab"
t = "b"

Expected:
"b"


Example 6:

Input:
s = "bba"
t = "ab"

Expected:
"ba"


Example 7:

Input:
s = "bbaa"
t = "aba"

Expected:
"baa"

Reason:

We need:
a = 2
b = 1

"baa" contains all required characters.


Example 8:

Input:
s = "abc"
t = "d"

Expected:
""

Reason:

The character "d" does not exist in s.


Example 9:

Input:
s = "aaflslflsldkalskaaa"
t = "aaa"

Expected:
"aaa"

Reason:

We need three "a" characters.
The shortest valid window is "aaa".


Example 10:

Input:
s = "ADOBECODEBANC"
t = "AABC"

Expected:
"ADOBECODEBA"

Reason:

We need:
A = 2
B = 1
C = 1

The shortest valid window has 11 characters.


3. APPROACH: SLIDING WINDOW
--------------------------------------------------------

We use:

- Sliding Window
- Two Pointers
- Hash Maps (Dictionaries)

We create two dictionaries.

count_t:
Stores how many times each character is needed.

window_count:
Stores how many times each character appears
inside our current window.


Example:

t = "AABC"

count_t = {
    "A": 2,
    "B": 1,
    "C": 1
}


We also use two pointers:

left:
Marks the beginning of our window.

right:
Marks the end of our window.


We use two while loops:

FIRST WHILE LOOP:

Expands the window by moving right.

SECOND WHILE LOOP:

When the window contains everything we need,
we move left to make the window smaller.

We save the smallest valid window.


IMPORTANT VARIABLES
--------------------------------------------------------

count_t:

Stores the required character frequencies.

window_count:

Stores the current window character frequencies.

required:

The number of different character types we need.

formed:

The number of different character types that currently
have enough characters in our window.

left:

The starting position of our window.

right:

The ending position of our window.

best_length:

Stores the length of the smallest valid window found.

best_start:

Stores the starting position of that smallest window.


4. COMPLETE PYTHON SOLUTION
--------------------------------------------------------
"""


class Solution:

    def minWindow(self, s: str, t: str) -> str:

        # Step 1: Check invalid or impossible inputs.
        if not s or not t or len(s) < len(t):
            return ""

        # Step 2: Count the required characters in t.
        count_t = {}

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Step 3: Count how many different character
        # types we need.
        required = len(count_t)

        # Step 4: Create our two pointers.
        left = 0
        right = 0

        # Step 5: Count how many required character
        # types are currently satisfied.
        formed = 0

        # Step 6: Store the best window.
        best_length = float("inf")
        best_start = 0

        # Step 7: Store character frequencies
        # inside the current window.
        window_count = {}

        # Step 8: Expand the window using right.
        while right < len(s):

            # Get the character at the right position.
            char = s[right]

            # Add this character to our window dictionary.
            window_count[char] = window_count.get(char, 0) + 1

            # Check whether this character has reached
            # its required frequency.
            if char in count_t and window_count[char] == count_t[char]:
                formed += 1

            # Step 9: Shrink the window when it is valid.
            while left <= right and formed == required:

                # Calculate the current window length.
                window_length = right - left + 1

                # Save this window if it is smaller
                # than the previous best window.
                if window_length < best_length:
                    best_length = window_length
                    best_start = left

                # Get the character at the left position.
                left_char = s[left]

                # Remove one occurrence from the window.
                window_count[left_char] -= 1

                # Check whether removing this character
                # makes the window invalid.
                if (left_char in count_t and
                        window_count[left_char] < count_t[left_char]):
                    formed -= 1

                # Move the left pointer forward.
                left += 1

            # Move the right pointer forward.
            right += 1

        # Step 10: Check whether we found a valid window.
        if best_length == float("inf"):
            return ""

        # Step 11: Return the smallest valid substring.
        return s[best_start:best_start + best_length]


"""
5. DETAILED CODE EXPLANATION
--------------------------------------------------------

STEP 1:

if not s or not t or len(s) < len(t):
    return ""

What does this mean?

not s:
Checks whether s is empty.

not t:
Checks whether t is empty.

len(s) < len(t):
Checks whether s is shorter than t.

If any condition is true, we return an empty string.

Why?

We cannot find the required characters if the
input is empty or too short.


STEP 2:

count_t = {}

What does this do?

Creates an empty dictionary.

We use it to count the characters in t.


for char in t:

What does this do?

Visits every character in t, one by one.


count_t[char] = count_t.get(char, 0) + 1

Break it down:

count_t.get(char, 0)

Looks for char inside the dictionary.

If the character exists:
Returns its current count.

If it does not exist:
Returns 0.

+ 1

Adds one to the count.

Example:

t = "AABC"

After the loop:

count_t = {
    "A": 2,
    "B": 1,
    "C": 1
}


STEP 3:

required = len(count_t)

What does this do?

Counts how many different character types we need.

Example:

count_t = {
    "A": 2,
    "B": 1,
    "C": 1
}

len(count_t) = 3

Therefore:

required = 3

IMPORTANT:

We count different character types, not total
characters.

We need three types:
A, B, and C.

But we still need two A characters.


STEP 4:

left = 0
right = 0

What does this do?

Creates our two pointers.

left = beginning of the window.

right = end of the window.

Both start at index 0.


STEP 5:

formed = 0

What does this mean?

We have not satisfied any required character types yet.

When a required character reaches its needed frequency,
formed increases by one.

Example:

We need:

A = 2
B = 1
C = 1

If our window contains:

A = 2
B = 1
C = 0

Then:

formed = 2

A and B are satisfied.

C is not satisfied.


STEP 6:

best_length = float("inf")
best_start = 0

What does float("inf") mean?

It represents infinity.

We use it because we want to find a smaller window.

Any real window length will be smaller than infinity.

best_start stores where our best window begins.


STEP 7:

window_count = {}

What does this do?

Creates an empty dictionary.

It stores character counts inside the current window.

Example:

If the current window is "AABC":

window_count = {
    "A": 2,
    "B": 1,
    "C": 1
}


STEP 8:

while right < len(s):

What does this mean?

Continue expanding the window while right is
inside the string.

len(s) gives the total number of characters.

right < len(s) prevents us from going outside
the string.


char = s[right]

What does this do?

Gets the character at the right pointer.

Example:

s = "ADOBE"

If right = 0:

char = "A"


window_count[char] = window_count.get(char, 0) + 1

What does this do?

Adds the character to our current window count.

If it already exists, increase its count.

If it does not exist, start its count at 1.


if char in count_t and window_count[char] == count_t[char]:

What does this check?

First:

char in count_t

Checks whether this character is required.

Second:

window_count[char] == count_t[char]

Checks whether we now have exactly the required
number of this character.

Both conditions must be true.


formed += 1

What does += mean?

It means:

formed = formed + 1

We have satisfied one more required character type.


STEP 9:

while left <= right and formed == required:

What does this mean?

We enter this loop only when the current window
contains everything we need.

left <= right:

Makes sure the window is valid.

formed == required:

All required character types have enough occurrences.

Now we try to make the window smaller.


window_length = right - left + 1

Why + 1?

Because Python indexes start at 0.

Example:

left = 2
right = 5

Window length:

5 - 2 + 1 = 4

The window contains four characters.


if window_length < best_length:

What does this check?

Is the current valid window smaller than the
best window we have found?

If yes, save it.


best_length = window_length
best_start = left

What does this do?

Saves the new smallest window length.

Also saves its starting position.


left_char = s[left]

What does this do?

Gets the character at the beginning of the window.

We need to remove it when shrinking the window.


window_count[left_char] -= 1

What does -= mean?

It means:

window_count[left_char] = window_count[left_char] - 1

We remove one occurrence of that character
from our current window.


if (left_char in count_t and
        window_count[left_char] < count_t[left_char]):

What does this check?

First:

left_char in count_t

Checks whether the character is required.

Second:

window_count[left_char] < count_t[left_char]

Checks whether we now have fewer copies than required.

If both are true, the window is no longer valid
for that character.


formed -= 1

We reduce formed because one required character
type is no longer satisfied.


left += 1

Moves the left pointer one position forward.

This makes our window smaller.


STEP 10:

right += 1

Moves the right pointer one position forward.

This expands the window again.


STEP 11:

if best_length == float("inf"):
    return ""

What does this mean?

If best_length is still infinity, we never found
a valid window.

Return an empty string.


STEP 12:

return s[best_start:best_start + best_length]

What does this do?

Returns the smallest substring.

Example:

s = "ADOBECODEBANC"

best_start = 9
best_length = 4

Python slicing:

s[9:13]

Returns:

"BANC"

IMPORTANT:

The ending index in Python slicing is not included.


6. DRY RUN
--------------------------------------------------------

Input:

s = "ADOBECODEBANC"
t = "ABC"

Required characters:

A = 1
B = 1
C = 1

Therefore:

required = 3


FIRST VALID WINDOW:

As right moves, we find:

"ADOBEC"

It contains:

A = 1
B = 1
C = 1

Therefore:

formed = 3

Window length:

6

We save:

best_length = 6


NOW SHRINK:

We move left forward.

The first character is A.

When we remove A, the window no longer contains
the required A.

Therefore:

formed = 2

The window is no longer valid.

We stop shrinking.


CONTINUE EXPANDING:

The right pointer continues moving.

Eventually, we find another valid window:

"CODEBA"

It contains:

A = 1
B = 1
C = 1

Its length is 6.

It is not smaller than our previous best window.


CONTINUE EXPANDING:

Eventually, we find:

"BANC"

It contains:

B = 1
A = 1
C = 1

Its length is 4.

This is smaller than 6.

We save:

best_length = 4


FINAL ANSWER:

"BANC"


7. TIME COMPLEXITY
--------------------------------------------------------

O(M + N)

Where:

M = len(s)
N = len(t)


Why O(N)?

We visit every character in t once to build count_t.

That takes O(N) time.


Why O(M)?

The right pointer moves forward through s.

It visits each position once.

The left pointer also moves forward.

It visits each position at most once.

Therefore, the total pointer movement is O(M).

Final time complexity:

O(M + N)


IMPORTANT:

We do not have O(M * M) time.

Why?

Because left and right never move backwards.

Each pointer moves forward only.


8. SPACE COMPLEXITY
--------------------------------------------------------

O(M + N)

Why?

count_t stores characters from t.

window_count stores characters from the current
window in s.

In the general case, both dictionaries can store
different characters from their input strings.

Therefore:

O(M + N)

If the character set is fixed and limited,
such as only 26 lowercase English letters,
the auxiliary space can be O(1).


9. TEST CASES
--------------------------------------------------------

Test 1:

Input:
s = "ADOBECODEBANC"
t = "ABC"

Expected:
"BANC"


Test 2:

Input:
s = "a"
t = "a"

Expected:
"a"


Test 3:

Input:
s = "a"
t = "aa"

Expected:
""


Test 4:

Input:
s = "aa"
t = "aa"

Expected:
"aa"


Test 5:

Input:
s = "ab"
t = "b"

Expected:
"b"


Test 6:

Input:
s = "bba"
t = "ab"

Expected:
"ba"


Test 7:

Input:
s = "bbaa"
t = "aba"

Expected:
"baa"


Test 8:

Input:
s = "abc"
t = "d"

Expected:
""


Test 9:

Input:
s = "aaflslflsldkalskaaa"
t = "aaa"

Expected:
"aaa"


Test 10:

Input:
s = "ADOBECODEBANC"
t = "AABC"

Expected:
"ADOBECODEBA"

Reason:

We need:
A = 2
B = 1
C = 1

The shortest valid window has 11 characters.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a substring is.
[ ] I understand what a minimum window means.
[ ] I understand why duplicate characters matter.
[ ] I understand what a sliding window is.
[ ] I understand the left pointer.
[ ] I understand the right pointer.
[ ] I understand how a dictionary counts characters.
[ ] I understand dict.get().
[ ] I understand count_t.
[ ] I understand window_count.
[ ] I understand required.
[ ] I understand formed.
[ ] I understand why formed increases.
[ ] I understand why formed decreases.
[ ] I understand why we use two while loops.
[ ] I understand how to calculate window_length.
[ ] I understand how we save the smallest window.
[ ] I understand Python string slicing.
[ ] I understand why the time complexity is O(M + N).
[ ] I understand why the space complexity is O(M + N).
[ ] I can write this solution without looking.


========================================================
10. TESTING THE SOLUTION
========================================================
"""


solution = Solution()

test_cases = [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("aa", "aa", "aa"),
    ("ab", "b", "b"),
    ("bba", "ab", "ba"),
    ("bbaa", "aba", "baa"),
    ("abc", "d", ""),
    ("aaflslflsldkalskaaa", "aaa", "aaa"),
    ("ADOBECODEBANC", "AABC", "ADOBECODEBA")
]

passed = 0

print("MINIMUM WINDOW SUBSTRING - TEST RESULTS")
print("----------------------------------")

for s, t, expected in test_cases:

    result = solution.minWindow(s, t)

    print("S:", s)
    print("T:", t)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")