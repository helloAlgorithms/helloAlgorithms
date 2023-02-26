#include <stdio.h>

int n, k;
int arr[500000];
int tmp[500000];
int count;
int end_flag;

void
merge(int begin, int mid, int end) {
  int i, j, t;

  if (end_flag)
    return;
  i = begin;
  j = mid + 1;
  t = 0;
  while (i <= mid && j <= end) {
    if (arr[i] < arr[j])
      tmp[t++] = arr[i++];
    else
      tmp[t++] = arr[j++];
  }
  while (i <= mid)
    tmp[t++] = arr[i++];
  while (j <= end)
    tmp[t++] = arr[j++];
  for (i = begin, t = 0; i <= end;) {
    arr[i++] = tmp[t++];
    ++count;
    if (count == k) {
      end_flag = tmp[t - 1];
      return;
    }
  }
}

void
sort(int begin, int end) {
  int mid;

  if (end_flag)
    return;
  if (begin < end) {
    mid = (begin + end) >> 1;
    sort(begin, mid);
    sort(mid + 1, end);
    merge(begin, mid, end);
  }
}

int
main(void) {
  int i;
  scanf("%d %d", &n, &k);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);
  sort(0, n - 1);
  printf("%d", (count == k) ? end_flag : -1);
  return (0);
}
