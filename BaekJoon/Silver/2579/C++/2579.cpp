// no.2579: 계단 오르기 (S3)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> scores;
    for(int i=0; i<n; i++) {
        int score;
        scanf("%d", &score);
        scores.push_back(score);
    }
    vector<int> dp(300, 0);
    dp[0] = scores[0];
    dp[1] = max(scores[1], scores[1]+dp[0]);
    dp[2] = max(scores[2]+scores[1], scores[2]+dp[0]);
    for(int i=3; i<n; i++) {
        dp[i] = max(scores[i]+scores[i-1]+dp[i-3], scores[i]+dp[i-2]);
    }
    printf("%d\n", dp[n-1]);
    return 0;
}