class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #find min k such that eat all bananas within h hours
        
        left, right = 1, max(piles)
        minK = right

        while left <= right:

            k = left + (right - left) // 2
            totalTime = 0 
            for p in piles:
                totalTime += math.ceil(p/k)
            
            if totalTime <= h:
                minK = k
                right = k - 1
            else:
                left = k + 1

        return minK 

