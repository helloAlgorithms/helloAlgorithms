import sys

N = int(sys.stdin.readline().rstrip())
# 중복 단어 제거
words = set()
for _ in range(N):
	words.add(sys.stdin.readline().rstrip())

# 정렬을 위한 리스트화
words = list(words)
# 길이가 같은 경우 알파벳 순으로 정렬
words.sort()
# 길이 순으로 정렬
words.sort(key = lambda x: len(x))

for word in words:
	print(word)
