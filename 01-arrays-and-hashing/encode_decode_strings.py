
"""
========================================================
PROBLEM: ENCODE AND DECODE STRINGS
TOPIC: ARRAYS AND HASHING
APPROACH: EXTRA CHARACTER (DELIMITER)
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given a list of strings:

Encode the list into one single string.

Then decode that single string back into
the original list of strings.

In simple words:

Machine 1 receives a list of strings.
It converts them into one string.

Machine 2 receives that one string.
It reconstructs the original list.

IMPORTANT:

The decoded list must be exactly the same
as the original list.

This includes:

- The same strings.
- The same order.
- Empty strings.
- Special characters inside strings.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
strs = ["hello", "world"]

Encoded:
hello<DELIMITER>world

Decoded:
["hello", "world"]


Example 2:

Input:
strs = ["I", "love", "Python"]

Encoded:
I<DELIMITER>love<DELIMITER>Python

Decoded:
["I", "love", "Python"]


Example 3:

Input:
strs = []

Encoded:
<EMPTY_LIST_MARKER>

Decoded:
[]


Example 4:

Input:
strs = ["", "hello", ""]

Encoded:
<DELIMITER>hello<DELIMITER>

Decoded:
["", "hello", ""]


3. MY APPROACH: EXTRA CHARACTER (DELIMITER)
--------------------------------------------------------

I use two special characters:

1. SEPARATOR

   Character 257: chr(257)

   Separates one string from another.

2. EMPTY LIST MARKER

   Character 258: chr(258)

   Represents an empty input list.

My steps:

ENCODE:

1. Check whether the input list is empty.
2. If it is empty, return the empty-list marker.
3. Create the separator character.
4. Join all strings using the separator.
5. Return the encoded string.

DECODE:

1. Check whether the encoded string is the empty-list marker.
2. If it is, return an empty list.
3. Create the same separator character.
4. Split the encoded string using the separator.
5. Return the original list of strings.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    # Encodes a list of strings into one string
    def encode(self, strs: list[str]) -> str:

        # Return a special character if the list is empty
        if len(strs) == 0:
            return chr(258)

        # Create the separator character
        separate = chr(257)

        # Join all strings using the separator
        return separate.join(strs)

    # Decodes one string back into a list of strings
    def decode(self, s: str) -> list[str]:

        # Check whether the encoded string represents an empty list
        if s == chr(258):
            return []

        # Create the same separator character
        separate = chr(257)

        # Split the encoded string using the separator
        return s.split(separate)


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def encode(self, strs: list[str]) -> str:

Creates a function called encode.

It receives a list of strings.

strs:
The original list of strings.

list[str]:
Means a list containing strings.

str:
Means the function returns one string.


if len(strs) == 0:

Checks whether the input list is empty.

Example:

strs = []

len(strs) = 0

Therefore, the condition is True.


return chr(258)

Returns a special character.

chr() converts a Unicode number into a character.

chr(258) represents the character with Unicode
code point U+0102.

We use this character to represent an empty list.

Why?

Because an empty list and a list containing
one empty string are different.

Example:

[]      means no strings.

[""]    means one empty string.

We must be able to distinguish them.


separate = chr(257)

Creates our separator character.

chr(257) represents the character with Unicode
code point U+0101.

We use this character between strings.

For example:

["hello", "world"]

Becomes:

hello + separator + world

The separator tells us where one string ends
and the next string begins.


return separate.join(strs)

join() combines all strings into one string.

It places the separator between each string.

Example:

strs = ["hello", "world", "python"]

separate.join(strs)

Result:

hello<DELIMITER>world<DELIMITER>python

IMPORTANT:

join() does not add a separator at the beginning
or at the end.

It only adds separators between strings.

This also preserves empty strings.

Example:

strs = ["", "hello", ""]

Result:

<DELIMITER>hello<DELIMITER>


def decode(self, s: str) -> list[str]:

Creates a function called decode.

It receives one encoded string.

s:
The encoded string.

list[str]:
Means the function returns a list of strings.


if s == chr(258):

Checks whether the encoded string is our
special empty-list marker.

If it is, the original list was empty.


return []

Returns an empty list.

This means there were no original strings.


separate = chr(257)

Creates the same separator character
that we used during encoding.

Both functions must use the same separator.

Otherwise, decoding will not work correctly.


return s.split(separate)

split() separates one string into multiple strings.

It looks for the separator character.

Example:

s = "hello<DELIMITER>world"

s.split(separate)

Result:

["hello", "world"]

The original list is reconstructed.

IMPORTANT:

split() also preserves empty strings
at the beginning, middle, or end.

Example:

s = "<DELIMITER>hello<DELIMITER>"

Result:

["", "hello", ""]


6. COMPLETE ENCODE AND DECODE EXAMPLE
--------------------------------------------------------

Original list:

strs = ["hello", "world"]

STEP 1: ENCODE

The encode() function receives:

["hello", "world"]

It creates:

separate = chr(257)

Then it joins the strings:

"hello" + separate + "world"

The encoded string becomes:

"hello<DELIMITER>world"


STEP 2: DECODE

The decode() function receives:

"hello<DELIMITER>world"

It creates the same separator.

Then it runs:

s.split(separate)

Result:

["hello", "world"]


FINAL RESULT:

Original:

["hello", "world"]

Decoded:

["hello", "world"]

Both lists are identical.


7. TIME COMPLEXITY
--------------------------------------------------------

Let:

N = Total number of characters across all strings.

K = Number of strings.

ENCODE:

We visit and combine all characters.

The separator is also added between strings.

Therefore:

TIME COMPLEXITY = O(N + K)


DECODE:

We visit the encoded string and split it
at every separator.

Therefore:

TIME COMPLEXITY = O(N + K)


TOTAL:

Both operations are linear in the size
of the encoded data.

TIME COMPLEXITY = O(N + K)


8. SPACE COMPLEXITY
--------------------------------------------------------

ENCODE:

The encoded string contains:

- All original characters.
- One separator between each pair of strings.

Therefore:

SPACE COMPLEXITY = O(N + K)


DECODE:

The decoded list stores all original strings.

Therefore:

SPACE COMPLEXITY = O(N + K)


TOTAL:

SPACE COMPLEXITY = O(N + K)


IMPORTANT:

The extra space is needed to create
the encoded string and decoded list.

The algorithm does not use complicated
additional data structures.


9. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
["hello", "world"]

Expected:
["hello", "world"]

Reason:
Two normal strings are separated and reconstructed.


Test 2:

Input:
[]

Expected:
[]

Reason:
The empty-list marker represents an empty list.


Test 3:

Input:
[""]

Expected:
[""]

Reason:
One empty string is different from an empty list.


Test 4:

Input:
["", "hello", ""]

Expected:
["", "hello", ""]

Reason:
Empty strings at the beginning and end
must be preserved.


Test 5:

Input:
["I", "love", "Python"]

Expected:
["I", "love", "Python"]

Reason:
Multiple strings must keep their original order.


Test 6:

Input:
["123", "456", "789"]

Expected:
["123", "456", "789"]

Reason:
Numbers stored as strings must be preserved.


Test 7:

Input:
["hello world", "Python is great"]

Expected:
["hello world", "Python is great"]

Reason:
Spaces inside strings must be preserved.


Test 8:

Input:
["a", "", "b", "", "c"]

Expected:
["a", "", "b", "", "c"]

Reason:
Empty strings between other strings must be preserved.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what encoding means.
[ ] I understand what decoding means.
[ ] I understand why we need an encode function.
[ ] I understand why we need a decode function.
[ ] I understand what a separator is.
[ ] I understand what chr() does.
[ ] I understand why we use chr(257).
[ ] I understand why we use chr(258).
[ ] I understand why an empty list needs a special marker.
[ ] I understand what join() does.
[ ] I understand what split() does.
[ ] I understand how empty strings are preserved.
[ ] I understand how the original order is preserved.
[ ] I understand the complete encoding process.
[ ] I understand the complete decoding process.
[ ] I understand the time complexity.
[ ] I understand the space complexity.
[ ] I can write this solution without looking.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    (["hello", "world"], ["hello", "world"]),
    ([], []),
    ([""], [""]),
    (["", "hello", ""], ["", "hello", ""]),
    (["I", "love", "Python"], ["I", "love", "Python"]),
    (["123", "456", "789"], ["123", "456", "789"]),
    (["hello world", "Python is great"], ["hello world", "Python is great"]),
    (["a", "", "b", "", "c"], ["a", "", "b", "", "c"])
]

passed = 0

print("ENCODE AND DECODE STRINGS - TEST RESULTS")
print("----------------------------------")

for strs, expected in test_cases:

    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)

    print("Original:", strs)
    print("Encoded:", repr(encoded))
    print("Expected:", expected)
    print("Actual:", decoded)

    if decoded == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
