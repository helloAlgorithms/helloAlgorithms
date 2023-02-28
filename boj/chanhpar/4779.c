#include <stdio.h>
#include <unistd.h>

int pow3[13];
char buff[1594324];
int idx;

void
space(int n) {
  int i;
  for (i = 0; i < n; ++i)
    buff[idx++] = ' ';
}

void
cantor(int n) {
  if (n == 0) {
    buff[idx++] = '-';
    return;
  }
  cantor(n - 1);
  space(pow3[n - 1]);
  cantor(n - 1);
}

int
main(void) {
  int n;
  int i;
  pow3[0] = 1;
  for (i = 1; i < 13; ++i)
    pow3[i] = 3 * pow3[i - 1];
  while (scanf("%d", &n) > 0) {
    cantor(n);
    buff[idx] = '\0';
    printf("%s\n", buff);
    idx = 0;
  }
  return (0);
}
