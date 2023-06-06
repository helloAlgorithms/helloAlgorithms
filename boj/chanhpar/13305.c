#include <stdio.h>

#define BUFFER_SIZE (1 << 20)

char buff[BUFFER_SIZE];

void
read_buff(void) {
  fread(buff, sizeof(char), BUFFER_SIZE, stdin);
}

char
get_char(void) {
  static size_t idx = BUFFER_SIZE;

  if (idx == BUFFER_SIZE) {
    read_buff();
    idx = 0;
  }
  return buff[idx++];
}

int
get_int(void) {
  int ret;
  char c;

  ret = 0;
  do {
    c = get_char();
  } while (c < '0' || c > '9');
  do {
    ret = ret * 10 + c - '0';
    c = get_char();
  } while (c >= '0' && c <= '9');
  return ret;
}

int
main(void) {
  int n;
  int dist[100000];
  int i, currPrice;
  long totalCost, minPrice;
  scanf("%d", &n);
  for (i = 1; i < n; ++i)
    dist[i] = get_int();

  currPrice = get_int();

  totalCost = 0;
  minPrice = currPrice;
  for (i = 1; i < n; ++i) {
    totalCost += minPrice * dist[i];
    currPrice = get_int();
    if (currPrice < minPrice)
      minPrice = currPrice;
  }
  printf("%ld", totalCost);
  return 0;
}
