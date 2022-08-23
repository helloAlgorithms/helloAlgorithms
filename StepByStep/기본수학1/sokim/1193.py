n = int(input())

# 사선 라인
line = 0
# 해당 라인의 마지막 인덱스(1, 3, 6, ...)
end = 0

while n > end:
    line += 1
    end += line
diff = end - n

# 짝수 라인
if line % 2 == 0:
    numerator = line - diff
    denominator = diff + 1
# 홀수 라인
else:
    numerator = diff + 1
    denominator = line - diff

print(f'{numerator}/{denominator}')
