#include <stdio.h>

int
main(void) {
  int n;
  scanf("%d", &n);
  printf((n % 7 == 0 || n % 7 == 2) ? "CY" : "SK");
  return 0;
}

/* f(1) = 1;                                         */
/* f(2) = 0;                                         */
/* f(3) = 1;                                         */
/* f(4) = 1;                                         */

/* f(n) = (!f(n - 1)) || (!f(n - 3)) || (!f(n - 4)); */
