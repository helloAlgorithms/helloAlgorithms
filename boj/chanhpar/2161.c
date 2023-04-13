#include <stdio.h>

int
main(void) {
  int n, i, x, front, back, flag;
  int q[1001];

  scanf("%d", &n);
  for (i = 1; i <= n; ++i)
    q[back++ % 1001] = i;
  flag = 0;
  while (front != back) {
    x = q[front++ % 1001];
    if (flag)
      q[back++ % 1001] = x;
    else
      printf("%d ", x);
    flag ^= 1;
  }
  return (0);
}
