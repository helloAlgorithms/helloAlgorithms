#include <stdio.h>

typedef struct {

	int c;
	int count;
	int y;
	int x;
} t_point;

int n, m;
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};
char temp[1002][1002];
int arr[1002][1002];
int v[2][1002][1002];
t_point q[5000001];
int head;
int tail;
int is_valid;
int min;

void enqueue(t_point t) {q[tail++] = t;}
void dequeue() {head++;}

int check_valid(int y, int x, int c) {

	if (y < 0 || x < 0 || y > n - 1 || x > m - 1)
		return 0;
	if (v[c][y][x])
		return 0;
	return 1;
}

void bfs() {

	t_point p = {1, 1, 0, 0};
	enqueue(p);
	v[p.c][0][0] = 1;

	while (head != tail) {
		t_point temp = q[head];
		if (temp.y == n - 1 && temp.x == m - 1) {
			is_valid = 1;
			min = temp.count;
			return ;
		}
		if (temp.c == 0) {
			for (int i = 0; i < 4; i++) {
				int ny = temp.y + dy[i];
				int nx = temp.x + dx[i];
				if (check_valid(ny, nx, temp.c)) {
					if (arr[ny][nx] == 1)
						continue ;
					t_point nt = {temp.c, temp.count + 1, ny, nx};
					enqueue(nt);
					v[temp.c][ny][nx] = 1;
				}
			}
		}
		else if (temp.c == 1) {
			for (int i = 0; i < 4; i++) {
				int ny = temp.y + dy[i];
				int nx = temp.x + dx[i];
				if (check_valid(ny, nx, temp.c)) {
					if (arr[ny][nx] == 1) {
						t_point nt = {temp.c - 1, temp.count + 1, ny, nx};
						enqueue(nt);
						v[temp.c - 1][ny][nx] = 1;
						continue ;
					}
					t_point nt = {temp.c, temp.count + 1, ny, nx};
					enqueue(nt);
					v[temp.c][ny][nx] = 1;
				}
			}
		}
		dequeue();
	}
}

int main() {

	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%s", temp[i]);
		for (int j = 0; j < m; j++) {
			arr[i][j] = temp[i][j] - 48;
		}
	}
	bfs();
	if (is_valid)
		printf("%d\n", min);
	else
		printf("-1\n");
	return 0;
}
