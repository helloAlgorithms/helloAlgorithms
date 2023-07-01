#include <stdio.h>

long gcd(long a, long b) { return a % b ? gcd(b, a % b) : b; }

long lcm(long a, long b) { return a * (b / gcd(a, b)); }

int main(void) {
  int a, b;
  scanf("%d %d", &a, &b);
  printf("%ld\n", lcm(a, b));
  return 0;
}
