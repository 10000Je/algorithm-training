// no.17626: Four Squares (S3)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> dp(n+1, 4);
    dp[0] = 0;
    for(int i=1; i*i<=n; i++) {
        dp[i*i] = 1;
    }
    for(int i=1; i<=n; i++) {
        if(dp[i]==1)
            continue;
        for(int j=1; j*j<=i; j++) {
            dp[i] = min(dp[j*j]+dp[i-j*j], dp[i]);
        }
    }
    printf("%d\n", dp[n]);
    return 0;
}