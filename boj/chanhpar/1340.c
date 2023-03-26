#include <stdio.h>
#include <string.h>

static int const days[2][12]
    = {{0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334},
       {0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335}};

static char const* const months[12] = {"January",
                                       "February",
                                       "March",
                                       "April",
                                       "May",
                                       "June",
                                       "July",
                                       "August",
                                       "September",
                                       "October",
                                       "November",
                                       "December"};

static int
isLeapYear(int y) {
  return (y % 4 == 0 && (y % 100 != 0 || y % 400 == 0));
}

int
main(void) {
  char month[15];
  int MM, dd, yy, hh, mm;
  int isLeap;
  double currMin, totalMin;
  scanf("%s %d, %d  %d:%d", month, &dd, &yy, &hh, &mm);
  isLeap = isLeapYear(yy);
  MM = 0;
  while (strcmp(months[MM], month) != 0)
    ++MM;
  currMin = (days[isLeap][MM] + dd - 1) * 24 * 60 + 60 * hh + mm;
  totalMin = (365 + isLeap) * 24 * 60;
  printf("%.9lf\n", 100 * currMin / totalMin);
  return (0);
}
