class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}


        for word in strs:
            w = ''.join(sorted(word))
            print(w)
            if w in result:
                result[w].append(word)
            else:
                result[w] = [word]
        
        return list(result.values())