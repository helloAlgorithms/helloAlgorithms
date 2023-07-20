#include <stdio.h>
#include <string.h>

int n, m, k, max;
int map[20][20];
int v[20][20];
int arr[3];
int visit[20];

typedef struct s_point {
	int y;
	int x;
	int dist;
} t_point;

int check(int r1, int c1, int r2, int c2) {

	int dis1 = r1 - r2;
	int dis2 = c1 - c2;
	if (dis1 < 0)
		dis1 = -dis1;
	if (dis2 < 0)
		dis2 = -dis2;
	if (dis1 + dis2 <= k)
		return dis1 + dis2;
	return 0;
}

void game(int a1, int a2, int a3) {

	int result = 0;
	for (int a = n; a > 0; a--) {
		t_point t1, t2, t3;
		memset(&t1, -1, sizeof(t_point));
		memset(&t2, -1, sizeof(t_point));
		memset(&t3, -1, sizeof(t_point));
		t1.dist = 2147483647;
		t2.dist = 2147483647;
		t3.dist = 2147483647;
		for (int i = 0; i < m; i++) {
			for (int j = a - 1; j > -1; j--) {
				if (map[j][i] == 1) {
					int m1, m2, m3;
					if (v[j][i])
						continue;
					m1 = check(a, a1, j, i);
					if (t1.dist > m1 && m1) {
						t1.dist = m1;
						t1.y = j;
						t1.x = i;
					}
					m2 = check(a, a2, j, i);
					if (t2.dist > m2 && m2) {
						t2.dist = m2;
						t2.y = j;
						t2.x = i;
					}
					m3 = check(a, a3, j, i);
					if (t3.dist > m3 && m3) {
						t3.dist = m3;
						t3.y = j;
						t3.x = i;
					}
				}
			}
		}
		if (t1.dist != 2147483647 && !v[t1.y][t1.x]) {
			result++;
			v[t1.y][t1.x] = 1;
		}
		if (t2.dist != 2147483647 && !v[t2.y][t2.x]) {
			result++;
			v[t2.y][t2.x] = 1;
		}
		if (t3.dist != 2147483647 && !v[t3.y][t3.x]) {
			result++;
			v[t3.y][t3.x] = 1;
		}
	}
	memset(v, 0, sizeof(v));
	if (result > max)
		max = result;
	return ;
}

void dfs(int depth, int num) {
	if (depth == 3) {
		game(arr[0], arr[1], arr[2]);
		return ;
	}
	if (num >= m)
		return ;
	arr[depth] = num;
	dfs(depth + 1, num + 1);
	dfs(depth, num + 1);
}

int main() {

	scanf("%d %d %d", &n, &m, &k);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%d", &map[i][j]);
	dfs(0, 0);
	printf("%d\n", max);
	return 0;
}
