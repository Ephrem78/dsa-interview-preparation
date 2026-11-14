
"""
============================================================
VALID PARENTHESES
============================================================

TOPIC:
Stack

APPROACH:
Hash Map + Stack

------------------------------------------------------------
1. PROBLEM DESCRIPTION
------------------------------------------------------------

You are given a string s containing brackets:

    (  )  {  }  [  ]

You must check whether the brackets are valid.

A string is valid when:

1. Every opening bracket has the correct closing bracket.
2. Brackets close in the correct order.
3. Every opening bracket is closed.

Examples:

Example 1:
Input:  s = "()"
Output: True

Explanation:
The opening parenthesis "(" is correctly closed by ")".

Example 2:
Input:  s = "{[()]}"
Output: True

Explanation:
Every opening bracket has the correct closing bracket.
They also close in the correct order.

Example 3:
Input:  s = "(]"
Output: False

Explanation:
"(" must be closed by ")".
But the string contains "]".

Example 4:
Input:  s = "(("
Output: False

Explanation:
Both opening brackets are still waiting to be closed.

Example 5:
Input:  s = "())"
Output: False

Explanation:
The final ")" does not have an opening bracket.

------------------------------------------------------------
2. MY APPROACH
------------------------------------------------------------

I will use two things:

1. A dictionary (Hash Map).
2. A stack.

WHAT IS THE DICTIONARY FOR?

The dictionary connects every closing bracket
to its correct opening bracket.

Example:

    mapped_brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }

This means:

    ")" must match "("
    "}" must match "{"
    "]" must match "["

WHAT IS THE STACK FOR?

A stack stores opening brackets until we find
their matching closing brackets.

A stack follows LIFO:

    Last In, First Out

This means the last opening bracket we add
must be the first one we close.

Example:

    s = "{[()]}" 

The opening brackets enter the stack:

    {
    { [

    { [ (

When ")" appears, we remove "(".

When "]" appears, we remove "[".

When "}" appears, we remove "{".

At the end, the stack must be empty.

------------------------------------------------------------
3. PYTHON SOLUTION
------------------------------------------------------------
"""

class Solution:

    def isValid(self, s: str) -> bool:

        # Dictionary: closing bracket -> opening bracket
        mapped_brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # List used as a stack
        stack = []

        # Check every character in the string
        for char in s:

            # If the character is an opening bracket
            if char in "({[":

                # Put the opening bracket on the stack
                stack.append(char)

            # If the character is a closing bracket
            elif char in mapped_brackets:

                # There must be an opening bracket to match it
                if not stack:
                    return False

                # Remove the most recent opening bracket
                top_element = stack.pop()

                # Check whether the brackets match
                if top_element != mapped_brackets[char]:
                    return False

            # Reject any character that is not a bracket
            else:
                return False

        # All opening brackets must have been closed
        return len(stack) == 0


