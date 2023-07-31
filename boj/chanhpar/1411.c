#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int
cmp(const void* a, const void* b) {
  return strcmp((const char*)a, (const char*)b);
}

void
convert(char* a) {
  int flag;
  char map[26];
  int c, i, b;

  flag = 0;
  b = 0;
  for (i = 0; a[i]; ++i) {
    c = a[i] - 'a';
    if (!(flag & (1 << c))) {
      map[c] = b++;
      flag |= 1 << c;
    }
    a[i] = 'a' + map[c];
  }
}

int
main(void) {
  int n, i, c, t;
  char(*a)[51];
  scanf("%d", &n);
  a = malloc(sizeof(char[51]) * n);
  for (i = 0; i < n; ++i) {
    scanf("%s", a[i]);
    convert(a[i]);
  }

  qsort(a, n, sizeof(char[51]), cmp);

  t = 0;
  c = 1;
  for (i = 1; i < n; ++i) {
    if (strcmp(a[i], a[i - 1]) == 0)
      ++c;
    else {
      t += (c * (c - 1)) / 2;
      c = 1;
    }
  }
  t += (c * (c - 1)) / 2;

  free(a);

  printf("%d", t);

  return 0;
}
