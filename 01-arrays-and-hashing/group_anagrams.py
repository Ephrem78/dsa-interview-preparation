
"""
========================================================
PROBLEM: GROUP ANAGRAMS
TOPIC: ARRAYS AND HASHING
APPROACH: HASH MAP + CHARACTER FREQUENCY COUNTING
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given a list of strings called strs:

Group all words that are anagrams of each other.

Anagrams are words that contain exactly the same
characters with the same frequency, but in a different
order.

In simple words:

Two words are anagrams if they contain the same letters
with the same number of occurrences.

Our task is to put all anagrams into the same group.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Explanation:

"eat", "tea", and "ate" contain:
- 1 e
- 1 a
- 1 t

Therefore, they belong to the same group.

"tan" and "nat" contain:
- 1 t
- 1 a
- 1 n

Therefore, they belong to another group.

"bat" has a different character frequency.
Therefore, it belongs to its own group.

NOTE:
The order of the groups does not matter.


Example 2:

Input:
strs = [""]

Output:
[[""]]

Explanation:
There is one empty string.
Therefore, it forms one group.


Example 3:

Input:
strs = ["a"]

Output:
[["a"]]

Explanation:
There is only one word.
Therefore, it forms one group.


3. MY APPROACH: HASH MAP + CHARACTER FREQUENCY
--------------------------------------------------------

I use a dictionary to group words that have the same
character frequencies.

My steps:

1. Create an empty dictionary called ans_map.

2. Visit every word in the input list.

3. Create a list of 26 zeros.
   Each position represents one English letter:
   a = position 0
   b = position 1
   c = position 2
   ...
   z = position 25

4. Visit every character in the current word.

5. Calculate the character's position in the alphabet.

6. Increase the counter at that position.

7. Convert the frequency list into a tuple.
   This tuple becomes the dictionary key.

8. Check whether this key already exists in ans_map.

9. If the key does not exist, create an empty list.

10. Add the current word to the correct group.

11. After visiting all words, return all groups.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # Create an empty dictionary to store anagram groups
        ans_map = {}

        # Visit every word in the input list
        for s in strs:

            # Create 26 counters, one for each English letter
            count = [0] * 26

            # Visit every character in the current word
            for char in s:

                # Find the character's position in the alphabet
                index = ord(char) - ord("a")

                # Increase the frequency of that character
                count[index] += 1

            # Convert the frequency list into a tuple
            key = tuple(count)

            # Check whether this frequency key already exists
            if key not in ans_map:

                # Create an empty group for this key
                ans_map[key] = []

            # Add the current word to its anagram group
            ans_map[key].append(s)

        # Return all the groups stored in the dictionary
        return list(ans_map.values())


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

Creates a function that groups anagrams.

self:
Refers to the current object of the class.

strs:
The input list containing words.

list[str]:
Means that strs is expected to be a list of strings.

-> list[list[str]]:
Means that the function returns a list of groups.
Each group is also a list of strings.


ans_map = {}

Creates an empty dictionary.

We use this dictionary to store our anagram groups.

Dictionary structure:

{
    character_frequency_key: [words]
}

The key represents the frequency of each character.

The value contains words with that same frequency.


for s in strs:

Visits every word in the input list.

Example:

strs = ["eat", "tea", "tan"]

First:
s = "eat"

Second:
s = "tea"

Third:
s = "tan"


count = [0] * 26

Creates a list containing 26 zeros.

Why 26?

Because the English alphabet has 26 letters.

Each position represents one letter.

Example:

a = position 0
b = position 1
c = position 2
d = position 3
e = position 4

And so on until z = position 25.


for char in s:

Visits every character in the current word.

Example:

If s = "eat":

First:
char = "e"

Second:
char = "a"

Third:
char = "t"


index = ord(char) - ord("a")

Finds the position of the current character
in the English alphabet.

ord() converts a character into its number code.

Example:

ord("a") = 97
ord("e") = 101
ord("t") = 116

For character "e":

index = 101 - 97
index = 4

Therefore, "e" belongs to position 4.


count[index] += 1

Increases the counter for the current character.

Example:

For the word "eat":

e is at position 4.
a is at position 0.
t is at position 19.

The frequency list will contain:

count[0] = 1
count[4] = 1
count[19] = 1

All other positions remain 0.


key = tuple(count)

Converts the frequency list into a tuple.

Why do we need a tuple?

Python dictionaries need hashable keys.

A list cannot be used as a dictionary key.

A tuple can be used as a dictionary key.

Therefore, we convert our frequency list into a tuple.

The tuple becomes the identity of the anagram group.

Important:

Words with the same character frequencies produce
the same tuple.

For example:

"eat"
"tea"
"ate"

All produce the same frequency key.


if key not in ans_map:

Checks whether this frequency key already exists
in our dictionary.

If it does not exist, we need to create a new group.


ans_map[key] = []

Creates an empty list for this anagram group.

Example:

ans_map[key] = []


ans_map[key].append(s)

Adds the current word to the correct group.

Example:

If the group already contains:

["eat", "tea"]

And the current word is "ate":

The group becomes:

["eat", "tea", "ate"]


return list(ans_map.values())

Returns all the groups from the dictionary.

values() gets the dictionary's group lists.

list() converts those values into a list.


6. TIME COMPLEXITY
--------------------------------------------------------

O(N * K)

Where:

N = Number of words in the input list.

K = Maximum length of a word.

Why?

There are two main operations:

1. We visit every word.

   This takes N visits.

2. For every word, we visit its characters.

   In the worst case, a word contains K characters.

   Therefore, character counting takes O(K).

3. Creating the frequency tuple takes O(26).

   Since 26 is a fixed number, this takes O(1).

Total:

O(N * (K + 26))

Because 26 is constant:

O(N * K)

Therefore:

TIME COMPLEXITY = O(N * K)


7. SPACE COMPLEXITY
--------------------------------------------------------

O(N * K) including the output.

Why?

We store all words in the final answer.

If there are N words and each word has at most K
characters, the output can contain O(N * K) characters.

The dictionary also stores:

- Frequency keys for the different groups.
- Lists containing the words in each group.

There are at most N different groups.

Each frequency key has 26 counters.

Therefore, frequency-key storage is O(26 * N),
which simplifies to O(N).

The output storage is O(N * K).

Therefore:

TOTAL SPACE COMPLEXITY = O(N * K)

Additional auxiliary space, excluding the output,
is O(N) for the dictionary and its keys, plus O(26)
for the temporary frequency list.

IMPORTANT:

In algorithm interviews, always explain whether
you include the output in your space complexity.


8. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
["eat", "tea", "tan", "ate", "nat", "bat"]

Expected:
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Reason:
Words with the same character frequencies belong
to the same group.


Test 2:

Input:
[""]

Expected:
[[""]]

Reason:
The empty string forms one group.


Test 3:

Input:
["a"]

Expected:
[["a"]]

Reason:
There is only one word.


Test 4:

Input:
["abc", "bca", "cab"]

Expected:
[["abc", "bca", "cab"]]

Reason:
All three words have the same characters.


Test 5:

Input:
["listen", "silent", "enlist", "hello"]

Expected:
[["listen", "silent", "enlist"], ["hello"]]

Reason:
The first three words are anagrams.
"hello" belongs to a different group.


Test 6:

Input:
["aab", "aba", "baa", "abb"]

Expected:
[["aab", "aba", "baa"], ["abb"]]

Reason:
The first three words have:
- 2 a characters
- 1 b character

The last word has:
- 1 a character
- 2 b characters


Test 7:

Input:
["eat", "eat", "tea"]

Expected:
[["eat", "eat", "tea"]]

Reason:
Repeated words are still added to the same group.


Test 8:

Input:
[]

Expected:
[]

Reason:
There are no words to group.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what an anagram is.
[ ] I understand how a Hash Map works.
[ ] I understand why we use 26 counters.
[ ] I understand how ord() works.
[ ] I understand how character frequency counting works.
[ ] I understand why we convert count into a tuple.
[ ] I understand how dictionary keys identify groups.
[ ] I understand how append() adds words to a group.
[ ] I understand how values() gets all dictionary groups.
[ ] I can write this solution without looking.
[ ] I understand O(N * K) time complexity.
[ ] I understand O(N * K) total space complexity.

========================================================
"""

# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    ),
    ([""], [[""]]),
    (["a"], [["a"]]),
    (["abc", "bca", "cab"], [["abc", "bca", "cab"]]),
    (
        ["listen", "silent", "enlist", "hello"],
        [["listen", "silent", "enlist"], ["hello"]]
    ),
    (
        ["aab", "aba", "baa", "abb"],
        [["aab", "aba", "baa"], ["abb"]]
    ),
    (["eat", "eat", "tea"], [["eat", "eat", "tea"]]),
    ([], [])
]

passed = 0

print("GROUP ANAGRAMS - TEST RESULTS")
print("----------------------------------")

for strs, expected in test_cases:

    result = solution.groupAnagrams(strs)

    # Sort words and groups because output order does not matter
    actual_sorted = sorted([sorted(group) for group in result])
    expected_sorted = sorted([sorted(group) for group in expected])

    print("Input:", strs)
    print("Expected:", expected)
    print("Actual:", result)

    if actual_sorted == expected_sorted:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
