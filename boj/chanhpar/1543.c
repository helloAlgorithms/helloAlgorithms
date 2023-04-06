#include <stdio.h>
#include <string.h>

int
main(void) {
  char doc[2501];
  char word[51];
  char* ptr;
  int count;
  int wordLen;

  scanf("%[^\n]", doc);
  getchar();
  scanf("%[^\n]", word);
  count = 0;
  wordLen = strlen(word);
  ptr = doc;
  while (*ptr) {
    ptr = strstr(ptr, word);
    if (ptr == NULL)
      break;
    ++count;
    ptr += wordLen;
  }
  printf("%d\n", count);
  return (0);
}
