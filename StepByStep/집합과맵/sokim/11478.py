S = input()

substrings = set()
for i in range(len(S)):
	for j in range(i, len(S)):
		tmp = S[i:j+1]
		substrings.add(tmp)
print(len(substrings))
