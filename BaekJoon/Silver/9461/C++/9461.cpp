// no.9461: 파도반 수열 (S3)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    vector<long long> dp(101, 0);
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 1;
    for(int i=4; i<=100; i++) {
        dp[i] = dp[i-2]+dp[i-3];
    }
    for(int i=0; i<t; i++) {
        int n;
        scanf("%d", &n);
        printf("%lld\n", dp[n]);
    }
    return 0;
} 