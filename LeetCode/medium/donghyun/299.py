class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        for i, j in zip(secret, guess):
            if i == j:
                A += 1
        B = len(secret) - (Counter(guess) - Counter(secret)).total() - A
        return f"{A}A{B}B"