#include <stdio.h>
#include <stdlib.h>

/* Use trie */

typedef struct trie_t {
  struct trie_t* child;
  struct trie_t* next;
  char c;
  int isEnd;
} trie_t;

trie_t head;
int count;

trie_t*
newNode(void) {
  trie_t* node = calloc(1, sizeof(trie_t));
  return (node);
}

void
insert(trie_t* node, char* buff) {
  trie_t* curr;

  if (*buff == '\0') {
    node->isEnd = 1;
    return;
  }

  for (curr = node->child; curr; curr = curr->next) {
    if (curr->c == *buff) {
      insert(curr, buff + 1);
      return;
    }
  }

  curr = newNode();
  curr->c = *buff;
  curr->next = node->child;
  node->child = curr;
  insert(curr, buff + 1);
}

void
find(trie_t* node, char* buff) {
  trie_t* curr;

  if (*buff == '\0') {
    count += node->isEnd;
    return;
  }

  for (curr = node->child; curr; curr = curr->next) {
    if (curr->c == *buff) {
      find(curr, buff + 1);
      return;
    }
  }
}

int
main(void) {
  int n, m, i;
  char buff[502];
  scanf("%d %d", &n, &m);
  for (i = 0; i < n; ++i) {
    scanf("%s", buff);
    insert(&head, buff);
  }
  count = 0;
  for (i = 0; i < m; ++i) {
    scanf("%s", buff);
    find(&head, buff);
  }
  printf("%d\n", count);
  return (0);
}
