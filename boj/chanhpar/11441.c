#include <stdio.h>

char buff[1 << 20];

char
readChar(void) {
  static size_t idx = 1 << 20;
  if (idx == 1 << 20) {
    fread(buff, sizeof(char), 1 << 20, stdin);
    idx = 0;
  }
  return buff[idx++];
}

int
readInt(void) {
  int r;
  int sign;
  char c;
  do {
    c = readChar();
  } while (c != '-' && (c < '0' || c > '9'));
  r = 0;
  sign = 1;
  if (c == '-') {
    c = readChar();
    sign = -1;
  }
  do {
    r = 10 * r + c - '0';
    c = readChar();
  } while (c >= '0' && c <= '9');
  return r * sign;
}

int
main(void) {
  int n, i, m, l, r;
  int a[100001];
  n = readInt();
  a[0] = 0;
  for (i = 1; i <= n; ++i) {
    a[i] = readInt();
    a[i] += a[i - 1];
  }
  m = readInt();
  for (i = 0; i < m; ++i) {
    l = readInt();
    r = readInt();
    printf("%d\n", a[r] - a[l - 1]);
  }
  return 0;
}
