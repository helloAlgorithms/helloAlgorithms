import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
cnt = int(input())
a = [int(input()) for _ in range(cnt)]
def quick_sort(array, start, end):
    if start >= end: return
    pivot = start 
    left, right = start + 1, end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
quick_sort(a, 0, cnt - 1)
for p in a:
    print(p)