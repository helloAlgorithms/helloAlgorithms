#include <stdio.h>
#include <stdlib.h>

int comb[10];
int stack[10];
int size;
char visit[10];
int n, target;
int sum;

void
dfs(void) {
  int i;
  if (size == n) {
    if (sum == target) {
      for (i = 0; i < n; ++i) {
        printf("%d ", stack[i]);
      }
      printf("\n");
      exit(0);
    } else {
      return;
    }
  }
  if (sum > target)
    return;

  for (i = 0; i < n; ++i) {
    if (visit[i] == 0) {
      visit[i] = 1;
      sum += comb[size] * (i + 1);
      stack[size++] = i + 1;
      dfs();
      visit[i] = 0;
      --size;
      sum -= comb[size] * (i + 1);
    }
  }
}

int
main(void) {
  int i;
  scanf("%d %d", &n, &target);
  comb[0] = 1;
  for (i = 1; i <= n - 1; ++i) {
    comb[i] = (comb[i - 1] * (n - i)) / i;
  }
  sum = 0;
  dfs();
  return (0);
}
