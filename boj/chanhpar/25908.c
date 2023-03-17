#include <stdio.h>

int
sumFn(int n) {
  int ret;
  int left, right;

  ret = 0;
  left = 1;
  while (left <= n) {
    right = n / (n / left);
    ret += (n / left) * (1 - (left & 1) - (right & 1));
    left = right + 1;
  }
  return (ret);
}

int
main(void) {
  int s, t;
  scanf("%d %d", &s, &t);
  printf("%d\n", sumFn(t) - sumFn(s - 1));
  return (0);
}
