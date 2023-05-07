#include <stdio.h>

/* Pattern: (100+1+ | 01)+ */

int
isPattern(char const* input) {
  if (*input == '\0')
    return 1;
  if (*input == '0') {
    ++input;
    if (*input == '1')
      return isPattern(input + 1);
    return 0;
  }

  if (input[1] != '0' || input[2] != '0')
    return 0;
  input += 3;
  while (*input == '0')
    ++input;
  while (*input == '1') {
    ++input;
    if (isPattern(input))
      return 1;
  }
  return 0;
}

int
main(void) {
  int t;
  char input[201];
  scanf("%d", &t);
  while (t-- > 0) {
    scanf("%s", input);
    printf(isPattern(input) ? "YES\n" : "NO\n");
  }
  return 0;
}
