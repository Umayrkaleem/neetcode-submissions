class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        oneString = ""

        for s in strs:
            oneString = oneString + "#" + str(len(s)) + "#" + s

        return oneString

    def decode(self, s: str) -> List[str]:
      result = []
      i = 0

      while i < len(s):
          i += 1  # skip first "#"

          j = i
          while j < len(s) and s[j].isdigit():
              j += 1

          length = int(s[i:j])
          i = j + 1  # skip second "#"

          result.append(s[i:i + length])
          i += length

      return result
