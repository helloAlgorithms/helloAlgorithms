#include <stdio.h>

int
main(void) {
  char input[2001];
  int idx, count, op, t;
  t = 0;
  while (scanf("%s", input) == 1 && input[0] != '-') {
    ++t;
    count = 0;
    op = 0;
    for (idx = 0; input[idx]; ++idx) {
      if (input[idx] == '{') {
        ++count;
      } else {
        if (count > 0) {
          --count;
        } else {
          ++op;
          ++count;
        }
      }
    }
    printf("%d. %d\n", t, count / 2 + op);
  }
  return 0;
}
