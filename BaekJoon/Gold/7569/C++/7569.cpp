// no.7569: 토마토 (G5)

#include <cstdio>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

int main() {
    int m, n, h;
    scanf("%d %d %d", &m, &n, &h);
    vector<vector<vector<int>>> box(h, vector<vector<int>>(n, vector<int>(m, 0)));
    queue<tuple<int, int, int>> que;
    vector<vector<vector<int>>> dist(h, vector<vector<int>>(n, vector<int>(m, -1)));
    for(int i=0; i<h; i++) {
        for(int j=0; j<n; j++) {
            for(int k=0; k<m; k++) {
                scanf("%d", &box[i][j][k]);
                if(box[i][j][k]==1) {
                    que.push(make_tuple(i, j, k));
                    dist[i][j][k] = 0;
                }
            }
        }
    }
    while(!que.empty()) {
        tuple<int, int, int> cur = que.front();
        que.pop();
        int i=get<0>(cur), j=get<1>(cur), k=get<2>(cur);
        vector<tuple<int, int, int>> nodes = {
            make_tuple(i-1, j, k), make_tuple(i+1, j, k), make_tuple(i, j-1, k),
            make_tuple(i, j+1, k), make_tuple(i, j, k-1), make_tuple(i, j, k+1)
        };
        for(tuple<int, int, int> node : nodes) {
            int ni=get<0>(node), nj=get<1>(node), nk=get<2>(node);
            if(ni<0 || ni>=h)
                continue;
            if(nj<0 || nj>=n)
                continue;
            if(nk<0 || nk>=m)
                continue;
            if(box[ni][nj][nk]==-1)
                continue;
            if(dist[ni][nj][nk]!=-1)
                continue;
            dist[ni][nj][nk] = dist[i][j][k]+1;
            que.push(node);
        }
    }
    int max = 0;
    for(int i=0; i<h; i++) {
        for(int j=0; j<n; j++) {
            for(int k=0; k<m; k++) {
                if(box[i][j][k] == -1)
                    continue;
                if(box[i][j][k]!=-1 && dist[i][j][k]==-1) {
                    printf("-1\n");
                    return 0;
                }
                else {
                    max = (dist[i][j][k] > max) ? dist[i][j][k] : max;
                }
            }
        }
    }
    printf("%d\n", max);
    return 0;
}