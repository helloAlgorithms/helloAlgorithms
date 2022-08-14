import sys
input = sys.stdin.readline
n_members = int(input())
members = list(map(int, input().split()))
members.sort()
for _ in range(1, n_members):
    members[_] += members[_-1]
print(sum(members))
