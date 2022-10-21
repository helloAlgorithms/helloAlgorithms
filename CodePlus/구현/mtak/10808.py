s = input().strip()
a = [0] * 26
for p in s:
    a[ord(p) - ord('a')] += 1
for p in a:
    print(p, end = " ")
