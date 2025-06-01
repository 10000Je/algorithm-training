// no.7576: 토마토 (G5)

#include <cstdio>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

int main() {
    int m, n;
    scanf("%d %d", &m, &n);
    vector<vector<int>> box(n, vector<int>(m, 0));
    queue<pair<int, int>> que;
    vector<vector<int>> dist(n, vector<int>(m, -1));
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            scanf("%d", &box[i][j]);
            if(box[i][j]==1) {
                que.push(make_pair(i, j));
                dist[i][j] = 0;
            }
        }
    }
    while(!que.empty()) {
        pair<int, int> cur = que.front();
        que.pop();
        int i=cur.first, j=cur.second;
        vector<pair<int, int>> nodes = {
            make_pair(i-1, j), make_pair(i+1, j), 
            make_pair(i, j-1), make_pair(i, j+1)
        };
        for(pair<int, int> node : nodes) {
            int ni=node.first, nj=node.second;
            if(ni<0 || ni>=n)
                continue;
            if(nj<0 || nj>=m)
                continue;
            if(box[ni][nj]==-1)
                continue;
            if(dist[ni][nj]!=-1)
                continue;
            dist[ni][nj] = dist[i][j]+1;
            que.push(node);
        }
    }
    int max = 0;
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            if(box[i][j] == -1)
                continue;
            if(box[i][j]!=-1 && dist[i][j]==-1) {
                printf("-1\n");
                return 0;
            }
            else {
                max = (dist[i][j] > max) ? dist[i][j] : max;
            }
        }
    }
    printf("%d\n", max);
    return 0;
}