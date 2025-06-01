// no.9251: LCS (G5)

#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    char s1[1001];
    char s2[1001];
    scanf("%s %s", s1, s2);
    int n = strlen(s1);
    int m = strlen(s2);
    vector<vector<int>> lcs(n+1, vector<int>(m+1, 0));
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=m; j++) {
            if(s1[i-1] == s2[j-1]) {
                lcs[i][j] = lcs[i-1][j-1]+1;
            }
            else {
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j]);
            }
        }
    }
    printf("%d\n", lcs[n][m]);
    return 0;
}