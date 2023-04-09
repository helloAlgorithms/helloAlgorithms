#include <stdio.h>

static int const arr[2][3] = {{1, 2, 3}, {3, 2, 1}};

int
main(void) {
  long a, b;
  scanf("%ld", &a);
  scanf("%ld", &b);
  if (a == 1)
    printf("%ld\n", 8 * b);
  else if (a == 5)
    printf("%ld\n", 8 * b + 4);
  else
    printf("%ld\n", 4 * b + arr[b % 2][a - 2]);
  return (0);
}
