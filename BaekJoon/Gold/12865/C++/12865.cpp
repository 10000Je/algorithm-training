// no.12865: 평범한 배낭 (G5)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<int> w(n+1, 0);
    vector<int> v(n+1, 0);
    for(int i=1; i<=n; i++)
        scanf("%d %d", &w[i], &v[i]);
    
    vector<vector<int>> dp(n+1, vector<int>(k+1, 0));
    for(int i=1; i<=n; i++) {
        for(int j=0; j<=k; j++) {
            if(w[i] <= j) {
                dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j]);
            }
            else {
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    printf("%d\n", dp[n][k]);
    return 0;
}