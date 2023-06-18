#include <stdio.h>

int
main(void) {
  int n, m, i, j, k, size;
  char square[51][51];
  scanf("%d %d", &n, &m);
  for (i = 0; i < n; ++i)
    scanf("%s", square[i]);
  size = 0;
  for (i = 0; i < n; ++i)
    for (j = 0; j < m; ++j)
      for (k = size + 1; i + k < n && j + k < m; ++k)
        if (square[i][j] == square[i + k][j] && square[i][j] == square[i][j + k]
            && square[i][j] == square[i + k][j + k])
          size = k;

  printf("%d", (size + 1) * (size + 1));
  return 0;
}
