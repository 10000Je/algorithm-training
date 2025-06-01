// no.2206: 벽 부수고 이동하기 (G3)

#include <cstdio>
#include <vector>
#include <queue>
#include <functional>
#define INF int(1e8)
using namespace std;

int n, m;
int map[1001][1001];
void bfs(vector<vector<vector<int>>>& dist);

int main() {
    scanf("%d %d", &n, &m);
    for(int i=1; i<=n; i++) {
        char row[1001];
        scanf("%s", row);
        getchar();
        for(int j=0; row[j]!=0; j++) {
            map[i][j+1] = row[j]-'0';
        }
    }
    vector<vector<vector<int>>> dist;
    bfs(dist);
    if(dist[n][m][0] >= INF && dist[n][m][1] >= INF) {
        printf("-1\n");
    }
    else if(dist[n][m][0] >= INF) {
        printf("%d\n", dist[n][m][1]);
    }
    else if(dist[n][m][1] >= INF) {
        printf("%d\n", dist[n][m][0]);
    }
    else {
        printf("%d\n", min(dist[n][m][0], dist[n][m][1]));
    }
    return 0;
}

void bfs(vector<vector<vector<int>>>& dist) {
    dist.clear();
    dist.assign(n+1, vector<vector<int>>(m+1, vector<int>(2, INF)));
    dist[1][1][0] = 1;
    queue<tuple<int, int, int>> que;
    que.push(make_tuple(1, 1, 0));
    while(!que.empty()) {
        tuple<int, int, int> x = que.front();
        que.pop();
        int i = get<0>(x), j = get<1>(x), k = get<2>(x);
        vector<pair<int, int>> nodes = {
            make_pair(i-1, j), make_pair(i+1, j), make_pair(i, j-1), make_pair(i, j+1)
        };
        for(pair<int, int> node : nodes) {
            int r = node.first, c = node.second;
            if(r < 1 || r > n || c < 1 || c > m) {
                continue;
            }
            if(map[r][c] == 1) {
                if(k == 0) {
                    if(dist[i][j][0] + 1 < dist[r][c][1]) {
                        dist[r][c][1] = dist[i][j][0] + 1;
                        que.push(make_tuple(r, c, 1));
                    }
                }
                else {
                    continue;
                }
            }
            else {
                if(dist[i][j][k] + 1 < dist[r][c][k]) {
                    dist[r][c][k] = dist[i][j][k] + 1;
                    que.push(make_tuple(r, c, k));
                }
            }
        }
    }
}