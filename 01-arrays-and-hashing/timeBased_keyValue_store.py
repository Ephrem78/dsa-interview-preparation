
"""
========================================================
PROBLEM: TIME-BASED KEY-VALUE STORE
TOPIC: HASH MAP + BINARY SEARCH
APPROACH: HASH MAP OF TIMESTAMP-VALUE PAIRS
========================================================
1. PROBLEM DESCRIPTION
--------------------------------------------------------
Design a data structure that stores multiple values for the same key at different timestamps.
We must support:
1. set(key, value, timestamp):
   Store a value for a key at a given timestamp.
2. get(key, timestamp):
   Return the value stored at the largest timestamp that is <= the requested timestamp.
If no valid value exists, return "".
Example:
set("alice", "happy", 1)
set("alice", "sad", 3)
set("alice", "angry", 5)
get("alice", 4) -> "sad"
get("alice", 5) -> "angry"
get("alice", 0) -> ""
IMPORTANT:
We cannot simply store one value per key.
We must preserve the history of values and timestamps.
========================================================
2. MY APPROACH: HASH MAP + BINARY SEARCH
--------------------------------------------------------
I use one main data structure:
1. HASH MAP
   Stores each key and its list of timestamp-value pairs.
2. BINARY SEARCH
   Finds the correct historical value efficiently.
STRUCTURE:
map = {
    "alice": [(1, "happy"), (3, "sad"), (5, "angry")]
}
Each key points to a list of pairs:
(timestamp, value)
MY STEPS:
1. Create an empty dictionary.
2. In set(), if the key does not exist, create an empty list.
3. Append the timestamp and value as a pair.
4. In get(), check whether the key exists.
5. If the key does not exist, return "".
6. If the key exists, perform binary search on its timestamps.
7. Find the largest timestamp <= requested timestamp.
8. Return the value belonging to that timestamp.
9. If no valid timestamp exists, return "".
IMPORTANT:
The timestamps for each key are guaranteed to be strictly increasing when set() is called.
This means the list is already sorted.
Therefore, binary search works without sorting.
========================================================
3. PYTHON SOLUTION
--------------------------------------------------------
"""
class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        values = self.map[key]
        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result

