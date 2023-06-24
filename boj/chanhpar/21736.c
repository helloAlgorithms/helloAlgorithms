#include <stdio.h>

int n, m;
char board[601][601];

int
bfs(int row, int col) {
  int que[80000];
  int f, r, a, b, c, i, t;
  const int x[] = {1, 0, -1, 0};
  const int y[] = {0, 1, 0, -1};

  board[row][col] = 'X';
  t = 0;
  f = r = 0;
  que[r++] = 600 * row + col;
  while (f != r) {
    f %= 80000;
    c = que[f++];
    for (i = 0; i < 4; ++i) {
      a = c / 600 + x[i];
      b = c % 600 + y[i];
      if (a < 0 || a >= n || b < 0 || b >= m || board[a][b] == 'X')
        continue;
      t += board[a][b] == 'P';
      board[a][b] = 'X';
      r %= 80000;
      que[r++] = 600 * a + b;
    }
  }
  return t;
}

int
main(void) {
  int i, j, count;
  scanf("%d %d", &n, &m);
  for (i = 0; i < n; ++i)
    scanf("%s", board[i]);

  for (i = 0; i < n; ++i) {
    for (j = 0; j < m; ++j) {
      if (board[i][j] == 'I') {
        count = bfs(i, j);
        count > 0 ? printf("%d", count) : printf("TT");
        return 0;
      }
    }
  }

  return 0;
}
