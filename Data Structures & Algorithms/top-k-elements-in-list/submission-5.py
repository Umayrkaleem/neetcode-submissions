class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)
        keys = sorted(counted, key=counted.get, reverse=True)
        mostK=[]

        for i in range(k):
            mostK.append(keys[i])

        return mostK

