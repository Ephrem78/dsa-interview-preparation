
"""
========================================================
PROBLEM: KOKO EATING BANANAS
TOPIC: BINARY SEARCH
APPROACH: BINARY SEARCH ON THE ANSWER
========================================================
1. PROBLEM DESCRIPTION
--------------------------------------------------------
Koko has n piles of bananas.
Each pile contains a certain number of bananas.
The guards will return after h hours.
Koko chooses an eating speed k:
- She eats k bananas per hour from one chosen pile.
- If the pile has fewer than k bananas, she eats all of it.
- She can only eat from one pile during each hour.
- She cannot switch to another pile during the same hour.
Return the minimum integer speed k that allows Koko to
finish all bananas within h hours.
In simple words:
Find the slowest eating speed that finishes all piles
before the guards return.
IMPORTANT:
Each pile needs its own number of hours.
We calculate the hours for every pile and add them.
2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------
Example 1:
Input:
piles = [3, 6, 7, 11]
h = 8
Output:
4
Explanation:
At speed 4:
Pile 1: 3 bananas -> 1 hour
Pile 2: 6 bananas -> 2 hours
Pile 3: 7 bananas -> 2 hours
Pile 4: 11 bananas -> 3 hours
Total:
1 + 2 + 2 + 3 = 8 hours
Koko finishes within 8 hours.
Speed 3 would take:
1 + 2 + 3 + 4 = 10 hours
Therefore, the minimum valid speed is 4.
Example 2:
Input:
piles = [30, 11, 23, 4, 20]
h = 5
Output:
30
Explanation:
There are five piles and only five hours.
Koko must finish one pile in each hour.
The minimum speed is the size of the largest pile:
30 bananas per hour.
Example 3:
Input:
piles = [30, 11, 23, 4, 20]
h = 6
Output:
23
Explanation:
At speed 23:
30 -> 2 hours
11 -> 1 hour
23 -> 1 hour
4 -> 1 hour
20 -> 1 hour
Total = 6 hours.
3. MY APPROACH: BINARY SEARCH ON THE ANSWER
--------------------------------------------------------
I use one main algorithm:
1. BINARY SEARCH
IMPORTANT:
We are not searching for a banana pile.
We are searching for the minimum possible eating speed.
The possible speeds are:
1, 2, 3, 4, 5, ..., maximum pile size.
WHY DOES BINARY SEARCH WORK?
If Koko can finish at speed 5:
She can also finish at speed 6, 7, 8, and higher.
A faster speed cannot require more hours.
If Koko cannot finish at speed 5:
She also cannot finish at speed 4, 3, 2, or 1.
This creates a pattern:
Speed:       1  2  3  4  5  6  7  8
Can finish:  No No No Yes Yes Yes Yes Yes
We want the FIRST speed that can finish.
MY STEPS:
1. Set left = 1 because the minimum speed is 1.
2. Find the largest pile.
3. Set right equal to the largest pile.
4. Continue while left is smaller than right.
5. Calculate the middle speed.
6. Check whether Koko can finish at that speed.
7. If she can finish:
   a. The speed is valid.
   b. Search for a smaller speed.
   c. Set right = mid.
8. If she cannot finish:
   a. The speed is too slow.
   b. Search for a faster speed.
   c. Set left = mid + 1.
9. When left equals right, return that speed.
4. PYTHON SOLUTION
--------------------------------------------------------
"""
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # The smallest possible eating speed is 1
        left = 1
        # The largest possible speed is the largest pile
        right = max(piles)
        # Search while more than one possible speed remains
        while left < right:
            # Calculate the middle possible speed
            mid = left + (right - left) // 2
            # Check whether Koko can finish at this speed
            if self.canFinish(piles, mid, h):
                # This speed works, so try a smaller speed
                right = mid
            else:
                # This speed is too slow, so try a faster speed
                left = mid + 1
        # Left is now the minimum valid eating speed
        return left

    def canFinish(self, piles: list[int], speed: int, h: int) -> bool:
        # Store the total number of hours needed
        hours = 0
        # Calculate the hours needed for every pile
        for pile in piles:
            # Calculate ceiling division without floating-point numbers
            hours += (pile + speed - 1) // speed
        # Check whether Koko can finish within the allowed hours
        return hours <= h

