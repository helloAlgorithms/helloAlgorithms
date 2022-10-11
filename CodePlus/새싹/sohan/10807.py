N = map(int, input())
mylist = list(map(int, input().split()))
v = list(map(int, input().split()))
if len(v):
    result = mylist.count(v[0])
    print(result)
