g = input().strip()
def f(a):
    if a == str(int(a[0]) * len(a)):
        return "FA"
    return f(str(int(a[0]) * len(a)))
print(f(g))    
