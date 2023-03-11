#include <stdio.h>

int
isPrime(int num) {
  int p;
  if (num == 1)
    return (0);
  for (p = 2; p <= num / p; ++p) {
    if (num % p == 0)
      return (0);
  }
  return (1);
}

int
isUnderPrime(int num) {
  int count;
  int p;

  count = 0;
  p = 2;
  while (num > 1) {
    if (p > num / p)
      return (isPrime(count + 1));
    if (num % p == 0) {
      num /= p;
      ++count;
    } else {
      ++p;
    }
  }
  return (isPrime(count));
}

int
main(void) {
  int a, b;
  int count;
  int i;
  scanf("%d %d", &a, &b);
  count = 0;
  for (i = a; i <= b; ++i) {
    count += isUnderPrime(i);
  }
  printf("%d\n", count);
  return (0);
}
