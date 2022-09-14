
n = int(input())
score = "F"
if 90 <= n <= 100:
    score = "A"
elif 80 <= n <= 89:
    score = "B"
elif 70 <= n <= 79:
    score = "C"
elif 60 <= n <= 69:
    score = "D"
else:
    score = "F"
print(score)


