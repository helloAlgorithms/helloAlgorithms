#include <stdio.h>

int
main(void) {
  unsigned long n, l, r, mid, ans;

  scanf("%lu", &n);
  l = 0;
  r = n;
  ans = 0;
  while (l < r) {
    mid = (l + r) >> 1;
    if (mid == 0 || mid < n / mid) {
      l = mid + 1;
    } else {
      ans = mid;
      r = mid;
    }
  }
  while (ans * ans < n)
    ++ans;

  printf("%lu", ans);
  return 0;
}
