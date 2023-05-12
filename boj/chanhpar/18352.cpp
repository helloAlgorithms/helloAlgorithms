#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

// BFS version

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int n, m, k, x;
  std::cin >> n >> m >> k >> x;

  std::vector<std::vector<int> > graph(n);

  for (int i = 0; i < m; ++i) {
    int a, b;
    std::cin >> a >> b;
    graph[a - 1].push_back(b - 1);  //
  }

  std::vector<bool> visit(n);

  std::queue<std::pair<int, int> > q;
  q.push(std::make_pair(x - 1, 0));
  visit[x - 1] = true;

  std::vector<int> ans;

  while (!q.empty()) {
    const std::pair<int, int> curr = q.front();
    q.pop();

    const std::vector<int>& curr_vec = graph[curr.first];

    for (std::vector<int>::const_iterator it = curr_vec.begin();
         it != curr_vec.end();
         ++it) {
      if (visit[*it])
        continue;
      if (curr.second + 1 == k)
        ans.push_back(*it + 1);
      else
        q.push(std::make_pair(*it, curr.second + 1));
      visit[*it] = true;
    }
  }

  if (ans.empty())
    std::cout << "-1\n";
  else {
    std::sort(ans.begin(), ans.end());
    for (std::vector<int>::const_iterator it = ans.begin(); it != ans.end();
         ++it) {
      std::cout << *it << "\n";
    }
  }

  return 0;
}

// dijkstra version
// {{{
// #define INF 200000000

// struct Edge {
//   int to;
//   int depth;

//   Edge(const int to, const int depth) : to(to), depth(depth) {
//   }

//   inline bool
//   operator<(const Edge& other) const {
//     return this->depth < other.depth;
//   }

//   inline bool
//   operator>(const Edge& other) const {
//     return this->depth > other.depth;
//   }
// };

// void
// dijkstra(const int x,
//          const std::vector<std::vector<int> >& graph,
//          std::vector<int>& dist) {
//   std::priority_queue<Edge, std::vector<Edge>, std::greater<Edge> > q;

//   dist[x] = 0;
//   q.push(Edge(x, 0));

//   while (!q.empty()) {
//     const int curr_node = q.top().to;
//     const int curr_depth = q.top().depth;
//     q.pop();

//     if (curr_depth > dist[curr_node])
//       continue;

//     const std::vector<int>& curr_vec = graph[curr_node];

//     for (std::vector<int>::const_iterator it = curr_vec.begin();
//          it != curr_vec.end();
//          ++it) {
//       const int next_node = *it;
//       const int next_depth = curr_depth + 1;

//       if (next_depth < dist[next_node]) {
//         dist[next_node] = next_depth;
//         q.push(Edge(next_node, next_depth));
//       }
//     }
//   }
// }

// int
// main(void) {
//   std::ios::sync_with_stdio(false);
//   std::cin.tie(NULL);
//   std::cout.tie(NULL);

//   int n, m, k, x;
//   std::cin >> n >> m >> k >> x;

//   std::vector<std::vector<int> > graph(n);

//   for (int i = 0; i < m; ++i) {
//     int a, b;
//     std::cin >> a >> b;
//     graph[a - 1].push_back(b - 1);  //
//   }

//   std::vector<int> dist(n, INF);

//   dijkstra(x - 1, graph, dist);

//   int count = 0;

//   for (size_t i = 0; i < dist.size(); ++i) {
//     if (dist[i] == k) {
//       std::cout << i + 1 << "\n";
//       ++count;
//     }
//   }

//   if (count == 0)
//     std::cout << "-1\n";

//   return 0;
// }
// }}}
