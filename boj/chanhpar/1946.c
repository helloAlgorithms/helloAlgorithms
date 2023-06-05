#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE (1 << 20)

char read_buff[BUFFER_SIZE];

void
read_input(void) {
  fread(read_buff, sizeof(char), BUFFER_SIZE, stdin);
}

char
read_char(void) {
  static size_t read_idx = BUFFER_SIZE;

  if (read_idx == BUFFER_SIZE) {
    read_input();
    read_idx = 0;
  }
  return read_buff[read_idx++];
}

int
read_int(void) {
  char c;
  int ret;

  do {
    c = read_char();
  } while (c < '0' || c > '9');

  ret = 0;
  do {
    ret = 10 * ret + c - '0';
    c = read_char();
  } while (c >= '0' && c <= '9');
  return ret;
}

typedef struct {
  int first;
  int second;
} pair;

int
cmp(const void* a, const void* b) {
  const pair* x = a;
  const pair* y = b;

  return x->first > y->first ? 1 : -1;
}

void
solve(void) {
  int n, i, m, count;
  pair arr[100000];

  n = read_int();
  for (i = 0; i < n; ++i) {
    arr[i].first = read_int();
    arr[i].second = read_int();
  }

  qsort(arr, n, sizeof(pair), cmp);

  m = n + 1;
  count = 0;
  for (i = 0; i < n; ++i) {
    if (arr[i].second < m) {
      ++count;
      m = arr[i].second;
    }
  }
  printf("%d\n", count);
}

int
main(void) {
  int t;
  t = read_int();
  while (t-- > 0)
    solve();
  return 0;
}
