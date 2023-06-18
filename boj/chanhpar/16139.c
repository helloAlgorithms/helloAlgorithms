#include <stdio.h>
#include <stdlib.h>

int
main(void) {
  char s[200001];
  int(*count)[26];
  char a;
  int q, l, r, i, j;

  scanf("%s", s);
  count = malloc(sizeof(int[26]) * 200002);
  for (j = 0; j < 26; ++j) {
    count[0][j] = 0;
  }
  for (i = 0; s[i]; ++i) {
    for (j = 0; j < 26; ++j) {
      count[i + 1][j] = count[i][j];
    }
    ++count[i + 1][s[i] - 'a'];
  }
  scanf("%d", &q);
  while (q-- > 0) {
    getchar();
    scanf("%c %d %d", &a, &l, &r);
    printf("%d\n", count[r + 1][a - 'a'] - count[l][a - 'a']);
  }
  return 0;
}
