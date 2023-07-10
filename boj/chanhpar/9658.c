#include <stdio.h>

int
main(void) {
  int n;
  scanf("%d", &n);
  printf((n % 7 == 1 || n % 7 == 3) ? "CY" : "SK");
  return 0;
}
