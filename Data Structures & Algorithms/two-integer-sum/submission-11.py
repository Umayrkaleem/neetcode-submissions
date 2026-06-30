class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # make a key/value hash map, value to index
        # then target - current key = diff
        # see if diff exists as a key
        # return diff index and current key

        hashy = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashy:
                return [hashy[diff], i]     
            hashy[n] = i

        return [0,0]

            