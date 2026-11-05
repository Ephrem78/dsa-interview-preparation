class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # Create an empty dictionary
        seen = {}

        # Visit every number using its index
        for i in range(len(nums)):

            # Calculate the number we need
            complement = target - nums[i]

            # Check whether the needed number exists
            if complement in seen:

                # Return both original indices
                return [seen[complement], i]

            # Store the current number and its index
            seen[nums[i]] = i

        return []

# Create an object from the Solution class
solution = Solution()

# Create test cases
test_cases = [
    ([15, 7, 2, 11], 9, [1, 2]),
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ([0, 4, 3, 0], 0, [0, 3]),
    ([1, 5, 3, 7], 10, [2, 3]),
    ([10, 1, 5, 3], 6, [1, 2])
]

# Count successful tests
passed = 0

print("TWO SUM - TEST RESULTS")
print("----------------------------------")

# Run every test case
for nums, target, expected in test_cases:

    # Call the Two Sum method
    result = solution.twoSum(nums, target)

    # Sort both results because the answer can be in any order
    actual_sorted = sorted(result)
    expected_sorted = sorted(expected)

    print("Numbers:", nums)
    print("Target:", target)
    print("Expected indices:", expected)
    print("Actual indices:", result)

    # Check whether the answer is correct
    if actual_sorted == expected_sorted:
        print("Status: PASS")
        passed += 1
    else:
        print("Status: FAIL")

    print("----------------------------------")

# Display the final result
print("FINAL RESULT:", passed, "/", len(test_cases), "TESTS PASSED")