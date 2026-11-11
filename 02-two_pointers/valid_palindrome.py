
"""
========================================================
PROBLEM: VALID PALINDROME
TOPIC: TWO POINTERS
APPROACH: TWO POINTERS (LEFT AND RIGHT)
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

A palindrome is a word or sentence that reads the same
forward and backward.

Examples:

"madam"  -> True
"racecar" -> True
"hello"  -> False

But there is one important rule.

Before checking whether a string is a palindrome:

1. Convert uppercase letters into lowercase.
2. Ignore spaces.
3. Ignore punctuation marks.
4. Ignore all non-alphanumeric characters.

Alphanumeric characters include:
- Letters: a, b, c, A, B, C
- Numbers: 0, 1, 2, 3, 4, 5

Our task:

Return True if the cleaned string is a palindrome.
Return False if it is not.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
s = "A man, a plan, a canal: Panama"

Output:
True

Explanation:

After removing spaces and punctuation and converting
uppercase letters to lowercase:

"amanaplanacanalpanama"

Reading forward and backward gives the same result.

Therefore: True


Example 2:

Input:
s = "race a car"

Output:
False

Cleaned string:

"raceacar"

The first and last characters are both "r".
But the next comparison is "a" and "a".
The next comparison is "c" and "a".

They are different.

Therefore: False


Example 3:

Input:
s = " "

Output:
True

Explanation:

The space is not an alphanumeric character.

After ignoring it:

""

The result is an empty string.

An empty string is considered a palindrome.

Therefore: True


3. MY APPROACH: TWO POINTERS
--------------------------------------------------------

I use two pointers:

1. LEFT POINTER
   Starts at the first character.

2. RIGHT POINTER
   Starts at the last character.

My steps:

1. Set left = 0.
2. Set right = len(s) - 1.
3. Continue while left is smaller than right.
4. Check the character at the left pointer.
5. If it is not alphanumeric, move left forward.
6. Check the character at the right pointer.
7. If it is not alphanumeric, move right backward.
8. Convert both characters to lowercase.
9. Compare them.
10. If they are different, return False.
11. If they match, move both pointers toward the middle.
12. If all comparisons match, return True.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def isPalindrome(self, s: str) -> bool:

        # Start the left pointer at the first character
        left = 0

        # Start the right pointer at the last character
        right = len(s) - 1

        # Continue while the pointers have not crossed
        while left < right:

            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare both characters without case differences
            if s[left].lower() != s[right].lower():
                return False

            # Move the left pointer one step forward
            left += 1

            # Move the right pointer one step backward
            right -= 1

        # All required character comparisons matched
        return True


"""
5. COMPLETE ELS10 EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------


class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def isPalindrome(self, s: str) -> bool:

Creates a function called isPalindrome.

s:
The input string we want to check.

str:
Means the input must be a string.

bool:
Means the function returns either:

True
or
False


left = 0

Creates the left pointer.

A pointer is a variable that remembers a position
inside a string.

Python starts counting string positions from 0.

Example:

s = "hello"

Position:

 h    e    l    l    o
 0    1    2    3    4

left = 0 means:

Start at the first character, "h".


right = len(s) - 1

Creates the right pointer.

len(s) counts how many characters are in the string.

Example:

s = "hello"

len(s) = 5

But the last position is 4, not 5.

Why?

Because positions start at 0.

Therefore:

right = 5 - 1
right = 4

The right pointer starts at "o".


while left < right:

This loop continues while left is smaller than right.

In simple words:

Continue checking while the two pointers
have not met or crossed.

Example:

left = 0
right = 4

0 < 4 is True.

So the loop runs.

When the pointers meet or cross,
there are no more pairs to compare.


while left < right and not s[left].isalnum():

This line checks the character at the left pointer.

Let's break it down.

s[left]

Gets the character at the current left position.

Example:

s = "A man"

left = 1

s[left] = " "

This gives us the space character.


isalnum()

Checks whether a character is a letter or a number.

Examples:

"a".isalnum() -> True
"Z".isalnum() -> True
"5".isalnum() -> True
" ".isalnum() -> False
",".isalnum() -> False
"!".isalnum() -> False


not s[left].isalnum()

The word "not" reverses True and False.

If a character is not a letter or number,
the result becomes True.

Therefore:

not " ".isalnum() -> True

not "a".isalnum() -> False


left += 1

Means:

left = left + 1

Move the left pointer one position forward.

Example:

left = 0

After:

left += 1

left = 1

We use this to skip spaces and punctuation
until we find a letter or number.


while left < right and not s[right].isalnum():

This does the same job on the right side.

But instead of checking the left character,
it checks the right character.

If the right character is not a letter or number,
we skip it.


right -= 1

Means:

right = right - 1

