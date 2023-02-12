#include <stdio.h>

int k;
char arr[10];
char buff[11];
char copy[11];
int idx;
char visit[2];
char isPrinted;

void
dfs(void) {
  int i;

  if (idx == k + 1) {
    if (!isPrinted)
      printf("%s\n", buff);
    for (i = 0; buff[i]; ++i)
      copy[i] = buff[i];
    copy[i] = '\0';
    isPrinted = 1;
    return;
  }

  for (i = 9; i >= 0; --i) {
    if (visit[i >> 3] & (1 << (i & 7)))
      continue;
    if (idx && ((buff[idx - 1] < i + '0') != arr[idx - 1]))
      continue;
    visit[i >> 3] |= 1 << (i & 7);
    buff[idx++] = i + '0';
    dfs();
    buff[idx--] = '\0';
    visit[i >> 3] &= ~(1 << (i & 7));
  }
}

int
main(void) {
  int i;
  scanf("%d", &k);
  for (i = 0; i < k; ++i) {
    scanf(" %c", &arr[i]);
    arr[i] = (arr[i] == '<');
  }

  dfs();
  printf("%s\n", copy);

  return (0);
}
