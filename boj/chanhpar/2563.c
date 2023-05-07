#include <stdio.h>

int main(void) {
  int n, x, y, i, j, count;
  char paper[100][100] = {};
  scanf("%d", &n);
  count = 0;
  while (n-- && scanf("%d %d", &x, &y))
    for (i = 0; i < 10; ++i)
      for (j = 0; j < 10; ++j)
        if (paper[x + i][y + j] == 0)
          (paper[x + i][y + j] = 1) && ++count;
  printf("%d", count);
  return (0);
}
