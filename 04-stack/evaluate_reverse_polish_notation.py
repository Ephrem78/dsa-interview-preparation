
"""
EVALUATE REVERSE POLISH NOTATION
================================

Problem
-------

You are given a list of strings called tokens.

The list represents an arithmetic expression written
in Reverse Polish Notation (RPN).

Evaluate the expression and return its integer result.

Valid operators:
    +
    -
    *
    /

Important rules:
    - Each operand is an integer or another expression.
    - Division truncates toward zero.
    - There is no division by zero.
    - The expression is always valid.
    - Results fit within a 32-bit integer.


EXAMPLES
--------

Example 1:

tokens = ["2", "1", "+", "3", "*"]

Calculation:

2 + 1 = 3
3 * 3 = 9

Output:
9


Example 2:

tokens = ["4", "13", "5", "/", "+"]

Calculation:

13 / 5 = 2
4 + 2 = 6

Output:
6


Example 3:

tokens = [
    "10", "6", "9", "3", "+", "-11",
    "*", "/", "*", "17", "+", "5", "+"
]

Output:
22


MY APPROACH: STACK
------------------

A Stack is a data structure that follows:

LIFO = Last In, First Out.

This means:
The last item we put into the stack
is the first item we remove.

We use a stack because RPN expressions
place operators AFTER their operands.

For example:

tokens = ["2", "1", "+"]

We read from left to right.

1. Read "2".
   It is a number.
   Push 2 into the stack.

   Stack: [2]

2. Read "1".
   It is a number.
   Push 1 into the stack.

   Stack: [2, 1]

3. Read "+".
   It is an operator.
   Pop the second operand: 1.
   Pop the first operand: 2.

4. Calculate:

   2 + 1 = 3

5. Push the result back into the stack.

   Stack: [3]

6. After reading all tokens,
   the final answer is at the top.

   Answer: 3


IMPORTANT: OPERAND ORDER
-----------------------

When we find an operator, we must pop
the second operand first, then the first operand.

For example:

tokens = ["8", "3", "-"]

First pop:
b = 3

Second pop:
a = 8

Calculation:
a - b = 8 - 3 = 5

Do NOT calculate b - a.

This is especially important for:
    - Subtraction
    - Division


PYTHON SOLUTION
---------------

"""


class Solution:

    def evalRPN(self, tokens: list[str]) -> int:

        # Create an empty stack.
        stack = []

        # Visit every token from left to right.
        for token in tokens:

            # Check whether the current token is an operator.
            if token in ("+", "-", "*", "/"):

                # Remove the second operand.
                b = stack.pop()

                # Remove the first operand.
                a = stack.pop()

                # Calculate the result.
                if token == "+":
                    result = a + b

                elif token == "-":
                    result = a - b

                elif token == "*":
                    result = a * b

                else:
                    # Division that truncates toward zero.
                    result = self.divide(a, b)

                # Put the result back into the stack.
                stack.append(result)

            else:
                # The token is a number.
                # Convert its string into an integer.
                stack.append(int(token))

        # The final answer is the only remaining stack item.
        return stack.pop()


    def divide(self, a: int, b: int) -> int:

        # Divide the absolute values.
        result = abs(a) // abs(b)

        # If the signs are different, make the result negative.
        if (a < 0) != (b < 0):
            return -result

        return result


