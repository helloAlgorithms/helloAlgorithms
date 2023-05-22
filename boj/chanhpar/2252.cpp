#include <iostream>
#include <stack>
#include <vector>

void
dfs(const int start,
    const std::vector<std::vector<int> >& graph,
    std::vector<bool>& visit,
    std::stack<int>& result) {
  visit[start] = true;

  const std::vector<int>& curr = graph[start];

  for (std::vector<int>::const_iterator it = curr.begin(); it != curr.end();
       ++it) {
    if (!visit[*it])
      dfs(*it, graph, visit, result);
  }
  result.push(start);
}

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int n, m;

  std::cin >> n >> m;

  std::vector<std::vector<int> > graph(n);
  std::stack<int> result;
  std::vector<bool> visit(n);

  while (m--) {
    int from, to;
    std::cin >> from >> to;
    graph[from - 1].push_back(to - 1);
  }

  for (int i = 0; i < n; ++i) {
    if (!visit[i])
      dfs(i, graph, visit, result);
  }
  while (!result.empty()) {
    std::cout << result.top() + 1 << " ";
    result.pop();
  }
  return 0;
}
