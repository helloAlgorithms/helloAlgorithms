class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        joint = ''.join(words)
        dic = {}
        
        for i in joint :
            if i not in dic :
                dic[i] = joint.count(i)
                
        for v in dic.values() :
            if v % len(words) != 0 : return False 
        return True