#include <stdio.h>

char flag[1000];

int
main(void) {
  int n, m, p, count;
  scanf("%d %d", &n, &p);

  m = n;
  count = 0;
  do {
    flag[m] = 1;
    m = (m * n) % p;
  } while (flag[m] == 0);
  do {
    flag[m] = 0;
    ++count;
    m = (m * n) % p;
  } while (flag[m] == 1);
  printf("%d\n", count);
  return (0);
}
