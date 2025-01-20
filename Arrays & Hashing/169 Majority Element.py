from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = defaultdict(int)  # Automatically initializes keys with 0

        # Count the frequency of each element
        for num in nums:
            frequency[num] += 1  # Increment count directly

        n = len(nums)  # Length of the array

        # Identify and return the majority element
        for num, count in frequency.items():
            if count > n // 2:
                return num  # Return the element (key) itself

