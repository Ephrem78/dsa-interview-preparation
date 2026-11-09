
"""
========================================================
PROBLEM: VALID SUDOKU
TOPIC: ARRAYS AND HASHING
APPROACH: HASH SET
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given a 9 x 9 Sudoku board, determine whether it is valid.

We must follow three rules:

RULE 1: ROWS

Each row must not contain repeated digits.

RULE 2: COLUMNS

Each column must not contain repeated digits.

RULE 3: 3 x 3 BOXES

Each of the nine 3 x 3 boxes must not contain
repeated digits.

IMPORTANT:

- Only filled cells need to be checked.
- A dot "." represents an empty cell.
- Empty cells are ignored.
- The board does not need to be solvable.
- We only check whether the current board is valid.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

Output:

True

Explanation:

There are no repeated digits in:

- Any row.
- Any column.
- Any 3 x 3 box.

Therefore, the Sudoku board is valid.


Example 2:

Input:

board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

Output:

False

Explanation:

The first column contains the digit 8 twice.

Therefore, the Sudoku board is invalid.


3. MY APPROACH: HASH SET
--------------------------------------------------------

I use three groups of Hash Sets.

1. ROWS

   Stores the digits already found in each row.

2. COLUMNS

   Stores the digits already found in each column.

3. BOXES

   Stores the digits already found in each 3 x 3 box.

My steps:

1. Create nine empty Hash Sets for rows.

2. Create nine empty Hash Sets for columns.

3. Create nine empty Hash Sets for boxes.

4. Visit every cell in the Sudoku board.

5. Get the current cell value.

6. If the cell contains ".", skip it.

7. Calculate which 3 x 3 box the cell belongs to.

8. Check whether the digit already exists in:
   - Its row.
   - Its column.
   - Its 3 x 3 box.

9. If the digit already exists in any of them,
   return False.

10. Otherwise, add the digit to all three Hash Sets.

11. If every cell passes the checks,
    return True.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # Create nine empty Hash Sets for rows
        rows = [set() for _ in range(9)]

        # Create nine empty Hash Sets for columns
        cols = [set() for _ in range(9)]

        # Create nine empty Hash Sets for 3 x 3 boxes
        boxes = [set() for _ in range(9)]

        # Visit every row
        for r in range(9):

            # Visit every column
            for c in range(9):

                # Get the current cell value
                val = board[r][c]

                # Skip empty cells
                if val == ".":
                    continue

                # Calculate the box number
                box_index = (r // 3) * 3 + (c // 3)

                # Check whether the digit is repeated
                if (
                    val in rows[r]
                    or val in cols[c]
                    or val in boxes[box_index]
                ):
                    return False

                # Record the digit in its row
                rows[r].add(val)

                # Record the digit in its column
                cols[c].add(val)

                # Record the digit in its 3 x 3 box
                boxes[box_index].add(val)

        # No repeated digits were found
        return True


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------


class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def isValidSudoku(self, board: list[list[str]]) -> bool:

Creates a function called isValidSudoku.

self:
Refers to the current object of the class.

board:
The Sudoku board.

list[list[str]]:
Means that the board is a list containing lists of strings.

bool:
Means that the function returns either:

True
or
False


rows = [set() for _ in range(9)]

Creates nine empty Hash Sets.

Each Hash Set belongs to one row.

Example:

rows[0] = set()
rows[1] = set()
rows[2] = set()

And so on, until rows[8].

Why do we use Hash Sets?

A Hash Set stores unique values.

For example:

my_set = {"5", "3", "7"}

If we try to add "5" again, the set does not
store a second copy.

We use this property to detect repeated digits.

IMPORTANT:

Each row has its own separate Hash Set.


cols = [set() for _ in range(9)]

Creates nine empty Hash Sets for columns.

Each Hash Set belongs to one column.

For example:

cols[0] stores digits found in column 0.

cols[1] stores digits found in column 1.

cols[2] stores digits found in column 2.

And so on.


boxes = [set() for _ in range(9)]

Creates nine empty Hash Sets for the nine 3 x 3 boxes.

Each box has its own Hash Set.

We need this because the same digit cannot appear
twice inside one 3 x 3 box.


for r in range(9):

Visits every row.

range(9) produces:

0, 1, 2, 3, 4, 5, 6, 7, 8

Therefore, r represents the current row index.

Remember:

Python starts counting indexes from 0.


for c in range(9):

Visits every column inside the current row.

c represents the current column index.

Together:

r = row index
c = column index

We use two loops because the board has two dimensions.

The first loop moves through rows.

The second loop moves through columns.


val = board[r][c]

Gets the value from the current cell.

Example:

board[0][0] = "5"

Therefore:

val = "5"

Another example:

board[0][2] = "."

Therefore:

val = "."


if val == ".":

Checks whether the current cell is empty.

The symbol "." represents an empty cell.

We use == because we want to compare two values.

We do not use = because = assigns a value.


continue

Skips the current iteration of the loop.

In simple words:

If the cell is empty, ignore it and move
to the next cell.

We do not need to check empty cells.


box_index = (r // 3) * 3 + (c // 3)

THIS IS THE MOST IMPORTANT CALCULATION.

It finds which 3 x 3 box contains the current cell.

We have nine boxes.

Their indexes are:

0 1 2

3 4 5

6 7 8


What does // mean?

// is integer division.

It divides two numbers and removes the decimal part.

Examples:

0 // 3 = 0

1 // 3 = 0

2 // 3 = 0

3 // 3 = 1

4 // 3 = 1

5 // 3 = 1

6 // 3 = 2

7 // 3 = 2

8 // 3 = 2


Let's calculate some box indexes.

Example 1:

r = 0
c = 0

box_index = (0 // 3) * 3 + (0 // 3)

box_index = 0 * 3 + 0

box_index = 0

The cell belongs to box 0.


Example 2:

r = 1
c = 4

box_index = (1 // 3) * 3 + (4 // 3)

box_index = 0 * 3 + 1

box_index = 1

The cell belongs to box 1.


Example 3:

r = 4
c = 7

box_index = (4 // 3) * 3 + (7 // 3)

box_index = 1 * 3 + 2

box_index = 5

The cell belongs to box 5.


if (
    val in rows[r]
    or val in cols[c]
    or val in boxes[box_index]
):

This checks whether the current digit already exists
in any of its three locations.

Let's understand each condition.


val in rows[r]

Checks whether the digit already exists in the current row.

Example:

rows[0] = {"5", "3", "7"}

val = "5"

"5" in rows[0] is True.

This means we found a repeated digit in the row.


val in cols[c]

Checks whether the digit already exists in the current column.

Example:

cols[0] = {"5", "6", "8"}

val = "5"

"5" in cols[0] is True.

This means we found a repeated digit in the column.


val in boxes[box_index]

Checks whether the digit already exists
in the current 3 x 3 box.

Example:

boxes[0] = {"5", "3", "6"}

val = "5"

"5" in boxes[0] is True.

This means we found a repeated digit in the box.


What does OR mean?

or means that at least one condition must be True.

For example:

True or False = True

False or True = True

False or False = False


if any of these three conditions is True:

return False

This means the Sudoku board is invalid.

Why?

Because the digit is repeated in at least one
of the required locations.


rows[r].add(val)

Adds the current digit to its row Hash Set.

Example:

rows[0] = {"5", "3"}

After:

rows[0].add("7")

The result becomes:

rows[0] = {"5", "3", "7"}


cols[c].add(val)

Adds the current digit to its column Hash Set.

We record the digit so that we can detect
a duplicate later in the same column.


boxes[box_index].add(val)

Adds the current digit to its 3 x 3 box Hash Set.

We record the digit so that we can detect
a duplicate later in the same box.


return True

This line runs only if all cells have been checked
without finding a repeated digit.

Therefore, the Sudoku board is valid.


6. DRY RUN: STEP-BY-STEP EXAMPLE
--------------------------------------------------------

Let's use a small part of the board.

First row:

["5", "3", ".", ".", "7", ".", ".", ".", "."]


INITIAL STATE:

rows[0] = set()

cols[0] = set()

boxes[0] = set()


FIRST CELL:

r = 0
c = 0
val = "5"

box_index = 0

Check:

"5" in rows[0]  -> False

"5" in cols[0]  -> False

"5" in boxes[0] -> False

No duplicate.

Add "5" to all three sets.

rows[0] = {"5"}

cols[0] = {"5"}

boxes[0] = {"5"}


SECOND CELL:

r = 0
c = 1
val = "3"

box_index = 0

Check:

"3" in rows[0]  -> False

"3" in cols[1]  -> False

"3" in boxes[0] -> False

No duplicate.

Add "3" to all three sets.

rows[0] = {"5", "3"}

cols[1] = {"3"}

boxes[0] = {"5", "3"}


THIRD CELL:

r = 0
c = 2
val = "."

The cell is empty.

Therefore:

continue

We skip this cell.


FOURTH CELL:

r = 0
c = 3
val = "."

Again, the cell is empty.

We skip it.


FIFTH CELL:

r = 0
c = 4
val = "7"

box_index = 1

Check:

"7" in rows[0]  -> False

"7" in cols[4]  -> False

"7" in boxes[1] -> False

No duplicate.

Add "7" to the three sets.

The same process continues for every cell.

If a repeated digit is found, the function
immediately returns False.

If all cells pass, it returns True.


7. TIME COMPLEXITY
--------------------------------------------------------

O(1) for a fixed 9 x 9 Sudoku board.

Why?

We always have:

9 rows x 9 columns = 81 cells.

We visit every cell once.

For every filled cell, we perform:

- One Hash Set lookup in rows.
- One Hash Set lookup in columns.
- One Hash Set lookup in boxes.
- Three Hash Set insertions.

Hash Set lookup and insertion take O(1)
on average.

Therefore:

81 cells × O(1) operations = O(81)

Since 81 is a fixed number:

TIME COMPLEXITY = O(1)


GENERALIZED VERSION:

If the board size were N x N,
we would visit N x N cells.

Therefore:

TIME COMPLEXITY = O(N²)


8. SPACE COMPLEXITY
--------------------------------------------------------

O(1) for a fixed 9 x 9 Sudoku board.

Why?

We create:

9 Hash Sets for rows.

9 Hash Sets for columns.

9 Hash Sets for boxes.

There are only 27 Hash Sets.

Each set can contain at most 9 different digits.

Therefore, the extra space is bounded by a fixed amount.

SPACE COMPLEXITY = O(1)


GENERALIZED VERSION:

For an N x N board:

- N row sets.
- N column sets.
- N box sets.

Each set can store up to N different values.

Therefore:

N x N = O(N²)

SPACE COMPLEXITY = O(N²)


IMPORTANT:

The space complexity above is auxiliary space.

We do not count the input Sudoku board itself.


9. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

A valid Sudoku board.

Expected: True


Test 2:

Two identical digits in the same row.

Expected: False


Test 3:

Two identical digits in the same column.

Expected: False


Test 4:

Two identical digits in the same 3 x 3 box.

Expected: False


Test 5:

A completely empty Sudoku board.

Expected: True

Reason:
There are no repeated filled digits.


Test 6:

A board with only one filled cell.

Expected: True


Test 7:

Repeated digits in different 3 x 3 boxes,
but the same row.

Expected: False

Reason:
The row rule is violated.


Test 8:

A valid board containing empty cells.

Expected: True


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what a Hash Set is.
[ ] I understand why we use sets for duplicate detection.
[ ] I understand why we create nine row sets.
[ ] I understand why we create nine column sets.
[ ] I understand why we create nine box sets.
[ ] I understand how board[r][c] works.
[ ] I understand why we use two loops.
[ ] I understand why "." cells are skipped.
[ ] I understand how the box_index formula works.
[ ] I understand the // operator.
[ ] I understand the meaning of "or".
[ ] I understand how "in" checks a Hash Set.
[ ] I understand how set.add() works.
[ ] I understand why we return False immediately.
[ ] I understand why we return True at the end.
[ ] I understand O(1) time for a fixed 9 x 9 board.
[ ] I understand O(1) auxiliary space for a fixed board.
[ ] I can write this solution without looking.

========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()


# Valid Sudoku board
valid_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]


# Invalid board: repeated digit in the first row
invalid_row = [
    ["5","3",".",".","7",".",".",".","5"],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]


# Invalid board: repeated digit in the first column
invalid_column = [
    ["5","3",".",".","7",".",".",".","."],
    ["5",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]


# Invalid board: repeated digit inside the top-left 3 x 3 box
invalid_box = [
    ["5","3",".",".","7",".",".",".","."],
    ["6","5",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]


# Completely empty board
empty_board = [
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]


# Board with one filled cell
one_cell_board = [
    ["1",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]


# Invalid board: repeated digit in one row,
# but in two different 3 x 3 boxes
invalid_same_row_different_boxes = [
    ["5",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]


test_cases = [
    ("Valid Sudoku board", valid_board, True),
    ("Repeated digit in a row", invalid_row, False),
    ("Repeated digit in a column", invalid_column, False),
    ("Repeated digit in a 3 x 3 box", invalid_box, False),
    ("Completely empty board", empty_board, True),
    ("Only one filled cell", one_cell_board, True),
    ("Same row, different boxes", invalid_same_row_different_boxes, False),
    ("Valid partially filled board", valid_board, True)
]


passed = 0

print("VALID SUDOKU - TEST RESULTS")
print("----------------------------------------")

for test_name, board, expected in test_cases:

    result = solution.isValidSudoku(board)

    print("Test:", test_name)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
