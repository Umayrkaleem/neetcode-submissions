class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in range(0, len(nums)-1):
            for y in range(1, len(nums)):
                if (nums[x] == nums[y]) and (x != y):
                    return True
        return False 

         