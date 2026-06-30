class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, 1

        while left < len(nums):
            print(left,right)
            if (nums[left] + nums[right]) == target:
                return [left, right]

            if right == len(nums)-1:
                left +=1 
                right = left +1
            else:
                right +=1 
        return [0,0]
             