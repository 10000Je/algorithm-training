// no.1389: 케빈 베이컨의 6단계 법칙 (S1)

#include <cstdio>
#include <queue>
#include <vector>
#include <set>
#include <map>
using namespace std;

int bfs(vector<vector<int>>&, map<int, int>&, int);

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> graph(n+1, vector<int>(n+1, -1));
    for(int i=1; i<=n; i++) {
        graph[i][i] = 0;
    }
    for(int i=0; i<m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        graph[a][b] = 1;
        graph[b][a] = 1;
    }
    pair<int, int> ret = make_pair(__INT_MAX__, 0);
    map<int, int> dist;
    for(int i=1; i<=n; i++) {
        int cur = bfs(graph, dist, i);
        if(cur < ret.first) {
            ret = make_pair(cur, i);
        }
        if(cur == ret.first && i < ret.second) {
            ret = make_pair(cur, i);
        }
        dist.clear();
    }
    printf("%d\n", ret.second);
    return 0;
}

int bfs(vector<vector<int>>& graph, map<int, int>& dist, int root) {
    queue<int> que;
    que.push(root);
    dist[root] = 0;
    set<int> visited;
    visited.insert(root);
    while(!que.empty()) {
        int cur = que.front();
        que.pop();
        for(int i=1; i<graph[cur].size(); i++) {
            if(graph[cur][i]==-1)
                continue;
            if(visited.count(i)!=0)
                continue;
            dist[i] = dist[cur] + 1;
            visited.insert(i);
            que.push(i);
        }
    }
    int ret = 0;
    for(pair<int, int> pr : dist) {
        ret += pr.second;
    }
    return ret;
}

