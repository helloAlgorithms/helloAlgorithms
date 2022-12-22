import sys

N,M,inventory = map(int, input().split())
ground = [list(map(int, sys.stdin.readline().strip('\n').split())) for i in range(N)]
answer = sys.maxsize
answer_level = 0

for level in range(257):
    remove_block = 0
    put_block = 0
    
    for column in range(M):
        for row in range(N):
            diff = level - ground[row][column]
            if level > ground[row][column]:
                put_block += diff
            else:
                remove_block += -diff
    
    if inventory + remove_block >= put_block:
        new_time = (remove_block * 2) + put_block 
        if  new_time <= answer:
            answer = new_time
            answer_level = level

print(answer, answer_level)
