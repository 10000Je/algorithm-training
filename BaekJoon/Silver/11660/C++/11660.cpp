// no.11660: 구간 합 구하기 5 (S1)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> val(n+1, vector<int>(n+1, 0));
    vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
    for(int i=1; i<=n; i++)
        for(int j=1; j<=n; j++)
            scanf("%d", &val[i][j]);

    for(int i=1; i<=n; i++)
        for(int j=1; j<=n; j++)
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + val[i][j];
            
    for(int i=0; i<m; i++) {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        int sum = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1];
        printf("%d\n", sum);
    }
    return 0;
}