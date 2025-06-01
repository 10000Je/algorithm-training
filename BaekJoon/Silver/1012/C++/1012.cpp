// no.1012: 유기농 배추 (S2)

#include <cstdio>
#include <vector>
using namespace std;

void dfs(vector<vector<bool>>&, int, int);

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        int m, n, k;
        scanf("%d %d %d", &m, &n, &k);
        vector<vector<bool>> ground(n, vector(m, false));
        for(int j=0; j<k; j++) {
            int x, y;
            scanf("%d %d", &x, &y);
            ground[y][x] = true;
        }
        int ret = 0;
        for(int r=0; r<n; r++) {
            for(int c=0; c<m; c++) {
                if(ground[r][c]) {
                    ret++;
                    dfs(ground, r, c);
                }
            }
        }
        printf("%d\n", ret);
    }
    return 0;
}

void dfs(vector<vector<bool>>& ground, int r, int c) {
    ground[r][c] = false;
    vector<pair<int, int>> near;
    near.push_back(make_pair(r-1, c));
    near.push_back(make_pair(r+1, c));
    near.push_back(make_pair(r, c-1));
    near.push_back(make_pair(r, c+1));
    for(pair<int, int> pr : near) {
        if(pr.first<0 || pr.first>=ground.size())
            continue;
        if(pr.second<0 || pr.second>=ground[pr.first].size())
            continue;
        if(!ground[pr.first][pr.second])
            continue;
        dfs(ground, pr.first, pr.second);
    }
}