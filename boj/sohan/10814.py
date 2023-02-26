N = int(input())
users = [input().split() for i in range(N)]
users.sort(key=lambda x:int(x[0]))
for user in users:
    print(' '.join(user))
