#include <stdio.h>

int
main(void) {
  char string[51];
  int stack[51];
  int size, idx, sum, coeff;
  scanf("%s", string);
  idx = 0;
  sum = 0;
  size = 0;
  coeff = 1;
  while (string[idx]) {
    if (string[idx] == '(') {
    } else if (string[idx] == ')') {
      coeff = stack[--size];
    } else {
      if (string[idx + 1] == '(') {
        stack[size++] = coeff;
        coeff *= string[idx] - '0';
      } else {
        sum += coeff;
      }
    }
    ++idx;
  }
  printf("%d\n", sum);
  return 0;
}
