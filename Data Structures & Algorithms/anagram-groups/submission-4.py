class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        check = {}

        for word in strs:
            counted = ''.join(sorted(word))
            if counted in check:
                check[counted].append(word)
            else:
                check.setdefault(counted, [])
                check[counted].append(word)
        
        for values in check.values():
            result.append(values)
        
        print(check)

        return result 

        


    # def isAnagram(self, a: string, b: string) -> bool:
    #     if Counter(a) == Counter(b):
    #         return True
    #     return False