"""
LINE-BY-LINE UNDERSTANDING
--------------------------


1. class Solution:

   Creates a class called Solution.

   LeetCode commonly expects this class structure.

   We put our solution inside this class.


2. def evalRPN(self, tokens: list[str]) -> int:

   Creates a method called evalRPN.

   tokens:
       The input list containing numbers and operators.

   list[str]:
       Means tokens is a list of strings.

   Example:

       ["2", "1", "+", "3", "*"]

   self:
       Refers to the current Solution object.

   -> int:
       Means the method returns an integer.


3. stack = []

   Creates an empty Python list.

   We use this list as our stack.

   Why?

   We need to save numbers until we find
   an operator that can use them.

   Example:

       stack = []

       stack.append(2)

       Stack: [2]


4. for token in tokens:

   Visits every item in tokens, one at a time.

   The loop moves from left to right.

   Example:

       tokens = ["2", "1", "+"]

   First loop:
       token = "2"

   Second loop:
       token = "1"

   Third loop:
       token = "+"


5. if token in ("+", "-", "*", "/"):

   Checks whether the current token is an operator.

   The word "in" checks whether an item
   exists inside a collection.

   Example:

       token = "+"

       "+" is inside ("+", "-", "*", "/").

       Therefore, the condition is True.

   But if:

       token = "15"

       "15" is not an operator.

       Therefore, the condition is False.


6. b = stack.pop()

   Removes and returns the last item from the stack.

   We call this the second operand.

   Example:

       Stack: [8, 3]

       b = stack.pop()

       b = 3

       Stack: [8]

   Why do we remove b first?

   Because the last number pushed into the stack
   is the second operand in the expression.


7. a = stack.pop()

   Removes the next item from the stack.

   We call this the first operand.

   Example:

       Stack: [8]

       a = stack.pop()

       a = 8

       Stack: []

   Now we have:

       a = 8
       b = 3

   We can calculate:

       a - b = 8 - 3 = 5


8. if token == "+":

   Checks whether the operator is addition.

   If it is:

       result = a + b

   Example:

       a = 2
       b = 1

       result = 2 + 1

       result = 3


9. elif token == "-":

   Checks whether the operator is subtraction.

   elif means:

       If the previous condition was False,
       check this condition.

   Calculation:

       result = a - b

   Example:

       a = 8
       b = 3

       result = 8 - 3

       result = 5

   Remember:
       The order matters.


10. elif token == "*":

    Checks whether the operator is multiplication.

    Calculation:

        result = a * b

    Example:

        a = 4
        b = 3

        result = 4 * 3

        result = 12

    In Python, * means multiplication.


11. else:

    If the operator is not +, -, or *,
    it must be /.

    This is safe because the problem guarantees
    that every input expression is valid.

    We call:

        result = self.divide(a, b)

    This uses our separate divide method.

    Why do we need it?

    Python's // operator rounds down for negative
    results. The problem requires truncation toward zero.

    We will explain divide() below.


12. stack.append(result)

    Adds the calculated result to the top of the stack.

    Example:

        Before:
            Stack: []

        result = 3

        After:
            stack.append(result)

            Stack: [3]

    Why?

    The result may be used by another operator later.


13. else:

    This belongs to the operator check.

    It means the current token is a number,
    not an operator.


14. stack.append(int(token))

    First:

        int(token)

    Converts the string into an integer.

    Example:

        token = "25"

        int(token) = 25

    Why do we need int()?

    The input contains strings.

    We need integers to perform arithmetic.

    Then:

        stack.append(25)

    Pushes the integer onto the stack.


15. return stack.pop()

    After all tokens have been processed,
    the final answer is the only item remaining
    in the stack.

    pop() removes and returns that item.

    Example:

        Stack: [9]

        return stack.pop()

        Answer: 9


UNDERSTANDING THE divide() METHOD
---------------------------------

16. def divide(self, a: int, b: int) -> int:

    Creates a separate method for division.

    a is the first operand.
    b is the second operand.

    Example:

        a = -7
        b = 2


17. result = abs(a) // abs(b)

    abs() returns the absolute value.

    Example:

        abs(-7) = 7
        abs(2) = 2

    Then:

        7 // 2 = 3

    result = 3

    We first divide positive numbers
    so that // gives the correct whole-number part.


18. if (a < 0) != (b < 0):

    Checks whether exactly one operand is negative.

    a < 0:
        Checks whether a is negative.

    b < 0:
        Checks whether b is negative.

    != means "not equal".

    Example 1:

        a = -7
        b = 2

        a < 0  -> True
        b < 0  -> False

        True != False -> True

    The signs are different.
    The answer must be negative.


19. return -result

    Returns the result with a negative sign.

    Example:

        result = 3

        return -3

    Therefore:

        -7 / 2 = -3

    This is truncation toward zero.


20. return result

    If both operands have the same sign,
    the result is positive.

    Examples:

        7 / 2 = 3

        -7 / -2 = 3


IMPORTANT PYTHON DIVISION DIFFERENCE
------------------------------------

The problem requires truncation toward zero.

Python's // rounds down.

Example:

    -7 // 2 = -4

But the correct answer for this problem is:

    -7 / 2 = -3

Our divide() method returns -3 correctly.

We also avoid converting to float.
This keeps the division safe for large integers.


DETAILED WALKTHROUGH: EXAMPLE 1
-------------------------------

tokens = ["2", "1", "+", "3", "*"]

Start:

stack = []


FIRST LOOP

token = "2"

Is "2" an operator?

No.

Convert "2" into integer 2.

Push 2.

Stack:
[2]


SECOND LOOP

token = "1"

Is "1" an operator?

No.

Convert "1" into integer 1.

Push 1.

Stack:
[2, 1]


THIRD LOOP

token = "+"

Is "+" an operator?

Yes.

Pop the second operand:

b = 1

Stack:
[2]

Pop the first operand:

a = 2

Stack:
[]

Calculate:

2 + 1 = 3

Push 3.

Stack:
[3]


FOURTH LOOP

token = "3"

Is "3" an operator?

No.

Convert it into integer 3.

Push 3.

Stack:
[3, 3]


FIFTH LOOP

token = "*"

Is "*" an operator?

Yes.

Pop the second operand:

b = 3

Stack:
[3]

Pop the first operand:

a = 3

Stack:
[]

Calculate:

3 * 3 = 9

Push 9.

Stack:
[9]


END OF LOOP

All tokens have been processed.

Return the last item:

return stack.pop()

Final answer:

9


ANOTHER WALKTHROUGH: SUBTRACTION
--------------------------------

tokens = ["8", "3", "-"]

Read "8":

Stack: [8]

Read "3":

Stack: [8, 3]

Read "-":

b = stack.pop()
b = 3

a = stack.pop()
a = 8

Calculate:

a - b

8 - 3 = 5

Push 5.

Stack: [5]

Final answer: 5


ANOTHER WALKTHROUGH: NEGATIVE DIVISION
--------------------------------------

tokens = ["0", "7", "2", "/", "-"]

Read "0":

Stack: [0]

Read "7":

Stack: [0, 7]

Read "2":

Stack: [0, 7, 2]

Read "/":

b = 2
a = 7

7 / 2 = 3

Stack: [0, 3]

Read "-":

b = 3
a = 0

0 - 3 = -3

Stack: [-3]

Final answer: -3


EDGE CASES
----------

1. One number:

   tokens = ["42"]

   Answer: 42

   There is no operator.
   The number remains in the stack.


2. Negative number:

   tokens = ["-5"]

   Answer: -5

   int("-5") converts the string into -5.


3. Negative division:

   tokens = ["-7", "2", "/"]

   Answer: -3

   Division truncates toward zero.


4. Negative divided by negative:

   tokens = ["-7", "-2", "/"]

   Answer: 3


5. Subtraction order:

   tokens = ["10", "4", "-"]

   Answer: 6

   We must calculate 10 - 4, not 4 - 10.


6. Multiple operations:

   tokens = ["2", "3", "+", "4", "*"]

   Answer: 20

   First: 2 + 3 = 5
   Then: 5 * 4 = 20


TIME COMPLEXITY
---------------

Let n = the number of tokens.

Time Complexity: O(n)

Why?

We visit every token exactly once.

For each token:

1. Check whether it is an operator.

   This takes O(1).

2. If it is a number:

   int(token) takes time proportional to the
   number of digits in the token.

   Under the usual algorithm-analysis assumption
   that each token is a bounded-size integer,
   this is treated as O(1).

3. If it is an operator:

   stack.pop() takes O(1) on average.

   Arithmetic operations take O(1) for the
   problem's bounded 32-bit integer values.

   stack.append() takes O(1) amortized.

We process n tokens.

Therefore:

    O(n)

The algorithm's running time grows linearly
with the number of tokens.


SPACE COMPLEXITY
----------------

Space Complexity: O(n)

Why?

We use a stack to store numbers and intermediate results.

In the worst case, the expression can contain
many numbers before an operator appears.

Example:

    ["1", "2", "3", "4", "5", "+", "+", "+", "+"]

Before the first operator:

    Stack: [1, 2, 3, 4, 5]

The stack can hold a number of elements
proportional to the number of tokens.

Therefore:

    O(n)

We also use a few variables:

    token
    a
    b
    result

These use O(1) extra space.

The stack is the part that determines
the overall space complexity.


COMPLEXITY SUMMARY
------------------

Time Complexity:
    O(n)

Space Complexity:
    O(n)

n = number of tokens.


OWN TEST CASES
--------------

Test 1:
    Input:
        ["2", "1", "+", "3", "*"]

    Expected:
        9

    Reason:
        (2 + 1) * 3 = 9


Test 2:
    Input:
        ["4", "13", "5", "/", "+"]

    Expected:
        6

    Reason:
        13 / 5 = 2
        4 + 2 = 6


Test 3:
    Input:
        ["10", "6", "9", "3", "+", "-11",
         "*", "/", "*", "17", "+", "5", "+"]

    Expected:
        22

    Reason:
        This tests a longer expression
        with several operators.


Test 4:
    Input:
        ["8", "3", "-"]

    Expected:
        5

    Reason:
        Tests subtraction order.


Test 5:
    Input:
        ["-7", "2", "/"]

    Expected:
        -3

    Reason:
        Tests truncation toward zero.


Test 6:
    Input:
        ["7", "-2", "/"]

    Expected:
        -3

    Reason:
        Tests positive divided by negative.


Test 7:
    Input:
        ["-7", "-2", "/"]

    Expected:
        3

    Reason:
        Tests negative divided by negative.


Test 8:
    Input:
        ["42"]

    Expected:
        42

    Reason:
        Tests an expression with one number.


Test 9:
    Input:
        ["2", "3", "+", "4", "*"]

    Expected:
        20

    Reason:
        Tests a result that is used by another operator.


TEST RUNNER
-----------

The following code tests all nine cases.

"""


def run_tests():

    solution = Solution()

    test_cases = [

        (
            ["2", "1", "+", "3", "*"],
            9
        ),

        (
            ["4", "13", "5", "/", "+"],
            6
        ),

        (
            [
                "10", "6", "9", "3", "+", "-11",
                "*", "/", "*", "17", "+", "5", "+"
            ],
            22
        ),

        (
            ["8", "3", "-"],
            5
        ),

        (
            ["-7", "2", "/"],
            -3
        ),

        (
            ["7", "-2", "/"],
            -3
        ),

        (
            ["-7", "-2", "/"],
            3
        ),

        (
            ["42"],
            42
        ),

        (
            ["2", "3", "+", "4", "*"],
            20
        )

    ]

    passed = 0

    for i, (tokens, expected) in enumerate(test_cases, start=1):

        actual = solution.evalRPN(tokens)

        if actual == expected:
            print(f"Test {i}: PASSED")
            passed += 1

        else:
            print(f"Test {i}: FAILED")
            print(f"Expected: {expected}")
            print(f"Actual:   {actual}")

    print()
    print(f"Results: {passed}/{len(test_cases)} tests passed.")


if __name__ == "__main__":
    run_tests()
