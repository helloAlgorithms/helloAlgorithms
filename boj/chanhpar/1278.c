#include <stdio.h>

char buff[1 << 20];
char* ptr;

void writeInt(int n) {
  *(ptr--) = '\n';
  while (n > 0) {
    *(ptr--) = '0' + n % 10;
    n /= 10;
  }
}

void play(int n) {
  if (n == 0)
    return;
  play(n - 1);
  writeInt(n);
  play(n - 1);
}

int main(void) {
  int n;
  scanf("%d", &n);
  printf("%d\n%d\n", (1 << n) - 1, n);
  ptr = buff + (1 << 20) - 2;
  play(n);
  printf("%s", ptr + 1);
  return (0);
}
