// no.18111: 마인크래프트 (S2)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n, m, b;
    scanf("%d %d %d", &n, &m, &b);
    vector<vector<int>> ground(n, vector<int>(m, 0));
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            scanf("%d", &ground[i][j]);
    int time = __INT_MAX__;
    int height = 0;
    for(int h=0; h<=256; h++) {
        int cur = 0;
        int block = b;
        for(int r=0; r<n; r++) {
            for(int c=0; c<m; c++) {
                if(ground[r][c] > h) {
                    cur += (ground[r][c]-h)*2;
                    block += (ground[r][c]-h);
                }
            }
        }
        for(int r=0; r<n; r++) {
            for(int c=0; c<m; c++) {
                if(ground[r][c] < h) {
                    cur += (h-ground[r][c]);
                    block -= (h-ground[r][c]);
                }
            }
        }
        if(block < 0)
            continue;
        if(cur < time) {
            time = cur;
            height = h;
        }
        if(cur==time && h > height) {
            height = h;
        }
    }
    printf("%d %d\n", time, height);
    return 0;
}