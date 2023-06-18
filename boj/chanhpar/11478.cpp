#include <iostream>
#include <string>
#include <unordered_set>

// TODO: use suffix array, LCP

int
main(void) {
  std::string str;
  std::unordered_set<std::string> s;
  std::cin >> str;
  const std::size_t size = str.size();
  for (size_t i = 0; i < size; ++i) {
    std::string tmp;
    for (size_t j = i; j < size; ++j) {
      tmp += str[j];
      s.insert(tmp);
    }
  }
  std::cout << s.size();
  return 0;
}
