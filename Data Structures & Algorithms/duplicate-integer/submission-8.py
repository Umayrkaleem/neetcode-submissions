class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stripped =set(nums)

        if len(stripped) == len(nums):
            return False
        return True