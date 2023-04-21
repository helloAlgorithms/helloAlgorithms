#include <algorithm>
#include <iostream>

int
isGood(int const idx, int const* const arr, int const size) {
  int i;
  for (i = 0; i + 1 < size; ++i) {
    if (i == idx)
      continue;
    std::pair<int const* const, int const* const> const p
        = std::equal_range(arr + i + 1, arr + size, arr[idx] - arr[i]);
    if (p.first != arr + size && *p.first + arr[i] == arr[idx]
        && (p.first != arr + idx || p.first + 1 != p.second))
      return (1);
  }
  return (0);
}

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);
  int n, count;
  int i;
  int arr[2000];
  std::cin >> n;
  for (i = 0; i < n; ++i) {
    std::cin >> arr[i];
  }
  std::sort(arr, arr + n);
  count = 0;
  for (i = 0; i < n; ++i) {
    count += isGood(i, arr, n);
  }
  std::cout << count;
  return (0);
}
