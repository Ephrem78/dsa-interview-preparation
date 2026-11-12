
"""
========================================================
PROBLEM: BEST TIME TO BUY AND SELL STOCK
TOPIC: ARRAYS AND HASHING
APPROACH: TWO POINTERS + GREEDY
========================================================


1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given an integer array called prices:

Each number represents the stock price on a particular day.

You can:

1. Buy one stock on one day.
2. Sell that stock on a different day in the future.

Your goal is to make the maximum possible profit.

Return the maximum profit.

If you cannot make a profit, return 0.


IMPORTANT RULE:

You must buy before you sell.

You cannot buy and sell on the same day.


2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
prices = [7, 1, 5, 3, 6, 4]

Output:
5

Explanation:

Buy on day 2:

Price = 1

Sell on day 5:

Price = 6

Profit:

6 - 1 = 5

Therefore:

Maximum profit = 5


Example 2:

Input:
prices = [7, 6, 4, 3, 1]

Output:
0

Explanation:

The stock price keeps decreasing.

There is no profitable transaction.

Therefore:

Maximum profit = 0


Example 3:

Input:
prices = [2, 4, 1]

Output:
2

Explanation:

Buy at price 2.

Sell at price 4.

Profit:

4 - 2 = 2

Therefore:

Maximum profit = 2


3. MY APPROACH: TWO POINTERS + GREEDY
--------------------------------------------------------

I use three variables:

1. BUY

   Stores the index of the day we buy the stock.

2. SELL

   Stores the index of the day we sell the stock.

3. PROFIT

   Stores the maximum profit found so far.


My steps:

1. Create buy = 0.

2. Create sell = 1.

3. Create profit = 0.

4. Start a loop from index 1.

5. Calculate the profit:

   prices[sell] - prices[buy]

6. Compare this profit with the maximum profit
   found so far.

7. If the current selling price is smaller
   than the buying price:

   - Move buy to the current sell position.

8. Move sell one position forward.

9. Continue until we reach the end of the list.

10. Return the maximum profit.


IMPORTANT:

We always buy before we sell.

If we find a cheaper stock price,
we update the buying position.

This gives us a better chance
to make a larger profit later.


4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def maxProfit(self, prices: list[int]) -> int:

        # Start the buying pointer at index 0
        buy = 0

        # Start the selling pointer at index 1
        sell = 1

        # Store the maximum profit
        profit = 0

        # Visit each possible selling position
        for i in range(1, len(prices)):

            # Calculate the current profit
            profit = max(profit, prices[sell] - prices[buy])

            # Check whether we found a cheaper buying price
            if prices[sell] < prices[buy]:

                # Move the buying pointer to the cheaper price
                buy = sell

            # Move the selling pointer forward
            sell += 1

        # Return the maximum profit
        return profit


"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------

class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.


def maxProfit(self, prices: list[int]) -> int:

Creates a method called maxProfit.

self:
Refers to the current object of the class.

prices:
The input list containing stock prices.

list[int]:
Means the input is a list of integers.

-> int:
Means the method returns an integer.


buy = 0

Creates the buying pointer.

It starts at index 0.

This means we initially consider buying
on the first day.


sell = 1

Creates the selling pointer.

It starts at index 1.

Why?

Because we must sell after buying.

We cannot buy and sell on the same day.

Therefore, sell starts one position
after buy.


profit = 0

Creates a variable to store the maximum profit.

At the beginning, we have not made any profit.

Therefore:

profit = 0


for i in range(1, len(prices)):

Starts a loop from index 1.

range(1, len(prices)) means:

Start at index 1.

Continue until the last index.

Why start at 1?

Because index 0 is our initial buying position.

We need to check selling prices
starting from the second day.


profit = max(profit, prices[sell] - prices[buy])

This is one of the most important lines.

First:

prices[sell] - prices[buy]

Calculates the current profit.

Example:

prices[buy] = 1
prices[sell] = 6

Calculate:

6 - 1 = 5

We make 5 units of profit.

Now:

max(profit, 5)

Compares:

1. The maximum profit found so far.
2. The current possible profit.

max() returns the larger value.

Example:

profit = 3
current profit = 5

Python calculates:

max(3, 5)

Result:

profit = 5

This ensures we always keep
the highest profit found so far.


if prices[sell] < prices[buy]:

Checks whether the current selling price
is cheaper than our current buying price.

Example:

prices[buy] = 7
prices[sell] = 1

Python checks:

1 < 7

This is True.

Why is this important?

Because buying at price 1 is better
than buying at price 7.

A cheaper buying price gives us
a better opportunity to make profit later.


buy = sell

Moves the buying pointer to the current
selling position.

Example:

buy = 0
sell = 1

If the current price at sell is cheaper,
we update:

buy = 1

Now we consider buying on day 2.

IMPORTANT:

We are not actually selling the stock here.

We are simply changing our best buying position.

We are looking for a cheaper price
to use for a future transaction.


sell += 1

Moves the selling pointer one position forward.

It is the same as:

sell = sell + 1

Why?

Because we need to check the next day's price.

We always move forward through time.


return profit

Returns the maximum profit found.

If no profitable transaction exists,
profit remains 0.

Therefore, the method returns 0.


6. HOW THE ALGORITHM WORKS
--------------------------------------------------------

Example:

prices = [7, 1, 5, 3, 6, 4]


STARTING VALUES:

buy = 0
sell = 1
profit = 0


DAY 1:

Buy price = 7
Sell price = 1

Current profit:

1 - 7 = -6

Maximum profit remains 0.

Because 1 is cheaper than 7:

buy = 1

Move sell forward.


DAY 2:

Buy price = 1
Sell price = 5

Current profit:

5 - 1 = 4

Maximum profit:

profit = 4

Move sell forward.


DAY 3:

Buy price = 1
Sell price = 3

Current profit:

3 - 1 = 2

Maximum profit remains 4.

Move sell forward.


DAY 4:

Buy price = 1
Sell price = 6

Current profit:

6 - 1 = 5

Maximum profit:

profit = 5

Move sell forward.


DAY 5:

Buy price = 1
Sell price = 4

Current profit:

4 - 1 = 3

Maximum profit remains 5.


FINAL ANSWER:

profit = 5


7. TIME COMPLEXITY
--------------------------------------------------------

O(N)

Where:

N = Number of elements in prices.

Why?

We use one for loop:

for i in range(1, len(prices)):

The loop visits each price once.

For every iteration, we perform
a fixed number of operations:

- Calculate the current profit.
- Compare prices.
- Update buy if necessary.
- Move sell forward.

These operations take constant time.

Therefore:

N elements × O(1)

= O(N)

TIME COMPLEXITY = O(N)


8. SPACE COMPLEXITY
--------------------------------------------------------

O(1)

Why?

We only create three main variables:

buy
sell
profit

These variables do not grow when
the input list becomes larger.

We do not create:

- Another list.
- A dictionary.
- A heap.
- An additional array.

Therefore:

SPACE COMPLEXITY = O(1)

This is called constant extra space.


9. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

Input:
prices = [7, 1, 5, 3, 6, 4]

Expected:
5

Reason:
Buy at 1 and sell at 6.


Test 2:

Input:
prices = [7, 6, 4, 3, 1]

Expected:
0

Reason:
The prices keep decreasing.
No profit is possible.


Test 3:

Input:
prices = [2, 4, 1]

Expected:
2

Reason:
Buy at 2 and sell at 4.


Test 4:

Input:
prices = [1, 2, 3, 4, 5]

Expected:
4

Reason:
Buy at 1 and sell at 5.


Test 5:

Input:
prices = [5, 5, 5, 5]

Expected:
0

Reason:
The prices never increase.


Test 6:

Input:
prices = [3, 2, 6, 5, 0, 3]

Expected:
4

Reason:
Buy at 2 and sell at 6.


Test 7:

Input:
prices = [1, 10]

Expected:
9

Reason:
Buy at 1 and sell at 10.


Test 8:

Input:
prices = [10, 1, 2, 3, 4, 5]

Expected:
4

Reason:
Buy at 1 and sell at 5.


Test 9:

Input:
prices = [2]

Expected:
0

Reason:
There is only one day.
We cannot buy and sell on different days.


Test 10:

Input:
prices = []

Expected:
0

Reason:
There are no stock prices.


========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand what stock prices represent.
[ ] I understand what buying and selling mean.
[ ] I understand why buying must happen before selling.
[ ] I understand what the buy pointer stores.
[ ] I understand what the sell pointer stores.
[ ] I understand what the profit variable stores.
[ ] I understand how prices[sell] - prices[buy] works.
[ ] I understand how max() works.
[ ] I understand why we update buy when we find a cheaper price.
[ ] I understand why sell moves forward.
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
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([2, 4, 1], 2),
    ([1, 2, 3, 4, 5], 4),
    ([5, 5, 5, 5], 0),
    ([3, 2, 6, 5, 0, 3], 4),
    ([1, 10], 9),
    ([10, 1, 2, 3, 4, 5], 4),
    ([2], 0),
    ([], 0)
]

passed = 0

print("BEST TIME TO BUY AND SELL STOCK - TEST RESULTS")
print("----------------------------------")

for prices, expected in test_cases:

    result = solution.maxProfit(prices)

    print("Prices:", prices)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
