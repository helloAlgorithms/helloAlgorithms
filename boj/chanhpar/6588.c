#include <stdio.h>

char check[1000001];
int n, a, b;

int
isPrime(int k) {
  int i;
  if (check[k] == 0) {
    for (i = 2; i <= k / i; ++i) {
      if (k % i == 0)
        return (check[k] = 2, 0);
    }
    return (check[k] = 1, 1);
  }
  return (check[k] & 1);
}

int
f(void) {
  for (a = 3; a <= (n >> 1); a += 2) {
    if (isPrime(a) && isPrime(n - a)) {
      b = n - a;
      return (1);
    }
  }
  return (1);
}

int
main(void) {
  while (scanf("%d", &n) && n != 0 && f())
    printf("%d = %d + %d\n", n, a, b);
  return (0);
}
