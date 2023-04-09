#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int
main(void) {
  int n;
  int count;
  std::vector<std::string> words;
  std::string word;
  std::cin >> n;
  words.reserve(n);
  for (int i = 0; i < n; ++i) {
    std::cin >> word;
    words.push_back(word);
  }
  std::sort(words.begin(), words.end(), std::greater<std::string>());
  count = 1;
  std::string prev = words[0];
  for (int i = 1; i < n; ++i) {
    if (prev.find(words[i]) != 0) {
      ++count;
      prev = words[i];
    }
  }
  std::cout << count;
  return (0);
}
