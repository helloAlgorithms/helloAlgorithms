N = int(input())
numbers = list(map(int, input().split(' ')))
primes = [True] * (1000 + 1)
primes[0] = False
primes[1] = False

NN = 1000 // 2
for i in range(2, NN):
    if (primes[i]):
        for j in range(i+i, 1000, i):
            primes[j] = False
answer = 0
for number in numbers:
    if primes[number]:
        answer = answer + 1
print(answer)
