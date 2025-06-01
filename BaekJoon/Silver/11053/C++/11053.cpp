// no.11053: 가장 긴 증가하는 부분 수열 (S2)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> a(n, 0);
    for(int i=0; i<n; i++) {
        scanf("%d", &a[i]);
    }
    vector<int> dp(n, 1);
    for(int i=0; i<n; i++) {
        for(int j=0; j<i; j++) {
            if(a[j] < a[i])
                dp[i] = max(dp[i], dp[j]+1);
        }
    }
    printf("%d\n", *max_element(dp.begin(), dp.end()));
    return 0;
}