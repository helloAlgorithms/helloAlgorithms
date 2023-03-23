#include <stdio.h>

char formula[101];
char* ptr;

int stack[100];
int size;

void push(int n) { stack[size++] = n; }

int pop(void) { return (stack[--size]); }

int top(void) { return (stack[size - 1]); }

int
getW(char c) {
  switch (c) {
    case 'H':
      return (1);
    case 'C':
      return (12);
    case 'O':
      return (16);
    default:
      return (0);
  }
}

int
main(void) {
  int acc;
  scanf("%s", formula);
  ptr = formula;
  while (*ptr) {
    if (*ptr == '(') {
      push(0);
    } else if (*ptr == ')') {
      acc = 0;
      while (top() != 0)
        acc += pop();
      pop();
      push(acc);
    } else if (*ptr >= '2' && *ptr <= '9') {
      push(pop() * (*ptr - '0'));
    } else {
      push(getW(*ptr));
    }
    ++ptr;
  }
  acc = 0;
  while (size)
    acc += pop();
  printf("%d\n", acc);
  return (0);
}
