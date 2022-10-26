class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = Counter()
        i, j = 0, 1
        maxrepeat = 0
        while j <= len(s):
            c[s[j - 1]] += 1
            length = j - i
            if length - c.most_common(1)[0][1] <= k:
                maxrepeat = length
                j += 1
            else:
                c[s[i]] -= 1
                i += 1
                j += 1
        return maxrepeat