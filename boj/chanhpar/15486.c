#include <stdio.h>
#include <stdlib.h>

#define SIZE (1 << 20)

char readChar(void) {
  static size_t idx = SIZE;
  static char buff[SIZE];
  if (idx == SIZE) { fread(buff, sizeof(char), SIZE, stdin); idx = 0; }
  return buff[idx++];
}

int readInt(void) {
  int r; char c;
  do { c = readChar(); } while (c < '0' || c > '9');
  r = 0;
  do { r = 10 * r + c - '0'; c = readChar(); } while (c >= '0' && c <= '9');
  return r;
}

int m(int const a, int const b) { return a > b ? a : b; }

int main(void) {
  int n, i, *t, *p, *d;
  scanf("%d", &n);
  t = malloc(sizeof(int) * n); p = malloc(sizeof(int) * n); d = malloc(sizeof(int) * (n + 1));
  for (i = 0; i < n; ++i) { t[i] = readInt(); p[i] = readInt(); };
  d[n] = 0;
  for (i = n - 1; i >= 0; --i) d[i] = m(d[i + 1], (i + t[i] <= n) * (p[i] + d[i + t[i]]));
  printf("%d", d[0]);
  free(t); free(p); free(d);
  return 0;
}
