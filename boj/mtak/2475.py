def power(ii):
    i = int(ii)
    return i * i
a = list(map(power, input().strip().split()))
print(sum(a)%10)
