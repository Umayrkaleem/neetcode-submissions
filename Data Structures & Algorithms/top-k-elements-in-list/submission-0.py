class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[]for n in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        #key is the int value is the count
        for integer, times in count.items():
            freq[times].append(integer)
        
        ans = []
        for i in reversed(freq):
            for n in i:
                if n!=[]:
                    ans.append(n)
                    if len(ans) == k:
                        return ans