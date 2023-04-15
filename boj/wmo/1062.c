#include <stdio.h>
#include <string.h>

int n, k, max;
int bit_len = 5;

char str[51][16];
int len[51];

void dfs(int depth, int flag, char alp) {

	if (depth == k) {
		int result = 0;
		for (int i = 0; i < n; i++) {
			int is_true = 1;
			for (int j = 4; j < len[i] - 4; j++) {
				if (!(flag & (1 << (str[i][j] - 97))))
					is_true = 0;
			}
			if (is_true)
				result++;
		}
		if (result > max) 
			max = result;
		return ;
	}
	if (alp > 'z')
		return ;
	for (int i = alp; i < 'z'; i++) {
		if (flag & (1 << (alp - 97)))
			alp++;
		else
			break;
	}
	dfs(depth + 1, flag | (1 << (alp - 97)), alp + 1);
	dfs(depth , flag, alp + 1);
}

int main() {

	const char temp[] = "antic";
	scanf("%d %d", &n, &k);

	int flag = 0;
	k -= 5;
	for (int i = 0; i < 5; i++) 
		flag |= (1 << (temp[i] - 97));
	
	for (int i = 0; i < n; i++) {
		scanf("%s", str[i]);
		len[i] = strlen(str[i]);
	}
	if (k >= 0)
		dfs(0, flag, 97);
	printf("%d\n", max);
	return 0;
}
