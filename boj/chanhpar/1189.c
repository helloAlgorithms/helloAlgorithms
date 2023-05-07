#include <stdio.h>

#define SIZE 26

int r, c, k;
char board[6][6];
int ans;

enum {
  EMPTY = '.',
  VISIT = '+',
  WALL = 'T'
};

void
dfs(int row, int col, int depth) {
  static const int dx[] = {0, 1, 0, -1};
  static const int dy[] = {1, 0, -1, 0};
  int i;

  board[row][col] = VISIT;

  for (i = 0; i < 4; ++i) {
    int nx = row + dx[i];
    int ny = col + dy[i];

    if (nx < 0 || nx >= r || ny < 0 || ny >= c || board[nx][ny] != EMPTY)
      continue;
    if (depth + 1 == k) {
      if (nx == 0 && ny == c - 1)
        ++ans;
      continue;
    }
    dfs(nx, ny, depth + 1);
  }

  board[row][col] = EMPTY;
}

int
main(void) {
  int i;
  scanf("%d %d %d", &r, &c, &k);
  for (i = 0; i < r; ++i)
    scanf("%s", board[i]);

  if (board[r - 1][0] == EMPTY)
    dfs(r - 1, 0, 1);

  printf("%d", ans);
  return (0);
}
