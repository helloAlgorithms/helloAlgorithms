#include <iostream>
#include <queue>
#include <stack>
#include <vector>

#define INF 200000000

struct Edge {
  int to;
  int weight;

  Edge(const int to, const int weight) : to(to), weight(weight) {
  }

  inline bool
  operator<(const Edge& other) const {
    return this->weight < other.weight;
  }

  inline bool
  operator>(const Edge& other) const {
    return this->weight > other.weight;
  }
};

void
dijkstra(const int start,
         const std::vector<std::vector<Edge> >& graph,
         std::vector<int>& dist,
         std::vector<int>& prev) {
  std::priority_queue<Edge, std::vector<Edge>, std::greater<Edge> > q;

  dist[start] = 0;
  q.push(Edge(start, 0));

  while (!q.empty()) {
    const int curr_node = q.top().to;
    const int curr_weight = q.top().weight;
    q.pop();

    if (curr_weight > dist[curr_node])
      continue;

    const std::vector<Edge>& curr_vec = graph[curr_node];

    for (std::vector<Edge>::const_iterator it = curr_vec.begin();
         it != curr_vec.end();
         ++it) {
      const int next_node = it->to;
      const int next_weight = curr_weight + it->weight;

      if (next_weight < dist[next_node]) {
        dist[next_node] = next_weight;
        prev[next_node] = curr_node;
        q.push(Edge(next_node, next_weight));
      }
    }
  }
}

void
printRoute(const int start, int end, const std::vector<int>& prev) {
  std::stack<int> st;

  while (end != start) {
    st.push(end);
    end = prev[end];
  }
  st.push(start);

  std::cout << st.size() << "\n";

  while (!st.empty()) {
    std::cout << st.top() + 1 << " ";
    st.pop();
  }
}

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int n, m;
  int start, end;
  std::cin >> n;
  std::cin >> m;

  std::vector<std::vector<Edge> > graph(n);

  for (int i = 0; i < m; ++i) {
    int a, b, c;
    std::cin >> a >> b >> c;
    graph[a - 1].push_back(Edge(b - 1, c));
  }

  std::cin >> start >> end;

  --start;
  --end;

  std::vector<int> dist(n, INF);
  std::vector<int> prev(n, -1);

  dijkstra(start, graph, dist, prev);

  std::cout << dist[end] << "\n";

  printRoute(start, end, prev);

  return 0;
}
