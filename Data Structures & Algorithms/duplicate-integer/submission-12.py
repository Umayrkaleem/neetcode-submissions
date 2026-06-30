class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe=set(nums)

        # for n in nums:
        #     if n in dupe:
        #         return True
        #     dupe.add(n)
        # return False

        if len(dupe) == len(nums):
            return False
        return True

