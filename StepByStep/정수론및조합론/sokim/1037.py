N = int(input())
array = list(map(int, input().split()))
smallest = min(array)
biggest = max(array)
print(biggest * smallest)
