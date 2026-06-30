class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = 0

        counted = Counter(nums)
        counted = dict(sorted(counted.items(), key=lambda item: item[1], reverse=True))

        
        for val in counted:
            counter +=1
            res.append(val)
            if counter >= k:
                break
            

        return res
        