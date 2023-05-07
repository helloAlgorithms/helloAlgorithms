#include <stdio.h>

int
getMax(int a, int b) {
  return a > b ? a : b;
}

int
getAbs(int a) {
  return a > 0 ? a : -a;
}

int
getPos(int row, int col) {
  const int bound = getMax(getAbs(row), getAbs(col));
  const int sq = (2 * bound + 1) * (2 * bound + 1);

  if (row == bound)
    return sq - (bound - col);
  if (-col == bound)
    return sq - 3 * bound + row;
  if (-row == bound)
    return sq - 5 * bound - col;
  return sq - 7 * bound - row;
}

int
getWidth(int num) {
  int w;
  w = 0;
  while (num > 0) {
    ++w;
    num /= 10;
  }
  return w;
}

int
getMaxWidth(int r1, int c1, int r2, int c2) {
  int w, i, j;

  w = 0;
  for (i = r1; i <= r2; ++i) {
    for (j = c1; j <= c2; ++j) {
      w = getMax(w, getWidth(getPos(i, j)));
    }
  }
  return w;
}

int
main(void) {
  int r1, c1, r2, c2;
  int i, j;
  int maxWidth;

  scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
  maxWidth = getMaxWidth(r1, c1, r2, c2);
  for (i = r1; i <= r2; ++i)
    for (j = c1; j <= c2; ++j)
      printf("%*d%c", maxWidth, getPos(i, j), j == c2 ? '\n' : ' ');
  return 0;
}
