class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        k = right
        

        while left <= right:
            # h is num of hours you have

            mid = (left + right) // 2
            totalTime = 0

            for p in piles:
                totalTime +=  math.ceil(float(p)/mid)
            
            if totalTime > h:
                left = mid + 1 # we need to INCREASE the rate, need to be fastser!
            elif totalTime <= h:
                k = mid
                right = mid - 1

        return k
        #return min k (rate) you can eat bannas within h hours
        


        
        