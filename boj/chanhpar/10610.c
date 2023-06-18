#include <stdio.h>

int
main(void) {
  char input[100001];
  int count[10];
  int idx, len, sum;
  scanf("%s", input);
  for (idx = 0; idx < 10; ++idx)
    count[idx] = 0;

  for (idx = 0; input[idx]; ++idx) {
    ++count[input[idx] - '0'];
  }
  sum = 0;
  for (idx = 1; idx < 10; ++idx)
    sum += count[idx] * idx;

  if (sum % 3 == 0 && count[0]) {
    len = 0;
    for (idx = 9; idx >= 0; --idx) {
      while (count[idx]) {
        input[len++] = idx + '0';
        --count[idx];
      }
    }
    printf("%s", input);
  } else {
    printf("-1");
  }
  return 0;
}
