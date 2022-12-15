N, K = map(int, input().split())
people = [i + 1 for i in range(N)]
print("<",end='')
while len(people) != 0:
    for i in range(K-1):
        a = people.pop(0)
        people.append(a)
    print(people.pop(0), end='')
    if len(people) == 0:
        print(">")
        break
    else: print(", ", end='')
    
