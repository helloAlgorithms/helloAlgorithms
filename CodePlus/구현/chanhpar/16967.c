#include <stdio.h>

int h, w, x, y;
int a[300][300];
int b[600][600];

int
main(void) {
  int i, j;
  scanf("%d %d %d %d", &h, &w, &x, &y);
  for (i = 0; i < h + x; ++i) {
    for (j = 0; j < w + y; ++j) {
      scanf("%d", &b[i][j]);
      if (i < x || j < y)
        a[i][j] = b[i][j];
      else if (i >= h || j >= w)
        continue;
      else {
        a[i][j] = b[i][j] - a[i - x][j - y];
      }
    }
  }
  for (i = 0; i < h; ++i) {
    for (j = 0; j < w; ++j) {
      printf("%d ", a[i][j]);
    }
    printf("\n");
  }
  return (0);
}
