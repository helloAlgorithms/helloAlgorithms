#include <stdio.h>

int n, idx;
int arr[10001];
char visit[10001];

void
print(void) {
  int i;
  for (i = 0; i < n; ++i)
    printf("%d ", arr[i]);
  printf("\n");
}

void
fill(void) {
  int i;
  if (idx == n) {
    print();
    return;
  }
  for (i = n; i >= 1; --i) {
    if (visit[i])
      continue;
    visit[i] = 1;
    arr[idx++] = i;
    fill();
  }
}

void
decrease(void) {
  int i;
  if (idx == -1) {
    printf("-1\n");
    return;
  }
  for (i = arr[idx] - 1; i >= 1; --i) {
    if (visit[i])
      continue;
    visit[i] = 1;
    visit[arr[idx]] = 0;
    arr[idx++] = i;
    fill();
    return;
  }
  visit[arr[idx--]] = 0;
  decrease();
}

int
main(void) {
  int i;
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%d", &arr[i]);
    visit[arr[i]] = 1;
  }
  idx = n - 1;
  decrease();
  return (0);
}
