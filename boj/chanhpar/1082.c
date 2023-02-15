#include <stdio.h>

int n, m;
int price[10];
char buff[51];

void
increment(int left, int count) {
  int i, j;
  for (i = 0; i < count; ++i) {
    j = n;
    while (j-- > 0) {
      if (left + price[buff[i] - '0'] >= price[j]) {
        left -= price[j] - price[buff[i] - '0'];
        buff[i] = '0' + j;
        break;
      }
    }
  }
}

int
main(void) {
  int i;
  int minIdx;
  int count;

  scanf("%d", &n);
  minIdx = 0;
  for (i = 0; i < n; ++i) {
    scanf("%d", &price[i]);
    if (price[minIdx] >= price[i])
      minIdx = i;
  }
  scanf("%d", &m);
  if (n == 1)
    return (printf("0\n"), 0);

  if (minIdx != 0) {
    count = m / price[minIdx];
    for (i = 0; i < count; ++i)
      buff[i] = '0' + minIdx;

    increment(m - count * price[minIdx], count);
  } else {
    minIdx = 1;
    for (i = 1; i < n; ++i) {
      if (price[minIdx] >= price[i])
        minIdx = i;
    }
    if (m < price[minIdx])
      return (printf("0\n"), 0);
    count = ((m - price[minIdx]) / price[0]) + 1;
    buff[0] = '0' + minIdx;
    for (i = 1; i < count; ++i)
      buff[i] = '0';

    increment(m - price[minIdx] - price[0] * (count - 1), count);
  }
  printf("%s\n", buff);
  return (0);
}
