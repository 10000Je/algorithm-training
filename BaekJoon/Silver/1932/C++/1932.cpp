// no.1932: 정수 삼각형 (S1)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> val(n+1, vector<int>(n+1, 0));
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=i; j++) {
            scanf("%d", &val[i][j]);
        }
    }
    vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=i; j++) {
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + val[i][j];
        }
    }
    printf("%d\n", *max_element(dp[n].begin(), dp[n].end()));
    return 0;
}