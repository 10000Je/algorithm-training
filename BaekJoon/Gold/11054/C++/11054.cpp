// no.11054: 가장 긴 바이토닉 부분 수열 (G4)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> nums(n, 0);
    for(int i=0; i<n; i++) {
        scanf("%d", &nums[i]);
    }
    vector<int> lis(n, 1);
    vector<int> rlis(n, 1);
    for(int i=0; i<n; i++) {
        for(int j=0; j<i; j++) {
            if(nums[j] < nums[i]) {
                lis[i] = max(lis[i], lis[j]+1);
            }
        }
    }
    for(int i=n-1; i>=0; i--) {
        for(int j=n-1; j>i; j--) {
            if(nums[j] < nums[i]) {
                rlis[i] = max(rlis[i], rlis[j]+1);
            }
        }
    }
    int ret = 0;
    for(int i=0; i<n; i++) {
        ret = max(ret, lis[i]+rlis[i]-1);
    }
    printf("%d\n", ret);
    return 0;
}