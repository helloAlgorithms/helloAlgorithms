#include <stdio.h>

int r, c;
char board[21][21];
int dp[21][21];
int maxDepth;

void
dfs(int row, int col, int depth, int visit) {
  static const int dx[4] = {1, 0, -1, 0};
  static const int dy[4] = {0, 1, 0, -1};
  int nx, ny;
  int i;

  visit |= 1 << board[row][col];
  if (dp[row][col] == visit)
    return;
  dp[row][col] = visit;

  ++depth;
  if (maxDepth < depth)
    maxDepth = depth;

  for (i = 0; i < 4; ++i) {
    nx = row + dx[i];
    ny = col + dy[i];
    if (nx < 0 || nx >= r || ny < 0 || ny >= c)
      continue;
    if (visit & (1 << board[nx][ny]))
      continue;
    dfs(nx, ny, depth, visit);
  }
}

int
main(void) {
  int i, j;
  scanf("%d %d", &r, &c);
  for (i = 0; i < r; ++i) {
    scanf("%s", board[i]);
    for (j = 0; j < c; ++j)
      board[i][j] -= 'A';
  }
  dfs(0, 0, 0, 0);
  printf("%d\n", maxDepth);
  return 0;
}
