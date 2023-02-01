#include <stdio.h>

char s[100001];
int in_idx;

char out[100001];
int out_idx;

char stack[100001];
int size;

void
push(char c) {
  stack[size++] = c;
}

char
pop(void) {
  return (stack[--size]);
}

int
_isalnum(char c) {
  if (c < '0' || c > '9')
    return (c >= 'a' && c <= 'z');
  return (1);
}

void
copy_tag(void) {
  do {
    out[out_idx++] = s[in_idx++];
  } while (s[in_idx] != '>');
  out[out_idx++] = s[in_idx++];
}

void
copy_space(void) {
  out[out_idx++] = s[in_idx++];
}

void
copy_rev_word(void) {
  while (_isalnum(s[in_idx])) {
    push(s[in_idx++]);
  }
  while (size > 0) {
    out[out_idx++] = pop();
  }
}

int
main(void) {
  scanf("%[^\n]", s);

  while (s[in_idx]) {
    switch (s[in_idx]) {
      case ('<'):
        copy_tag();
        break;
      case (' '):
        copy_space();
        break;
      default:
        copy_rev_word();
        break;
    }
  }

  printf("%s", out);
  return (0);
}
