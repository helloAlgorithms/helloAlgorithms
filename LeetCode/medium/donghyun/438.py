class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams = []
        chars = Counter(p)
        i, j = 0, len(p)
        window = Counter(s[:j])
        while True:
            if chars == window:
                anagrams.append(i)
            window[s[i]] -= 1
            i, j = i + 1, j + 1
            if j <= len(s):
                window[s[j-1]] += 1
            else:
                break
        return anagrams