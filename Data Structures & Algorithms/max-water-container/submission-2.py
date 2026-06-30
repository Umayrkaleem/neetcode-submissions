class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights)-1

        while l < r:
            total = min(heights[l], heights[r]) * (r - l)
            area = max(area, total)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return area
        