"""
========================================================
4. COMPLETE ELS10 CODE EXPLANATION
========================================================
A. CREATE THE CLASS
--------------------------------------------------------
class TimeMap:
Creates a class named TimeMap.
A class is a blueprint for creating objects.
We will create an object that stores timestamp-based values.
B. INITIALIZE THE OBJECT
--------------------------------------------------------
def __init__(self):
This is the constructor.
It runs automatically when we create a TimeMap object.
Example:
timeMap = TimeMap()
Python automatically calls __init__().
self:
Refers to the current object.
self.map = {}
Creates an empty dictionary belonging to this object.
The dictionary stores:
KEY -> LIST OF TIMESTAMP-VALUE PAIRS
Example:
self.map = {
    "alice": [(1, "happy"), (3, "sad")]
}
The dictionary allows us to find a key quickly.
C. SET METHOD
--------------------------------------------------------
def set(self, key: str, value: str, timestamp: int) -> None:
This method stores a value.
key:
The name used to identify the data.
value:
The value we want to store.
timestamp:
The time when the value was stored.
-> None:
Means this method does not return a value.
if key not in self.map:
Checks whether the key is already inside the dictionary.
Example:
self.map = {}
key = "alice"
"alice" is not in the dictionary.
Therefore, the condition is True.
self.map[key] = []
Creates an empty list for this key.
Example:
self.map["alice"] = []
Now:
self.map = {
    "alice": []
}
Why do we need a list?
Because the same key can have multiple values at different times.
self.map[key].append((timestamp, value))
Adds a pair to the list.
(timestamp, value):
A Python tuple containing two elements.
Example:
timestamp = 1
value = "happy"
The tuple is:
(1, "happy")
append():
Adds the pair to the end of the list.
After three set() calls:
self.map = {
    "alice": [(1, "happy"), (3, "sad"), (5, "angry")]
}
IMPORTANT:
Each key has its own history.
Different keys have different lists.
D. GET METHOD
--------------------------------------------------------
def get(self, key: str, timestamp: int) -> str:
Returns the value that was stored at the latest timestamp <= requested timestamp.
-> str:
Means the method returns a string.
if key not in self.map:
Checks whether this key exists.
If it does not exist, there is no history to search.
return ""
Returns an empty string immediately.
Example:
get("bob", 10)
If "bob" was never stored:
Output = ""
E. GET THE HISTORY
--------------------------------------------------------
values = self.map[key]
Gets the list of timestamp-value pairs belonging to this key.
Example:
self.map = {
    "alice": [(1, "happy"), (3, "sad"), (5, "angry")]
}
If:
key = "alice"
Then:
values = [(1, "happy"), (3, "sad"), (5, "angry")]
IMPORTANT:
We search only Alice's history.
We do not search every key in the dictionary.
F. INITIALIZE BINARY SEARCH
--------------------------------------------------------
left, right = 0, len(values) - 1
left:
The first index of the list.
right:
The last index of the list.
Example:
values = [(1, "happy"), (3, "sad"), (5, "angry")]
len(values) = 3
left = 0
right = 2
The valid indices are:
0, 1, 2
result = ""
Stores the best valid value found so far.
Why initialize it to ""?
If every timestamp is greater than the requested timestamp, no valid value exists.
The answer must be "".
If we find a valid timestamp, result will be updated.
G. BINARY SEARCH LOOP
--------------------------------------------------------
while left <= right:
Continues searching while the search area is not empty.
When left becomes greater than right:
There are no more indices to search.
The search is finished.
mid = left + (right - left) // 2
Calculates the middle index.
Example:
left = 0
right = 2
mid = 0 + (2 - 0) // 2
mid = 1
//:
Integer division.
It removes the decimal part.
We use it because list indices must be integers.
H. CHECK THE MIDDLE TIMESTAMP
--------------------------------------------------------
if values[mid][0] <= timestamp:
This is a very important condition.
values[mid]:
Gets the tuple at the middle index.
Example:
values = [(1, "happy"), (3, "sad"), (5, "angry")]
mid = 1
values[mid] = (3, "sad")
values[mid][0]:
Gets the first element of the tuple.
That is the timestamp.
values[mid][1]:
Gets the second element of the tuple.
That is the stored value.
The condition asks:
Is this timestamp <= the requested timestamp?
If TRUE:
This timestamp is valid.
But there might be a newer valid timestamp on the right.
I. SAVE THE BEST VALID VALUE
--------------------------------------------------------
result = values[mid][1]
Stores the value belonging to the current valid timestamp.
Example:
values[mid] = (3, "sad")
result = "sad"
We save it because it is currently the best answer.
We might find a newer valid timestamp later.
J. SEARCH TO THE RIGHT
--------------------------------------------------------
left = mid + 1
The current timestamp is valid.
We want the largest valid timestamp.
Therefore, we search the right half.
Example:
timestamps = [1, 3, 5]
requested timestamp = 4
If mid timestamp = 3:
3 <= 4
The value at 3 is valid.
But timestamp 5 might be too large.
We search to the right to see whether another valid timestamp exists.
K. SEARCH TO THE LEFT
--------------------------------------------------------
else:
right = mid - 1
This happens when:
values[mid][0] > timestamp
The middle timestamp is too large.
It cannot be the answer.
Because timestamps are sorted:
All timestamps to the right are also larger.
Therefore, we eliminate the middle and right side.
We search the left half.
L. RETURN THE ANSWER
--------------------------------------------------------
return result
After binary search finishes:
result contains the value belonging to the largest timestamp <= requested timestamp.
If no valid timestamp was found:
result remains "".
========================================================
5. COMPLETE DRY RUN
========================================================
OPERATIONS:
set("alice", "happy", 1)
set("alice", "sad", 3)
set("alice", "angry", 5)
get("alice", 4)
INITIAL STATE:
self.map = {}
SET 1:
key = "alice"
value = "happy"
timestamp = 1
Key does not exist.
Create:
self.map["alice"] = []
Append:
(1, "happy")
STATE:
self.map = {
    "alice": [(1, "happy")]
}
SET 2:
key = "alice"
value = "sad"
timestamp = 3
Key already exists.
Append:
(3, "sad")
STATE:
self.map = {
    "alice": [(1, "happy"), (3, "sad")]
}
SET 3:
key = "alice"
value = "angry"
timestamp = 5
Key already exists.
Append:
(5, "angry")
FINAL HISTORY:
self.map = {
    "alice": [(1, "happy"), (3, "sad"), (5, "angry")]
}
NOW GET:
get("alice", 4)
We want the latest timestamp <= 4.
HISTORY:
Index 0: (1, "happy")
Index 1: (3, "sad")
Index 2: (5, "angry")
INITIAL:
left = 0
right = 2
result = ""
ITERATION 1:
mid = 0 + (2 - 0) // 2
mid = 1
values[mid] = (3, "sad")
Timestamp:
3
Compare:
3 <= 4
TRUE.
Save:
result = "sad"
Search right:
left = mid + 1
left = 2
STATE:
left = 2
right = 2
result = "sad"
ITERATION 2:
mid = 2 + (2 - 2) // 2
mid = 2
values[mid] = (5, "angry")
Timestamp:
5
Compare:
5 <= 4
FALSE.
Search left:
right = mid - 1
right = 1
STATE:
left = 2
right = 1
result = "sad"
LOOP ENDS:
left > right
Return:
"sad"
WHY?
Timestamp 3 is the largest timestamp <= 4.
Timestamp 5 is too large.
Therefore:
OUTPUT = "sad"
========================================================
6. DRY RUN: REQUEST BEFORE ALL TIMESTAMPS
========================================================
History:
[(1, "happy"), (3, "sad"), (5, "angry")]
get("alice", 0)
INITIAL:
left = 0
right = 2
result = ""
ITERATION 1:
mid = 1
Timestamp = 3
3 <= 0
FALSE.
right = mid - 1
right = 0
ITERATION 2:
mid = 0
Timestamp = 1
1 <= 0
FALSE.
right = -1
LOOP ENDS:
left = 0
right = -1
result = ""
RETURN:
""
No timestamp is <= 0.
Therefore, no valid value exists.
========================================================
7. DRY RUN: EXACT TIMESTAMP
========================================================
History:
[(1, "happy"), (3, "sad"), (5, "angry")]
get("alice", 3)
INITIAL:
left = 0
right = 2
result = ""
ITERATION 1:
mid = 1
Timestamp = 3
3 <= 3
TRUE.
result = "sad"
left = 2
ITERATION 2:
mid = 2
Timestamp = 5
5 <= 3
FALSE.
right = 1
LOOP ENDS.
Return:
"sad"
An exact timestamp is valid because we use <=.
========================================================
8. WHY BINARY SEARCH WORKS
========================================================
The timestamps are stored in increasing order.
Example:
[1, 3, 5, 8, 12]
We need:
The largest timestamp <= target.
Example:
target = 7
Valid timestamps:
1, 3, 5
Invalid timestamps:
8, 12
Answer:
5
Binary search avoids checking every timestamp.
If the middle timestamp is valid:
We save its value and search right for a newer valid timestamp.
If the middle timestamp is too large:
We search left.
This continues until no search area remains.
The saved result is the latest valid timestamp.
========================================================
9. TIME COMPLEXITY
========================================================
SET:
O(1) average time.
1. Dictionary lookup is O(1) average.
2. Appending a pair to a list is O(1) amortized.
Therefore:
set() = O(1) average.
GET:
O(log N)
Where N is the number of timestamps stored for the requested key.
1. We use binary search.
2. Every iteration eliminates approximately half the search area.
Example:
16 timestamps
8 timestamps
4 timestamps
2 timestamps
1 timestamp
Therefore:
get() = O(log N)
IMPORTANT:
N means the number of timestamps for that particular key.
It does not mean the total number of keys.
========================================================
10. SPACE COMPLEXITY
========================================================
O(N)
Where N is the total number of set() operations stored.
Every set() call stores:
1. A timestamp.
2. A value.
3. A pair inside a list.
All histories remain stored inside the dictionary.
Therefore, memory grows with the number of stored timestamp-value pairs.
The binary search itself uses:
left
right
mid
result
These are constant extra variables.
Binary search extra space = O(1).
But the stored history = O(N).
TOTAL SPACE COMPLEXITY = O(N).
========================================================
11. EDGE CASES
========================================================
EDGE CASE 1: KEY DOES NOT EXIST
get("bob", 10)
Expected:
""
Reason:
The key is not in the dictionary.
EDGE CASE 2: REQUEST BEFORE FIRST TIMESTAMP
History:
[(5, "hello")]
get("alice", 2)
Expected:
""
Reason:
5 > 2.
EDGE CASE 3: EXACT TIMESTAMP
History:
[(1, "A"), (3, "B"), (5, "C")]
get("alice", 3)
Expected:
"B"
Reason:
Timestamp 3 is valid.
EDGE CASE 4: BETWEEN TIMESTAMPS
History:
[(1, "A"), (3, "B"), (5, "C")]
get("alice", 4)
Expected:
"B"
Reason:
3 is the latest timestamp <= 4.
EDGE CASE 5: AFTER ALL TIMESTAMPS
History:
[(1, "A"), (3, "B"), (5, "C")]
get("alice", 10)
Expected:
"C"
Reason:
5 is the latest stored timestamp.
EDGE CASE 6: ONLY ONE TIMESTAMP
History:
[(2, "hello")]
get("alice", 2)
Expected:
"hello"
EDGE CASE 7: MULTIPLE KEYS
set("alice", "A", 1)
set("bob", "B", 1)
get("alice", 1)
Expected:
"A"
Reason:
Each key has a separate history.
EDGE CASE 8: LATEST VALUE
History:
[(1, "A"), (2, "B"), (3, "C")]
get("alice", 3)
Expected:
"C"
========================================================
12. MY OWN TEST CASES
========================================================
Test 1:
set("foo", "bar", 1)
get("foo", 1)
Expected: "bar"
Test 2:
set("foo", "bar", 1)
get("foo", 3)
Expected: "bar"
Test 3:
set("foo", "bar", 1)
get("foo", 0)
Expected: ""
Test 4:
set("foo", "bar", 1)
set("foo", "baz", 2)
get("foo", 2)
Expected: "baz"
Test 5:
set("foo", "bar", 1)
set("foo", "baz", 2)
get("foo", 3)
Expected: "baz"
Test 6:
set("foo", "bar", 1)
set("foo", "baz", 2)
get("foo", 1)
Expected: "bar"
Test 7:
get("missing", 5)
Expected: ""
Test 8:
set("alice", "A", 1)
set("bob", "B", 1)
get("alice", 1)
Expected: "A"
Test 9:
set("foo", "a", 1)
set("foo", "b", 5)
set("foo", "c", 10)
get("foo", 7)
Expected: "b"
Test 10:
set("foo", "a", 1)
set("foo", "b", 5)
set("foo", "c", 10)
get("foo", 0)
Expected: ""
========================================================
MY LEARNING CHECKLIST
========================================================
[ ] I understand the problem.
[ ] I understand why one key can have multiple values.
[ ] I understand why we store timestamp-value pairs.
[ ] I understand how the dictionary works.
[ ] I understand why each key has its own list.
[ ] I understand what __init__ does.
[ ] I understand what self means.
[ ] I understand what set() does.
[ ] I understand how append() works.
[ ] I understand what a tuple is.
[ ] I understand values = self.map[key].
[ ] I understand why a missing key returns "".
[ ] I understand left and right.
[ ] I understand binary search.
[ ] I understand how mid is calculated.
[ ] I understand values[mid][0].
[ ] I understand values[mid][1].
[ ] I understand why we use <=.
[ ] I understand why a valid timestamp makes us search right.
[ ] I understand why an invalid timestamp makes us search left.
[ ] I understand why result stores the best answer.
[ ] I understand why binary search is O(log N).
[ ] I understand why set() is O(1) average.
[ ] I understand why space complexity is O(N).
[ ] I can implement TimeMap without looking.
========================================================
"""


