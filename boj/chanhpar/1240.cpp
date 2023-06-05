#include <iostream>
#include <vector>

int n, m;

int dp[1000][1000];

struct Edge {
  int to;
  int weight;

  Edge(const int to, const int weight) : to(to), weight(weight) {
  }
};

int
dfs(const std::vector<std::vector<Edge> >& graph,
    const int curr,
    const int target,
    const int parent,
    const int acc) {
  if (curr == target)
    return acc;

  const std::vector<Edge>& curr_vec = graph[curr];

  for (std::vector<Edge>::const_iterator it = curr_vec.begin();
       it != curr_vec.end();
       ++it) {
    if (it->to == parent)
      continue;
    const int distance = dfs(graph, it->to, target, curr, acc + it->weight);
    if (distance > 0)
      return distance;
  }
  return 0;
}

int
getDistance(const std::vector<std::vector<Edge> >& graph,
            const int from,
            const int to) {
  if (dp[from][to] == 0) {
    dp[from][to] = dp[to][from] ? dp[to][from] : dfs(graph, from, to, -1, 0);
  }
  return dp[from][to];
}

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  std::cin >> n >> m;

  std::vector<std::vector<Edge> > graph(n);

  for (int i = 0; i < n - 1; ++i) {
    int from, to, weight;
    std::cin >> from >> to >> weight;
    graph[from - 1].push_back(Edge(to - 1, weight));
    graph[to - 1].push_back(Edge(from - 1, weight));
  }

  for (int i = 0; i < m; ++i) {
    int from, to;
    std::cin >> from >> to;
    std::cout << getDistance(graph, from - 1, to - 1) << "\n";
  }

  return 0;
}
