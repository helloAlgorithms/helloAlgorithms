#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

void
find_number(std::vector<std::string>& dict, std::string& line) {
  std::string::size_type left = 0;
  std::string::size_type right = 0;

  while (left < line.size()) {
    if (!std::isdigit(line[left])) {
      ++left;
      continue;
    }
    right = left;
    while (std::isdigit(line[right])) {
      ++right;
    }
    while (right - left > 1 && line[left] == '0')
      ++left;
    dict.push_back(line.substr(left, right - left));
    left = right;
  }
}

struct Cmp {
  bool
  operator()(const std::string& a, const std::string& b) {
    if (a.size() == b.size())
      return (a < b);
    return (a.size() < b.size());
  }
};

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int n;
  std::string line;
  std::vector<std::string> dict;
  std::cin >> n;
  for (int i = 0; i < n; ++i) {
    std::cin >> line;
    find_number(dict, line);
  }
  std::sort(dict.begin(), dict.end(), Cmp());
  for (std::vector<std::string>::const_iterator it = dict.begin();
       it != dict.end();
       ++it)
    std::cout << *it << "\n";
  return (0);
}
