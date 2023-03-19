#include <stdio.h>

static const int days[2][12]
    = {{0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334},
       {0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335}};

int
isLeapYear(int y) {
  return (y % 4 == 0 && (y % 100 != 0 || y % 400 == 0));
}

int
diff(int y1, int m1, int d1, int y2, int m2, int d2) {
  int tillNewYear;
  int isLeap = isLeapYear(y1);
  if (y1 < y2) {
    tillNewYear = 366 + isLeap - days[isLeap][m1 - 1] - d1;
    return (tillNewYear + diff(y1 + 1, 1, 1, y2, m2, d2));
  } else {
    return (days[isLeap][m2 - 1] + d2 - days[isLeap][m1 - 1] - d1);
  }
}

int
main(void) {
  int y1, m1, d1, y2, m2, d2;
  scanf("%d %d %d", &y1, &m1, &d1);
  scanf("%d %d %d", &y2, &m2, &d2);
  if (y2 > y1 + 1000
      || (y2 == y1 + 1000 && (m2 > m1 || (m2 == m1 && d2 >= d1)))) {
    printf("gg\n");
  } else {
    printf("D-%d\n", diff(y1, m1, d1, y2, m2, d2));
  }
  return (0);
}
