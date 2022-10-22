# 사용시간 1431 1458
# 답봄
# 문제의 말뜻을 이해를 못했다. 말뜻만 이해하면 쉬운 문제였다.

from collections import deque
n, k = map(int, input().split())
s = deque([])
for i in range(1, n + 1):
    s.append(i)
print('<', end='')
while s:
    for i in range(k - 1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    if s:
        print(', ', end='')
    print(s)
print('>')