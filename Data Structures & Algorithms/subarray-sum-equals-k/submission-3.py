class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        seen = {0:1}

        for n in nums:
            curr  += n
            diff = curr - k

            res += seen.get(diff,0)
            seen[curr] = seen.get(curr,0) +1

        return res
