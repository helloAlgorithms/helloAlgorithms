#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int l, n;
  int left, right;
  std::vector<int> v;

  std::cin >> l;
  v.reserve(l);
  for (int i = 0; i < l; ++i) {
    int tmp;
    std::cin >> tmp;
    v.push_back(tmp);
  }
  std::sort(v.begin(), v.end());
  std::cin >> n;
  std::vector<int>::const_iterator it = std::lower_bound(v.begin(), v.end(), n);

  assert(it != v.end());

  if (*it == n) {
    std::cout << 0 << "\n";
    return (0);
  }

  if (it == v.begin())
    left = 1;
  else
    left = *(it - 1) + 1;

  right = *it - 1;

  std::cout << (n - left + 1) * (right - n + 1) - 1 << "\n";

  return (0);
}
