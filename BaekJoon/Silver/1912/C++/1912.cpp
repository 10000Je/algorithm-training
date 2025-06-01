// no.1912: 연속합 (S2)
/*
 * 이게 어떻게 실버2
 * 얼탱X
 */

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> sum(n+1, 0);
    vector<int> dp(n+1, 0);
    int tmp = 0;
    for(int i=1; i<=n; i++) {
        int num;
        scanf("%d", &num);
        sum[i] = sum[i-1] + num;
        tmp += num;
        if(tmp < 0) {
            dp[i] = dp[i-1] + tmp;
            tmp = 0;
        } else {
            dp[i] = dp[i-1];
        }
    }
    int ret = sum[n] - dp[0];
    for(int i=1; i<=n; i++) {
        ret = max(sum[i]-dp[i-1], ret);
    }
    printf("%d\n", ret);
    return 0;
}