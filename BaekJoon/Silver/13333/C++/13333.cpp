// no.13333: Q-인덱스
// O(N^2) 해법 (완전탐색 사용)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> arr;
    for(int i=0; i<n; i++) {
        int cnt;
        scanf("%d", &cnt);
        arr.push_back(cnt);
    }
    int q_index = 0;
    for(int i=0; i<=n; i++) {
        int cnt = 0;
        for(int j=0; j<n; j++) {
            if(arr[j] >= i)
                cnt++;
        }
        if(cnt < i)
            continue;
        cnt = 0;
        for(int j=0; j<n; j++) {
            if(arr[j] <= i)
                cnt++;
        }
        if(cnt >= n-i) {
            q_index = i;
            break;
        }
    }
    printf("%d\n", q_index);
    return 0;
}
