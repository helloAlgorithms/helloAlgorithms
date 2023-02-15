#include <stdio.h>

double stack[101];
int idx;

void
push(double k) {
  stack[idx++] = k;
}

double
pop(void) {
  return (stack[--idx]);
}

double
add(void) {
  double x, y;
  x = pop();
  y = pop();
  return (x + y);
}

double
sub(void) {
  double x, y;
  x = pop();
  y = pop();
  return (y - x);
}

double
mul(void) {
  double x, y;
  x = pop();
  y = pop();
  return (x * y);
}

double
div(void) {
  double x, y;
  x = pop();
  y = pop();
  return (y / x);
}

int
main(void) {
  int n;
  int i;
  int data[26];
  char buff[102];

  scanf("%d", &n);
  scanf("%s", buff);
  for (i = 0; i < n; ++i)
    scanf("%d", &data[i]);
  for (i = 0; buff[i]; ++i) {
    if (buff[i] == '+')
      push(add());
    else if (buff[i] == '-')
      push(sub());
    else if (buff[i] == '*')
      push(mul());
    else if (buff[i] == '/')
      push(div());
    else
      push(data[buff[i] - 'A']);
  }

  printf("%.2lf\n", pop());
  return (0);
}