"""
5. EXPLANATION OF IMPORTANT LINES
--------------------------------------------------------
class Solution:
Creates a class called Solution.
LeetCode commonly uses this class structure.
def minEatingSpeed(self, piles: list[int], h: int) -> int:
Creates the main function.
piles:
A list containing the number of bananas in each pile.
h:
The maximum number of hours available.
-> int:
The function returns an integer: the minimum eating speed.
A. INITIALIZE THE LEFT BOUNDARY
--------------------------------------------------------
left = 1
The minimum possible eating speed is 1 banana per hour.
Koko cannot eat zero bananas per hour because she must
finish the piles.
Therefore:
left = 1
B. INITIALIZE THE RIGHT BOUNDARY
--------------------------------------------------------
right = max(piles)
max() returns the largest value in the piles list.
Why is the largest pile a valid upper boundary?
If Koko eats at the speed of the largest pile:
She can finish every pile in one hour or less.
Example:
piles = [3, 6, 7, 11]
max(piles) = 11
At speed 11:
3 -> 1 hour
6 -> 1 hour
7 -> 1 hour
11 -> 1 hour
Total = 4 hours.
The right boundary is a speed that can finish all piles,
assuming h is at least the number of piles.
C. START THE BINARY SEARCH
--------------------------------------------------------
while left < right:
This loop continues while more than one possible speed
remains.
Example:
left = 1
right = 11
1 < 11
Result: True.
WHY USE < INSTEAD OF <=?
We are searching for the first valid speed.
When left equals right, only one possible answer remains.
There is no need to continue.
D. CALCULATE THE MIDDLE SPEED
--------------------------------------------------------
mid = left + (right - left) // 2
Calculates the middle possible eating speed.
Example:
left = 1
right = 11
mid = 1 + (11 - 1) // 2
mid = 6
The speed we are testing is 6 bananas per hour.
WHY USE //?
// performs integer division.
Example:
10 // 2 = 5
We need an integer eating speed.
E. CHECK WHETHER THE SPEED WORKS
--------------------------------------------------------
if self.canFinish(piles, mid, h):
Calls another method named canFinish().
We give it three values:
piles = The banana piles.
mid = The speed we want to test.
h = The maximum allowed hours.
self:
Refers to the current Solution object.
canFinish() checks whether the total required hours are
less than or equal to h.
It returns:
True = Koko can finish.
False = Koko cannot finish.
F. IF THE SPEED WORKS, SEARCH LEFT
--------------------------------------------------------
right = mid
This runs when canFinish() returns True.
It means the current speed is fast enough.
But we want the MINIMUM valid speed.
Therefore, we try smaller speeds.
Example:
left = 1
right = 11
mid = 6
If speed 6 works:
right = 6
New search area:
1 to 6
IMPORTANT:
Why do we use right = mid instead of mid - 1?
Because mid is already a valid answer.
We must keep it as a possible answer.
G. IF THE SPEED DOES NOT WORK, SEARCH RIGHT
--------------------------------------------------------
left = mid + 1
This runs when canFinish() returns False.
It means the current speed is too slow.
We must try a faster speed.
Example:
left = 1
right = 6
mid = 3
If speed 3 does not work:
left = 4
New search area:
4 to 6
WHY mid + 1?
Because we already know mid is too slow.
There is no reason to test it again.
H. RETURN THE MINIMUM SPEED
--------------------------------------------------------
return left
When the loop finishes:
left == right
Only one possible answer remains.
Because of our binary search decisions, this is the
smallest speed that can finish all piles within h hours.
6. UNDERSTANDING THE canFinish() METHOD
--------------------------------------------------------
def canFinish(self, piles: list[int], speed: int, h: int) -> bool:
This method answers one question:
Can Koko finish all piles using this speed?
It does not find the minimum speed.
It only checks one speed.
A. INITIALIZE THE HOURS
--------------------------------------------------------
hours = 0
Stores the total hours needed for all piles.
We start at zero because no pile has been processed yet.
B. VISIT EVERY PILE
--------------------------------------------------------
for pile in piles:
The loop visits each pile one by one.
Example:
piles = [3, 6, 7, 11]
The loop visits:
pile = 3
pile = 6
pile = 7
pile = 11
C. CALCULATE THE HOURS FOR ONE PILE
--------------------------------------------------------
hours += (pile + speed - 1) // speed
THIS IS THE MOST IMPORTANT LINE IN canFinish().
It calculates how many complete hours Koko needs for
one pile.
We must round UP because Koko cannot use part of an hour
to finish a pile.
Example:
pile = 7
speed = 4
7 / 4 = 1.75
Koko needs 2 complete hours.
Therefore:
hours = 2
WHY NOT USE NORMAL DIVISION?
If we use:
7 / 4
Python returns:
1.75
But the required hours must be an integer.
WHY NOT USE int(pile / speed)?
int(1.75) returns 1.
That rounds DOWN.
We need to round UP.
We can use math.ceil(), but integer division is simpler.
INTEGER CEILING DIVISION:
(pile + speed - 1) // speed
Example 1:
pile = 7
speed = 4
(7 + 4 - 1) // 4
10 // 4
2
Example 2:
pile = 8
speed = 4
(8 + 4 - 1) // 4
11 // 4
2
Example 3:
pile = 9
speed = 4
(9 + 4 - 1) // 4
12 // 4
3
Example 4:
pile = 3
speed = 4
(3 + 4 - 1) // 4
6 // 4
1
IMPORTANT:
Even if the pile has fewer bananas than the speed,
Koko still uses one complete hour.
The += operation means:
Add the hours for this pile to the total hours.
D. CHECK THE TOTAL HOURS
--------------------------------------------------------
return hours <= h
Compares the required hours with the available hours.
Example:
hours = 8
h = 8
8 <= 8
True.
Koko can finish on time.
Another example:
hours = 10
h = 8
10 <= 8
False.
Koko cannot finish on time.
7. COMPLETE DRY RUN
--------------------------------------------------------
Input:
piles = [3, 6, 7, 11]
h = 8
INITIAL STATE:
left = 1
right = max(piles)
right = 11
ITERATION 1:
--------------------------------------------------------
left = 1
right = 11
Calculate middle:
mid = 1 + (11 - 1) // 2
mid = 6
Test speed = 6.
CALL canFinish(piles, 6, 8):
Pile 1:
3 bananas
(3 + 6 - 1) // 6 = 8 // 6 = 1 hour
hours = 1
Pile 2:
6 bananas
(6 + 6 - 1) // 6 = 11 // 6 = 1 hour
hours = 2
Pile 3:
7 bananas
(7 + 6 - 1) // 6 = 12 // 6 = 2 hours
hours = 4
Pile 4:
11 bananas
(11 + 6 - 1) // 6 = 16 // 6 = 2 hours
hours = 6
Total:
hours = 6
Check:
6 <= 8
True.
Speed 6 works.
Search for a smaller speed:
right = mid
right = 6
New state:
left = 1
right = 6
ITERATION 2:
--------------------------------------------------------
left = 1
right = 6
Calculate middle:
mid = 1 + (6 - 1) // 2
mid = 3
Test speed = 3.
CALL canFinish(piles, 3, 8):
Pile 1:
3 bananas -> 1 hour
Pile 2:
6 bananas -> 2 hours
Pile 3:
7 bananas -> 3 hours
Pile 4:
11 bananas -> 4 hours
Total:
hours = 1 + 2 + 3 + 4
hours = 10
Check:
10 <= 8
False.
Speed 3 does not work.
Search for a faster speed:
left = mid + 1
left = 4
New state:
left = 4
right = 6
ITERATION 3:
--------------------------------------------------------
left = 4
right = 6
Calculate middle:
mid = 4 + (6 - 4) // 2
mid = 5
Test speed = 5.
CALL canFinish(piles, 5, 8):
Pile 1:
3 bananas -> 1 hour
Pile 2:
6 bananas -> 2 hours
Pile 3:
7 bananas -> 2 hours
Pile 4:
11 bananas -> 3 hours
Total:
hours = 1 + 2 + 2 + 3
hours = 8
Check:
8 <= 8
True.
Speed 5 works.
Search for a smaller speed:
right = mid
right = 5
New state:
left = 4
right = 5
ITERATION 4:
--------------------------------------------------------
left = 4
right = 5
Calculate middle:
mid = 4 + (5 - 4) // 2
mid = 4
Test speed = 4.
CALL canFinish(piles, 4, 8):
Pile 1:
3 bananas -> 1 hour
Pile 2:
6 bananas -> 2 hours
Pile 3:
7 bananas -> 2 hours
Pile 4:
11 bananas -> 3 hours
Total:
hours = 1 + 2 + 2 + 3
hours = 8
Check:
8 <= 8
True.
Speed 4 works.
Search for a smaller speed:
right = mid
right = 4
New state:
left = 4
right = 4
THE LOOP FINISHES:
Condition:
left < right
4 < 4
False.
Return:
left = 4
FINAL RESULT:
Minimum eating speed = 4 bananas per hour.
8. WHY THIS IS BINARY SEARCH ON THE ANSWER
--------------------------------------------------------
Normal binary search:
We search for a target inside sorted data.
Binary search on the answer:
We search for the smallest possible answer that satisfies
a condition.
In this problem:
The answer is the eating speed.
The condition is:
Can Koko finish within h hours?
Example:
Speed:       1   2   3   4   5   6   7   8
Can finish:  No  No  No  Yes Yes Yes Yes Yes
This is called a monotonic condition.
WHY MONOTONIC?
If one speed works, every faster speed also works.
If one speed fails, every slower speed also fails.
This lets us eliminate half of the possible speeds each
time.
IMPORTANT:
The condition must follow this pattern for binary search
on the answer to work.
9. TIME COMPLEXITY
--------------------------------------------------------
O(N * log M)
Where:
N = Number of banana piles.
M = Size of the largest pile.
A. FIND THE LARGEST PILE
--------------------------------------------------------
right = max(piles)
Python checks the piles to find the largest value.
It visits N elements.
Time:
O(N)
B. BINARY SEARCH
--------------------------------------------------------
while left < right:
The possible speeds are from 1 to M.
Binary search cuts this range approximately in half
after every iteration.
Number of iterations:
O(log M)
C. CHECK ONE SPEED
--------------------------------------------------------
self.canFinish(piles, mid, h)
The canFinish() method visits every pile once.
There are N piles.
Time for one check:
O(N)
D. TOTAL TIME COMPLEXITY
--------------------------------------------------------
Binary search performs O(log M) checks.
Each check takes O(N).
Therefore:
O(N) * O(log M)
TIME COMPLEXITY = O(N * log M)
The initial max(piles) operation takes O(N), which does
not change the final Big O result.
IMPORTANT:
The canFinish() method is called inside the binary search.
That is why we multiply the two costs.
10. SPACE COMPLEXITY
--------------------------------------------------------
O(1)
Why?
We use a fixed number of variables:
left
right
mid
hours
pile
speed
m
No new list or data structure grows with the input size.
The canFinish() method processes one pile at a time.
It does not store all the calculated hours in another list.
Therefore:
SPACE COMPLEXITY = O(1)
IMPORTANT:
The input piles list is not counted as extra space.
11. EDGE CASES
--------------------------------------------------------
EDGE CASE 1: ONE PILE
Input:
piles = [5]
h = 1
Expected:
5
Reason:
Koko has only one hour.
She must eat all five bananas in that hour.
EDGE CASE 2: ONE PILE WITH EXTRA HOURS
Input:
piles = [5]
h = 5
Expected:
1
Reason:
She can eat one banana per hour.
EDGE CASE 3: ALL PILES ARE EQUAL
Input:
piles = [4, 4, 4]
h = 3
Expected:
4
Reason:
She has exactly one hour for each pile.
EDGE CASE 4: MINIMUM POSSIBLE SPEED
Input:
piles = [1, 1, 1]
h = 6
Expected:
1
Reason:
Speed 1 is already enough.
EDGE CASE 5: ONLY ONE EXTRA HOUR
Input:
piles = [3, 6, 7, 11]
h = 5
Expected:
11
Reason:
There are four piles and five hours.
Speed 10 requires:
1 + 1 + 1 + 2 = 5 hours.
Correction:
The minimum speed is 10, not 11.
EDGE CASE 6: SPEED EQUALS THE LARGEST PILE
Input:
piles = [30, 11, 23, 4, 20]
h = 5
Expected:
30
Reason:
There are five piles and only five hours.
Each pile must take one hour.
EDGE CASE 7: LARGE PILE
Input:
piles = [1000000000]
h = 2
Expected:
500000000
Reason:
Koko must eat half the pile in each of two hours.
12. MY OWN TEST CASES
--------------------------------------------------------
Test 1:
piles = [3, 6, 7, 11]
h = 8
Expected: 4
Test 2:
piles = [30, 11, 23, 4, 20]
h = 5
Expected: 30
Test 3:
piles = [30, 11, 23, 4, 20]
h = 6
Expected: 23
Test 4:
piles = [5]
h = 1
Expected: 5
Test 5:
piles = [5]
h = 5
Expected: 1
Test 6:
piles = [4, 4, 4]
h = 3
Expected: 4
Test 7:
piles = [1, 1, 1]
h = 6
Expected: 1
Test 8:
piles = [3, 6, 7, 11]
h = 5
Expected: 10
Test 9:
piles = [1000000000]
h = 2
Expected: 500000000
Test 10:
piles = [9, 9, 9, 9]
h = 8
Expected: 5
========================================================
MY LEARNING CHECKLIST
========================================================
[ ] I understand the Koko Eating Bananas problem.
[ ] I understand what eating speed means.
[ ] I understand why each pile needs at least one hour.
[ ] I understand why we search for the minimum speed.
[ ] I understand why left starts at 1.
[ ] I understand why right is max(piles).
[ ] I understand what binary search on the answer means.
[ ] I understand what a monotonic condition is.
[ ] I understand why a faster speed cannot need more hours.
[ ] I understand what the while left < right condition means.
[ ] I understand how mid is calculated.
[ ] I understand why canFinish() is a separate method.
[ ] I understand how canFinish() checks one speed.
[ ] I understand why we count hours for every pile.
[ ] I understand why we round up the hours for each pile.
[ ] I understand how integer ceiling division works.
[ ] I understand why normal int division would be incorrect.
[ ] I understand what hours <= h checks.
[ ] I understand why right = mid keeps a valid answer.
[ ] I understand why left = mid + 1 removes an invalid speed.
[ ] I understand why the answer is left when the loop ends.
[ ] I understand why time complexity is O(N * log M).
[ ] I understand why space complexity is O(1).
[ ] I can write this solution without looking.
========================================================
"""
# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------
solution = Solution()
test_cases = [
    ([3, 6, 7, 11], 8, 4),
    ([30, 11, 23, 4, 20], 5, 30),
    ([30, 11, 23, 4, 20], 6, 23),
    ([5], 1, 5),
    ([5], 5, 1),
    ([4, 4, 4], 3, 4),
    ([1, 1, 1], 6, 1),
    ([3, 6, 7, 11], 5, 10),
    ([1000000000], 2, 500000000),
    ([9, 9, 9, 9], 8, 5)
]
passed = 0
print("KOKO EATING BANANAS - TEST RESULTS")
print("----------------------------------------------")
for piles, h, expected in test_cases:
    result = solution.minEatingSpeed(piles, h)
    print("Piles:", piles)
    print("Available hours:", h)
    print("Expected:", expected)
    print("Actual:", result)
    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")
    print("----------------------------------------------")
print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
