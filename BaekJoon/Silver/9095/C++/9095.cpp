// no.9095: 1, 2, 3 더하기 (S3)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    vector<int> dp(11, 0);
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for(int i=4; i<=10; i++) {
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3];
    }
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        int n;
        scanf("%d", &n);
        printf("%d\n", dp[n]);
    }
    return 0;
}