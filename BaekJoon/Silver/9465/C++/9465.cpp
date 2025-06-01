// no.9465: 스티커 (S1)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        vector<vector<int>> val(100'000, vector<int>(2, 0));
        int n;
        scanf("%d", &n);
        for(int i=0; i<2; i++)
            for(int j=0; j<n; j++)
                scanf("%d", &val[j][i]);
        vector<vector<int>> dp(100'000, vector<int>(2, 0));
        dp[0] = val[0];
        dp[1][0] = dp[0][1] + val[1][0];
        dp[1][1] = dp[0][0] + val[1][1];
        for(int i=2; i<n; i++) {
            dp[i][0] = max({dp[i-1][1], dp[i-2][0], dp[i-2][1]}) + val[i][0];
            dp[i][1] = max({dp[i-1][0], dp[i-2][0], dp[i-2][1]}) + val[i][1];
        }
        printf("%d\n", max(dp[n-1][0], dp[n-1][1]));
    }
    return 0;
}