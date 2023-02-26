#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int c;
  int count;
} pair;

int
cmp(const void* a, const void* b) {
  const int x = ((const pair*)a)->count;
  const int y = ((const pair*)b)->count;

  if (x > y)
    return (-1);
  if (x < y)
    return (1);
  return (0);
}

int n;
pair count[26];
char value[26];
char buff[10];

int
main(void) {
  int i, j;
  int mask;
  int result;
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%s", buff);
    for (j = 0; buff[j]; ++j)
      ;
    mask = 1;
    while (j-- > 0) {
      count[buff[j] - 'A'].count += mask;
      mask *= 10;
    }
  }

  for (i = 0; i < 26; ++i)
    count[i].c = i;

  qsort(count, 26, sizeof(pair), cmp);

  for (i = 0; i < 10 && count[i].count > 0; ++i)
    value[count[i].c] = 9 - i;

  result = 0;

  for (i = 0; i < 10; ++i)
    result += count[i].count * value[count[i].c];

  printf("%d\n", result);
  return (0);
}
