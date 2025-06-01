// no.17175: 피보나치는 지겨웡~

#include <cstdio>
#include <vector>
#define R 1'000'000'007
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> dp(51, 0);
    dp[0] = 1;
    dp[1] = 1;
    for(int i=2; i<=n; i++) {
        dp[i] = (dp[i-1]+dp[i-2]+1)%R;
    }
    printf("%d\n", dp[n]);
    return 0;
}