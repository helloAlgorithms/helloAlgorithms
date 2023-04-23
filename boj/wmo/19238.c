#include <stdio.h>
#include <string.h>

typedef struct {

	int y;
	int x;
	int dis;
	int f;
	int dy;
	int dx;
} t_point;

t_point q[10000001];
t_point p[401];
t_point start;

int head, tail, n, m, k;

int dy[4] = {0, 1, -1, 0};
int dx[4] = {1, 0, 0, -1};

int v[22][22];
int u[401];
int map[22][22];

void init() {
	//memset(q, 0, sizeof(q));
	memset(v, 0, sizeof(v));
	head = 0;
	tail = 0;
}
void enqueue(t_point p) {q[tail++] = p;}
void dequeue() {head++;}
int check(int y, int x) {

	if (y <= 0 || x <= 0 || y > n || x > n)
		return 0;
	if (v[y][x] || map[y][x] == 1)
		return 0;
	return 1;
}

//최단거리를 찾아주는 bfs
int bfs(t_point start, int dest_y, int dest_x) {

	v[start.y][start.x] = 1;
	enqueue(start);

	while (head < tail) {
		t_point temp = q[head];
		dequeue();
		if (temp.y == dest_y && temp.x == dest_x)
			return (temp.dis);
		//if (temp.dis > max)
		//	return (2147483647);
		if (temp.f == 0) continue;
		for (int i = 0; i < 4; i++) {
			int ny = dy[i] + temp.y;
			int nx = dx[i] + temp.x;
			if (check(ny, nx)) {
				t_point new;
				memset(&new, 0, sizeof(t_point));
				new.y = ny;
				new.x = nx;
				new.f = temp.f - 1;
				new.dis = temp.dis + 1;
				v[ny][nx] = 1;
				enqueue(new);
			}
		}
	}
	return 2147483647;
}
int find_dest(t_point start) {

	int min = 2147483646;
	int min_index = -1;
	for (int i = 0; i < m; i++) {
		if (u[i]) continue;
		int temp = bfs(start, p[i].y, p[i].x);
		init();
		if (min > temp) {
			min_index = i;
			min = temp;
		}
		else if (min == temp) {
			if (p[min_index].y == p[i].y) {
				if (p[min_index].x > p[i].x)
					min_index = i;
				continue;
			}
			if (p[min_index].y > p[i].y)
				min_index = i;
		}
	}
	if (min_index != -1)
		u[min_index] = 1;
	return (min_index);
}

int main() {

	int try;
	memset(&start, 0, sizeof(t_point));

	scanf("%d %d %d", &n, &m, &k);
	try = m;
	start.f = k;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			scanf("%d", &map[i][j]);
	scanf("%d %d", &start.y, &start.x);
	for (int i = 0; i < m; i++)
		scanf("%d %d %d %d", &p[i].y, &p[i].x, &p[i].dy, &p[i].dx);

	while (try--) {
		int index = find_dest(start);
		if (index == -1) {
			printf("-1\n");
			return 0;
		}
		int dis = bfs(start, p[index].y, p[index].x);
		init();
		start.f -= dis;
		start.y = p[index].y;
		start.x = p[index].x;
		dis = bfs(start, p[index].dy, p[index].dx);
		init();
		start.f = start.f - dis + dis * 2;
		start.y = p[index].dy;
		start.x = p[index].dx;
		if (dis == 2147483647) {
			printf("-1\n");
			return 0;
		}
	}
	printf("%d\n", start.f);
	return 0;
}


