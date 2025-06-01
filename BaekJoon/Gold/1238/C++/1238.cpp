// no.1238: 파티 (G3)

#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<pair<int, int>>> town;
int n;

void dijkstra(int x, vector<int>& dist);

int main() {
    int m, x;
    scanf("%d %d %d", &n, &m,&x);
    town.assign(n+1, vector<pair<int, int>>());
    for(int i=0; i<m; i++) {
        int a, b, t;
        scanf("%d %d %d", &a, &b, &t);
        town[a].push_back(make_pair(b, t));
    }
    vector<int> dist;
    dijkstra(x, dist);
    vector<int> ret = dist;
    for(int i=1; i<=n; i++) {
        dijkstra(i, dist);
        ret[i] += dist[x];
    }
    printf("%d\n", *max_element(ret.begin(), ret.end()));
    return 0;
}

void dijkstra(int x, vector<int>& dist) {
    priority_queue<pair<int, int>> queue;
    vector<bool> visit(n+1, false);
    dist.clear();
    dist.assign(n+1, -1);
    dist[x] = 0;
    queue.push(make_pair(-dist[x], x));
    while(!queue.empty()) {
        int cur = queue.top().second;
        queue.pop();
        if(visit[cur]) {
            continue;
        }
        visit[cur] = true;
        for(pair<int, int> val : town[cur]) {
            int node = val.first, cost = val.second;
            if(visit[node]) {
                continue;
            }
            if(dist[node] == -1 || dist[cur] + cost < dist[node]) {
                dist[node] = dist[cur] + cost;
                queue.push(make_pair(-dist[node], node));
            }
        }
    }
}