// no.17070: 파이프 옮기기 1 (G5)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> home(n+1, vector<int>(n+1, 0));
    for(int i=1; i<=n; i++)
        for(int j=1; j<=n; j++)
            scanf("%d", &home[i][j]);
    vector<vector<vector<int>>> dp(n+1, 
        vector<vector<int>>(n+1, 
            vector<int>(3, 0)
        )
    );
    dp[1][2][0] = 1;
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=n; j++) {
            if(i==1 && j==2)
                continue;
            if(home[i][j] == 0)
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2];
            if(home[i][j] == 0)
                dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2];
            if(home[i][j] == 0 && home[i-1][j] == 0 && home[i][j-1] == 0)
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2];
        }
    }
    printf("%d\n", dp[n][n][0] + dp[n][n][1] + dp[n][n][2]);
    return 0;
}