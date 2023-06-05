#include <stdio.h>
#include <string.h>

int
main(void) {
  char channels[100][11];
  char ans[501];
  int n, i, kbs1, kbs2, pos;
  scanf("%d", &n);
  kbs1 = 0;
  kbs2 = 0;
  for (i = 0; i < n; ++i) {
    scanf("%s", channels[i]);
    if (strcmp(channels[i], "KBS1") == 0)
      kbs1 = i;
    if (strcmp(channels[i], "KBS2") == 0)
      kbs2 = i;
  }
  pos = 0;
  for (i = 0; i < kbs1; ++i)
    ans[pos++] = '1';
  for (i = 0; i < kbs1; ++i)
    ans[pos++] = '4';
  if (kbs1 > kbs2)
    ++kbs2;
  for (i = 0; i < kbs2; ++i)
    ans[pos++] = '1';
  for (i = 1; i < kbs2; ++i)
    ans[pos++] = '4';
  ans[pos] = '\0';
  printf("%s", ans);
  return 0;
}
