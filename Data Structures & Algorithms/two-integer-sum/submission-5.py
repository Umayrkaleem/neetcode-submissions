class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums)-1):
            for j in range(1, len(nums)):
                total = nums[i] + nums[j]
                if (total == target) and (i != j):
                    return [i,j]

    
        