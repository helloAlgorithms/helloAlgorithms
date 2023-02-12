#include <stdio.h>
#include <unistd.h>

char buff[1002];
char rev[1002];
char stack[20];
int size;
int idx;

void
push(char c) {
  stack[size++] = c;
}

char
pop(void) {
  return (stack[--size]);
}

void
reverse(char* ptr) {
  idx = 0;
  while (*ptr != '\n') {
    if (*ptr == ' ') {
      while (size > 0) {
        rev[idx++] = pop();
      }
      rev[idx++] = ' ';
    } else {
      push(*ptr);
    }
    ++ptr;
  }
  while (size > 0) {
    rev[idx++] = pop();
  }
  rev[idx++] = '\n';
}

int
main(void) {
  int t;
  scanf("%d", &t);
  getchar();
  while (t--) {
    fgets(buff, 1002, stdin);
    reverse(buff);
    write(1, rev, idx);
  }
  return (0);
}
