class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for digit in digits:
            num = num * 10 + digit
        num += 1
        ret = []
        while num > 0:
            ret.append(num % 10)
            num //= 10
        return reversed(ret)   