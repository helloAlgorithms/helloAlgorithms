#include <stdio.h>

int
getMax(int a, int b) {
  return a > b ? a : b;
}

int
main(void) {
  int n, d, k, c;
  int i;
  int arr[30001];
  int visit[3001] = {0};
  int count, maxCount;
  scanf("%d %d %d %d", &n, &d, &k, &c);
  for (i = 0; i < n; ++i) {
    scanf("%d", &arr[i]);
  }
  count = 0;
  for (i = 0; i < k; ++i) {
    ++visit[arr[i]];
    if (visit[arr[i]] == 1)
      ++count;
  }
  maxCount = count;
  if (visit[c] == 0)
    ++maxCount;

  if (k < n) {
    for (i = 0; i < n; ++i) {
      --visit[arr[i]];
      if (visit[arr[i]] == 0)
        --count;
      ++visit[arr[(i + k) % n]];
      if (visit[arr[(i + k) % n]] == 1)
        ++count;
      maxCount = getMax(maxCount, count + (visit[c] == 0));
    }
  }
  printf("%d", maxCount);
  return 0;
}
