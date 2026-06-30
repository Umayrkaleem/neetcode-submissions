class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        bucket = set(nums)
        longest = 0

        for n in nums:
            largest  = 1
            while n+1 in bucket:
                largest +=1
                n+=1
            longest = max(largest, longest)
        
        return longest

