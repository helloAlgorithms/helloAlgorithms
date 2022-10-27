a = int(input())
def fib(n):
    if n < 2:
        return n
    pre = 1
    ppre = 0
    cur = 0
    for i in range(2, n + 1):
        cur = pre + ppre
        ppre = pre
        pre = cur
    return cur

print(fib(a))
