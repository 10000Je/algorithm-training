// no.1967: 트리의 지름 (G4)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

void dfs(int, vector<int>&);
vector<vector<pair<int, int>>> graph;

int main() {
    int n;
    scanf("%d", &n);
    graph.assign(n+1, vector<pair<int, int>>());
    for(int i=0; i<n-1; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        graph[a].push_back(make_pair(b, c));
        graph[b].push_back(make_pair(a, c));
    }
    vector<int> dist(n+1, -1);
    dist[1] = 0;
    dfs(1, dist);
    int ret = 0;
    int st = 1;
    for(int i=1; i<=n; i++) {
        if(dist[i] > ret) {
            ret = dist[i];
            st = i;
        }
    }
    dist.clear();
    dist.assign(n+1, -1);
    dist[st] = 0;
    dfs(st, dist);
    ret = 0;
    for(int i=1; i<=n; i++) {
        ret = max(ret, dist[i]);
    }
    printf("%d\n", ret);
    return 0;

}

void dfs(int root, vector<int>& dist) {
    for(pair<int, int> val : graph[root]) {
        int node = val.first;
        int cost = val.second;
        if(dist[node] != -1)
            continue;
        dist[node] = dist[root] + cost;
        dfs(node, dist);
    }
}