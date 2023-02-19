#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

std::string
rev(std::string str) {
  std::reverse(str.begin(), str.end());
  return (str);
}

int
main(void) {
  std::string str;
  std::cin >> str;
  std::vector<std::string> v;
  for (size_t i = 1; i + 2 < str.size(); ++i) {
    for (size_t j = i + 1; j < str.size(); ++j) {
      v.push_back(rev(str.substr(0, i)) + rev(str.substr(i, j - i)) + rev(str.substr(j)));
    }
  }
  std::sort(v.begin(), v.end());
  std::cout << v.front() << std::endl;
  return (0);
}
