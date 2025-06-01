// no.18870: 좌표 압축 (S2)

#include <cstdio>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> x(n, 0);
    for(int i=0; i<n; i++) {
        scanf("%d", &x[i]);
    }
    vector<int> sorted(x);
    sort(sorted.begin(), sorted.end());
    unordered_map<int, int> cnt;
    cnt[sorted[0]] = 0;
    for(int i=1; i<n; i++) {
        if(sorted[i]==sorted[i-1]) {
            cnt[sorted[i]] = cnt[sorted[i-1]];
        }
        else {
            cnt[sorted[i]] = cnt[sorted[i-1]]+1;
        }
    }
    for(int i=0; i<n; i++) {
        printf("%d ", cnt[x[i]]);
    }
    printf("\n");
    return 0;
}