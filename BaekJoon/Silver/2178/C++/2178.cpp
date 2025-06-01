// no.2178: 미로 탐색 (S1)

#include <cstdio>
#include <queue>
#include <vector>
#include <map>
using namespace std;

int bfs(vector<vector<int>>&, pair<int, int>);

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> graph(n, vector<int>(m, 0));
    for(int i=0; i<n; i++) {
        char str[101];
        scanf("%s", str);
        for(int j=0; j<m; j++) {
            graph[i][j] = str[j]-'0';
        }
    }
    printf("%d\n", bfs(graph, make_pair(n, m)));
    return 0;
}

int bfs(vector<vector<int>>& graph, pair<int, int> size) {
    queue<pair<int, int>> que;
    que.push(make_pair(0, 0));
    map<pair<int, int>, int> dist;
    dist[make_pair(0, 0)] = 1;
    int n=size.first, m=size.second;
    while(!que.empty()) {
        pair<int, int> cur = que.front();
        int r=cur.first, c=cur.second;
        que.pop();
        vector<pair<int, int>> nodes({make_pair(r-1, c), make_pair(r+1, c), make_pair(r, c+1), make_pair(r, c-1)});
        for(pair<int, int> node : nodes) {
            if(node.first<0 || node.first>=n)
                continue;
            if(node.second<0 || node.second>=m)
                continue;
            if(dist.count(node)!=0)
                continue;
            if(graph[node.first][node.second]==0)
                continue;
            dist[node] = dist[cur]+1;
            que.push(node);
        }
    }
    return dist[make_pair(n-1, m-1)];
}