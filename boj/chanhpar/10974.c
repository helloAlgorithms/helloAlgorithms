#include <stdio.h>
#include <unistd.h>

int n;
int arr[8];
char buff[18];
int idx;
char visit;

void
print(void) {
  int i;
  for (i = 0; i < n; ++i) {
    buff[2 * i] = arr[i] + '0';
    buff[2 * i + 1] = ' ';
  }
  buff[2 * n] = '\n';
  buff[2 * n + 1] = '\0';
  printf("%s", buff);
}

void
dfs(void) {
  int i;
  if (idx == n) {
    print();
    return;
  }
  for (i = 0; i < n; ++i) {
    if (visit & (1 << i))
      continue;
    visit |= 1 << i;
    arr[idx++] = i + 1;
    dfs();
    --idx;
    visit &= ~(1 << i);
  }
}

int
main(void) {
  scanf("%d", &n);
  dfs();
  return (0);
}
