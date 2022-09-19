
n,m = map(int, input().split())

li_A = list(map(int,input().split()))
li_B = list(map(int,input().split()))
# 두 원소의 갯수를 합치고 거기서 겨치는것만큼 빼면 답이 나온다.
# 그러기 위해 겹치는거는 dict로 체크하면 좋을듯
dic = {}

for i in range(n):  
    dic[li_A[i]] = 0
overlap = 0
for i in range(m):
    if li_B[i] in dic:
        overlap += 1
print(m+n-overlap*2)
