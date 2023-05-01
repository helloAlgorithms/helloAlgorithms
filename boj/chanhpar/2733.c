#include <stdio.h>
#include <string.h>

#define MEM_SIZE 32768
#define PROGRAM_SIZE 128000

void
run(unsigned char* program, int* pair_pos) {
  unsigned char memory[MEM_SIZE];
  size_t pos, curr;

  memset(memory, 0, MEM_SIZE);
  pos = 0;
  curr = 0;
  while (program[curr]) {
    if (program[curr] == '[') {
      if (memory[pos] == 0) {
        curr = pair_pos[curr];
      } else
        ++curr;
      continue;
    }
    if (program[curr] == ']') {
      if (memory[pos] != 0) {
        curr = pair_pos[curr];
      } else
        ++curr;
      continue;
    }
    switch (program[curr++]) {
      case '>':
        pos = (pos + 1) % MEM_SIZE;
        break;
      case '<':
        pos = (pos + MEM_SIZE - 1) % MEM_SIZE;
        break;
      case '+':
        memory[pos] += 1;
        break;
      case '-':
        memory[pos] -= 1;
        break;
      case '.':
        printf("%c", memory[pos]);
        break;
      default:
        break;
    }
  }
  printf("\n");
}

void
testcase(void) {
  unsigned char program[PROGRAM_SIZE + 1];
  char buffer[PROGRAM_SIZE + 1];
  int pair_pos[PROGRAM_SIZE + 1];
  int stack[PROGRAM_SIZE + 1];
  int level, offset, idx;

  offset = 0;
  level = 0;
  while (1) {
    scanf(" %[^\n]", buffer);
    if (strcmp("end", buffer) == 0)
      break;
    idx = 0;
    while (buffer[idx]) {
      if (buffer[idx] == '%')
        break;
      if (buffer[idx] == '[') {
        stack[level++] = offset;
      } else if (buffer[idx] == ']') {
        if (level) {
          pair_pos[offset] = stack[--level];
          pair_pos[stack[level]] = offset;
        } else {
          printf("COMPILE ERROR\n");
          return;
        }
      }
      program[offset++] = buffer[idx++];
    }
  }
  if (level != 0) {
    printf("COMPILE ERROR\n");
    return;
  }
  program[offset] = '\0';
  run(program, pair_pos);
}

int
main(void) {
  int t, i;
  scanf("%d", &t);
  for (i = 0; i < t; ++i) {
    printf("PROGRAM #%d:\n", i + 1);
    testcase();
  }
  return 0;
}
