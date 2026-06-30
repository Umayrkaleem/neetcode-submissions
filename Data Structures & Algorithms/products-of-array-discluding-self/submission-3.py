class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero = 1, 0
        result = len(nums) * [0]

        for num in nums: 
            if num != 0:
                product = num * product
            else:
                zero += 1
        if zero >= 2:
            return result

        for i,c in enumerate(nums):
            if zero: 
                result[i] = 0
                if c:
                    result[i] = 0
                else: 
                    result[i] = product
            else: 
                result[i] = product // c
        
        return result 

        return result 