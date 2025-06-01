// no.1676: 팩토리얼 0의 개수 (S5)

#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    int two, five = 0;
    for(int i=1; i<=n; i++) {
        int num = i;
        while(num%2==0) {
            num/=2;
            two++;
        }
        num = i;
        while(num%5==0) {
            num/=5;
            five++;
        }
    }
    printf("%d\n", min(two, five));
    return 0;
}