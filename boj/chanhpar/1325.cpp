#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

#define NUMBER 10000

int n, m;

static std::vector<int> Computers[NUMBER];

int visitCount;
char visited[NUMBER];
int stack[NUMBER];
int stackSize;

void
dfs(int start) {
  visited[start] = 1;
  ++visitCount;
  for (std::vector<int>::const_iterator it = Computers[start].begin();
       it != Computers[start].end();
       ++it) {
    if (!visited[*it]) {
      dfs(*it);
    }
  }
}

void
bfs(int start) {
  std::queue<int> q;
  visited[start] = 1;
  ++visitCount;
  q.push(start);
  while (!q.empty()) {
    int top = q.front();
    q.pop();
    for (std::vector<int>::const_iterator it = Computers[top].begin();
         it != Computers[top].end();
         ++it) {
      if (!visited[*it]) {
        q.push(*it);
        visited[*it] = 1;
        ++visitCount;
      }
    }
  }
}

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int i, a, b;
  int max;
  std::cin >> n >> m;
  for (i = 0; i < m; ++i) {
    std::cin >> a >> b;
    Computers[b - 1].push_back(a - 1);
  }
  max = 0;
  for (i = 0; i < n; ++i) {
    visitCount = 0;
    std::fill(visited, visited + n, 0);
    bfs(i);
    if (max < visitCount) {
      stackSize = 0;
      max = visitCount;
      stack[stackSize++] = i;
    } else if (max == visitCount) {
      stack[stackSize++] = i;
    }
  }
  for (i = 0; i < stackSize; ++i)
    std::cout << (stack[i] + 1) << " ";
  return (0);
}
