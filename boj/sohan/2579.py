N = int(input())
st = {i:int(input()) for i in range(N)}
p = [0] * 300

p[0] = st[0]
p[1] = max(st[0] + st.get(1, 0), st.get(1, 0))
p[2] = max(st[0] + st.get(2, 0), st.get(1, 0) + st.get(2, 0))

for i in range(3,N):
    p[i] = max(p[i - 2] + st[i], p[i - 3] + st[i - 1] + st[i])

print(p[N - 1])
