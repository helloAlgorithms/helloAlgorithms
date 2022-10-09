class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        ret = []
        while (i <= n):
            if i % 5 == 0 and i % 3 == 0:
                ret.append("FizzBuzz")
            elif i % 3 == 0:
                ret.append("Fizz")
            elif i % 5 == 0:
                ret.append("Buzz")
            else:
                ret.append(str(i))
            i += 1
        return ret

# list comprehension        
    def fizzBuzz(self, n):
        return [str(i) * (i % 3 != 0 and i % 5 != 0) + "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) 
                for i in range(1, n + 1)]