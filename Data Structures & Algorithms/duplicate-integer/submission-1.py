class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dump = set()
        for n in nums:
            if n in dump:
                return True
            dump.add(n)
        return False


         