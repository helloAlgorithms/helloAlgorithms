class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        tens = 1
        len_digits = len(digits)
        
        for i in range(len_digits):
            num += (tens) * digits[len_digits - i - 1]
            tens *= 10
        num = num + 1
        new_digits = []
        while (int(num) > 0):
            new_digits.insert(0, int(num % 10))
            num //= 10
        return new_digits
