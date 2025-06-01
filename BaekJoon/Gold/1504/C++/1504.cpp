// no.1504: 특정한 최단 경로 (G4)

#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int dijkstra(int, int);
int n;
vector<vector<pair<int, int>>> graph;

int main() {
    int e;
    scanf("%d %d", &n, &e);
    graph.assign(n+1, vector<pair<int,int>>());
    for(int i=0; i<e; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        graph[a].push_back(make_pair(b, c));
        graph[b].push_back(make_pair(a, c));
    }
    int v1, v2;
    scanf("%d %d", &v1, &v2);
    int ret1;
    try {
        ret1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n);
    }
    catch(int e) {
        ret1 = -1;
    }
    int ret2;
    try {
        ret2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n);
    }
    catch(int e) {
        ret2 = -1;
    }
    if(ret1 == -1 && ret2 == -1) {
        printf("%d\n", -1);
    }
    else if(ret1 == -1) {
        printf("%d\n", ret2);
    }
    else if(ret2 == -1) {
        printf("%d\n", ret1);
    }
    else {
        printf("%d\n", min(ret1, ret2));
    }
    return 0;
}

int dijkstra(int a, int b) {
    vector<int> dist(n+1, -1);
    vector<bool> visit(n+1, false);
    priority_queue<pair<int, int>> queue;
    dist[a] = 0;
    queue.push(make_pair(-dist[a], a));
    while(!queue.empty()) {
        int cur = queue.top().second;
        queue.pop();
        if(visit[cur])
            continue;
        for(pair<int, int> val : graph[cur]) {
            int node = val.first;
            int cost = val.second;
            if(visit[node])
                continue;
            if(dist[node] == -1 || dist[cur]+cost < dist[node]) {
                dist[node] = dist[cur] + cost;
                queue.push(make_pair(-dist[node], node));
            }
        }
    }
    if(dist[b] == -1)
        throw -1;
    else
        return dist[b];
}