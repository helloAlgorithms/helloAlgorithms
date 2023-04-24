#include <iostream>

int
gcd(int a, int b) {
  int c;

  while (a % b != 0) {
    c = a;
    a = b;
    b = c % b;
  }
  return (b);
}

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);
  int n, g, count, prev, curr, first;
  int i;
  std::cin >> n;
  g = 0;
  std::cin >> first;

  prev = first;
  for (i = 1; i < n; ++i) {
    std::cin >> curr;
    if (g == 0)
      g = curr - prev;
    else
      g = gcd(curr - prev, g);
    prev = curr;
  }
  count = (curr - first) / g + 1 - n;
  std::cout << count;
  return (0);
}
