// no.14938: 서강그라운드 (G4)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> dp;
void floydwashal();
int n;

int main() {
    int m, r;
    scanf("%d %d %d", &n, &m, &r);
    vector<int> cost(n+1, 0);
    for(int i=1; i<=n; i++) {
        scanf("%d", &cost[i]);
    }
    dp.assign(n+1, vector<int>(n+1, -1));
    for(int i=1; i<=n; i++) {
        dp[i][i] = 0;
    }
    for(int i=0; i<r; i++) {
        int a, b, l;
        scanf("%d %d %d", &a, &b, &l);
        dp[a][b] = l;
        dp[b][a] = l;
    }
    floydwashal();
    int ret = 0;
    for(int i=1; i<=n; i++) {
        int cnt = 0;
        for(int j=1; j<=n; j++) {
            if(dp[i][j] != -1 && dp[i][j] <= m)
                cnt += cost[j];
        }
        ret = max(ret, cnt);
    }
    printf("%d\n", ret);
    return 0;
}

void floydwashal() {
    for(int k=1; k<=n; k++) {
        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                if(dp[i][k] == -1 || dp[k][j] == -1) {
                    continue;
                }
                if(dp[i][j] == -1 || dp[i][k] + dp[k][j] < dp[i][j]) {
                    dp[i][j] = dp[i][k] + dp[k][j];
                }
            }
        }
    }
}