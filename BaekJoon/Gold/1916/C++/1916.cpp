// no.1916: 최소비용 구하기 (G5)

#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int dijkstra(int, int); 
vector<vector<pair<int, int>>> graph;
int n;

int main() {
    int m;
    scanf("%d", &n);
    scanf("%d", &m);
    graph.assign(n+1, vector<pair<int, int>>());
    for(int i=0; i<m; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        graph[a].push_back(make_pair(b, c));
    }
    int s, e;
    scanf("%d %d", &s, &e);
    int ret = dijkstra(s, e);
    printf("%d\n", ret);
}

int dijkstra(int s, int e) {
    priority_queue<pair<int, int>> heap;
    vector<int> dist(n+1, -1);
    vector<bool> visit(n+1, false);
    dist[s] = 0;
    heap.push(make_pair(-dist[s], s));
    while(!heap.empty()) {
        int cur = heap.top().second;
        heap.pop();
        if(visit[cur])
            continue;
        visit[cur] = true;
        for(pair<int, int> pr : graph[cur]) {
            int node = pr.first;
            int cost = pr.second;
            if(visit[node])
                continue;
            if(dist[node] == -1 || dist[node] > dist[cur]+cost) {
                dist[node] = dist[cur] + cost;
                heap.push(make_pair(-dist[node], node));
            }
        }
    }
    return dist[e];
}