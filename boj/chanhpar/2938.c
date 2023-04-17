#include <stdio.h>

int
main(void) {
  int mod[3][10000];
  int size[3];
  int n;
  int i, j;
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%d", &j);
    mod[j % 3][size[j % 3]++] = j;
  }
  if ((size[1] + size[2] < size[0] - 1) || (size[1] && size[2] && size[0] == 0))
    return (printf("-1"), 0);
  while (size[1] && size[0] > 1) {
    printf("%d ", mod[0][--size[0]]);
    printf("%d ", mod[1][--size[1]]);
  }
  while (size[1])
    printf("%d ", mod[1][--size[1]]);
  while (size[2] && size[0]) {
    printf("%d ", mod[0][--size[0]]);
    printf("%d ", mod[2][--size[2]]);
  }
  while (size[0])
    printf("%d ", mod[0][--size[0]]);
  while (size[2])
    printf("%d ", mod[2][--size[2]]);
  return (0);
}
