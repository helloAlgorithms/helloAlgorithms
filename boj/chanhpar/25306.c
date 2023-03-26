#include <stdio.h>

unsigned long accXOR(unsigned long n) {
  switch ((n + 1) % 4) {
    case 0:
      return 0;
    case 1:
      return n;
    case 2:
      return 1;
    default:
      return n + 1;
  }
}

int main(void) {
  unsigned long a, b;
  scanf("%lu %lu", &a, &b);
  printf("%lu\n", accXOR(a - 1) ^ accXOR(b));
  return (0);
}
