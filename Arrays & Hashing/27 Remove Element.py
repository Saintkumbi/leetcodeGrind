class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the position of the next non-val element

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
