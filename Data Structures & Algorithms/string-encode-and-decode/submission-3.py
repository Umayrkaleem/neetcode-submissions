class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""

        for word in strs:
            newString += str(len(word)) + "#" + word 

        return newString

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            i = j +1
            j = j + length

            print(s[i:j+1])

            decoded.append(s[i:j+1])

            i = j + 1

        return decoded
