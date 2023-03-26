#include <stdio.h>

int
main(void) {
  int a, k, count;
  scanf("%d %d", &a, &k);
  count = 0;
  while (k > a) {
    if (k >= 2 * a) {
      if (k & 1) {
        --k;
      } else {
        k >>= 1;
      }
      ++count;
    } else {
      count += k - a;
      break;
    }
  }
  printf("%d\n", count);
  return (0);
}
