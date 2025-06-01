// no.14670: 병약한 영정 (S4)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> arr(101, -1);
    for(int i=0; i<n; i++) {
        int me, mn;
        scanf("%d %d", &me, &mn);
        arr[me] = mn;
    }
    int r;
    scanf("%d", &r);
    for(int i=0; i<r; i++) {
        vector<int> ret;
        bool p = true;
        int l;
        scanf("%d", &l);
        for(int j=0; j<l; j++) {
            int s;
            scanf("%d", &s);
            if(arr[s]==-1) {
                p = false;
            }
            else {
                ret.push_back(arr[s]);
            }
        }
        if(p) {
            for(int name : ret) {
                printf("%d ", name);
            }
            printf("\n");
        }
        else {
            printf("YOU DIED\n");
        }
    }
    return 0;
}