// no.30805: 사전 순 최대 공통 부분 수열 (G4)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> arr1(n);
    for(int i=0; i<n; i++) {
        scanf("%d", &arr1[i]);
    }
    int m;
    scanf("%d", &m);
    vector<int> arr2(m);
    for(int i=0; i<m; i++) {
        scanf("%d", &arr2[i]);
    }
    vector<int> common;
    int ist = 0, jst = 0;
    while(true) {
        int max = 0;
        int ti = ist, tj = jst;
        for(int i=ist; i<n; i++) {
            for(int j=jst; j<m; j++) {
                if(arr1[i] == arr2[j] && arr1[i] > max) {
                    max = arr1[i];
                    ti = i+1;
                    tj = j+1;
                }
            }
        }
        if(max == 0) {
            break;
        }
        ist = ti;
        jst = tj;
        common.push_back(max);
    }
    printf("%lu\n", common.size());
    for(int num : common) {
        printf("%d ", num);
    }
    printf("\n");
    return 0;    
}