class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfNums = set(nums)

        if len(nums) == len(setOfNums):
            return False

        return True
         