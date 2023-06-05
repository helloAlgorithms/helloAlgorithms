#include <stdio.h>

int
main(void) {
  int n, r1, c1, r2, c2;
  scanf("%d", &n);
  scanf("%d %d %d %d", &r1, &c1, &r2, &c2);

  r1 = r1 >= r2 ? r1 - r2 : r2 - r1;
  c1 = c1 >= c2 ? c1 - c2 : c2 - c1;
  if (r1 % 2 == 1 || ((r1 / 2 + c1) % 2 == 1))
    printf("-1");
  else
    printf("%d", (r1 / 2 >= c1) ? r1 / 2 : ((c1 + r1 / 2) / 2));

  return 0;
}
