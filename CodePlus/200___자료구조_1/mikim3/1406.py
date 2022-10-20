# 시작시간 0925
# 답봄

# 깊게 집중해서 생각하지 않고 어림잡아 생각하면서 코드를 조금씩 바꾸면서 풀었다.
# 그런데 처음 cur = len(sentence)를 cur = len(sentence) - 1 로 풀어서
# 잘못된 방향으로 계속 풀었다.
# 그러니 당연히 몇몇 케이스에서 계속 막혔다.
# 그렇게 슬라이싱으로 거의 50분 날리고 애초에 방법이 시간복잡도가 안됨을 깨달았다.
# 그래서 스택두개를 연결하는 방법으로 다시 풀었다. ㅇ


import sys
input = sys.stdin.readline

if __name__ == '__main__':
    stackLeft = list(input().rstrip())
    stackRight = list()
    
    n = int(input().rstrip())
    for i in range(0, n):
        command = list(input().split())
        if command[0] == 'L' and stackLeft:
            stackRight.append(stackLeft.pop())
        elif command[0] == 'D' and stackRight:
            stackLeft.append(stackRight.pop())
        elif command[0] == 'B' and stackLeft:
            stackLeft.pop()
        elif command[0] == 'P':
            stackLeft.append(command[1])

    print(''.join(stackLeft) + ''.join(list(reversed(stackRight))))

#####시간초과 소스 

# sentence = input().strip()
# command = []
# n = int(input())
# for i in range(n):
#     command.append(input().strip())
# cur = len(sentence)
# sentence_temp = sentence
# for i in range(n):
#     if command[i][0] == "P":
#         sentence_temp = sentence[:cur] + command[i][2] + sentence[cur:]  
#         cur = cur + 1
#     if command[i][0] == "L":
#         if cur-1 >= 0:
#             cur = cur - 1
#     if command[i][0] == "D":
#         if cur + 1 <= len(sentence):
#             cur = cur + 1
#     if command[i][0] == "B":
#         if cur >= 1:
#             sentence_temp = sentence[ : cur-1] + sentence[cur: ]  
#             cur = cur - 1
#     sentence = sentence_temp
#     # print("%d번째에 sentenc %s cur == %d"%(i,sentence,cur))
# print(sentence)


