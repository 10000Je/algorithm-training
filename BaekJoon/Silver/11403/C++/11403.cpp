// no.11403: 경로 찾기 (S1)

#include <cstdio>
#include <vector>
#include <algorithm>
#define INF (__INT_MAX__/2)
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> dp(n, vector(n, INF));
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            int e;
            scanf("%d", &e);
            if(e!=0)
                dp[i][j] = e;
        }
    }
    for(int k=0; k<n; k++) {
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(dp[i][k]==INF || dp[k][j]==INF)
                    continue;
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]);
            }
        }
    }
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            printf("%d ", dp[i][j]!=INF ? 1 : 0);
        }
        printf("\n");
    }
    return 0;
}