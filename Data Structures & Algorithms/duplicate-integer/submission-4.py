class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collection = Counter(nums)

        for n in collection.values():
            if n > 1:
                return True

        return False
         