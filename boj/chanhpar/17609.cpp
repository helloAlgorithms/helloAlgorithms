#include <iostream>
#include <string>

int
checkPalindrome(const std::string& str,
                size_t left,
                size_t right,
                const bool isDeleted) {
  while (left < right) {
    if (str[left] != str[right]) {
      if (isDeleted)
        return 2;
      const int r = checkPalindrome(str, left + 1, right, true);
      if (r == 2)
        return checkPalindrome(str, left, right - 1, true);
      return r;
    }
    ++left;
    --right;
  }
  return isDeleted;
}

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int t;
  std::cin >> t;
  while (t-- > 0) {
    std::string str;
    std::cin >> str;
    std::cout << checkPalindrome(str, 0, str.size() - 1, false) << "\n";
  }
  return 0;
}
