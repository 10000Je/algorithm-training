// no.11659: 구간 합 구하기 4 (S3)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> nums(n+1, 0);
    vector<int> dp(n+1, 0);
    for(int i=1; i<=n; i++) {
        int num;
        scanf("%d", &num);
        nums[i] = num;
        dp[i] = nums[i] + dp[i-1];
    }
    for(int i=0; i<m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%d\n", dp[b]-dp[a-1]);
    }
    return 0;
}