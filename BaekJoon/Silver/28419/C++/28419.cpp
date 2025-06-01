// no.28419: 더하기 (S4)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> arr;
    for(int i=0; i<n; i++) {
        int a;
        scanf("%d", &a);
        arr.push_back(a);
    }
    long long o=0, e=0;
    for(int i=0; i<n; i+=2) {
        o += arr[i];
    }
    for(int i=1; i<n; i+=2) {
        e += arr[i];
    }
    if(n==3) {
        if(o > e) {
            printf("-1\n");
        }
        else {
            printf("%lld\n", (e-o));
        }
    }
    else {
        printf("%lld\n", (e>o) ? (e-o) : (o-e));
    }
    return 0;
}