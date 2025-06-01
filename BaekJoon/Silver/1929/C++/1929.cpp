// no.1929: 소수 구하기 (S3)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int m, n;
    scanf("%d %d", &m, &n);

    vector<bool> arr(n+1, true);

    arr[1] = false;
    for(int i=2; i*i<=n; i++) {
        if(!arr[i])
            continue;
        int j = i*2;
        while(j <= n) {
            arr[j] = false;
            j+=i;
        }
    }

    for(int i=m; i<=n; i++) {
        if(arr[i])
            printf("%d\n", i);
    }
    return 0;
}