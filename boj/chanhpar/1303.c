#include <stdio.h>

int n, m;
char board[101][101];
char visit[101][101];
int que[10001];
int head;
int tail;
int bPower;
int wPower;

void
enque(int a, int b) {
  que[tail++] = 100 * a + b;
  tail %= 10001;
}

int
deque(void) {
  head %= 10001;
  return (que[head++]);
}

static const int dx[] = {1, 0, -1, 0};
static const int dy[] = {0, 1, 0, -1};

int
main(void) {
  int i, j, k;
  int x, y, nx, ny;
  int count;
  char color;
  scanf("%d %d", &m, &n);
  for (i = 0; i < n; ++i)
    scanf("%s", board[i]);
  for (i = 0; i < n; ++i) {
    for (j = 0; j < m; ++j) {
      if (visit[i][j])
        continue;
      count = 1;
      visit[i][j] = 1;
      enque(i, j);
      color = board[i][j];
      while (head != tail) {
        x = deque();
        y = x % 100;
        x /= 100;
        for (k = 0; k < 4; ++k) {
          nx = x + dx[k];
          ny = y + dy[k];
          if (nx < 0 || ny < 0 || nx >= n || ny >= m)
            continue;
          if (visit[nx][ny] || board[nx][ny] != color)
            continue;
          visit[nx][ny] = 1;
          enque(nx, ny);
          ++count;
        }
      }
      if (color == 'W')
        wPower += count * count;
      else
        bPower += count * count;
    }
  }
  printf("%d %d", wPower, bPower);
  return (0);
}
