#include <iostream>
#include <map>
#include <string>

int
main(void) {
  int n;
  int maxCount = 0;
  std::string maxEntry;
  std::map<std::string, int> m;
  std::string title;
  std::cin >> n;
  for (int i = 0; i < n; ++i) {
    std::cin >> title;
    m[title] += 1;
    if (maxCount < m[title]) {
      maxCount = m[title];
      maxEntry = title;
    } else if (maxCount == m[title]) {
      maxEntry = maxEntry < title ? maxEntry : title;
    }
  }
  std::cout << maxEntry;
  return (0);
}
