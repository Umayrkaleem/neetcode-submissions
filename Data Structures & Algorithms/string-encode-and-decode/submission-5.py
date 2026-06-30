class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            length = str(len(word))
            encoded += length + "#"
            encoded += word
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
    
        result = []
        left = 0
    
        while left < len(s):
            j = left
            while s[j] != '#':
                j += 1  # Properly indented inside the while loop
            
            length = int(s[left:j])
            end = j+1+length
            result.append(s[j+1:end])
            left = end
        
        return result 
