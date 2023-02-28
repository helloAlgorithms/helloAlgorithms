#include <stdio.h>

int n;

static int
dist(int a, int b) {
  return (a > b ? a - b : b - a);
}

static char
pattern(int row, int col) {
  const int side = 2 * n - 1;
  const int d = dist(row % side, n - 1) + dist(col % side, n - 1);

  if (d >= n)
    return ('.');
  return ('a' + d % 26);
}

int
main(void) {
  int r1, r2, c1, c2;
  int i, j;
  scanf("%d %d %d %d %d", &n, &r1, &c1, &r2, &c2);
  for (i = r1; i <= r2; ++i) {
    for (j = c1; j <= c2; ++j) {
      printf("%c", pattern(i, j));
    }
    printf("\n");
  }
  return (0);
}
