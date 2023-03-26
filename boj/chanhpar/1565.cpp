#include <iostream>
#include <map>
#include <vector>

void
updateMap(std::map<int, int>& m, int p, int order) {
  std::map<int, int>::iterator it = m.find(p);
  if (it == m.end())
    m.insert(std::make_pair(p, order));
  else
    it->second = std::max(it->second, order);
}

int
gcd(int a, int b) {
  if (a % b)
    return (gcd(b, a % b));
  return (b);
}

void
makeMap(std::map<int, int>& m, int num) {
  int p = 2;

  while (num > 1) {
    if (p > num / p) {
      updateMap(m, num, 1);
      return;
    }
    if (num % p == 0) {
      int order = 0;
      while (num % p == 0) {
        num /= p;
        ++order;
      }
      updateMap(m, p, order);
    }
    ++p;
  }
}

void
reduceOrder(std::map<int, int>& gcdMap, std::map<int, int>& lcmMap) {
  if (gcdMap.empty() && !lcmMap.empty()) {
    gcdMap.insert(std::make_pair(2, -1));
    return;
  }
  for (std::map<int, int>::const_iterator it = lcmMap.begin();
       it != lcmMap.end();
       ++it) {
    std::map<int, int>::iterator jt = gcdMap.find(it->first);
    if (jt == gcdMap.end() || jt->second < it->second) {
      gcdMap.begin()->second = -1;
      return;
    }
    jt->second -= it->second;
  }
}

int
countDivisor(std::map<int, int>& m) {
  int ret = 1;
  for (std::map<int, int>::const_iterator it = m.begin(); it != m.end(); ++it) {
    if (it->second < 0)
      return (0);
    ret *= 1 + it->second;
  }
  return (ret);
}

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int sizeD, sizeM, tmp, g;
  std::vector<int> vecD;
  std::map<int, int> gcdMap;
  std::map<int, int> lcmMap;

  std::cin >> sizeD >> sizeM;
  vecD.reserve(sizeD);
  for (int i = 0; i < sizeD; ++i) {
    std::cin >> tmp;
    vecD.push_back(tmp);
  }

  std::cin >> g;
  for (int i = 1; i < sizeM; ++i) {
    std::cin >> tmp;
    g = gcd(g, tmp);
  }

  for (int i = 0; i < sizeD; ++i)
    makeMap(lcmMap, vecD[i]);

  makeMap(gcdMap, g);

  reduceOrder(gcdMap, lcmMap);

  std::cout << countDivisor(gcdMap);

  return (0);
}
