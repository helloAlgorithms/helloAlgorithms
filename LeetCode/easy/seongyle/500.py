class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ret = [];
        first_one = set("qwertyuiop");
        second_one = set("asdfghjkl");
        third_one = set("zxcvbnm");
        
        ret += [word for word in words if (set(word.lower()).issubset(first_one))];
        ret += [word for word in words if (set(word.lower()).issubset(second_one))];
        ret += [word for word in words if (set(word.lower()).issubset(third_one))];
        return ret;