# ------------------------------------------------------
# TESTING THE SOLUTION
# ------------------------------------------------------
test_cases = [
    ([("set", "foo", "bar", 1), ("get", "foo", 1)], ["", "bar"]),
    ([("set", "foo", "bar", 1), ("get", "foo", 3)], ["", "bar"]),
    ([("set", "foo", "bar", 1), ("get", "foo", 0)], ["", ""]),
    ([("set", "foo", "bar", 1), ("set", "foo", "baz", 2), ("get", "foo", 2)], ["", "", "baz"]),
    ([("set", "foo", "bar", 1), ("set", "foo", "baz", 2), ("get", "foo", 3)], ["", "", "baz"]),
    ([("set", "foo", "bar", 1), ("set", "foo", "baz", 2), ("get", "foo", 1)], ["", "", "bar"]),
    ([("get", "missing", 5)], [""]),
    ([("set", "alice", "A", 1), ("set", "bob", "B", 1), ("get", "alice", 1)], ["", "", "A"]),
    ([("set", "foo", "a", 1), ("set", "foo", "b", 5), ("set", "foo", "c", 10), ("get", "foo", 7)], ["", "", "", "b"]),
    ([("set", "foo", "a", 1), ("set", "foo", "b", 5), ("set", "foo", "c", 10), ("get", "foo", 0)], ["", "", "", ""])
]

passed = 0
print("TIME-BASED KEY-VALUE STORE - TEST RESULTS")
print("----------------------------------------------")

for operations, expected_results in test_cases:
    timeMap = TimeMap()
    actual_results = []

    for operation in operations:
        if operation[0] == "set":
            _, key, value, timestamp = operation
            timeMap.set(key, value, timestamp)
            actual_results.append("")
        else:
            _, key, timestamp = operation
            actual_results.append(timeMap.get(key, timestamp))

    result = actual_results[-1]
    expected = expected_results[-1]

    print("Operations:", operations)
    print("Expected:", expected)
    print("Actual:", result)

    if actual_results == expected_results:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------------------")

print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")
