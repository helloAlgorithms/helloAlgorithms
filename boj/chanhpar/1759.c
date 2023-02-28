#include <stdio.h>
#include <stdlib.h>

enum {
  CONSONANT,
  VOWEL
};

int l, c;
char arr[16];
char buff[16];
int count[2];
int idx;

int
isVowel(char c) {
  static const char vowel[5] = {'a', 'e', 'i', 'o', 'u'};
  int i;
  for (i = 0; i < 5; ++i) {
    if (vowel[i] == c)
      return (VOWEL);
  }
  return (CONSONANT);
}

int
cmp(const void* a, const void* b) {
  const char x = *(const char*)a;
  const char y = *(const char*)b;
  if (x > y)
    return (1);
  if (x < y)
    return (-1);
  return (0);
}

void
dfs(int start) {
  int i;
  if (idx == l && count[VOWEL] >= 1 && count[CONSONANT] >= 2) {
    printf("%s\n", buff);
    return;
  }
  for (i = start + 1; i < c; ++i) {
    buff[idx++] = arr[i];
    ++(count[isVowel(arr[i])]);
    dfs(i);
    --(count[isVowel(arr[i])]);
    buff[idx--] = '\0';
  }
}

int
main(void) {
  int i;
  scanf("%d %d", &l, &c);
  for (i = 0; i < c; ++i)
    scanf(" %c", &arr[i]);
  qsort(arr, c, sizeof(char), cmp);
  dfs(-1);
  return (0);
}
