#include <stdio.h>

static int
isSame(char (*input)[51], int n, int j) {
  int ret;
  int i;

  ret = 1;
  for (i = 0; i < n && ret; ++i) {
    ret &= input[i][j] == input[0][j];
  }
  return ret;
}

int
main(void) {
  int n;
  int i;
  char input[50][51];
  char result[51];
  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    scanf("%s", input[i]);
  for (i = 0; input[0][i]; ++i)
    result[i] = isSame(input, n, i) ? input[0][i] : '?';
  result[i] = '\0';
  printf("%s", result);
  return 0;
}
