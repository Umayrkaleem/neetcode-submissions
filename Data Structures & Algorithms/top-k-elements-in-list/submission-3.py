class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_freq = []

        for n,m in count.most_common():
            if len(most_freq) < k:
                most_freq.append(n)
            else: 
                break

        return most_freq