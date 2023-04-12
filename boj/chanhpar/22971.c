#include <stdio.h>

#define MOD 998244353

int
main(void) {
  int n, i, j;
  int arr[5000];
  int ans[5000];
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%d", &arr[i]);
    ans[i] = 1;
    for (j = 0; j < i; ++j) {
      if (arr[j] < arr[i]) {
        ans[i] += ans[j];
        ans[i] %= MOD;
      }
    }
    printf("%d ", ans[i]);
  }
  return (0);
}
