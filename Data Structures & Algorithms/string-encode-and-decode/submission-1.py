class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j=i
            while s[j]!="#":
                j+=1
            print(s[i:j])
            length = int(s[i:j])
            # print(length)
            i = j + 1
            # print("i:", i)
            j = i + length
            # print("j: ", j)
            result.append(s[i:j])
            i = j
        return result
