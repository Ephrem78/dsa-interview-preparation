"""
========================================================
PROBLEM: CAR FLEET
TOPIC: STACKS / SORTING
APPROACH: 2D ARRAY + SORTING
========================================================

1. PROBLEM DESCRIPTION
--------------------------------------------------------

Given:

- An integer called target.
- An integer array called position.
- An integer array called speed.

Each car has:
- A starting position.
- A driving speed.

All cars are travelling toward the same destination.

A car cannot pass another car.

If a faster car catches a slower car:
- The faster car must slow down.
- Both cars drive together.
- They become one car fleet.

A car fleet can contain:
- One car.
- Two cars.
- Many cars.

Our task:

Return the total number of car fleets that arrive
at the destination.

2. EXAMPLE INPUT AND OUTPUT
--------------------------------------------------------

Example 1:

Input:
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

Output:
3

Explanation:

Calculate the time each car needs to reach target.

Car at position 10:
Distance = 12 - 10 = 2
Speed = 2
Time = 2 / 2 = 1 hour

Car at position 8:
Distance = 12 - 8 = 4
Speed = 4
Time = 4 / 4 = 1 hour

Car at position 0:
Distance = 12 - 0 = 12
Speed = 1
Time = 12 / 1 = 12 hours

Car at position 5:
Distance = 12 - 5 = 7
Speed = 1
Time = 7 / 1 = 7 hours

Car at position 3:
Distance = 12 - 3 = 9
Speed = 3
Time = 9 / 3 = 3 hours

Now sort cars by position, from closest to target
to farthest from target.

Position    Arrival Time
10          1
8           1
5           7
3           3
0           12

Fleet formation:

1. Car at position 10 needs 1 hour.
   It creates Fleet 1.

2. Car at position 8 needs 1 hour.
   It joins Fleet 1.
   It cannot arrive before the car ahead.

3. Car at position 5 needs 7 hours.
   It creates Fleet 2.

4. Car at position 3 needs 3 hours.
   It catches up to the fleet ahead.
   It joins Fleet 2.

5. Car at position 0 needs 12 hours.
   It creates Fleet 3.

Final answer:

3 car fleets.

3. MY APPROACH: 2D ARRAY + SORTING
--------------------------------------------------------

We use one 2D list called cars.

Each row stores:

[position, arrival_time]

For example:

cars = [
    [10, 1.0],
    [8, 1.0],
    [0, 12.0],
    [5, 7.0],
    [3, 3.0]
]

STEP 1: Calculate arrival time.

Formula:

arrival_time = (target - position) / speed

STEP 2: Store each car's position and arrival time.

Each car becomes:

[position, arrival_time]

STEP 3: Sort the cars by position in descending order.

Why?

We need to process the car closest to the destination
first.

The car closest to the destination controls what
happens to the cars behind it.

STEP 4: Create a fleet counter.

count = 0

This stores the number of fleets.

STEP 5: Create a variable called prev_time.

prev_time = 0

It stores the arrival time of the fleet ahead.

Initially, no fleet exists.

STEP 6: Visit each car in sorted order.

Compare its arrival time with prev_time.

CASE 1:

arrival_time > prev_time

The current car needs more time than the fleet ahead.

It cannot catch that fleet.

Therefore, it creates a new fleet.

Actions:

count += 1
prev_time = arrival_time

CASE 2:

arrival_time <= prev_time

The current car needs the same or less time.

It can catch the fleet ahead before or exactly
at the destination.

Therefore, it joins the fleet ahead.

We do not increase count.

We do not update prev_time.

STEP 7:

Return count.

4. PYTHON SOLUTION
--------------------------------------------------------
"""

class Solution:

    def carFleet(
        self,
        target: int,
        position: list[int],
        speed: list[int]
    ) -> int:

        # Store each car's position and arrival time
        cars = []

        for i in range(len(position)):

            arrival_time = (
                (target - position[i]) / speed[i]
            )

            cars.append((position[i], arrival_time))

        # Sort cars from closest to target to farthest
        cars.sort(reverse=True)

        # Count the number of car fleets
        count = 0

        # Store the arrival time of the fleet ahead
        prev_time = 0

        # Process every car from front to back
        for car_position, arrival_time in cars:

            # A slower arrival time creates a new fleet
            if arrival_time > prev_time:

                count += 1

                prev_time = arrival_time

            # Otherwise, the car joins the fleet ahead

        return count

