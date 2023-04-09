#include <stdio.h>

static char const* const yes = "Stan may be honest";
static char const* const no = "Stan is dishonest";

int isPossible[10];

int
main(void) {
  int n;
  int i;
  char buff[10];

  for (i = 0; i < 10; ++i) {
    isPossible[i] = 1;
  }
  while (1) {
    scanf("%d", &n);
    if (n == 0)
      break;
    getchar();
    scanf("%[^\n]", buff);
    if (buff[4] == 'h') {
      for (i = n; i <= 10; ++i) {
        isPossible[i - 1] = 0;
      }
    } else if (buff[4] == 'l') {
      for (i = 1; i <= n; ++i) {
        isPossible[i - 1] = 0;
      }
    } else {
      if (isPossible[n - 1])
        printf("%s\n", yes);
      else
        printf("%s\n", no);
      for (i = 0; i < 10; ++i) {
        isPossible[i] = 1;
      }
    }
  }
  return (0);
}
