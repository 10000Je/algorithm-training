// no.2839: 설탕 배달 (S4)
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);\
    int ret = 2000;
    for(int i=0; 5*i <= n; i++) {
        if((n-5*i)%3 != 0) {
            continue;
        }
        ret = min(ret, i+(n-5*i)/3);
    }
    printf("%d\n", (ret == 2000) ? -1 : ret);
    return 0;
}