"""
5. COMPLETE ELS10 LINE-BY-LINE EXPLANATION
--------------------------------------------------------

CLASS DEFINITION
--------------------------------------------------------

class Solution:

Creates a class called Solution.

LeetCode commonly uses this class structure.

We put our solution function inside this class.

FUNCTION DEFINITION
--------------------------------------------------------

def carFleet(
    self,
    target: int,
    position: list[int],
    speed: list[int]
) -> int:

Creates a function called carFleet.

self:
Refers to the current object of the class.

target:
The destination position.

position:
A list containing the starting positions of the cars.

speed:
A list containing the speeds of the cars.

-> int:
Means that the function returns an integer.

Why an integer?

Because we need to return the total number of fleets.

CARS = []
--------------------------------------------------------

cars = []

Creates an empty list.

We use this list to store information about every car.

Each car will contain two values:

(position, arrival_time)

Example:

(10, 1.0)

Means:

The car starts at position 10.
The car needs 1 hour to reach the destination.

Why do we need arrival time?

Because arrival time helps us understand whether
a car can catch the fleet ahead.

FOR LOOP
--------------------------------------------------------

for i in range(len(position)):

Visits every car using its index.

len(position):

Returns the total number of cars.

Example:

position = [10, 8, 0, 5, 3]

len(position) = 5

range(5) produces:

0, 1, 2, 3, 4

Therefore, the loop visits every car.

Why use i?

Because we need to access the same car's position
and speed from two different lists.

ARRIVAL TIME CALCULATION
--------------------------------------------------------

arrival_time = (
    (target - position[i]) / speed[i]
)

This is the most important calculation.

We calculate how many hours each car needs
to reach the destination.

Formula:

Time = Distance / Speed

Distance:

target - position[i]

Why?

Because the destination is ahead of the car.

Example:

target = 12
position[i] = 10

Distance = 12 - 10 = 2 miles.

Speed:

speed[i]

Example:

speed[i] = 2 miles per hour.

Therefore:

Time = 2 / 2 = 1 hour.

Python's / operator returns a floating-point number.

This is important because arrival times can contain
decimal values.

APPENDING CAR INFORMATION
--------------------------------------------------------

cars.append((position[i], arrival_time))

append():

Adds a new item to the end of a list.

We add a tuple containing:

(position, arrival_time)

Example:

cars.append((10, 1.0))

The list becomes:

[(10, 1.0)]

After processing every car:

cars = [
    (10, 1.0),
    (8, 1.0),
    (0, 12.0),
    (5, 7.0),
    (3, 3.0)
]

IMPORTANT:

We store both values together.

This helps us keep each car's position
connected to its arrival time.

SORTING
--------------------------------------------------------

cars.sort(reverse=True)

sort():

Sorts the items in the list.

reverse=True:

Sorts the list in descending order.

Example:

Before sorting:

[
    (10, 1.0),
    (8, 1.0),
    (0, 12.0),
    (5, 7.0),
    (3, 3.0)
]

After sorting:

[
    (10, 1.0),
    (8, 1.0),
    (5, 7.0),
    (3, 3.0),
    (0, 12.0)
]

Why does this work?

Python sorts tuples by their first value first.

The first value is the car's position.

Therefore, cars are sorted from the highest position
to the lowest position.

This means:

Closest to destination first.
Farthest from destination last.

IMPORTANT:

We need this order because cars cannot pass
the cars ahead of them.

We must process the front cars before the cars behind.

FLEET COUNTER
--------------------------------------------------------

count = 0

Creates a variable called count.

It stores the number of fleets we have found.

Initially:

count = 0

No fleet has been counted yet.

PREVIOUS FLEET TIME
--------------------------------------------------------

prev_time = 0

Creates a variable called prev_time.

It stores the arrival time of the fleet ahead.

Initially:

prev_time = 0

Why zero?

All valid cars have a positive arrival time.

Therefore, the first car will create a new fleet.

PROCESSING EVERY CAR
--------------------------------------------------------

for car_position, arrival_time in cars:

Visits every car in the sorted list.

Each car contains two values:

(position, arrival_time)

Python automatically unpacks these two values.

Example:

car = (10, 1.0)

Python assigns:

car_position = 10
arrival_time = 1.0

Next:

car = (8, 1.0)

Python assigns:

car_position = 8
arrival_time = 1.0

We do not need the position after sorting.

We mainly need arrival_time to count fleets.

THE IMPORTANT IF CONDITION
--------------------------------------------------------

if arrival_time > prev_time:

Compares the current car's arrival time
with the arrival time of the fleet ahead.

Let's understand both situations.

SITUATION 1: NEW FLEET
--------------------------------------------------------

if arrival_time > prev_time:

Example:

prev_time = 1

arrival_time = 7

The current car needs 7 hours.

The fleet ahead needs 1 hour.

The current car is too slow to catch the fleet ahead.

Therefore:

It creates a new fleet.

count += 1

Increases the fleet counter by 1.

This is the same as:

count = count + 1

Example:

Before:

count = 1

After:

count = 2

prev_time = arrival_time

Updates the previous fleet arrival time.

Example:

Before:

prev_time = 1

Current arrival_time = 7

After:

prev_time = 7

Why update it?

Because this new fleet is now the fleet immediately
ahead of the remaining cars.

The next car must be compared with this fleet.

SITUATION 2: JOINS EXISTING FLEET
--------------------------------------------------------

When:

arrival_time <= prev_time

The current car needs the same or less time
than the fleet ahead.

It can catch that fleet.

Example:

prev_time = 7

arrival_time = 3

The current car would arrive in 3 hours
if it could drive freely.

But it cannot pass the fleet ahead.

It catches the fleet and slows down.

It joins the fleet.

Therefore:

We do not increase count.

We do not update prev_time.

Why not update prev_time?

Because the fleet ahead still determines
the arrival time of the combined fleet.

IMPORTANT:

If arrival_time equals prev_time,
the cars are also one fleet.

Even if they meet exactly at the destination,
they count as one fleet.

RETURN
--------------------------------------------------------

return count

Returns the total number of car fleets.

Example:

count = 3

Output:

3

6. STEP-BY-STEP DRY RUN
--------------------------------------------------------

Input:

target = 12

position = [10, 8, 0, 5, 3]

speed = [2, 4, 1, 1, 3]

STEP 1: CALCULATE ARRIVAL TIMES

Position 10:

(12 - 10) / 2 = 1

Position 8:

(12 - 8) / 4 = 1

Position 0:

(12 - 0) / 1 = 12

Position 5:

(12 - 5) / 1 = 7

Position 3:

(12 - 3) / 3 = 3

STEP 2: CREATE THE 2D LIST

cars = [
    (10, 1),
    (8, 1),
    (0, 12),
    (5, 7),
    (3, 3)
]

STEP 3: SORT BY POSITION

cars = [
    (10, 1),
    (8, 1),
    (5, 7),
    (3, 3),
    (0, 12)
]

STEP 4: INITIALIZE VARIABLES

count = 0

prev_time = 0

STEP 5: PROCESS THE CARS

CAR 1:

Position = 10
Arrival time = 1

Compare:

1 > 0

True.

A new fleet is created.

count = 1

prev_time = 1

CAR 2:

Position = 8
Arrival time = 1

Compare:

1 > 1

False.

This car joins Fleet 1.

count = 1

prev_time = 1

CAR 3:

Position = 5
Arrival time = 7

Compare:

7 > 1

True.

A new fleet is created.

count = 2

prev_time = 7

CAR 4:

Position = 3
Arrival time = 3

Compare:

3 > 7

False.

This car joins Fleet 2.

count = 2

prev_time = 7

CAR 5:

Position = 0
Arrival time = 12

Compare:

12 > 7

True.

A new fleet is created.

count = 3

prev_time = 12

FINAL RESULT:

return count

Output:

3

7. TIME COMPLEXITY
--------------------------------------------------------

O(N log N)

Where:

N = Total number of cars.

OPERATION 1: BUILD THE 2D LIST

for i in range(len(position)):

We visit every car once.

For each car:
- Calculate its arrival time.
- Store its position and arrival time.

If there are N cars:

Time = O(N)

OPERATION 2: SORTING

cars.sort(reverse=True)

We sort N cars by position.

Python uses Timsort.

Sorting takes:

O(N log N)

OPERATION 3: COUNT FLEETS

for car_position, arrival_time in cars:

We visit every car once.

Each comparison takes O(1).

Therefore:

Time = O(N)

TOTAL TIME COMPLEXITY:

O(N) + O(N log N) + O(N)

The sorting operation dominates.

Therefore:

TIME COMPLEXITY = O(N log N)

8. SPACE COMPLEXITY
--------------------------------------------------------

O(N)

Why?

2D LIST:

cars stores information about every car.

Each car stores:
- Position.
- Arrival time.

For N cars:

Space = O(N)

OTHER VARIABLES:

count and prev_time store only one value each.

Space = O(1)

TOTAL AUXILIARY SPACE:

O(N)

Python's sorting algorithm also uses temporary
memory, but the dominant space complexity
remains O(N).

9. MY OWN TEST CASES
--------------------------------------------------------

Test 1:

target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

Expected: 3

Test 2:

target = 10
position = [3]
speed = [3]

Expected: 1

Reason:
One car creates one fleet.

Test 3:

target = 10
position = [6, 8]
speed = [3, 2]

Expected: 2

Reason:
The car at position 8 is ahead and slower.
The car at position 6 cannot catch it.

Test 4:

target = 10
position = [6, 8]
speed = [4, 2]

Expected: 1

Reason:
The car at position 6 is faster.
It catches the slower car ahead.

Test 5:

target = 10
position = [0, 4, 2]
speed = [2, 1, 3]

Expected: 1

Reason:
All cars eventually join the same fleet.

Test 6:

target = 100
position = [0, 10, 20]
speed = [4, 2, 1]

Expected: 3

Reason:
Every car ahead is slower.
No car behind can catch the fleet ahead.

Test 7:

target = 10
position = [1, 5]
speed = [3, 1]

Expected: 1

Reason:
The car at position 1 catches the slower car
at position 5 before reaching the destination.

Test 8:

target = 10
position = [1, 5]
speed = [1, 1]

Expected: 2

Reason:
Both cars have the same speed.
The distance between them never disappears.

10. IMPORTANT ENGINEERING LESSONS
--------------------------------------------------------

1. A 2D list can store related information together.

2. Sorting helps us process cars in the correct order.

3. Arrival time is more important than current speed.

4. A car's original speed can change when it joins a fleet.

5. The fleet ahead controls the arrival time
   of every car that joins it.

6. We count a new fleet only when:

   arrival_time > prev_time

7. Equal arrival times mean the cars form one fleet.

8. We do not need to simulate the actual driving.

9. We only need to calculate arrival times and compare them.

========================================================
MY LEARNING CHECKLIST
========================================================

[ ] I understand the car fleet problem.
[ ] I understand distance divided by speed.
[ ] I can calculate each car's arrival time.
[ ] I understand why we store position and time together.
[ ] I understand how tuple sorting works.
[ ] I understand reverse=True.
[ ] I understand why we sort from front to back.
[ ] I understand what count stores.
[ ] I understand what prev_time stores.
[ ] I understand when a new fleet is created.
[ ] I understand when a car joins an existing fleet.
[ ] I understand why equality means one fleet.
[ ] I can perform the dry run without looking.
[ ] I can write the solution without looking.
[ ] I understand O(N log N) time complexity.
[ ] I understand O(N) space complexity.

========================================================
"""

# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------

solution = Solution()

test_cases = [
    (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
    (10, [3], [3], 1),
    (10, [6, 8], [3, 2], 2),
    (10, [6, 8], [4, 2], 1),
    (10, [0, 4, 2], [2, 1, 3], 1),
    (100, [0, 10, 20], [4, 2, 1], 3),
    (10, [1, 5], [3, 1], 1),
    (10, [1, 5], [1, 1], 2),
]

passed = 0

print("CAR FLEET - TEST RESULTS")
print("----------------------------------")

for target, position, speed, expected in test_cases:

    result = solution.carFleet(target, position, speed)

    print("Target:", target)
    print("Positions:", position)
    print("Speeds:", speed)
    print("Expected:", expected)
    print("Actual:", result)

    if result == expected:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
