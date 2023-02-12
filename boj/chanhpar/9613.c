#include <stdio.h>

int
gcd(int a, int b) {
  int tmp;

  do {
    tmp = a % b;
    a = b;
    b = tmp;
  } while (tmp);
  return (a);
}

long
gcdSum(int n, int* arr) {
  int i, j;
  long sum;

  sum = 0;
  for (i = 0; i < n; ++i) {
    for (j = i + 1; j < n; ++j) {
      sum += gcd(arr[i], arr[j]);
    }
  }
  return (sum);
}

int
main(void) {
  int t;
  int n;
  int arr[100];
  int i;

  scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);
    for (i = 0; i < n; ++i) {
      scanf("%d", &arr[i]);
    }
    printf("%ld\n", gcdSum(n, arr));
  }
  return (0);
}