Move the right pointer one position backward.

Example:

right = 5

After:

right -= 1

right = 4

We use this to skip spaces and punctuation
from the right side.


WHY DO WE CHECK left < right AGAIN?

Example:

s = "!!!"

Every character is punctuation.

We keep skipping characters.

The pointers can eventually meet.

The condition left < right prevents us from
moving past the other pointer.

It also prevents us from comparing characters
after there are no pairs left to check.


if s[left].lower() != s[right].lower():

This compares the left and right characters.

Let's break it down.

s[left]

Gets the character at the left position.

.lower()

Converts an uppercase letter into lowercase.

Example:

"A".lower() -> "a"
"B".lower() -> "b"

"!="

Means "not equal".

Therefore:

s[left].lower() != s[right].lower()

Means:

Are the two characters different
after converting them to lowercase?


Example:

"A" and "a"

After lowercase:

"a" and "a"

They are equal.

Therefore the condition is False.

But:

"a" and "b"

They are different.

Therefore the condition is True.


return False

If the two characters are different,
the string cannot be a palindrome.

We immediately stop the function
and return False.

We do not need to check the remaining characters.


left += 1

If both characters match, move the left pointer
one position toward the middle.

Example:

left = 0

After:

left += 1

left = 1


right -= 1

Move the right pointer one position
toward the middle.

Example:

right = 5

After:

right -= 1

right = 4


return True

If the loop finishes without finding
any different character pairs, return True.

This means the string is a palindrome.


6. STEP-BY-STEP EXECUTION
--------------------------------------------------------

Let's use:

s = "A man, a plan, a canal: Panama"

We begin:

left = 0
right = 30

The pointers start at opposite ends.

Comparison 1:

Left character = "A"
Right character = "a"

Convert to lowercase:

"a" == "a"

They match.

Move both pointers toward the middle.


Comparison 2:

Left character = " "
Right character = "m"

The left character is a space.

Skip it.

Now compare:

"a" and "m"

They are different? No.

Actually, after skipping the space,
the left character is "m".

So:

"m" == "m"

They match.


The same process continues:

Compare the next valid characters.
Skip spaces and punctuation.
Convert letters to lowercase.
Move toward the middle.

Every pair matches.

The pointers eventually meet or cross.

Final result:

True


7. TIME COMPLEXITY
--------------------------------------------------------

O(N)

Where:

N = Number of characters in the input string.

WHY?

The left pointer moves forward.

The right pointer moves backward.

Neither pointer moves backward or forward repeatedly
through the same positions.

Each character is visited at most a constant number
of times.

Therefore:

TIME COMPLEXITY = O(N)


8. SPACE COMPLEXITY
--------------------------------------------------------

O(1)

WHY?

We only create two pointer variables:

left
right

We do not create another cleaned string.

We do not create a list or dictionary.

We compare characters directly inside the original
string.

The extra memory stays constant,
even when the input string becomes larger.

Therefore:

SPACE COMPLEXITY = O(1)


IMPORTANT:

This solution does not build a new cleaned string.

It checks the original string directly
using two pointers.

That is why its extra space complexity is O(1).


9. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
"A man, a plan, a canal: Panama"

Expected:
True


Test 2:

Input:
"race a car"

Expected:
False


Test 3:

Input:
" "

Expected:
True


Test 4:

Input:
"madam"

Expected:
True


Test 5:

Input:
"RaceCar"

Expected:
True


Test 6:

Input:
"hello"

Expected:
False


Test 7:

Input:
"0P"

Expected:
False


Test 8:

Input:
"a"

Expected:
True


Test 9:

Input:
"...."

Expected:
True


Test 10:

Input:
"1a2"

Expected:
False


Test 11:

Input:
"Was it a car or a cat I saw?"

Expected:
True


Test 12:

Input:
"12321"

Expected:
True


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a palindrome is.
[ ] I understand what a Two Pointer approach is.
[ ] I understand why left starts at 0.
[ ] I understand why right starts at len(s) - 1.
[ ] I understand how while left < right works.
[ ] I understand what isalnum() does.
[ ] I understand what not means.
[ ] I understand how left += 1 works.
[ ] I understand how right -= 1 works.
[ ] I understand what lower() does.
[ ] I understand what != means.
[ ] I understand why we return False immediately.
[ ] I understand why we return True at the end.
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
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("madam", True),
    ("RaceCar", True),
    ("hello", False),
    ("0P", False),
    ("a", True),
    ("....", True),
    ("1a2", False),
    ("Was it a car or a cat I saw?", True),
    ("12321", True)
]

passed = 0

print("VALID PALINDROME - TEST RESULTS")
print("----------------------------------")

for s, expected in test_cases:

    result = solution.isPalindrome(s)

    print("Input:", repr(s))
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
