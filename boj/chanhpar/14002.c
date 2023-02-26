#include <stdio.h>

int n;
int arr[1000];
int aux[1001];
int parent[1001];

void
printLis(int idx) {
  if (idx < 0)
    return;
  printLis(parent[idx]);
  printf("%d ", arr[idx]);
}

int
main(void) {
  int len, newLen, left, right, mid;
  int i;
  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);

  len = 0;
  aux[0] = -1;

  for (i = 0; i < n; ++i) {
    left = 1;
    right = len + 1;
    while (left < right) {
      mid = (left + right) >> 1;
      if (arr[aux[mid]] >= arr[i])
        right = mid;
      else
        left = mid + 1;
    }

    newLen = left;
    aux[newLen] = i;
    parent[aux[newLen]] = aux[newLen - 1];

    if (newLen > len)
      len = newLen;
  }

  printf("%d\n", len);
  printLis(aux[len]);

  return (0);
}
