#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int score;
  int num;
} pair;

pair scores[8];

int
cmp(const void* a, const void* b) {
  if (((const pair*)a)->score < ((const pair*)b)->score)
    return (1);
  return (-1);
}

int
main(void) {
  int i;
  int sum, flag;
  for (i = 0; i < 8; ++i) {
    scanf("%d", &scores[i].score);
    scores[i].num = i + 1;
  }

  qsort(scores, 8, sizeof(pair), cmp);

  sum = 0;
  flag = 0;
  for (i = 0; i < 5; ++i) {
    sum += scores[i].score;
    flag |= 1 << (scores[i].num - 1);
  }
  printf("%d\n", sum);
  for (i = 0; i < 8; ++i) {
    if (flag & (1 << i))
      printf("%d ", i + 1);
  }
  return (0);
}
