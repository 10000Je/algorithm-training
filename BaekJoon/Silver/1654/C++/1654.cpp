// no.1654: 랜던 자르기 (S2)

#include <cstdio>
#include <vector>
using namespace std;


int main() {
    int k, n;
    scanf("%d %d", &k, &n);
    vector<int> line;
    for(int i=0; i<k; i++) {
        int len;
        scanf("%d", &len);
        line.push_back(len);
    }
    long long left = 1;
    long long right = 0x7fffffff;
    while(left <= right) {
        long long mid = (left+right)/2;
        int cnt = 0;
        for(int len : line) {
            cnt += len / mid;
        }
        if(cnt < n) {
            right = mid-1;
        } else {
            left = mid+1;
        }
    }
    printf("%lld\n", right);
    return 0;
}