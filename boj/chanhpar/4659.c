#include <stdio.h>
#include <string.h>

int
isVowel(char c) {
  return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int
isValid(char* str) {
  int vowelCount;
  int threeCount;
  char prevChar;

  vowelCount = 0;
  threeCount = 1;
  prevChar = '\0';
  while (*str) {
    if (isVowel(*str))
      ++vowelCount;
    if (prevChar) {
      if (isVowel(prevChar) == isVowel(*str)) {
        ++threeCount;
        if (threeCount >= 3)
          return (0);
      } else
        threeCount = 1;
      if (prevChar == *str && (*str != 'e' && *str != 'o'))
        return (0);
    }
    prevChar = *str;
    ++str;
  }
  return (vowelCount > 0);
}

int
main(void) {
  char buff[21];

  do {
    scanf("%s", buff);
    if (strcmp(buff, "end") == 0)
      break;
    printf("<%s> is %sacceptable.\n", buff, isValid(buff) ? "" : "not ");
  } while (1);
  return (0);
}
