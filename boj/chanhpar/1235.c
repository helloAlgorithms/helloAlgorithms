#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int len;

int
cmp(const void* a, const void* b) {
  return (strcmp((const char*)a, (const char*)b));
}

void
rev(char* name) {
  int i, j;
  char c;
  if (len <= 0) {
    while (name[len])
      ++len;
  }

  i = 0;
  j = len - 1;
  while (i < j) {
    c = name[i];
    name[i++] = name[j];
    name[j--] = c;
  }
}

int
main(void) {
  int n, i, j, k;
  char(*names)[101];

  scanf("%d", &n);
  names = malloc(sizeof(char[101]) * n);
  for (i = 0; i < n; ++i) {
    scanf("%s", names[i]);
    rev(names[i]);
  }
  qsort(names, n, sizeof(char[101]), cmp);
  k = 1;
  for (i = 1; i < n; ++i) {
    j = 0;
    while (names[i - 1][j] == names[i][j])
      ++j;
    if (j + 1 > k)
      k = j + 1;
  }
  printf("%d\n", k);
  return (0);
}
