import sys
e, s, m = map(int, input().split())
cnt = 1;
while not ((cnt - e) % 15 == 0 and (cnt - s)% 28 == 0 and (cnt - m) % 19 == 0):
    cnt+= 1
print(cnt);
