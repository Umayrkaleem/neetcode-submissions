class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        #nums[i] + nums[j] == target and i != j
        #return small index first

        prev = {}

        for i, val in enumerate(nums):
            total = target - val

            if total in prev:
                result.append(prev[total])
                result.append(i)
                return result
            
            prev[val] = i

        

