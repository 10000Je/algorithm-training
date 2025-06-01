// no.1330: 두 수 비교하기 (B5)

#include <cstdio>
using namespace std;

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    if(a>b) {
        printf(">\n");
    } else if(a<b) {
        printf("<\n");
    } else {
        printf("==\n");
    }
    return 0;
}