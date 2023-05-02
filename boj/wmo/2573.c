#include <stdio.h>
#include <string.h>

int n, m;

int v[301][301];

int map[301][301];
int map2[301][301];

int dy[4] = {0, 1, -1 , 0};
int dx[4] = {1, 0, 0, -1};

int	check(int y, int x) {

	if (y <= 0 || x <= 0 || y >= n || x >= m)
		return 0;
	if (!map[y][x] || v[y][x])
		return 0;
	return 1;
}

void dfs(int y, int x) {

	if (map[y][x] == 0 || v[y][x])
		return ;
	v[y][x] = 1;
	for (int i = 0; i < 4; i++) {
		int ny = y + dy[i];
		int nx = x + dx[i];
		if (map[ny][nx] == 0 && map2[y][x] > 0)
			map2[y][x]--;
	}
	for (int i = 0; i < 4; i++) {
		int ny = y + dy[i];
		int nx = x + dx[i];
		if (check(ny, nx)) {
			dfs(ny, nx);
		}
	}
}

int main() {

	int year = 0;

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%d", &map[i][j]);
	memcpy(map2, map, sizeof(map));
	while (1) {
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] && !v[i][j]) {
					dfs(i, j);
					cnt++;
				}
			}
		}
		if (cnt > 1) {
			printf("%d\n", year);
			return 0;
		}
		if (cnt == 0) {
			printf("0\n");
			return 0;
		}
		memcpy(map, map2, sizeof(map));
		memset(v, 0, sizeof(v));
		year++;
	}
	return 0;
}
