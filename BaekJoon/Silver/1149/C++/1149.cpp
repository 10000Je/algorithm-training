// no.1149: RGB 거리 (S1)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> cost(n, vector<int>(3, 0));
    for(int i=0; i<n; i++)
        for(int j=0; j<3; j++)
            scanf("%d", &cost[i][j]);
    vector<vector<int>> dp(n, vector<int>(3, 0));
    dp[0] = cost[0];
    for(int i=1; i<n; i++) {
        dp[i][0] = min(dp[i-1][1], dp[i-1][2])+cost[i][0];
        dp[i][1] = min(dp[i-1][0], dp[i-1][2])+cost[i][1];
        dp[i][2] = min(dp[i-1][0], dp[i-1][1])+cost[i][2];
    }
    printf("%d\n", min({dp[n-1][0], dp[n-1][1], dp[n-1][2]}));
    return 0;
}