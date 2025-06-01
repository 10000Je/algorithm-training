// no.14940: 쉬운 최단거리 (S1)

#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

void bfs(vector<vector<int>>&, vector<vector<int>>&, pair<int, int>);

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> graph(n, vector(m, 0));
    vector<vector<int>> dist(n, vector(m, -1));
    pair<int, int> start;
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            scanf("%d", &graph[i][j]);
            if(graph[i][j]==2) {
                start = make_pair(i, j);
                dist[i][j] = 0;
            }
        }
    }
    bfs(graph, dist, start);
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            if(dist[i][j]==-1 && graph[i][j]==0) {
                printf("0 ");
            }
            else {
                printf("%d ", dist[i][j]);
            }
        }
        printf("\n");
    }
    return 0;
}

void bfs(vector<vector<int>>& graph, vector<vector<int>>& dist, pair<int, int> start) {
    queue<pair<int, int>> que;
    que.push(start);
    int n=graph.size(), m=graph[0].size();
    while(!que.empty()) {
        pair<int, int> cur = que.front();
        int r=cur.first, c=cur.second;
        que.pop();
        vector<pair<int, int>> nodes({make_pair(r-1, c), make_pair(r+1, c), make_pair(r, c-1), make_pair(r, c+1)});
        for(pair<int, int> node : nodes) {
            if(node.first<0 || node.first>=n)
                continue;
            if(node.second<0 || node.second>=m)
                continue;
            if(graph[node.first][node.second]==0)
                continue;
            if(dist[node.first][node.second]!=-1)
                continue;
            dist[node.first][node.second] = dist[r][c]+1;
            que.push(node);
        }
    }
}