class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        slowPointer = 0
        fastPointer = 1

        for fastPointer in range(1, len(nums)):
            if nums[slowPointer] != nums[fastPointer]:
                slowPointer += 1
                nums[slowPointer] = nums[fastPointer] 

        return slowPointer +  1 
