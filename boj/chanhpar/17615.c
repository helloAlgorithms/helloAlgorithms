#include <stdio.h>

int
getMin(int a, int b) {
  return a < b ? a : b;
}

int
main(void) {
  int n, idx, left, right, countRed, tmp;
  char s[500001];

  scanf("%d", &n);
  scanf("%s", s);
  countRed = 0;
  for (idx = 0; s[idx] == s[0]; ++idx)
    countRed += s[idx] == 'R';
  tmp = idx;

  for (; s[idx]; ++idx)
    countRed += s[idx] == 'R';
  if (s[0] == 'R')
    left = getMin(countRed - tmp, n - countRed);
  else
    left = getMin(countRed, n - countRed - tmp);

  for (idx = n - 1; idx >= 0 && s[idx] == s[n - 1]; --idx)
    ;
  if (s[n - 1] == 'R')
    right = getMin(countRed - (n - idx - 1), n - countRed);
  else
    right = getMin(countRed, n - countRed - (n - idx - 1));

  printf("%d", getMin(left, right));
  return 0;
}
