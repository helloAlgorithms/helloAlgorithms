class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True
        if bits[0] == 0:
            return self.isOneBitCharacter(bits[1:])
        if len(bits) == 0 or len(bits) == 2:
            return False   
        return self.isOneBitCharacter(bits[2:])

# 뒤부터 돌면서, 1이 짝수개 있으면 참, 1이 홀수개 있으면 거짓
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ret = True
        for bit in bits[-2::-1]:
            if bit:
                ret = not ret
            else:
                break
        return ret