
"""
========================================================
PROBLEM: VALID ANAGRAM
TOPIC: ARRAYS AND HASHING
APPROACH: HASH MAP (PYTHON DICTIONARY)
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given two strings s and t:

Return True if t is an anagram of s.

Return False if t is not an anagram of s.

What is an anagram?

An anagram is a word made by rearranging all the
characters of another word.

The two strings must contain:
- The same characters.
- The same number of each character.

The order of the characters can be different.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
s = "anagram"
t = "nagaram"

Output:
True

Explanation:
Both strings contain:
a = 3 times
n = 1 time
g = 1 time
r = 1 time
m = 1 time

They contain exactly the same characters.


Example 2:

Input:
s = "rat"
t = "car"

Output:
False

Explanation:
The first string contains "r", "a", "t".
The second string contains "c", "a", "r".

They do not contain the same characters.


3. MY APPROACH: HASH MAP
--------------------------------------------------------

I use a Python dictionary called count.

The dictionary remembers how many times each
character appears.

My steps:

1. Check whether both strings have the same length.
2. If their lengths are different, return False.
3. Create an empty dictionary called count.
4. Go through both strings using the same index.
5. Add 1 for the character from string s.
6. Subtract 1 for the character from string t.
7. Check every frequency in the dictionary.
8. If any frequency is not zero, return False.
9. If all frequencies are zero, return True.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        # Check whether both strings have the same length
        if len(s) != len(t):
            return False

        # Create an empty dictionary to count characters
        count = {}

        # Visit both strings using the same index
        for i in range(len(s)):

            # Add 1 to the character from string s
            count[s[i]] = count.get(s[i], 0) + 1

            # Subtract 1 from the character from string t
            count[t[i]] = count.get(t[i], 0) - 1

        # Check every frequency stored in the dictionary
        for value in count.values():

            # If any frequency is not zero, they are not anagrams
            if value != 0:
                return False

        # All character frequencies are zero
        return True


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:

Creates a class called Solution.


def isAnagram(self, s: str, t: str) -> bool:

Creates a function that checks whether two strings
are anagrams.

s:
The first string.

t:
The second string.

str:
Means that s and t are strings.

-> bool:
Means that the function returns True or False.


if len(s) != len(t):

Checks whether the two strings have different lengths.

len():
Counts how many characters are inside a string.

!=:
Means "not equal to".

return False:

If the lengths are different, the strings cannot
be anagrams. The function stops here.


count = {}

Creates an empty dictionary.

A dictionary stores information using key-value pairs.

In our problem:
- Key = character.
- Value = frequency (how many times it appears).


for i in range(len(s)):

Visits every character using its index.

range(len(s)) creates index numbers:
0, 1, 2, 3, and so on.


count[s[i]] = count.get(s[i], 0) + 1

This is one of the most important lines.

s[i]:
Gets the character at position i in string s.

count.get(s[i], 0):

Looks for the character inside the dictionary.

If the character exists:
Returns its current frequency.

If the character does not exist:
Returns 0.

+ 1:
Increases its frequency by one.


count[t[i]] = count.get(t[i], 0) - 1

Gets the character at position i in string t.

It subtracts 1 from that character's frequency.

Why?

Because we are comparing the characters in both strings.

String s adds frequencies.
String t removes frequencies.


for value in count.values():

Goes through all the values stored in the dictionary.

.values() gives us the dictionary's values,
without its keys.


if value != 0:

Checks whether a character has an unbalanced frequency.

If a value is not zero, the strings do not have
the same character frequencies.


return False:

Reports that the strings are not anagrams.


return True:

If every frequency is zero, the strings are anagrams.


6. TIME COMPLEXITY
--------------------------------------------------------

O(n)

n = number of characters in each string.

Why?

1. Checking the lengths takes O(1).
2. The first loop visits n positions.
3. The second loop checks at most 2n dictionary entries.

Both loops take O(n) time.

Therefore, total time complexity is O(n).


7. SPACE COMPLEXITY
--------------------------------------------------------

O(k)

k = number of different characters stored in the dictionary.

The dictionary stores character frequencies.

In the worst case, every character is different,
so the dictionary can store up to n different keys.

Therefore, worst-case space complexity is O(n).

For lowercase English letters only, k cannot exceed 26,
so the extra space is O(1).


8. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

s = "anagram"
t = "nagaram"

Expected: True

Reason:
Both strings contain the same characters
with the same frequencies.


Test 2:

s = "rat"
t = "car"

Expected: False

Reason:
They contain different characters.


Test 3:

s = "listen"
t = "silent"

Expected: True

Reason:
Both strings contain the same characters.


Test 4:

s = "a"
t = "a"

Expected: True

Reason:
Both strings contain one identical character.


Test 5:

s = "a"
t = "b"

Expected: False

Reason:
The characters are different.


Test 6:

s = ""
t = ""

Expected: True

Reason:
Both strings are empty and have the same characters.


Test 7:

s = "aabb"
t = "bbaa"

Expected: True

Reason:
Both strings contain two a characters and two b characters.


Test 8:

s = "aabb"
t = "abbb"

Expected: False

Reason:
The character frequencies are different.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a Hash Map is.
[ ] I understand Python dictionaries.
[ ] I understand dictionary keys and values.
[ ] I understand count.get(character, 0).
[ ] I understand why we add 1.
[ ] I understand why we subtract 1.
[ ] I understand dictionary.values().
[ ] I can write this solution without looking.
[ ] I understand O(n) time complexity.
[ ] I understand O(k) space complexity.

========================================================
"""

# ------------------------------------------------------
# TESTING MY SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("listen", "silent", True),
    ("a", "a", True),
    ("a", "b", False),
    ("", "", True),
    ("aabb", "bbaa", True),
    ("aabb", "abbb", False)
]

print("VALID ANAGRAM - TEST RESULTS")
print("----------------------------------")

for s, t, expected in test_cases:

    result = solution.isAnagram(s, t)

    print("First string:", repr(s))
    print("Second string:", repr(t))
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
    else:
        print("Status: FAIL")

    print("----------------------------------")
