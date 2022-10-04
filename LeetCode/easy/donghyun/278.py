# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, pivot, end = 1, max(1, n//2), n
        while True:
            if end - pivot <= 1:
                return pivot if isBadVersion(pivot) else end
            if isBadVersion(pivot):
                pivot, end = (pivot+start)//2, pivot
            else:
                start, pivot = pivot, (pivot+end)//2