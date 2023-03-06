#include <stdio.h>

int picture[100][100];

int
main(void) {
  int n, m, x1, y1, x2, y2;
  int i, j;
  int count;
  scanf("%d %d", &n, &m);
  while (n--) {
    scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
    for (i = x1 - 1; i < x2; ++i) {
      for (j = y1 - 1; j < y2; ++j) {
        ++picture[i][j];
      }
    }
  }
  count = 0;
  for (i = 0; i < 100; ++i) {
    for (j = 0; j < 100; ++j) {
      if (picture[i][j] > m)
        ++count;
    }
  }
  printf("%d\n", count);
  return (0);
}
