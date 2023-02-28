N = int(input())
words = {}
for i in range(N):
    word =str(input().split('\n'))
    words[word] = len(word)
answer = sorted(sorted(words.items()), key=lambda item:item[1]) 
for item in answer:
    print(item[0].strip('[\']'))
