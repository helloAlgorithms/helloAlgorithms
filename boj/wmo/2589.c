#include <stdio.h>
#include <string.h>

typedef struct {
    int y;
    int x;
    int c;
} t_point;
int n, m, max, head, tail;
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};
int v[52][52];
char map[52][52];
t_point q[10001];

void enqueue(t_point p) {q[tail++] = p;}
void dequeue(){head++;}
int check(int y, int x) {
    if (y < 0 || x < 0 || y >= n || x >= m)
        return 0;
    if (v[y][x] || map[y][x] == 'W')
        return 0;
    return 1;
}

void bfs(int y, int x) {
    t_point t = {y, x, 0};
    enqueue(t);
    v[y][x] = 1;
    while (head <= tail) {
        t_point temp = q[head];
        if (temp.c > max)
            max = temp.c;
        for (int i = 0; i < 4; ++i) {
            int ny = dy[i] + temp.y;
            int nx = dx[i] + temp.x;
            if (check(ny, nx)) {
                t_point new = {ny, nx, temp.c + 1};
                v[ny][nx] = 1;
                enqueue(new);
            }
        }
        dequeue();
    }
}

int main() {

    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; ++i) {
        scanf("%s", map[i]);
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (map[i][j] == 'L') {
                bfs(i, j);
                memset(v, 0, sizeof(v));
                memset(q, 0, sizeof(q));
                head = 0;
                tail = 0;
            }
        }
    }
    printf("%d\n", max);
    return 0;
}




