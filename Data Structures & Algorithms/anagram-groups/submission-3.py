class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        usedIndex = set()
        grouped = []

        for left in range(0,len(strs)):
            if left in usedIndex:
                continue
            subGroup = [strs[left]]
            for right in range(left+1, len(strs)):
                if Counter(strs[left]) == Counter(strs[right]):
                    if right not in usedIndex:
                        subGroup.append(strs[right])
                        usedIndex.add(right)
            grouped.append(subGroup)
        return grouped

                
        