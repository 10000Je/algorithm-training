// no.1463: 1로 만들기 (S3)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> dp(n+1, 0);
    dp[1] = 0;
    for(int i=2; i<=n; i++) {
        if(i%3==0 && i%2==0) {
            dp[i] = min({dp[i/3]+1, dp[i/2]+1, dp[i-1]+1});
        } else if(i%3==0) {
            dp[i] = min(dp[i/3]+1, dp[i-1]+1);
        } else if(i%2==0) {
            dp[i] = min(dp[i/2]+1, dp[i-1]+1);
        } else {
            dp[i] = dp[i-1]+1;
        }
    }
    printf("%d\n", dp[n]);
    return 0;
}