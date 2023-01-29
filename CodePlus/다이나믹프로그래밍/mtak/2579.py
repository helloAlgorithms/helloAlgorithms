n = int(input())
score = [int(input()) for _ in range(n)]
if len(score) < 4:
	score.extend([0, 0])
utmost = [0, score[0], score[0] + score[1], max(score[0], score[1]) + score[2]] + [0] * 300
for i in range(1, n + 1):
	if utmost[i] != 0:continue
	utmost[i] = max(utmost[i - 2], utmost[i - 3] + score[i - 2]) + score[i - 1]
print(utmost[n])
