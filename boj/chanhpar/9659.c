#include <stdio.h>

int
main(void) {
  long n;
  scanf("%ld", &n);
  printf(n & 1 ? "SK" : "CY");
  return 0;
}
