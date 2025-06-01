// no.11727: 2xn 타일링 2 (S3)

#include <cstdio>
#include <vector>
#define R 10'007
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> dp(1001, 0);
    dp[1] = 1;
    dp[2] = 3;
    for(int i=3; i<=n; i++) {
        dp[i] = (dp[i-1] + 2*dp[i-2])%R;
    }
    printf("%d\n", dp[n]);
    return 0;
}