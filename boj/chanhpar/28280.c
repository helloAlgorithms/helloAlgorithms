#include <stdio.h>

void
a(void) {
  int k, b;
  scanf("%d", &k);
  b = 0;
  while (k != 1) {
    if (k & 1)
      ++k;
    else
      k >>= 1;
    ++b;
  }
  printf("%d\n", b);
}

int
main(void) {
  int t;
  scanf("%d", &t);
  while (t--)
    a();
  return 0;
}
