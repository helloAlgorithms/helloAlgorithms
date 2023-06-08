#include <stdio.h>

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

void
tc(void) {
  int n, i, j, cycleCount;
  int arr[1001];
  char visit[1001];

  n = read_int();
  for (i = 0; i < n; ++i) {
    arr[i] = read_int();
    visit[arr[i]] = 0;
  }
  cycleCount = 0;
  for (i = 0; i < n; ++i) {
    if (visit[arr[i]])
      continue;
    ++cycleCount;
    j = arr[i];
    while (!visit[j]) {
      visit[j] = 1;
      j = arr[j - 1];
    }
  }
  printf("%d\n", cycleCount);
}

int
main(void) {
  int t;
  t = read_int();
  while (t-- > 0)
    tc();
  return 0;
}
