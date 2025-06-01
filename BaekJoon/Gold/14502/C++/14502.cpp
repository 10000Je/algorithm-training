// no.14502: 연구소 (G4)

#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int n, m;
vector<vector<int>> graph;
vector<pair<int, int>> virus;
vector<pair<int, int>> blank;

int bfs(pair<int, int>, pair<int, int>, pair<int, int>);

int main() {
    scanf("%d %d", &n, &m);
    graph.assign(n, vector<int>(m, 0));
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            scanf("%d", &graph[i][j]);
            if(graph[i][j] == 0) {
                blank.push_back(make_pair(i, j));
            }
            if(graph[i][j] == 2) {
                virus.push_back(make_pair(i, j));
            }
        }
    }
    int ret = 0;
    for(pair<int, int> i : blank) {
        for(pair<int, int> j : blank) {
            for(pair<int, int> k : blank) {
                if(i==j || j==k || k==i)
                    continue;
                int cnt = bfs(i, j, k);
                ret = max(ret, cnt-3);
            }
        }
    }
    printf("%d\n", ret);
    return 0;

}

int bfs(pair<int, int> i, pair<int, int> j, pair<int, int> k) {
    graph[i.first][i.second] = 1;
    graph[j.first][j.second] = 1;
    graph[k.first][k.second] = 1;
    queue<pair<int, int>> que;
    vector<vector<bool>> visit(n, vector<bool>(m, false));
    for(pair<int, int> v : virus) {
        que.push(v);
        visit[v.first][v.second] = true;
    }
    while(!que.empty()) {
        pair<int, int> cur = que.front();
        que.pop();
        int r = cur.first, c = cur.second;
        vector<pair<int, int>> nodes = {
            make_pair(r-1, c), make_pair(r+1, c), make_pair(r, c-1), make_pair(r, c+1)
        };
        for(pair<int, int> node : nodes) {
            int nr = node.first, nc = node.second;
            if(nr < 0 || nr >= n || nc < 0 || nc >= m)
                continue;
            if(graph[nr][nc] == 1)
                continue;
            if(visit[nr][nc])
                continue;
            visit[nr][nc] = true;
            que.push(node);
        }
    }
    graph[i.first][i.second] = 0;
    graph[j.first][j.second] = 0;
    graph[k.first][k.second] = 0;
    int cnt = 0;
    for(pair<int, int> b : blank) {
        int r = b.first, c = b.second;
        if(!visit[r][c])
            cnt++;
    }
    return cnt;
}