#include <stdio.h>

int
main(void) {
  int n, count;
  int num;
  int result[10] = {0};
  int i, j;

  scanf("%d", &n);

  for (i = 0; i < n; ++i) {
    scanf("%d", &num);
    count = 0;
    for (j = 0; j < n; ++j) {
      if (count > num)
        break;
      if (result[j] == 0)
        ++count;
    }
    result[j - 1] = i + 1;
  }
  for (i = 0; i < n; ++i) {
    printf("%d ", result[i]);
  }
  return (0);
}
