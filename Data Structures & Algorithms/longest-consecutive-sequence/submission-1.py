class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengthNums = len(nums)
        if lengthNums == 0:
            return 0
        if lengthNums == 1:
            return 1

        nums.sort()
        maxLen = 1
        counter = 1

        for i in range(0, len(nums)-1):
            # should we take care of duplicates?
            if nums[i] == nums[i+1]:
                continue
            if  nums[i]+1 == nums[i+1]:
                counter +=1
                maxLen = max(maxLen, counter)
            else:
                counter = 1
            maxLen = max(maxLen, counter)


        return maxLen