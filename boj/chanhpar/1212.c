#include <stdio.h>

char input[333335];
char output[333335 * 3];
char* ptr1;
char* ptr2;

int
main(void) {
  int c;
  ptr1 = input;
  ptr2 = output;
  scanf("%s", input);

  while (*ptr1) {
    c = *ptr1 - '0';
    *ptr2++ = !!(c & 4) + '0';
    *ptr2++ = !!(c & 2) + '0';
    *ptr2++ = !!(c & 1) + '0';
    ++ptr1;
  }

  ptr2 = output;
  while (*ptr2 == '0')
    ++ptr2;
  if (*ptr2)
    printf("%s\n", ptr2);
  else
    printf("0\n");
  return (0);
}
