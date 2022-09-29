class Solution:
    def encode(self, string: str) -> List[int]:
        idx = 0
        char_dict = {}
        encoded = []
        for char in string:
            if char not in char_dict:
                char_dict[char] = idx
                idx += 1
            encoded.append(char_dict[char])
        return encoded
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.encode(s) == self.encode(t)