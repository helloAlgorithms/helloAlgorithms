#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

std::vector<int> cranes;
std::deque<int> boxes;

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);
  int n, m;
  int x;
  int days = 0;
  std::cin >> n;
  cranes.reserve(n);
  for (int i = 0; i < n; ++i) {
    std::cin >> x;
    cranes.push_back(x);
  }
  std::cin >> m;
  for (int i = 0; i < m; ++i) {
    std::cin >> x;
    boxes.push_back(x);
  }

  std::sort(cranes.begin(), cranes.end(), std::greater<int>());
  std::sort(boxes.begin(), boxes.end(), std::greater<int>());

  if (cranes.front() < boxes.front()) {
    std::cout << "-1\n";
    return (0);
  }

  while (!boxes.empty()) {
    for (std::vector<int>::const_iterator vit = cranes.begin();
         vit != cranes.end();
         ++vit) {
      std::deque<int>::const_iterator dit = std::lower_bound(
          boxes.begin(), boxes.end(), *vit, std::greater<int>());
      if (dit != boxes.end())
        boxes.erase(dit);
      else
        break;
    }
    ++days;
  }

  std::cout << days << "\n";
  return (0);
}
