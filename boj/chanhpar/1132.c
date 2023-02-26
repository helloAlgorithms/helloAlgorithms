#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int c;
  long count;
} pair;

int
cmp(const void* a, const void* b) {
  const long x = ((const pair*)a)->count;
  const long y = ((const pair*)b)->count;

  if (x > y)
    return (-1);
  if (x < y)
    return (1);
  return (0);
}

int n;
pair count[10];
char isNotZero[10];
char value[10];
char buff[13];

int
main(void) {
  int i, j;
  long mask;
  long result;
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%s", buff);
    isNotZero[buff[0] - 'A'] = 1;
    for (j = 0; buff[j]; ++j)
      ;
    mask = 1;
    while (j-- > 0) {
      count[buff[j] - 'A'].count += mask;
      mask *= 10;
    }
  }

  for (i = 0; i < 10; ++i)
    count[i].c = i;

  qsort(count, 10, sizeof(pair), cmp);

  for (i = 0; i < 10 && count[i].count > 0; ++i) {
    value[count[i].c] = 9 - i;
  }

  if (i == 10) {
    --i;
    while (i > 0 && isNotZero[count[i].c]) {
      value[count[i].c] = value[count[i - 1].c];
      value[count[i - 1].c] = 0;
      --i;
    }
  }

  result = 0;

  for (i = 0; i < 10; ++i)
    result += count[i].count * value[count[i].c];

  printf("%ld\n", result);
  return (0);
}