"""
------------------------------------------------------------
4. EXPLANATION OF IMPORTANT CODE LINES
------------------------------------------------------------

LINE 1:

    class Solution:

WHAT DOES class MEAN?

A class is a structure that holds related code.

Here, Solution is the name of our class.

LeetCode expects this class name for this problem.

------------------------------------------------------------

LINE 2:

    def isValid(self, s: str) -> bool:

WHAT DOES def MEAN?

def is used to create a function.

isValid is the function name.

WHAT IS s?

s is the input string.

Example:

    s = "{[()]}"

WHAT DOES -> bool MEAN?

It tells us that the function returns a Boolean value.

A Boolean has only two possible values:

    True
    False

WHAT DOES self MEAN?

self refers to the current object created
from the Solution class.

------------------------------------------------------------

LINE 3:

    mapped_brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }

WHAT IS THIS?

This is a Python dictionary.

A dictionary stores information using key-value pairs.

For example:

    ")": "("

The key is:

    ")"

The value is:

    "("

WHY DO WE NEED THIS?

When we find a closing bracket, we need to know
which opening bracket it must match.

For example:

    mapped_brackets[")"]

Python returns:

    "("

So we can compare the closing bracket
with the correct opening bracket.

IMPORTANT:

The dictionary connects closing brackets
to their required opening brackets.

------------------------------------------------------------

LINE 4:

    stack = []

WHAT IS THIS?

We create an empty Python list.

We will use this list as a stack.

WHY AN EMPTY STACK?

At the beginning, we have not found any opening brackets.

WHAT DOES A STACK DO?

A stack follows:

    LIFO = Last In, First Out

Example:

    stack = []

    stack.append("(")
    stack.append("[")

Now:

    stack = ["(", "["]

The last item added is "[".

When we remove an item using pop():

    stack.pop()

Python removes "[" first.

The stack becomes:

    ["("]

This is exactly what we need because
brackets must close in the correct order.

------------------------------------------------------------

LINE 5:

    for char in s:

WHAT DOES for MEAN?

A for loop repeats code for every item
inside a sequence.

WHAT IS char?

char is a variable that stores one character
from the string at a time.

Example:

    s = "{[()]}"

The loop reads:

    char = "{"
    char = "["
    char = "("
    char = ")"
    char = "]"
    char = "}"

It checks each character one by one.

------------------------------------------------------------

LINE 6:

    if char in "({[":

WHAT DOES if MEAN?

if checks whether a condition is True.

WHAT DOES in MEAN?

in checks whether something exists inside
another sequence.

Example:

    char = "("

    char in "({["

The result is:

    True

WHY?

Because "(" is inside the string "({[".

WHAT DOES THIS CONDITION CHECK?

It checks whether the current character
is an opening bracket.

The opening brackets are:

    (
    {
    [

------------------------------------------------------------

LINE 7:

    stack.append(char)

WHAT DOES append() MEAN?

append() adds a new item to the end of a list.

Example:

    stack = []

    stack.append("(")

Now:

    stack = ["("]

Another example:

    stack.append("[")

Now:

    stack = ["(", "["]

WHY DO WE ADD OPENING BRACKETS?

We need to remember every opening bracket
until its matching closing bracket appears.

The stack remembers the most recent opening bracket.

------------------------------------------------------------

LINE 8:

    elif char in mapped_brackets:

WHAT DOES elif MEAN?

elif means "else if".

It checks another condition when the previous
if condition was False.

WHAT DOES THIS CONDITION CHECK?

It checks whether the current character
is a closing bracket.

Remember our dictionary:

    mapped_brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }

All dictionary keys are closing brackets.

Therefore:

    ")" in mapped_brackets  -> True
    "}" in mapped_brackets  -> True
    "]" in mapped_brackets  -> True

------------------------------------------------------------

LINE 9:

    if not stack:

WHAT DOES not MEAN?

not reverses a Boolean result.

For example:

    not True  -> False
    not False -> True

WHAT DOES if not stack MEAN?

It checks whether the stack is empty.

An empty list behaves like False in a condition.

Therefore:

    stack = []

    if not stack:

This condition is True.

WHY DO WE CHECK THIS?

Imagine:

    s = ")"

The first character is a closing bracket.

But we have not seen an opening bracket.

There is nothing to match it with.

Therefore, the string is invalid.

We return False.

------------------------------------------------------------

LINE 10:

    return False

WHAT DOES return MEAN?

return sends the answer back from the function.

It also immediately stops the function.

Example:

    if not stack:
        return False

If there is no opening bracket to match
the closing bracket, we stop immediately.

We do not need to check the remaining characters.

------------------------------------------------------------

LINE 11:

    top_element = stack.pop()

WHAT DOES pop() MEAN?

pop() removes and returns the last item
from a list.

Example:

    stack = ["(", "["]

    top_element = stack.pop()

Now:

    top_element = "["

    stack = ["("]

WHY DO WE USE pop()?

Because brackets must close in reverse order.

The most recent opening bracket must close first.

For example:

    s = "{[()]}"
    
The last opening bracket is "(".

So ")" must close it first.

pop() gives us the most recent opening bracket.

------------------------------------------------------------

LINE 12:

    if top_element != mapped_brackets[char]:

WHAT DOES != MEAN?

!= means "not equal".

Example:

    5 != 3  -> True
    5 != 5  -> False

WHAT DOES mapped_brackets[char] DO?

It looks up the correct opening bracket
for the current closing bracket.

Example:

    char = ")"

    mapped_brackets[char]

Python returns:

    "("

NOW THE CONDITION:

    if top_element != mapped_brackets[char]:

It compares:

    The opening bracket removed from the stack

WITH:

    The opening bracket required by the closing bracket

Example 1:

    top_element = "("
    char = ")"

    mapped_brackets[char] = "("

Comparison:

    "(" != "("

Result:

    False

The brackets match.

Example 2:

    top_element = "("
    char = "]"

    mapped_brackets[char] = "["

Comparison:

    "(" != "["

Result:

    True

The brackets do not match.

We return False.

------------------------------------------------------------

LINE 13:

    else:
        return False

WHY DO WE NEED THIS?

The problem says the string must contain
only these six bracket characters:

    ( ) { } [ ]

If another character appears, such as "a",
we reject the string.

This is an extra safety check.

The original Java code assumes the input
contains only the six allowed characters.

------------------------------------------------------------

FINAL LINE:

    return len(stack) == 0

WHAT DOES len() MEAN?

len() counts how many items are inside
a list, string, or other sequence.

Example:

    stack = ["(", "["]

    len(stack)

Result:

    2

WHAT DOES == MEAN?

== means "is equal to".

Example:

    5 == 5  -> True
    5 == 3  -> False

WHAT DOES THIS LINE CHECK?

    return len(stack) == 0

It checks whether the stack is empty.

WHY?

Every opening bracket must have a closing bracket.

If the stack is empty:

    All opening brackets were matched.

Return:

    True

If the stack still contains something:

    Some opening brackets were never closed.

Return:

    False

------------------------------------------------------------
5. COMPLETE DRY RUN
------------------------------------------------------------

Let's understand the solution using:

    s = "{[()]}"

Initial state:

    stack = []

STEP 1:

    char = "{"

Is "{" an opening bracket?

Yes.

Add it to the stack.

    stack = ["{"]

STEP 2:

    char = "["

Is "[" an opening bracket?

Yes.

Add it to the stack.

    stack = ["{", "["]

STEP 3:

    char = "("

Is "(" an opening bracket?

Yes.

Add it to the stack.

    stack = ["{", "[", "("]

STEP 4:

    char = ")"

Is ")" a closing bracket?

Yes.

Is the stack empty?

No.

Remove the top item:

    top_element = stack.pop()

Now:

    top_element = "("
    stack = ["{", "["]

Find the required opening bracket:

    mapped_brackets[")"] = "("

Compare:

    "(" == "("

They match.

Continue.

STEP 5:

    char = "]"

Is "]" a closing bracket?

Yes.

Remove the top item:

    top_element = stack.pop()

Now:

    top_element = "["
    stack = ["{"]

Find the required opening bracket:

    mapped_brackets["]"] = "["

Compare:

    "[" == "["

They match.

Continue.

STEP 6:

    char = "}"

Is "}" a closing bracket?

Yes.

Remove the top item:

    top_element = stack.pop()

Now:

    top_element = "{"
    stack = []

Find the required opening bracket:

    mapped_brackets["}"] = "{"

Compare:

    "{" == "{"

They match.

Continue.

FINAL CHECK:

    return len(stack) == 0

The stack is empty.

    len(stack) = 0

Therefore:

    0 == 0

Result:

    True

FINAL ANSWER:

    "{[()]}" -> True

------------------------------------------------------------
6. TIME COMPLEXITY
------------------------------------------------------------

TIME COMPLEXITY:

    O(N)

WHAT IS N?

N means the number of characters in the string.

Example:

    s = "{[()]}"

There are 6 characters.

So:

    N = 6

WHY IS THE TIME COMPLEXITY O(N)?

We use:

    for char in s:

The loop visits every character once.

For each character, we perform operations
such as:

    Dictionary lookup
    Stack append()
    Stack pop()
    Comparison

These operations take O(1) average time.

O(1) means the operation takes approximately
constant time.

If the string has:

    10 characters  -> about 10 loop steps
    100 characters -> about 100 loop steps
    1000 characters -> about 1000 loop steps

The work grows in proportion to the input size.

Therefore:

    TIME COMPLEXITY = O(N)

------------------------------------------------------------
7. SPACE COMPLEXITY
------------------------------------------------------------

SPACE COMPLEXITY:

    O(N)

WHY?

We create a stack:

    stack = []

The stack stores opening brackets.

Imagine this input:

    s = "((((((("

There are 7 opening brackets and no closing brackets.

The stack stores all 7:

    stack = ["(", "(", "(", "(", "(", "(", "("]

In the worst case, every character is an opening bracket.

Therefore, the stack can grow to contain N characters.

The dictionary always contains only 3 pairs:

    ")": "("
    "}": "{"
    "]": "["

Its size does not grow with the input.

So its space is O(1).

The stack needs O(N) space.

Therefore:

    SPACE COMPLEXITY = O(N)

------------------------------------------------------------
8. MY OWN TEST CASES
------------------------------------------------------------
"""

solution = Solution()

test_cases = [

    # Basic valid brackets
    ("()", True),
    ("{}", True),
    ("[]", True),

    # Different types of valid brackets
    ("()[]{}", True),
    ("{[()]}", True),
    ("({[]})", True),

    # Wrong bracket types
    ("(]", False),
    ("([)]", False),
    ("{[}", False),

    # Missing opening or closing brackets
    ("(", False),
    ("[", False),
    ("{", False),
    (")", False),
    ("]", False),
    ("}", False),

    # Extra closing brackets
    ("())", False),
    ("((()))", True),

    # Empty string
    ("", True),

    # Other edge cases
    ("(((((", False),
    ("}}}}", False),
    ("(){}}", False),

    # Invalid characters
    ("(a)", False),
    ("( | )", False),
]

passed = 0

for s, expected in test_cases:

    actual = solution.isValid(s)

    if actual == expected:
        print(f"PASS | Input: {s!r} | Expected: {expected} | Got: {actual}")
        passed += 1

    else:
        print(f"FAIL | Input: {s!r} | Expected: {expected} | Got: {actual}")

print("----------------------------------------")
print(f"Tests passed: {passed}/{len(test_cases)}")
