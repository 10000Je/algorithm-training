// no.1003: 피보나치 함수 (S3)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    vector<int> zero_dp(41, 0);
    vector<int> one_dp(41, 0);
    zero_dp[0] = 1;
    one_dp[1] = 1;
    for(int i=2; i<=40; i++) {
        zero_dp[i] = zero_dp[i-1]+zero_dp[i-2];
        one_dp[i] = one_dp[i-1]+one_dp[i-2];
    }
    for(int i=0; i<t; i++) {
        int n;
        scanf("%d", &n);
        printf("%d %d\n", zero_dp[n], one_dp[n]);
    }
    return 0;
}