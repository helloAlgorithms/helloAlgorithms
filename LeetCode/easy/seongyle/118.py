class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def factorial(num: int) -> int:
            result = 1
            if (num == 0):
                return (result)
            while (num > 0):
                result *= num
                num -= 1
            return (result)
        def rowGenerate(numRows: int) -> List[int]:
            row = []
            for i in range(0, numRows + 1):
                row.append(factorial(numRows) // (factorial(i) * factorial(numRows - i)))
            return (row)
        resultList = []
        for i in range(numRows):
            tempList = rowGenerate(i)
            resultList.append(tempList)
        return (resultList)
