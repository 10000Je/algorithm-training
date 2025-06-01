// no.1753: 최단경로 (G4)

#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

void dijkstra(vector<int>&);
vector<vector<pair<int, int>>> graph;
int v, k;

int main() {
    int e;
    scanf("%d %d", &v, &e);
    scanf("%d", &k);
    graph.assign(v+1, vector<pair<int, int>>());
    for(int i=0; i<e; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        graph[u].push_back(make_pair(v, w));
    }
    vector<int> dist(v+1, -1);
    dijkstra(dist);
    for(int i=1; i<=v; i++) {
        if(dist[i] == -1)
            printf("INF\n");
        else
            printf("%d\n", dist[i]);
    }
    return 0;
}

void dijkstra(vector<int>& dist) {
    priority_queue<pair<int, int>> queue;
    dist[k] = 0;
    vector<bool> visit(v+1, false);
    queue.push(make_pair(-dist[k], k));
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
            if(dist[node]==-1 || dist[cur]+cost < dist[node]) {
                dist[node] = dist[cur]+cost;
                queue.push(make_pair(-dist[node], node));
            }
        }
    }
}