class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        recorded = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in recorded:
                return [recorded[diff],index]
            recorded[num] = index