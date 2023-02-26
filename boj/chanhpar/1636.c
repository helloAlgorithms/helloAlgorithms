#include <stdio.h>

enum {
  START,
  END
};

int n;
int snacks[100000][2];

int diff[100001];

int
max(int a, int b) {
  return (a > b ? a : b);
}

int
min(int a, int b) {
  return (a < b ? a : b);
}

int
overlap(int idx1, int idx2) {
  if (snacks[idx1][END] < snacks[idx2][START]
      || snacks[idx1][START] > snacks[idx2][END])
    return (0);
  return (1);
}

void
reduce(int idx1, int idx2) {
  snacks[idx2][START] = max(snacks[idx1][START], snacks[idx2][START]);
  snacks[idx2][END] = min(snacks[idx1][END], snacks[idx2][END]);
}

int
main(void) {
  int i;
  int sum;
  int first;

  scanf("%d", &n);
  sum = 0;
  first = -1;
  scanf("%d %d", &snacks[0][START], &snacks[0][END]);
  if (n == 1)
    return (printf("0\n%d\n", snacks[0][START]), 0);
  for (i = 1; i < n; ++i) {
    scanf("%d %d", &snacks[i][START], &snacks[i][END]);
    if (overlap(i - 1, i)) {
      reduce(i - 1, i);
      diff[i] = 0;
    } else {
      if (first < 0)
        first = i;
      if (snacks[i - 1][END] < snacks[i][START])
        diff[i] = snacks[i][START] - snacks[i - 1][END];
      else
        diff[i] = snacks[i][END] - snacks[i - 1][START];
    }
  }

  if (first < 0) {
    printf("0\n");
    for (i = 0; i < n; ++i) {
      printf("%d\n", snacks[n - 1][START]);
    }
    return (0);
  }

  if (snacks[first - 1][END] < snacks[first][START])
    diff[0] = snacks[first - 1][END];
  else
    diff[0] = snacks[first - 1][START];

  for (i = 1; i < n; ++i) {
    if (diff[i] == 0) {
      if (diff[i - 1] < snacks[i][START]) {
        diff[i] = snacks[i][START];
        sum += snacks[i][START] - diff[i - 1];
      } else if (diff[i - 1] > snacks[i][END]) {
        diff[i] = snacks[i][END];
        sum += diff[i - 1] - snacks[i][END];
      } else
        diff[i] = diff[i - 1];
    } else {
      if (diff[i] > 0) {
        diff[i] = snacks[i][START];
        sum += diff[i] - diff[i - 1];
      } else {
        diff[i] = snacks[i][END];
        sum += diff[i - 1] - diff[i];
      }
    }
  }

  printf("%d\n", sum);

  for (i = 0; i < n; ++i) {
    printf("%d\n", diff[i]);
  }
  return (0);
}
