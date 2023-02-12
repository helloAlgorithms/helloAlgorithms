#include <stdio.h>

int n;
char board[52][52];
int maxCount;

void
swap(int a, int b, int x, int y) {
  char c;

  c = board[a][b];
  board[a][b] = board[x][y];
  board[x][y] = c;
}

void
check(int row, int col) {
  int i, j;

  i = row;
  j = row;
  while (i >= 0 && board[row][col] == board[i][col])
    --i;
  while (j < n && board[row][col] == board[j][col])
    ++j;
  if (maxCount < j - i - 1)
    maxCount = j - i - 1;
  i = col;
  j = col;
  while (i >= 0 && board[row][col] == board[row][i])
    --i;
  while (j < n && board[row][col] == board[row][j])
    ++j;
  if (maxCount < j - i - 1)
    maxCount = j - i - 1;
}

int
main(void) {
  int i, j, count;
  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    scanf("%s", board[i]);

  for (i = 0; i < n; ++i) {
    j = 0;
    while (j < n) {
      count = 1;
      while (board[i][j] == board[i][j + 1]) {
        ++j;
        ++count;
      }
      if (maxCount < count)
        maxCount = count;
      ++j;
    }
  }

  for (i = 0; i < n; ++i) {
    j = 0;
    while (j < n) {
      count = 1;
      while (board[j][i] == board[j + 1][i]) {
        ++j;
        ++count;
      }
      if (maxCount < count)
        maxCount = count;
      ++j;
    }
  }

  for (i = 0; i < n; ++i) {
    for (j = 1; j < n; ++j) {
      if (board[i][j - 1] == board[i][j])
        continue;
      swap(i, j - 1, i, j);
      check(i, j);
      check(i, j - 1);
      swap(i, j - 1, i, j);
    }
  }

  for (i = 1; i < n; ++i) {
    for (j = 0; j < n; ++j) {
      if (board[i - 1][j] == board[i][j])
        continue;
      swap(i - 1, j, i, j);
      check(i, j);
      check(i - 1, j);
      swap(i - 1, j, i, j);
    }
  }

  printf("%d\n", maxCount);

  return (0);
}
