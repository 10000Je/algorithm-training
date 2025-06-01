// O(NlogN) 해법 (정렬사용)

#include <cstdio>
#include <algorithm>
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
    sort(arr.begin(), arr.end(), greater<int>());
    int q_index;
    for(int q=0; q<=n; q++) {
        if(q==0) {
            if(arr[0]<=0) {
                q_index = 0;
                break;
            }
        }
        else if(q==n) {
            if(arr[n-1]>=n) {
                q_index = n;
                break;
            }
        }
        else {
            if(arr[q-1]>=q && arr[q]<=q) {
                q_index = q;
                break;
            }
        }
    }
    printf("%d\n", q_index);
    return 0;
}