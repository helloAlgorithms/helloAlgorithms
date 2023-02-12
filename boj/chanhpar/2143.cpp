#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>

int t, n, m;
long* arrA;
long* arrB;

char* maskA;
char* maskB;

char buff[10001];
int idx;

long count;

long
getInt(void) {
  long ret;
  long sign;

  ret = 0;
  sign = 1;
  while (buff[idx] == ' ')
    ++idx;
  if (buff[idx] == '-') {
    sign *= -1;
    ++idx;
  }
  while (buff[idx] >= '0' && buff[idx] <= '9') {
    ret = 10 * ret + buff[idx++] - '0';
  }
  return (ret * sign);
}

int
main(void) {
  int i, j;
  /* get input {{{ */

  scanf("%d", &t);

  scanf("%d", &n);
  arrA = static_cast<long*>(malloc(sizeof(long) * (n + 1)));
  getchar();
  fgets(buff, 10 * n, stdin);
  arrA[0] = 0;
  for (i = 1; i <= n; ++i)
    arrA[i] = getInt() + arrA[i - 1];
  idx = 0;

  scanf("%d", &m);
  arrB = static_cast<long*>(malloc(sizeof(long) * (m + 1)));
  getchar();
  fgets(buff, 10 * m, stdin);
  arrB[0] = 0;
  for (i = 1; i <= m; ++i)
    arrB[i] = getInt() + arrB[i - 1];
  /* }}} */

  std::map<long, long> maskA;
  std::map<long, long>::iterator it;
  for (i = 1; i <= n; ++i)
    for (j = 0; j < i; ++j)
      maskA[arrA[i] - arrA[j]] += 1;
  for (i = 1; i <= m; ++i) {
    for (j = 0; j < i; ++j) {
      it = maskA.find(t - (arrB[i] - arrB[j]));
      if (it != maskA.end())
        count += it->second;
    }
  }
  printf("%ld", count);
  return (0);
}
