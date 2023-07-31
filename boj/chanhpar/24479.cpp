#include <algorithm>
#include <iostream>
#include <vector>

int order = 1;

void
dfs(const std::vector<std::vector<int> >& graph,
    std::vector<int>& visitOrder,
    const int curr) {
  visitOrder[curr] = order++;
  for (size_t i = 0; i < graph[curr].size(); ++i) {
    if (visitOrder[graph[curr][i]])
      continue;
    dfs(graph, visitOrder, graph[curr][i]);
  }
}

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int n, m, r;
  std::cin >> n >> m >> r;
  std::vector<std::vector<int> > graph(n);
  std::vector<int> visitOrder(n);
  for (int i = 0; i < m; ++i) {
    int u, v;
    std::cin >> u >> v;
    graph[u - 1].push_back(v - 1);
    graph[v - 1].push_back(u - 1);
  }
  for (int i = 0; i < n; ++i) {
    std::sort(graph[i].begin(), graph[i].end());
  }
  dfs(graph, visitOrder, r - 1);
  for (int i = 0; i < n; ++i) {
    std::cout << visitOrder[i] << "\n";
  }
  return 0;
}
