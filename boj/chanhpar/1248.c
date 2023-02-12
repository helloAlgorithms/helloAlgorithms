#include <stdio.h>
#include <stdlib.h>

#define RANGE 10

int n;
int seq[11];
int sumSeq[12];
char sign[11][11];

int
sum(int start, int end) {
  return (sumSeq[end + 1] - sumSeq[start]);
}

int
isPos(int k) {
  return (k > 0);
}

int
isNeg(int k) {
  return (k < 0);
}

int
isZero(int k) {
  return (k == 0);
}

int (*getComp(char c))(int) {
  switch (c) {
    case ('+'):
      return (isPos);
    case ('-'):
      return (isNeg);
    default:
      return (isZero);
  }
}

int
isValid(int idx) {
  int i;

  for (i = idx; i >= 0; --i) {
    if (!getComp(sign[i][idx])(sum(i, idx)))
      return (0);
  }
  return (1);
}

void
print(void) {
  int i;
  for (i = 0; i < n; ++i)
    printf("%d ", seq[i]);
  printf("\n");
}

void
dfs(int start) {
  int i;

  if (start == n) {
    print();
    exit(0);
  }

  for (i = -RANGE; i <= RANGE; ++i) {
    seq[start] = i;
    sumSeq[start + 1] = sumSeq[start] + i;
    if (isValid(start)) {
      dfs(start + 1);
    }
  }
}

int
main(void) {
  int i, j;
  scanf("%d", &n);
  getchar();
  for (i = 0; i < n; ++i) {
    for (j = i; j < n; ++j) {
      scanf("%c", &sign[i][j]);
    }
  }

  dfs(0);

  return (0);
}
