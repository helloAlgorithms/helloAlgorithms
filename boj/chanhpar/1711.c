#include <stdio.h>

long point[1500][2];

int
isRect(int i, int j, int k) {
  return ((point[i][0] - point[j][0]) * (point[i][0] - point[k][0])
              + (point[i][1] - point[j][1]) * (point[i][1] - point[k][1])
          == 0);
}

int
main(void) {
  int n;
  int i, j, k;
  int count;
  scanf("%d", &n);
  count = 0;
  for (i = 0; i < n; ++i) {
    scanf("%ld %ld", &point[i][0], &point[i][1]);
    for (j = 0; j < i; ++j) {
      for (k = 0; k < j; ++k) {
        count += isRect(i, j, k) || isRect(j, k, i) || isRect(k, i, j);
      }
    }
  }
  printf("%d\n", count);
  return (0);
}
