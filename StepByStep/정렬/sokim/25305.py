# 응시자 수, 상을 받는 사람 수
N, k = map(int, input().split())
# 응시자들의 점수
scores = list(map(int, input().split()))
scores.sort(reverse=True)
print(scores[k - 1])
