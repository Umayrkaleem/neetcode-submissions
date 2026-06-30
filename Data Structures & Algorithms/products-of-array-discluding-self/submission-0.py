class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 0
        result = []
        hide = 0
        

        while left < len(nums):
            product = 1
            
            for i, n in enumerate(nums):
                if i != hide:
                    product = product * n

            result.append(product)
            hide +=1
            left +=1
        
        return result



            




