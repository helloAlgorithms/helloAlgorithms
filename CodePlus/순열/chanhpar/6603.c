#include <stdio.h>

#define MAX 6

int k, idx;
int s[13];
int buff[13];

void
print(void) {
  int i;
  for (i = 0; i < MAX; ++i)
    printf("%d ", buff[i]);
  printf("\n");
}

void
dfs(int start) {
  int i;
  if (idx == MAX) {
    print();
    return;
  }
  for (i = start + 1; i < k; ++i) {
    buff[idx++] = s[i];
    dfs(i);
    --idx;
  }
}

int
main(void) {
  int i;
  while (scanf("%d", &k) && k != 0) {
    for (i = 0; i < k; ++i)
      scanf("%d", &s[i]);
    dfs(-1);
    printf("\n");
  }
  return (0);
}
