#include <stdio.h>

int
main(void) {
  int n, m, l, t;
  int arr1[25], arr2[25], count1, count2;
  scanf("%d", &n);
  t = n;

  m = (int)((double)(0.61803398875) * n);
  count1 = 0;
  arr1[count1++] = n;
  while (m >= 0) {
    arr1[count1++] = m;
    l = n - m;
    n = m;
    m = l;
  }

  n = t;
  m = (int)((((double)sqrt(5) - 1) / 2) * n);
  ++m;
  count2 = 0;
  arr2[count2++] = n;
  while (m >= 0) {
    arr2[count2++] = m;
    l = n - m;
    n = m;
    m = l;
  }

  if (count1 > count2) {
    printf("%d\n", count1);
    for (l = 0; l < count1; ++l)
      printf("%d ", arr1[l]);
  } else {
    printf("%d\n", count2);
    for (l = 0; l < count2; ++l)
      printf("%d ", arr2[l]);
  }
  return 0;
}
