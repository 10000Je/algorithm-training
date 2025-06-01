// no.14465: 소가 길을 건너간 이유 5 (S2)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, k, b;
    scanf("%d %d %d", &n, &k, &b);
    vector<bool> light(n+1, true);
    for(int i=0; i<b; i++) {
        int num;
        scanf("%d", &num);
        light[num] = false;
    }
    vector<int> dp(n+1, 0);
    for(int i=1; i<=n; i++) {
        if(light[i]) {
            dp[i] = dp[i-1]+1; 
        }
        else {
            dp[i] = dp[i-1];
        }
    }
    int ret = k;
    for(int i=k; i<=n; i++) {
        ret = min(k-(dp[i]-dp[i-k]), ret);
    }
    printf("%d\n", ret);
    return 0;
}