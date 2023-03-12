#include <stdio.h>

int
gcd(int a, int b) {
  if (a % b == 0)
    return (b);
  return (gcd(b, a % b));
}

int
lcm(int a, int b) {
  return (a * b / gcd(a, b));
}

int n;
char scores[50][7];

int
readFloat(char* score) {
  int s;
  s = 0;
  while (*score != '.')
    s = 10 * s + *(score++) - '0';
  ++score;
  while (*score != '\0')
    s = 10 * s + *(score++) - '0';
  return (s);
}

int
isPossible(int s, int x) {
  int i;

  for (i = 0; i < x; ++i) {
    if (s % 1000 == (i * 1000) / x)
      return (1);
  }
  return (0);
}

int
check(int x) {
  int i;
  int s;

  for (i = 0; i < n; ++i) {
    s = readFloat(scores[i]);
    if (!isPossible(s, x))
      return (0);
  }
  return (1);
}

int
main(void) {
  int i;
  int x;
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%s", scores[i]);
  }
  x = 1;
  while (!check(x))
    ++x;
  printf("%d\n", x);
  return (0);
}
